from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user_auth = models.OneToOneField(User, primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    email_id = models.EmailField(verbose_name="Email ID")
    phone_number = models.IntegerField(verbose_name="Phone Number")
    password = models.CharField(max_length=20, verbose_name="Password")
    create_date = models.DateField(verbose_name="Create Date", auto_now_add=True)

    def __str__(self):
        return self.user_auth.firstname

class AddExpenses(UserProfile):
    name = models.CharField(max_length=30, verbose_name="Name")
    total_price = models.IntegerField(verbose_name="Total Price")
    upload_image = models.ImageField(upload_to= "path", blank=True, null=True)

    def __str__(self):
        return self.name

class AddMore(UserProfile):
    super_model = models.ForeignKey(AddExpenses, verbose_name="Super model")



