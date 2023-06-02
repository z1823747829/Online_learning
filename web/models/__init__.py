from django.db import models
from django.forms import forms
from django.template.defaultfilters import filesizeformat


class MyFileField(models.FileField):
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types", [])
        self.max_upload_size = kwargs.pop("max_upload_size", [])
        super().__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super().clean(*args, **kwargs)  # clean()方法来自于FileField的父类Field, 用于验证
        file = data.file
        try:
            content_type = file.content_type

            if self.content_types == [] or content_type in self.content_types:
                if self.max_upload_size == [] or file.size > self.max_upload_size:
                    limit_size = filesizeformat(self.max_upload_size)
                    real_size = filesizeformat(file.size)
                    raise forms.ValidationError(f'请将文件大小控制在{limit_size}以下。当前文件大小{real_size}')
            else:
                for i in self.content_types:
                    if i.split('/')[1] == '*' and content_type.split('/')[0] == i.split('/')[0]:
                        if self.max_upload_size == [] or file.size > self.max_upload_size:
                            limit_size = filesizeformat(self.max_upload_size)
                            real_size = filesizeformat(file.size)
                            raise forms.ValidationError(f'请将文件大小控制在{limit_size}以下。当前文件大小{real_size}')
                        return data
                print(content_type)
                raise forms.ValidationError('文件类型不被允许')
        except AttributeError:
            pass
        return data
