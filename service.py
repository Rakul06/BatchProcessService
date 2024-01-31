import os,requests,json ,configparser, mysql.connector
from flask import Flask, request, jsonify
from BatchCreation import createDefaultArgs,createMailBodyStr,createImportStmnt,createNewDag,creatingTask, createConnObjectStr, getOwnerInfoStr, createListOfRecipitents, createEmailFunc,getAuthTokenStr,getMicroserviceInvocation,createTaskFlow, creatingSeqBatch, creatingMicroserviceToInvoke
from Roles import createViewerRole, createAdminRole, createExecutorRole
from solartisMicroservices import updateScheduleInterval

app = Flask(__name__)

file_path='config.ini'
config = configparser.ConfigParser()
config.read(file_path)

tasks =["createDBConnectionPoolObject","getOwnerInfoFromPoolObject","checkHoliday","holidayEmail","getAuthToken","onSuccessEmail"]

conn = mysql.connector.connect(
    host=config.get('BatchInfoDB', 'hostname'),
    user=config.get('BatchInfoDB', 'username'),
    password=config.get('BatchInfoDB', 'password'),
    database=config.get('BatchInfoDB', 'database')
)

cursor = conn.cursor()
head = {"Authorization":"Basic YWRtaW46YWlyZmxvd0AxMjM="}

@app.route('/NodeHealthCheck', methods=['GET'])
def NodeHealthCheck():
   return "Service is UP"

@app.route('/createUser', methods=['POST'])
def createUser():
   url = "http://10.200.18.62:8080/api/v1/users"
   request_body = request.get_json()
   try:
      response = requests.post(url,json=request_body,headers=head)
      if response.status_code // 100 == 2:
          return jsonify(f'Hiii, {request_body["first_name"]}{request_body["last_name"]} profile created successfully \nResponse: {response.text}')
      else:
          return jsonify(f'Error in Creating Profile.\n Status Code: {response.status_code}, Response: {response.text}')
   except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/createRole', methods=['POST'])
def createRoleAdmin():
   batchList = []
   url = "http://10.200.18.62:8080/api/v1/roles"
   request_body = request.get_json()
   role = request_body["role"]
   roleName = request_body["name"]
   owner_id = request_body["owner_id"]

   query = f"""select batch_id from batch_info where owner_id='{owner_id}'"""
   cursor.execute(query)
   batchs = cursor.fetchall()
   
   for batch in batchs :
      batchList.append(batch[0])

   if(role.lower() == "admin"):
      req_body = createAdminRole(roleName, batchList)
   elif(role.lower() == "executor"):
      req_body = createExecutorRole(roleName, batchList)
   elif(role.lower() == "viewer"):
      req_body = createViewerRole(roleName, batchList)
      
   role_details = json.loads(req_body)
   try:
      response = requests.post(url,json=role_details,headers=head)
      if response.status_code // 100 == 2:
          return jsonify(f'To {roleName} {role} role is created successfully \nResponse: {response.text}')
      else:
          return jsonify(f'Error in creating Admin Role.\n Status Code: {response.status_code}, Response: {response.text}')
      
   except Exception as e:
        return jsonify({'error': str(e)})

   

@app.route('/createBatch', methods=['POST'])
def createBatch():
    str_dag = f"""
"""
    taskList=[]
    taskNameList=[]
    seqBatchList=[]
    try:
        # Get data from the JSON payload
        data = request.get_json()
        # Extract directory path and file name from the JSON payload
        file_name = data.get('batch_name', '')+".py"
      #   tasks = data.get('tasks', [])
        batch_seq=data.get('seq_batch',[])  
        def_args=data.get('def_args','')
        dag_info = data.get('batch_info','')
        microserviceToInvoke = data.get('microserviceToInvoke','')

        # Combine the directory path and file name
        full_path = os.path.join("Z:\\dags", file_name)

        # Create the file with the specified content
        with open(full_path, "w") as file:
            file.write(createImportStmnt())
            file.write(createListOfRecipitents(def_args))
            file.write(createMailBodyStr(dag_info, def_args))
            file.write(createEmailFunc(dag_info))
            file.write(createConnObjectStr())
            file.write(getOwnerInfoStr())
            file.write(getAuthTokenStr())
            # file.write(getMicroserviceInvocation())
            # for item in tasks:
            #    file.write("from OverAllTasks import "+str(item) + '\n')
            file.write(createDefaultArgs(def_args))  
            file.write(createNewDag(dag_info))
            creatingTask(tasks,taskList)
            creatingMicroserviceToInvoke(microserviceToInvoke,taskList, seqBatchList)
            creatingSeqBatch(batch_seq,taskList, seqBatchList)    
            for item_ in taskList:
               file.write(str(item_) + '\n') 
            file.write(createTaskFlow(seqBatchList))
        cursor.execute('INSERT INTO batch_info (owner_id,batch_id) VALUES (%s, %s)', (def_args["owner"],dag_info["batch_id"]))
        conn.commit()
        response = {'status': 'success', 'message': f"Dag '{full_path}' created successfully.","owner":def_args.get('owner',' ')}
        print(str_dag)
        return jsonify(response)

    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return jsonify(response), 500


@app.route('/stopBatch', methods=['POST'])
def stopBatch():
     body = request.get_json()
     batch_id=body["batch_id"]
     req_body={
"is_paused": True
}
     url = 'http://10.200.18.62:8080/api/v1/dags/'+batch_id
     try:
        response = requests.patch(url, json=req_body,headers=head)
          # Check if the request was successful (status code 2xx)
        if response.status_code // 100 == 2:
          return jsonify(f'{batch_id} is stoped successfully \nResponse: {response.text}')
        else:
          return jsonify(f'Error in POST request. Status Code: {response.status_code}, Response: {response.text}')

     except Exception as e:
        return jsonify({'error': str(e)})
     
@app.route('/startBatch', methods=['POST'])   
def startBatch():
     body = request.get_json()
     batch_id=body["batch_id"]
     req_body={
"is_paused": False
}
     head= {"Authorization":"Basic YWRtaW46YWlyZmxvd0AxMjM="}
     url = 'http://10.200.18.62:8080/api/v1/dags/'+batch_id
     try:
        response = requests.patch(url, json=req_body,headers=head)
          # Check if the request was successful (status code 2xx)
        if response.status_code // 100 == 2:
          return jsonify(f'{batch_id} is started successfully \nResponse: {response.text}')
        else:
          return jsonify(f'Error in POST request. Status Code: {response.status_code}, Response: {response.text}')

     except Exception as e:
        return jsonify({'error': str(e)})
        
@app.route('/updateTime', methods=['POST'])
def updateTime():
   data = request.get_json()
   batch_id = data["batch_id"]
   new_schedule_interval = data["new_time"]
   return jsonify(updateScheduleInterval(batch_id,new_schedule_interval))




if __name__ == '__main__':
    app.run(debug=True)
