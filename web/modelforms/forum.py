from django import forms

from web.models.forum import Forum,ForumImg


class ForumAddModelForm(forms.ModelForm):
    class Meta:
        model = Forum
        exclude = ['user', 'keyword', 'status']


class ForumImgAddModelForm(forms.ModelForm):
    class Meta:
        model = ForumImg
        fields = '__all__'
