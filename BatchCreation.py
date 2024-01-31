microservices = {
    "BatchAutoLapseQuote_WF_1.0.0.1":{
        "url":"https://ucicommonwfkbv6-11.solartis.net/KnowledgeEngineV6_11/KnowledgeBase/FireEventV4",
        "task_name":"BatchAutoLapseQuote_WF"
    },
    "BatchAutoLapseSubmission_WF_1.0.0.1":{
        "url":"https://ucicommonwfkbv6-11.solartis.net/KnowledgeEngineV6_11/KnowledgeBase/FireEventV4",
        "task_name":"BatchAutoLapseSubmission_WF"
    }
}

def createMailBodyStr(batch_info, datas):
    body =f"""
emailBody = {{
    "Batch_id":"{batch_info.get("batch_id")}",
    "Owner_id":"4482",
    "Owner_name":"{datas.get("owner")}"
}}

"""
    return body


def createListOfRecipitents(datas):
     print(str(datas.get("email_to")))
     listOfRecipitents = f"""
listOfReciptents = {str(datas.get("email_to"))}
"""
     return listOfRecipitents

def createConnObjectStr():
     connObjectString = f"""
def createDBConnectionPoolObject(**kwargs):
    poolingObject = createdbConnectionPooling()
    kwargs['ti'].xcom_push(key='connPoolingObject', value=poolingObject)
"""
     return connObjectString

def createEmailFunc(batch_info):
     batch_id = batch_info.get("batch_id")
     emailFunc = f"""
def onFailureEmail(context):
    sendEmailNotification(listOfReciptents, 'Failed', emailBody)

def onSuccessEmail():
    sendEmailNotification(listOfReciptents, 'Success', emailBody)

def holidayEmail():
    sendEmailNotification(listOfReciptents, 'Holiday Success', emailBody)
"""
     return emailFunc

def getOwnerInfoStr():
     ownerInfoString = f"""
def getOwnerInfoFromPoolObject(**kwargs):
    ti = kwargs['ti']
    poolingObject = ti.xcom_pull(task_ids='createDBConnectionPoolObject__', key='connPoolingObject')
    result = get_ownerInfo(poolingObject)
    kwargs['ti'].xcom_push(key='ownerInfo', value=result)
"""
     return ownerInfoString

def getAuthTokenStr():
     authTokenStr = f"""
def getAuthToken(**kwargs):
    ti = kwargs['ti']
    ownerInfo = ti.xcom_pull(task_ids='getOwnerInfoFromPoolObject__', key='ownerInfo')
    auth_token = getAuthToken_(ownerInfo['username'],ownerInfo['password'],ownerInfo['url'])
    print(auth_token)
    kwargs['ti'].xcom_push(key='authToken', value=auth_token)
"""
     return authTokenStr

def getMicroserviceInvocation():
     microserviceInvocation = f"""
def microserviceInvocation(**kwargs):
    print("Batch Microservice Invoked Successfully !!!")
"""
     return microserviceInvocation
    
    
def createImportStmnt():
    st= """from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from DBconnection.dbConnectionPool import createdbConnectionPooling , get_ownerInfo
from DBconnection.Holiday import checkHoliday
from API_req_res.api_utils import getAuthToken_ , getResponse
from EmailService.emailService import sendEmailNotification
import requests
"""
    return st

def createDefaultArgs(datas):
    defArgs = f"""
default_args = {{
    'owner': '{datas.get("owner", " ")}',
    'depends_on_past': False,
    'start_date': {"datetime("+datas.get("startDate", " ")+")"},
    'retries': 1,
    'retry_delay': timedelta(seconds=3),
    'catchup': {datas.get("catchUp", " ")}
}}
"""
    return defArgs


def createNewDag(batch_info):
    schedule_interval = batch_info.get("schedule_intervel")
    dag = ""
    if(schedule_interval == 'None'):
        dag = dag + f"""
dag = DAG(
    '{batch_info.get("batch_id","")}',
    default_args=default_args,
    description='{batch_info.get("description","")}',
    schedule_interval = {batch_info.get("schedule_intervel","")}
)
"""
    else:
        dag = dag + f"""
dag = DAG(
    '{batch_info.get("batch_id","")}',
    default_args=default_args,
    description='{batch_info.get("description","")}',
    schedule_interval = '{batch_info.get("schedule_intervel","")}'
)
"""
    
    return dag

def creatingTask(task,taskList):
    n=0
    # successEmail = getSuccessEmail(datas=def_args,batch_info=batch_info)
    #taskList.append(successEmail)
    for item in task :
          if(item == "checkHoliday"):
            #    taskNameList.append(f"""{item+"__"}""")
               task= f"""
{item+"__"} = BranchPythonOperator(
    task_id = '{item+"__"}',
    python_callable = {item},
    on_failure_callback = onFailureEmail,
    provide_context = True,
    dag = dag
)"""
               taskList.append(task)
          else:   
            # taskNameList.append(f"""{item+"__"}""")
            task= f"""
{item+"__"} = PythonOperator(
    task_id = '{item+"__"}',
    python_callable = {item},
    on_failure_callback = onFailureEmail,
    provide_context = True,
    dag = dag
)"""
            taskList.append(task)

def createTaskFlow(seq_batch_list):
     seqBatchStr = "getAuthToken__ "
     flow = f"""
createDBConnectionPoolObject__ >> getOwnerInfoFromPoolObject__ >> checkHoliday__
checkHoliday__ >> [holidayEmail__ , getAuthToken__]
"""
     for i in range (len(seq_batch_list)):
        if i < len(seq_batch_list)-1:
            seqBatchStr = seqBatchStr + (" >> " + str(seq_batch_list[i]))
        elif i >= len(seq_batch_list)-1:
            seqBatchStr = seqBatchStr + (" >> " + str(seq_batch_list[i]))

     flow = flow + seqBatchStr + " >> onSuccessEmail__"

     return flow

# batch invoking 

def creatingMicroserviceToInvoke(microserviceToInvoke, taskList, microserviceList):
    for item in microserviceToInvoke :
          microserviceList.append(f"{microservices[item]['task_name']}__")
          task= f"""
{microservices[item]['task_name']}__ = PythonOperator(
     task_id= '{microservices[item]['task_name']}__' ,
     python_callable = getResponse,
     op_kwargs={{'url':'{microservices[item]['url']}','eventName':'{item}'}},
     on_failure_callback = onFailureEmail,
     dag = dag
)"""
          taskList.append(task)

       
def creatingSeqBatch(seq_batch,taskList, seq_batch_list):
    n=0
    for item in seq_batch :
          seq_batch_list.append(f"nextBatchToInvoke{item}__")
          task= f"""
nextBatchToInvoke{item}__ = TriggerDagRunOperator(
    task_id='nextBatchToInvoke{item}__',
    trigger_dag_id='{item}',
    on_failure_callback = onFailureEmail,
    dag = dag
)"""
          taskList.append(task)


# def getSuccessEmail(datas,batch_info):
#     email=f'''
# email_fun=EmailOperator(
#     task_id="Success_email",
#     to={datas.get("email_to")," "},
#     subject="Batch Processing success Alert",
#     html_content="""<h1>Batch {batch_info.get("batch_id","")} Executed Successfully !!! <h1>""",
#     dag = dag
# )'''
#     return email