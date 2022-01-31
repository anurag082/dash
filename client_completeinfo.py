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
offset = 0
count=0
d=[]
try:
    # while offset <= total_result:
    for k in range(0,total_result):
        url_clients = "https://api.mindbodyonline.com/public/v6/client/clients?limit=200&offset="+str(offset)
        response_clients = requests.request("GET", url_clients, headers=headers_client)
        response_clients_json=response_clients.json()
        # cid = response_clientcompleteinfo_json.get("Clients").get("Id")
        print(url_clients)
        for i in response_clients_json["Clients"]:
            url_clientcompleteinfo = "https://api.mindbodyonline.com/public/v6/client/clientcompleteinfo?ClientId="+str(i["Id"])
            response_clientcompleteinfo = requests.request("GET", url_clientcompleteinfo, headers=headers_client)
            response_clientcompleteinfo_json=response_clientcompleteinfo.json()
            print(url_clientcompleteinfo)
            # totalResult = response_clientcompleteinfo_json.get("PaginationResponse").get("TotalResults")
            # if (not response_clientcompleteinfo_json):
            #     pass
            # else:
                # d.append(response_clientcompleteinfo_json)
            # clientcompleteinfo_dataset.append(response_clientcompleteinfo_json)
            print(i["Id"])
            print(count)
            # print(json.dumps(response_clientcompleteinfo_json))
            
            count+=1
        offset+=200      
    # print(json.dumps(d))  
except Exception as e:
    print(e)
    print(url_clientcompleteinfo)


