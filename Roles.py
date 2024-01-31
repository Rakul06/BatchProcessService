def createAdminRole(roleName, listOfBatch):
     admin=f"""{"{"}
     "name":"{roleName}",
     "actions": [
          {{
               "action" : {{
                    "name" : "can_create"
               }},
               "resource" : {{
                    "name" : "DAG Runs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "DAG Runs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_edit"
               }},
               "resource" : {{
                    "name" : "DAG Runs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "DAG Runs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Browse"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Jobs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Jobs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Audit Logs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Audit Logs"
               }}
          }},
          
          {{
               "action" : {{
                    "name" : "can_create"
               }},
               "resource" : {{
                    "name" : "Task Instances"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Task Instances"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_edit"
               }},
               "resource" : {{
                    "name" : "Task Instances"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Task Instances"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "DAG Dependencies"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Documentation"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Docs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "ImportError"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "DAG Code"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "DAG Warnings"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "DAG Dependencies"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Task Logs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Website"
               }}
          }},
          {{
               "action":{{
                    "name" : "can_edit"
               }},
               "resource" : {{
                    "name" : "Passwords"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Passwords"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_edit"
               }},
               "resource" : {{
                    "name" : "My Password"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "My Password"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_edit"
               }},
               "resource" : {{
                    "name" : "My Profile"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "My Profile"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_create"
               }},
               "resource" : {{
                    "name" : "Users"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Users"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_edit"
               }},
               "resource" : {{
                    "name" : "Users"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_delete"
               }},
               "resource" : {{
                    "name" : "Users"
               }}

          }},
          {{
               "action":{{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Users"
               }}

          }},
          {{
               "action":{{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Security"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_create"
               }},
               "resource" : {{
                    "name" : "Roles"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Roles"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_edit"
               }},
               "resource" : {{
                    "name" : "Roles"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_delete"
               }},
               "resource" : {{
                    "name" : "Roles"
               }}

          }},
          {{
               "action":{{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Roles"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "User Stats Chart"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Permissions"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "View Menus"
               }}

          }},
          {{
               "action":{{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Resources"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Permission Views"
               }}

          }},
          {{
               "action":{{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Permission Pairs"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_create"
               }},
               "resource" : {{
                    "name" : "DAG Runs"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_delete"
               }},
               "resource" : {{
                    "name" : "DAG Runs"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_create"
               }},
               "resource" : {{
                    "name" : "Variables"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Variables"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_edit"
               }},
               "resource" : {{
                    "name" : "Variables"
               }}

          }},
          {{
               "action":{{
                    "name" : "can_delete"
               }},
               "resource" : {{
                    "name" : "Variables"
               }}

          }},
          {{
               "action":{{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Variables"
               }}

          }},
          {{
               "action":{{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Admin"
               }}

          }},
          {{
               "action":{{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Admin"
               }}

          }},
          {{
               "action" : {{
                    "name" : "can_delete"
               }},
               "resource" : {{
                    "name" : "Task Instances"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Task Reschedules"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Task Reschedules"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Triggers"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Triggers"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Configurations"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Configurations"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_create"
               }},
               "resource" : {{
                    "name" : "Connections"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Connections"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_edit"
               }},
               "resource" : {{
                    "name" : "Connections"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_delete"
               }},
               "resource" : {{
                    "name" : "Connections"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Connections"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "SLA Misses"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "SLA Misses"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Plugins"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Plugins"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Providers"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Providers"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_create"
               }},
               "resource" : {{
                    "name" : "Pools"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Pools"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_edit"
               }},
               "resource" : {{
                    "name" : "Pools"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_delete"
               }},
               "resource" : {{
                    "name" : "Pools"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Pools"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_create"
               }},
               "resource" : {{
                    "name" : "XComs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "XComs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_delete"
               }},
               "resource" : {{
                    "name" : "XComs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "XComs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "XComs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Cluster Activity"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Cluster Activity"
               }}
          }},
     
"""
     batch=""
     for batchItems in listOfBatch:
          dagAcess =f"""
{{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "DAG:{batchItems}"
               }}
          }},
{{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "DAG:{batchItems}"
               }}
          }},
{{
               "action" : {{
                    "name" : "can_edit"
               }},
               "resource" : {{
                    "name" : "DAG:{batchItems}"
               }}
          }},
{{
               "action" : {{
                    "name" : "can_delete"
               }},
               "resource" : {{
                    "name" : "DAG:{batchItems}"
               }}
          }},
"""
          batch = batch+dagAcess

     admin = admin + batch + f"""
     {"{}"}
    ]
{"}"}
"""
     return admin


