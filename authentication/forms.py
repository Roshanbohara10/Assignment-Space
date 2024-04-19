from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from homework_app.models import Subject, SubjectTeacher


class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    group = forms.ModelChoiceField(label='Register as' , queryset=Group.objects.all(), empty_label=None)
    subject = forms.ModelChoiceField(label='Choose a subject if registering as teacher', \
                                     queryset=Subject.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'group', 'subject']

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('This email address is already in use.')
    #     return email

    def clean(self):
        cleaned_data = super().clean()

        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'This email address is already in use')
    
        role = cleaned_data.get('group')
        subject = cleaned_data.get('subject')

        if role.name == 'Teacher' and subject:
            if SubjectTeacher.objects.filter(subject=subject).exists():
                self.add_error('subject', 'This subject is already assigned to a teacher.')

        if role.name == 'Teacher' and not subject:
            self.add_error('subject', 'This field is required for teachers')

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)