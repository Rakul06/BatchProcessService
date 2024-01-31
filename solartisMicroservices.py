import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from flask import Flask, jsonify
import requests
import fileinput
import re

app = Flask(__name__)

microservices = {
     "AutomatedLapseSubmission":["https://ucicommonwfkbv6-11.solartis.net/KnowledgeEngineV6_11/KnowledgeBase/FireEventV4","BatchAutoLapseSubmission_WF_1.0.0.1","AutomatedLapseSubmission"],
     "AutomatedLapseQuote":["https://ucicommonwfkbv6-11.solartis.net/KnowledgeEngineV6_11/KnowledgeBase/FireEventV4","BatchAutoLapseQuote_WF_1.0.0.1","AutomatedLapseQuote"],
     "AutomatedInspectionCancelEmail":["https://uciorchidwfkbv6-11.solartis.net/KnowledgeEngineV6_11/KnowledgeBase/FireEventV3","BatchInspectionCancelEmail_WF_1.0.0.1","AutomatedInspectionCancelEmail"],
     "AutomatedInspectionStatusAndReport":["https://uciorchidwfkbv6-11.solartis.net/KnowledgeEngineV6_11/KnowledgeBase/FireEventV3","InvokeInspectionStatusCheck_WF_1.0.0.1","AutomatedInspectionStatusAndReport"],
     "AutomatedVoidPolicy":["https://uciorchidwfkbv6-11.solartis.net/KnowledgeEngineV6_11/KnowledgeBase/FireEventV3","InvokeVoidPolicyBatchProcess_WF_1.0.0.1","AutomatedVoidPolicy"],
     "AutomatedCancelPolicy":["https://uciorchidwfkbv6-11.solartis.net/KnowledgeEngineV6_11/KnowledgeBase/FireEventV3","InvokeCancelPolicyBatchProcess_WF_1.0.0.1","AutomatedCancelPolicy"],
     "AutomatedSendPolicyData":["https://uciorchidwfkbv6-11.solartis.net/KnowledgeEngineV6_11/KnowledgeBase/FireEventV3","InvokeSendPolicyData_WF_1.0.0.1","AutomatedSendPolicyData"],
     "AutomatedDocumentForPrinting":["https://uciorchidwfkbv6-11.solartis.net/KnowledgeEngineV6_11/KnowledgeBase/FireEventV4","InvokeBatchDocumentForPrinting_WF_1.0.0.1","AutomatedDocumentForPrinting"]
}

def send_email(subject, body, to_email, attachment_path=None):
    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = 'rakulb0605@gmail.com'  # Replace with your Gmail address
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach body to the email
    msg.attach(MIMEText(body, 'plain'))

    # Attach a file if specified
    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            part = MIMEApplication(attachment.read(), Name="attachment_name.txt")  # Replace with the desired attachment name
            part['Content-Disposition'] = f'attachment; filename="{part["Name"]}"'
            msg.attach(part)

    # Connect to the SMTP server (in this case, Gmail's SMTP server)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('rakulb0605@gmail.com', 'jcbk zuqx tfkh dxeb')  # Replace with your Gmail credentials
        server.sendmail('rakulb0605@gmail.com', to_email, msg.as_string())
        print("Mail Sent Successfully")



def getResponse(microservice_to_invoke,email):
     try:
          with app.app_context():
               url=microservices[microservice_to_invoke][0]
               eventName=microservices[microservice_to_invoke][1]
               userName=microservices[microservice_to_invoke][2]
               req_body={
                    "OwnerId": "4742",
                    "ServiceRequestDetail": {
                         "OwnerId": "4742",
                         "EndClientUserUniqueSessionId": "1.0",
                         "ServiceRequestVersion": "1.0",
                         "LanguageCode": "en",
                         "UserName": userName,
                         "RegionCode": "US",
                         "ServiceResponseVersion": "1.0",
                         "ResponseType": "json",
                         "Token": "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",
                         "Lob": "PL",
                         "BrowserIp": "192.158.1.38.",
                         "UserRole": "Underwriter",
                         "RMSModeledPremium": "425.21"
                    },
                    "EventName": eventName,
                    "ProductNumber": "PL_4742_12",
                    "ProductVerNumber": "PL_4742_12_V1"
                         }

               headers = {
                         'EventName':eventName,
                         'OwnerId':'4742',
                         'Token':'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',
                         'Environment': '15',
                         'Mode':'LIVE' 
                         }
               response = requests.post(url, json=req_body,headers=headers)
               if response.status_code // 100 == 2:
                    print("working")
                    send_email("Notification for Batch Job",f'Successful POST request!\nResponse: {response.text}',email)
                    return jsonify(f'Successful POST request!\nResponse: {response.text}')
                    # print(f'Successful POST request! Response: {response.text}')
               else:
                    send_email("Alert Task Failed",f'Error in POST request.\nStatus Code: {response.status_code},\nResponse: {response.text}',email)
                    return jsonify(f'Error in POST request. Status Code: {response.status_code}, Response: {response.text}')
                    #print(f'Error in POST request. Status Code: {response.status_code}, Response: {response.text}')
     except Exception as e:
        return jsonify({'error': str(e)})


def getAuthToken_(uname, password,url):
     url = url
     # JSON data to be sent in the POST request
     req_body = {
     "ServiceRequestDetail": {
          "OwnerId": "4742",
          "ResponseType": "JSON",
          "BrowserIp": "192.168.5.98",
          "ServiceRequestVersion": "2.0"
     },
     "UserCredential": {
          "UserName":uname,
          "Password": password
     }
     }

     # Headers for the request (if needed)
     headers = {
     'Environment': '15',
     'Mode':'LIVE' 
     }

     # Make the POST request with JSON data and headers
     response = requests.post(url, json=req_body, headers=headers)

     # Check the response
     if response.status_code == 200:
          print("POST request successful!")
          print("Response content:", response.json())
          res_json = response.json()
          return res_json['Token']

     else:
          print(f"POST request failed with status code {response.status_code}")
          print("Error content:", response.text)

def updateScheduleInterval(dag_id,new_schedule_interval):
     # Specify the DAG file path and DAG ID
     dag_file_path = f'Z:\\dags\\{dag_id}.py'
     # Pattern to search for in the DAG file
     pattern = re.compile(r"schedule_interval\s*=\s*'[^\']*'", re.MULTILINE)
     # Replacement string with the new schedule interval
     replacement = f"schedule_interval = '{new_schedule_interval}'"
     # Open the DAG file and perform the replacement
     with fileinput.FileInput(dag_file_path, inplace=True) as file:
          for line in file:
               print(re.sub(pattern, replacement, line), end='')

     return(f"Schedule interval for Batch '{dag_id}' updated to '{new_schedule_interval}' in '{dag_file_path}'.")