def createExecutorRole(roleName, listOfBatch):
     dag=""
     executor = f"""{"{"}
     "name":"{roleName}",
     "actions": [
          {{
               "action" : {{
                    "name" : "can_create"
               }},
               "resource" : {{
                    "name" : "DAG Runs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "DAG Runs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_edit"
               }},
               "resource" : {{
                    "name" : "DAG Runs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "DAG Runs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Browse"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Jobs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Jobs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Audit Logs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Audit Logs"
               }}
          }},
          
          {{
               "action" : {{
                    "name" : "can_create"
               }},
               "resource" : {{
                    "name" : "Task Instances"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Task Instances"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_edit"
               }},
               "resource" : {{
                    "name" : "Task Instances"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Task Instances"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "DAG Dependencies"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Documentation"
               }}
          }},
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "Docs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "ImportError"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "DAG Code"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "DAG Warnings"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "DAG Dependencies"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "DAG Dependencies"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Task Logs"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "Website"
               }}
          }}
     """
     for batchItems in listOfBatch:
          dagAcess =f"""
,
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "DAG:{batchItems}"
               }}
          }},
		  {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "DAG:{batchItems}"
               }}
          }},
          {{
               "action" : {{
                    "name" : "can_edit"
               }},
               "resource" : {{
                    "name" : "DAG:{batchItems}"
               }}
          }}

"""
          dag += dagAcess
          
     executor = executor + dag + f"""
    ]
{"}"}
"""
     return executor

def createViewerRole(roleName, listOfBatch):

     viewer =f"""{"{"}
     "name": "{roleName}",
     "actions": [
     {{
          "action": {{
          "name": "can_read"
          }},
          "resource": {{
          "name": "My Password"
          }}
     }},
     {{
          "action": {{
          "name": "can_read"
          }},
          "resource": {{
          "name": "DAG Runs"
          }}
     }},
     {{
          "action": {{
          "name": "menu_access"
          }},
          "resource": {{
          "name": "DAG Runs"
          }}
     }},
     {{
          "action": {{
          "name": "menu_access"
          }},
          "resource": {{
          "name": "Browse"
          }}
     }},
     {{
          "action": {{
          "name": "can_read"
          }},
          "resource": {{
          "name": "Jobs"
          }}
     }},
          {{
          "action": {{
          "name": "menu_access"
          }},
          "resource": {{
          "name": "Jobs"
          }}
     }},
          {{
          "action": {{
          "name": "can_read"
          }},
          "resource": {{
          "name": "Audit Logs"
          }}
     }},
          {{
          "action": {{
          "name": "menu_access"
          }},
          "resource": {{
          "name": "Audit Logs"
          }}
     }},
     {{
          "action": {{
          "name": "can_read"
          }},
          "resource": {{
          "name": "Task Instances"
          }}
     }},
          {{
          "action": {{
          "name": "menu_access"
          }},
          "resource": {{
          "name": "Task Instances"
          }}
     }},
     {{
          "action": {{
          "name": "can_read"
          }},
          "resource": {{
          "name": "SLA Misses"
          }}
     }},
     {{
          "action": {{
          "name": "menu_access"
          }},
          "resource": {{
          "name": "SLA Misses"
          }}
     }},
     {{
          "action": {{
          "name": "can_read"
          }},
          "resource": {{
          "name": "Plugins"
          }}
     }},
          {{
          "action": {{
          "name": "menu_access"
          }},
          "resource": {{
          "name": "Plugins"
          }}
     }},
     {{
          "action": {{
          "name": "can_read"
          }},
          "resource": {{
          "name": "XComs"
          }}
     }},
     {{
          "action": {{
          "name": "menu_access"
          }},
          "resource": {{
          "name": "DAG Dependencies"
          }}
     }},
     {{
          "action": {{
          "name": "menu_access"
          }},
          "resource": {{
          "name": "Cluster Activity"
          }}
     }},
     {{
          "action": {{
          "name": "menu_access"
          }},
          "resource": {{
          "name": "Datasets"
          }}
     }},
     {{
          "action": {{
          "name": "menu_access"
          }},
          "resource": {{
          "name": "Documentation"
          }}
     }},
     {{
          "action": {{
          "name": "menu_access"
          }},
          "resource": {{
          "name": "Docs"
          }}
     }},
     {{
          "action": {{
          "name": "can_read"
          }},
          "resource": {{
          "name": "Datasets"
          }}
     }},
     {{
          "action": {{
          "name": "can_read"
          }},
          "resource": {{
          "name": "ImportError"
          }}
     }},
     {{
          "action": {{
          "name": "can_read"
          }},
          "resource": {{
          "name": "DAG Code"
          }}
     }},
     {{
          "action": {{
          "name": "can_read"
          }},
          "resource": {{
          "name": "DAG Warnings"
          }}
     }},
     {{
          "action": {{
          "name": "can_read"
          }},
          "resource": {{
          "name": "DAG Dependencies"
          }}
     }},
     {{
          "action": {{
          "name": "can_read"
          }},
          "resource": {{
          "name": "Cluster Activity"
          }}
     }},
     {{
          "action": {{
          "name": "can_read"
          }},
          "resource": {{
          "name": "Task Logs"
          }}
     }},
     {{
          "action": {{
          "name": "can_read"
          }},
          "resource": {{
          "name": "Website"
          }}
     }}"""

     dag=f""""""


     for batchItems in listOfBatch:
          dagAcess =f"""
,
          {{
               "action" : {{
                    "name" : "menu_access"
               }},
               "resource" : {{
                    "name" : "DAG:{batchItems}"
               }}
          }},
		  {{
               "action" : {{
                    "name" : "can_read"
               }},
               "resource" : {{
                    "name" : "DAG:{batchItems}"
               }}
          }}

"""
          dag += dagAcess
     viewer = viewer + dag + f"""
    ]
{"}"}
"""
     return viewer
