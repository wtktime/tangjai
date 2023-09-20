from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# เรียกใช้ API
url = 'http://tangjaikonlakan.dyndns.org:8080/demo/isapi.dll/datasnap/rest/v1'
api_key = 'gihuFSYfpM8d3240k2ZS7J4z236g84'
headers = {'api-key': api_key}

@app.route("/")
def index():
    # devicelist (GET)
    response = requests.get(url + '/devicelist', headers=headers)
    devices = response.json()
    return render_template("index.html", devices=devices)

@app.route("/search", methods=["POST"])
def search():
    # SearchDevice (PUT)
    search_data = {"device_id": request.form["device_id"], "device_name": request.form["device_name"], "serial_no": request.form["serial_no"]}
    response = requests.put(url + '/SearchDevice', headers=headers, json=search_data)
    result = response.json()
    return render_template("search.html", result=result)

@app.route("/update", methods=["POST"])
def update():
    # UpdateDevice (PUT)
    update_data = {"device_id": request.form["device_id"], "device_name": request.form["device_name"]}
    response = requests.put(url + '/UpdateDevice', headers=headers, json=update_data)
    result = response.json()
    return render_template("update.html", result=result)

@app.route("/delete", methods=["POST"])
def delete():
    # DeleteDevice (PUT)
    delete_data = {"device_id": request.form["device_id"]}
    response = requests.put(url + '/DeleteDevice', headers=headers, json=delete_data)
    result = response.json()
    return render_template("delete.html", result=result)

@app.route("/add", methods=["POST"])
def add():
    # Device (POST)
    new_device_data = {"device_id": request.form["device_id"], "device_name": request.form["device_name"], "serial_no": request.form["serial_no"]}
    response = requests.post(url + '/Device', headers=headers, json=new_device_data)
    result = response.json()
    return render_template("add.html", result=result)

if __name__ == "__main__":
    app.run()