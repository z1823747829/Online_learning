from django.db import models


class Academy(models.Model):
    academy = models.CharField(verbose_name='学院', max_length=32)
    code = models.CharField(verbose_name='学院代码', max_length=6)
    img = models.ImageField(verbose_name='图片', upload_to='academy/', default='academy/default.jpg')
    profile = models.TextField(verbose_name='学院简介', default='暂无简介')

    def __str__(self):
        return self.academy

    def profile_80(self):
        if len(self.profile) > 80:
            return f'{self.profile[:80]}......'
        else:
            return self.profile

    class Meta:
        verbose_name_plural = '学院'
        app_label = 'web'
