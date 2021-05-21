import requests
import json
api_url = "http://127.0.0.1:9102/index"
headers = {"Content-Type": "application/json"}
raw_data_dir = "/mnt/seqdata/raw_data"
for i in range(1000):
    data = '{{"line": "touch /home/wangzy/startweb/flaskdemo/dir/text{num}.txt"}}'.format(num = i)
    response = requests.post(url=api_url, headers=headers, data=data)
    print(response.text)