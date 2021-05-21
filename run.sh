#!/bin/bash


# 1. kill all process
echo "----KILL PROCESS----"
ps auxww | grep 'flaskdemo/venv/bin/celery' | awk '{print $2}' | xargs kill -9
ps auxww | grep 'flaskdemo/venv/bin/supervisor' | awk '{print $2}' | xargs kill -9
ps auxww | grep 'flaskdemo/venv/bin/gunicorn' | awk '{print $2}' | xargs kill -9


# 2.start all task
echo "----START ALL TASKS----"
cd /home/wangzy/startweb/flaskdemo/deploy/supervisor
/home/wangzy/startweb/flaskdemo/venv/bin/supervisord -c  supervisord.conf
/home/wangzy/startweb/flaskdemo/venv/bin/supervisorctl  start all