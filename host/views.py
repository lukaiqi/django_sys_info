#host/views.py
from datetime import datetime
from django.shortcuts import render
import  psutil
import  os, platform
# Create your views here.

def index(request):
    """
    sys_name
    kernel_name
    kernel_no
    kernel_version
    sys_framework
    now_time
    boot_time
    up_time
    """
    try:
        info = os.uname()
    except Exception as e:
        info = platform.uname()
    sys_name = info.node
    kernel_name = info.system
    kernel_no = info.release
    kernel_version = info.version
    sys_framework = info.machine
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    now_time = datetime.now()
    print(boot_time, now_time)
    up_time = now_time - boot_time

    return  render(request, 'host/index.html', locals())

def user(request):
    users = psutil.users()
    return  render(request, 'host/user.html', locals())

def cpu(request):
    pass
    return  render(request, 'host/cpu.html', locals())

def memory(request):
    pass
    return  render(request, 'host/memory.html', locals())

def disk(request):
    pass
    return  render(request, 'host/disk.html', locals())

def network(request):
    pass
    return  render(request, 'host/network.html', locals())

def process(request):
    pass
    return  render(request, 'host/process.html', locals())
