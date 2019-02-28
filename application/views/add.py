from django.shortcuts import render
from application.models import AddExpenses
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

def page(request):
    if request.POST:
        form = Form_addexpenses(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            total_price = form.cleaned_data['total_price']
            upload_image = form.cleaned_data['upload_image']
            email = form.cleaned_data['email']

            new_user = User.objects.create_user(username = login, email = email, password = password)
            new_user.is_active = True
            new_user.final_name = full_name
            new_user.save()
            new_addexpenses = AddExpenses(user_auth = new_user, name=name, total_price=total_price, upload_image=upload_image)
            new_addexpenses.save()
            return HttpResponseRedirect(reverse('public_empty'))
        else:
            return render(request, {'form' : form})
    else:
        form = Form_addexpenses()
    form = Form_addexpenses()
    return render(request, {'form':form})

class Form_addexpenses(forms.Form):
    full_name = forms.CharField(label="Full Name", max_length=30)
    login = forms.CharField(label="Login")
    email = forms.EmailField(label="Email")
    name = forms.CharField(label="Name", max_length=30)
    total_price = forms.IntegerField(label="Total Price")
    upload_image = forms.ImageField(label="Upload Image")
    password = forms.CharField(label="Password", widget= forms.PasswordInput)
    password_bis = forms.CharField(label="Password", widget= forms.PasswordInput)

    def clean(self):
        cleaned_data = super(Form_addexpenses, self).clean()
        password = self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')

        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Password are not find.")
        return self.cleaned_data

"""
def page(request):
    if request.POST:
        form = Form_inscription(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['First Name']
            last_name = form.cleaned_data['Last Name']
            email_id = form.cleaned_data['Email Id']
            phone_number = form.cleaned_data['Phone Number']
            password = form.cleaned_data['Password']
            super_model = form.cleaned_data['Super Model']
            new_user = User.objects.create_user(username = last_name, password=password)
            new_user.is_active = True
            new_user.final_name = first_name
            new_user.save()
            return HttpResponse("New user data added")
        else:
            return render(request, {'form': form})
    else:
        form = Form_inscription()
        return render(request, {'form': form})
class Form_inscription(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=30)
    last_name = forms.CharField(label="Last Name", max_length=30)
    email_id = forms.EmailField(label="Email Id")
    phone_number = forms.IntegerField(label="Phone Number", max_value=10)
    password = forms.CharField(label="Password", widget= forms.PasswordInput)
    super_model = forms.CharField(label="Super Model")

    def clean(self):
        cleaned_data = super(Form_inscription, self).clean()
        password = self.cleaned_data.get('password')
        password_is = self.cleaned_data.get('password_is')

        if password and password_is and password != password_is:
            raise forms.ValidationError("password are not identical")
        return self.cleaned_data
        """
