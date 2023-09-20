import requests

url = "http://tangjaikonlakan.dyndns.org:8080/demo/isapi.dll/datasnap/rest/v1/About"

headers = {
    "api-key": "gihuFSYfpM8d3240k2ZS7J4z236g84"
}

response = requests.get(url, headers=headers)

result = response.json()

print(result)