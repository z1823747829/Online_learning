from django.db import models


class Keyword(models.Model):
    keyword = models.CharField(verbose_name='关键词', max_length=32)

    def __str__(self):
        return self.keyword

    class Meta:
        verbose_name_plural = '关键词'
        app_label = 'web'
