import requests

url = 'http://tangjaikonlakan.dyndns.org:8080/demo/isapi.dll/datasnap/rest/v1'
api_key = 'gihuFSYfpM8d3240k2ZS7J4z236g84'

headers = {'api-key': api_key}

# devicelist (GET)
response = requests.get(url + '/devicelist', headers=headers)
devices = response.json()

# SearchDevice (PUT)
search_data = {"device_id": "", "device_name": "", "serial_no": ""}
response = requests.put(url + '/SearchDevice', headers=headers, json=search_data)
result = response.json()

# UpdateDevice (PUT)
update_data = {"device_id": "ระบุรหัสอุปกรณ์", "device_name": "ชื่อใหม่"}
response = requests.put(url + '/UpdateDevice', headers=headers, json=update_data)
result = response.json()

# DeleteDevice (PUT)
delete_data = {"device_id": "ระบุรหัสอุปกรณ์"}
response = requests.put(url + '/DeleteDevice', headers=headers, json=delete_data)
result = response.json()

# Device (POST)
new_device_data = {"device_id": "รหัสอุปกรณ์", "device_name": "ชื่ออุปกรณ์ใหม่", "serial_no": "เลขซีเรียลใหม่"}
response = requests.post(url + '/Device', headers=headers, json=new_device_data)
result = response.json()