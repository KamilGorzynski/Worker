from sched import scheduler
from time import time, sleep
from urllib import request
from socket import timeout
from django import setup
import os
import datetime

# Settings configure
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GWP_API.settings")
setup()

from Main.models import UrlObject, RequestHistory


def send_request_task(sc, url_object, interval, url):
    try:
        start = datetime.datetime.now()
        response = request.urlopen(url, timeout=5).read().decode('utf-8')
        end = datetime.datetime.now()
        duration = (end - start).microseconds
    except timeout:
        response = None
        duration = 10000000
    except ValueError:
        response = None
        duration = 0

    RequestHistory.objects.create(
        url_object=url_object,
        response=response,
        duration=duration,
        created_at=datetime.datetime.now()
    )

    worker.enter(interval, 1, send_request_task, (sc, url_object, interval, url))


def make_tasks():
    """Function make send_request_task for every single UrlObject from DB"""
    tasks = UrlObject.objects.all()
    for task in tasks:
        worker.enter(task.interval, 1, send_request_task, (worker, task, task.interval, task.url))


if __name__ == '__main__':
    worker = scheduler(time, sleep)
    make_tasks()
    worker.run()
