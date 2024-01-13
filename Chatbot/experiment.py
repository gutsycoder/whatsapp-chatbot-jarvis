import requests

url = "https://www.fast2sms.com/dev/bulk"


querystring = {"authorization":"nap0VxTCMcK4wd6SNBQOAofH1jDi2ezZPXErRu7mG9vtk3UWqYadbmuoelZFQI45DwCR0KnzMyY386Hc","sender_id":"FSTSMS","message":"Hello, From Suyash.","language":"english","route":"p","numbers":"6387799112"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
