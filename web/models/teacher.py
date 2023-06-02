from django.db import models


class Teacher(models.Model):
    name = models.CharField(verbose_name='教师', max_length=32)
    academy = models.ForeignKey(verbose_name='学院', to='Academy', on_delete=models.CASCADE)
    code = models.CharField(verbose_name="职工编号", max_length=64, default='123456')
    professional_title_choices = ((0, '讲师'), (1, '副教授'), (2, '教授'),)
    professional_title = models.SmallIntegerField(verbose_name='职称', choices=professional_title_choices, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '教师'
        app_label = 'web'
