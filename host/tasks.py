#host/tasks.py
import psutil
from celery import shared_task

from host.models import UserCpuPercent

@shared_task()
def scan_cpu_info():
    percent = UserCpuPercent( user_percent=psutil.cpu_times_percent().user)
    percent.save()