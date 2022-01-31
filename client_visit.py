import requests
import json
url_token = "https://api.mindbodyonline.com/public/v6/usertoken/issue"
payload_token = json.dumps({
"Username": "Siteowner",
"Password": "apitest1234"
})
headers_token = {
'User-Agent': 'DashboardLim-Splunk-Dev',
'Content-Type': 'application/json',
'Api-Key': '0ef989559ac444549755ba4e2a9cbd19',
'SiteId': '-99',
}
response_token = requests.request("POST", url_token, headers=headers_token, data=payload_token)
response_token_json=response_token.json()
token=""
for i in response_token_json:
    token=response_token_json["AccessToken"]
# print(token)
# print(json.dumps(r,indent=4))
headers_client = {
    'User-Agent': 'DashboardLim-Splunk-Dev',
    'Authorization': token,
    'Api-Key': '0ef989559ac444549755ba4e2a9cbd19',
    'Content-Type': 'application/json',
    'SiteId': '-99',
}

url_client = "https://api.mindbodyonline.com/public/v6/client/clients"
response_client = requests.request("GET", url_client, headers=headers_client)
response_client_json=response_client.json()
total_result = response_client_json.get("PaginationResponse").get("TotalResults")
# total_result=200
offset = 0
count=0
Id=[]
while offset <= total_result:
    url_clients = "https://api.mindbodyonline.com/public/v6/client/clients?limit=200&offset="+str(offset)
    # print(url_clients)
    response_clients = requests.request("GET", url_clients, headers=headers_client)
    response_clients_json=response_clients.json()
    offset+=200
    for j in response_clients_json["Clients"]:
        Id.append(str(j["Id"]))
        # count+=1
        # print(url_clients)
# print(Id)
# print(count)
for i in Id:
    try:
        url_clientvisit = "https://api.mindbodyonline.com/public/v6/client/clientvisits?ClientId="+i
        # print(url_clientvisit)
        response_clientvisit = requests.request("GET", url_clientvisit, headers=headers_client)
        response_clientvisit_json=response_clientvisit.json()
        for k in response_clientvisit_json["Visits"]:
            print(count)
        # print(url_clientvisit)
            count+=1
            print(json.dumps(k))
    except Exception as e:
        print(e)
        print(url_clientvisit)
# try:
#     # while offset <= total_result:
    
#         # cid = response_clientvisit_json.get("Clients").get("Id")
#         print(url_clients)
#         for i in response_clients_json["Clients"]:
#             url_clientvisit = "https://api.mindbodyonline.com/public/v6/client/clientvisit?ClientId="+str(i["Id"])
#             response_clientvisit = requests.request("GET", url_clientvisit, headers=headers_client)
#             response_clientvisit_json=response_clientvisit.json()
#             print(url_clientvisit)
#             # totalResult = response_clientvisit_json.get("PaginationResponse").get("TotalResults")
#             # if (not response_clientvisit_json):
#             #     pass
#             # else:
#                 # d.append(response_clientvisit_json)
#             # clientvisit_dataset.append(response_clientvisit_json)
#             print(i["Id"])
#             print(count)
#             # print(json.dumps(response_clientvisit_json))
            
#             count+=1
#         offset+=200      
#     # print(json.dumps(d))  
# except Exception as e:
#     print(e)
#     print(url_clientvisit)


