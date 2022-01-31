# encoding = utf-8

import os
import sys
import time
import datetime
import requests
import json

'''
    IMPORTANT
    Edit only the validate_input and collect_events functions.
    Do not edit any other part in this file.
    This file is generated only once when creating the modular input.
'''
'''
# For advanced users, if you want to create single instance mod input, uncomment this method.
def use_single_instance_mode():
    return True
'''

def validate_input(helper, definition):
    """Implement your own validation logic to validate the input stanza configurations"""
    # This example accesses the modular input variable
    # username = definition.parameters.get('username', None)
    # password = definition.parameters.get('password', None)
    # user_agent = definition.parameters.get('user_agent', None)
    # api_key = definition.parameters.get('api_key', None)
    # siteid = definition.parameters.get('siteid', None)
    # password = definition.parameters.get('password', None)
    pass

def collect_events(helper, ew):
    
    opt_username = helper.get_global_setting('username')
    opt_password = helper.get_global_setting('password')
    opt_app_source_name = helper.get_global_setting('app_source_name')
    opt_api_key = helper.get_global_setting('api_key')
    opt_siteid = helper.get_global_setting('siteid')
  
    
    
    ########################### Getting Token ######################################################
    url_token = "https://api.mindbodyonline.com/public/v6/usertoken/issue"
    payload_token = json.dumps({
        "Username": opt_username,
        "Password": opt_password
    })
    headers_token = {
        'User-Agent': opt_app_source_name,
        'Content-Type': 'application/json',
        'Api-Key': opt_api_key,
        'SiteId': opt_siteid,
    }
    response_token = requests.request("POST", url_token, headers=headers_token, data=payload_token)
    response_token_json=response_token.json()
    token=""
    for i in response_token_json:
        token=response_token_json["AccessToken"]
        
    ############################### Purchase API #########################################################

    headers_client = {
        'User-Agent': opt_app_source_name,
        'Api-Key': opt_api_key,
        'Authorization': token,
        'Content-Type': 'application/json',
        'SiteId': opt_siteid
    }
    
    # clientpurchases_dataset=[]
    url_client = "https://api.mindbodyonline.com/public/v6/client/clients"
    response_client = requests.request("GET", url_client, headers=headers_client)
    response_client_json=response_client.json()
    total_result = response_client_json.get("PaginationResponse").get("TotalResults")
    offset = 0
    count=0
    while offset <= total_result:
        url_clients = f"https://api.mindbodyonline.com/public/v6/client/clients?limit=200&offset={offset}"
        response_clients = requests.request("GET", url_clients, headers=headers_client)
        response_clients_json=response_clients.json()
        total_result1 = response_client_json.get("PaginationResponse").get("TotalResults")
        if total_result1 != 0:
            for i in response_clients_json["Clients"]:
                url_clientpurchases = "https://api.mindbodyonline.com/public/v6/client/clientpurchases?ClientId="+str(i["Id"])
                response_clientpurchases = requests.request("GET", url_clientpurchases, headers=headers_client)
                response_clientpurchases_json=response_clientpurchases.json()
                for j in response_clientpurchases_json["Purchases"]:
                # clientpurchases_dataset.append(j)
                    event = helper.new_event(json.dumps(j,indent=2))
                    ew.write_event(event)
                    count+=1
        offset+=200
                # state = helper.get_check_point(str(j['Sale'].get('Id')))
            # if state is None:
            #     clientpurchases_dataset.append(j)
            #     helper.save_check_point(str(j['Sale'].get('Id')), "Indexed")
            # helper.delete_check_point(str(j['Sale'].get('Id')))
   
 
    status = response_clientpurchases.status_code
    # count = len(clientpurchases_dataset)
    status = "API="+"https://api.mindbodyonline.com/public/v6/client/clientpurchases"+" | response_code="+str(status)+" | number_of_events="+str(count)
    helper.log_info(status)
    # event = helper.new_event(json.dumps(clientpurchases_dataset,indent=2))
    # ew.write_event(event)

      
   
