from django.db import models

from web.utils.tools import md5_salt


class User(models.Model):
    nickname = models.CharField(verbose_name="昵称", max_length=32)
    uname = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    gender_choices = ((0, '未知'), (1, '男'), (2, '女'))
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices, default=0)
    birthday = models.DateField(verbose_name='出生日期', default='2000-1-1')
    phone = models.CharField(verbose_name='手机号码', max_length=20, blank=True, null=True)
    email = models.CharField(verbose_name='邮箱地址', max_length=64, blank=True, null=True)
    head = models.ImageField(verbose_name='头像', upload_to='head', default='head/default.jpg')

    def __str__(self):
        return self.uname

    def save(self, *args, **kwargs):
        if not User.objects.filter(id=self.id).exists() or self.password != User.objects.get(id=self.id).password:
            self.password = md5_salt(self.password)
        super(User, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = '用户'
        app_label = 'web'
