from django import forms
from .models import Registration,Feedback
from django.http import HttpResponse

class Login(forms.ModelForm):
    class Meta():
        model=Registration
        fields = ['uname','pwd','cpwd']
    def clean(self):
        cleaned_data=super().clean()
        pwd = cleaned_data.get("pwd")
        cpwd = cleaned_data.get("cpwd")
        if pwd != cpwd:
            print("password mismatch")
            msg = "password mismatch"
            self.add_error('cpwd', msg)
        Name=cleaned_data.get("uname")
        PW=cleaned_data.get("pwd")
        if Registration.objects.filter(uname=Name):
            print("valid user name")
        else:
            print("invalid username")
            msg1="invalid username"
            self.add_error('uname',msg1)

        if Registration.objects.filter(pwd=PW):
            print("valid password")
        else:
            msg2="invalid password"
            self.add_error('pwd',msg2)

class Reg_form(forms.ModelForm):
    class Meta():
        model=Registration
        fields='__all__'
    def clean(self):
        cleaned_data=super().clean()
        Name=cleaned_data.get("uname")
        if Registration.objects.filter(uname=Name):
            print("user name already exists")
            msg="user name already exists!"
            self.add_error('uname',msg)
        pwd=cleaned_data.get("pwd")
        cpwd=cleaned_data.get("cpwd")
        if pwd!=cpwd:
            print("password mismatch")
            msg="password mismatch"
            self.add_error('cpwd',msg)

#
# class Log_form(forms.ModelForm):
#     class meta():
#         model=Log_model
#         fields='__all__'
class Feed_form(forms.ModelForm):
    class Meta():
        model=Feedback
        fields='__all__'
