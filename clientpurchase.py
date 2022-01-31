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
headers_purchase = {
    'User-Agent': 'DashboardLim-Splunk-Dev',
    # 'Authorization': token,
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
        url_clientpurchase = "https://api.mindbodyonline.com/public/v6/client/clientpurchases?ClientId="+i
        # print(url_clientpurchase)
        response_clientpurchase = requests.request("GET", url_clientpurchase, headers=headers_purchase)
        response_clientpurchase_json=response_clientpurchase.json()
        for k in response_clientpurchase_json["Purchases"]:
            print(count)
        # print(url_clientpurchase)
            count+=1
            print(json.dumps(k))
    except Exception as e:
        print(e)
        print(url_clientpurchase)