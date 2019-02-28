from django.contrib import admin
from application.models import UserProfile, AddExpenses, AddMore

admin.site.register(UserProfile)
admin.site.register(AddExpenses)
admin.site.register(AddMore)