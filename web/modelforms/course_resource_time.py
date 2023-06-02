from django import forms

from web.models.course_resource import CourseResourceTime


class CourseResourceTimeModelForm(forms.ModelForm):
    class Meta:
        model = CourseResourceTime
        fields = ['time']
