from django.db import models
# import django.utils.timezone as timezone


class Task(models.Model):
    """
    Model: 任务/日程
    Fields: 创建时间(created), 创建者(owner), 任务标题(title), 任务详情(detail),
            任务日期时间(date), 是否完成(isDone)
    """
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='tasks',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100, blank=True, default='No title')
    detail = models.TextField(blank=True, default='')
    date = models.DateTimeField(null=True)
    isDone = models.BooleanField(default=False)

    class Meta:
        ordering = ('created', )
