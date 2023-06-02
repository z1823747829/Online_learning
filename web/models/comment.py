from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(verbose_name='用户', to='User', on_delete=models.CASCADE)
    course = models.ForeignKey(verbose_name='课程', to='Course', blank=True, null=True, on_delete=models.CASCADE)
    forum = models.ForeignKey(verbose_name='帖子', to='Forum', blank=True, null=True, on_delete=models.CASCADE)
    content = models.CharField(verbose_name="评论", max_length=128)
    time = models.DateTimeField(verbose_name="评论时间", auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = '评论'
        app_label = 'web'
