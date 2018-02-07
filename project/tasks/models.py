from django.db import models
# import django.utils.timezone as timezone


class Plan(models.Model):
    """
    Model: 计划
    """
    created_datetime = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='plans',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100, blank=True, default='No name')
    detail = models.TextField(blank=True, default='')

    class Meta:
        ordering = ('created_datetime', )


class Tag(models.Model):
    """
    Model: 标签
    """
    created_datetime = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='tags',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100, blank=True, default='No name')


class Task(models.Model):
    """
    Model: 任务/日程
    Fields: 创建时间(created), 创建者(owner), 任务标题(title), 任务详情(detail),
            任务日期时间(date), 是否完成(isDone)
    """
    created_datetime = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='tasks',
        on_delete=models.CASCADE
    )

    plan = models.ForeignKey(
        Plan,
        related_name='tasks',
        on_delete=models.CASCADE,
        null=True
    )
    title = models.CharField(max_length=100, blank=True, default='No title')
    content = models.TextField(blank=True, default='')
    label = models.IntegerField(null=True)
    tags = models.ManyToManyField(
        Tag,
        related_name='tasks',
    )

    is_finished = models.BooleanField(default=False)
    finished_datetime = models.DateTimeField(null=True, default=None)

    is_all_day = models.BooleanField(default=True)
    begin_datetime = models.DateTimeField(null=True, default=None)
    end_datetime = models.DateTimeField(null=True, default=None)

    class Meta:
        ordering = ('created_datetime', )


class Account(models.Model):
    """
    Model: 账户信息
    """
    user = models.OneToOneField(
        'auth.User',
        related_name='account',
        on_delete=models.CASCADE
    )
    nickname = models.CharField(max_length=100, blank=True, default='No name')
