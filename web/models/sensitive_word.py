from django.db import models


class SensitiveWord(models.Model):
    kind_choices = ((0, '其他'), (1, '色情'), (2, '民生'), (3, '反动'), (4, '贪腐'), (5, '暴恐'))
    kind = models.SmallIntegerField(verbose_name='类别', choices=kind_choices, default=0)
    word = models.CharField(verbose_name='敏感词', max_length=32)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name_plural = '敏感词'
        app_label = 'web'
