#celery -A sysinfo beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
#celery worker -A taskproj -l debug   linux下的启动worker命令
Celery -A sysinfo worker -l info -P eventlet