from django.db import models


class CourseClick(models.Model):
    user = models.ForeignKey(verbose_name='用户', to='User', on_delete=models.CASCADE)
    course = models.ForeignKey(verbose_name='课程', to='Course', on_delete=models.CASCADE)
    time = models.DateTimeField(verbose_name="点击时间", auto_now_add=True)

    class Meta:
        app_label = 'web'
