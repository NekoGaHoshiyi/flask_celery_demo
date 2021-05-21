from flask import Flask
from flask import request
import json
import subprocess
from celery import Celery
import time
from gevent import monkey

monkey.patch_all()

celeryapp = Celery()
celeryapp.config_from_object('celery_config')

# create a flask app, indicates its package __name__
getfile = Flask(__name__)

@celeryapp.task
def runcmd(line):
    time.sleep(10)
    process = subprocess.Popen(line.split(), stdout = subprocess.PIPE, encoding='utf-8')
    output, _ = process.communicate()
    return output
# via deco,binds view to url
@getfile.route('/index', methods=["POST"])
def index():
    data = request.data
    data_str = data.decode("utf-8")
    data_dic = json.loads(data_str)
    line = data_dic['line']
    #runcmd(line)
    output = runcmd.apply_async((line,))
    return '200 OK'


# start the app
if __name__ == '__main__':
    getfile.run()
