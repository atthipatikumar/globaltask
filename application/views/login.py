from django.shortcuts import render
from django import forms
from django.contrib.auth import authenticate, login


def page(request):
    if request.POST:
        form = Form_loginconnect(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                return render(request, {'form': form})
        else:
            form = Form_loginconnect()
            return render(request, {'form': form})
class Form_loginconnect(forms.Form):
    username = forms.CharField(label="Login")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(Form_loginconnect, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if not authenticate(username=username, password=password):
            raise forms.ValidationError("wrong details login or password")
        return self.cleaned_data