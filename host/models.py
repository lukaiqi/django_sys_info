from django.db import models
# 定时任务定期扫描并存储。
class UserCpuPercent(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="扫描时间")
    user_percent = models.FloatField(verbose_name="用户CPU占用百分比")

