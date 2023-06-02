from django.db import models

from web.models.keyword import Keyword


class Course(models.Model):
    course = models.CharField(verbose_name='课程', max_length=32)
    img = models.ImageField(verbose_name='图片', upload_to='course/img/', default='course/img/default.jpg')
    profile = models.TextField(verbose_name='课程简介', default='暂无简介')
    teacher = models.ForeignKey(verbose_name='教师', to='Teacher', on_delete=models.CASCADE)
    keyword = models.ManyToManyField(verbose_name='关键词', to=Keyword, blank=True)

    def __str__(self):
        return self.course

    def profile_80(self):
        if len(self.profile) > 80:
            return f'{self.profile[:80]}......'
        else:
            return self.profile

    class Meta:
        verbose_name_plural = '课程'
        app_label = 'web'
