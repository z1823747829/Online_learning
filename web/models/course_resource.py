from django.db import models

from web.models import MyFileField


class CourseResource(models.Model):
    resource = models.CharField(verbose_name='分段名', max_length=64)
    resource_file = MyFileField(verbose_name='学习资源', upload_to='course/resource/',
                                content_types=['application/pdf', 'video/mp4', 'video/*'],
                                max_upload_size=1024 * 1024 * 200,
                                default='course/resource/default.pdf')
    course = models.ForeignKey(verbose_name='课程', to='Course', on_delete=models.CASCADE)
    order = models.SmallIntegerField(verbose_name="次序", default=1)

    def __str__(self):
        return self.resource

    class Meta:
        verbose_name_plural = '课程资源'
        app_label = 'web'


class CourseResourceTime(models.Model):
    user = models.ForeignKey(verbose_name='用户', to='User', on_delete=models.CASCADE)
    course_resource = models.ForeignKey(verbose_name='课程资源', to='CourseResource', on_delete=models.CASCADE)
    time = models.FloatField(verbose_name='时间')

    class Meta:
        app_label = 'web'
