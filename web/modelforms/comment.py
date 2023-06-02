from django import forms

from web.models.comment import Comment


class CommentAddModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user']
