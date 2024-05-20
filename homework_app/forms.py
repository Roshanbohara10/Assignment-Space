from django import forms
from . import models


class ReviewForm(forms.Form):
    review = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


# class HomeworkForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', None)
#         super(HomeworkForm, self).__init__(*args, **kwargs)
#         if user:
#             self.fields['student'].initial = user
#             self.fields['student'].widget.attrs['disabled'] = True

#     class Meta:
#         model = models.Homework
#         fields = ['subject', 'file']


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = models.Homework
        fields = ['subject', 'file']
