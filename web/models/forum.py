import os

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from mdeditor.fields import MDTextField

from web.models import MyFileField
from web.models.keyword import Keyword

KB = 1024
MB = 1024 * 1024


class Forum(models.Model):
    user = models.ForeignKey(verbose_name='用户', to='User', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='标题', max_length=128)
    profile = models.TextField(verbose_name='简介', max_length=128)
    rtf_content = RichTextUploadingField(verbose_name='富文本格式内容', config_name='default', blank=True, null=True)
    md_content = MDTextField(verbose_name="Markdown格式内容", blank=True, null=True)
    content_type_choices = ((0, '富文本'), (1, 'Markdown'))
    content_type = models.SmallIntegerField(choices=content_type_choices, default=0)
    annex = MyFileField(verbose_name='附件', upload_to='forum/annex/', max_upload_size=100 * MB, blank=True, null=True)
    keyword = models.ManyToManyField(verbose_name='关键词', to=Keyword, blank=True)
    time = models.DateTimeField(verbose_name="发贴时间", auto_now_add=True)
    status_choices = ((0, '待审核'), (1, '审核通过'), (2, '含有敏感字段'), (3, '退回'),)
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '论坛'
        app_label = 'web'


class ForumImg(models.Model):
    img = models.ImageField(verbose_name='图片', upload_to='forum/img/')

    class Meta:
        app_label = 'web'
