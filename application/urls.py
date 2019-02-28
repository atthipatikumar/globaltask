from django.conf.urls import url
from application.views.add import page
from application.views.login import page
from application.views.update import page
from application.views.delete import page

urlpatterns = [

    url(r'^adduser/$', 'views.add.page', name='add'),
    url(r'^loginuser/$', 'views.login.page', name='login'),
    url(r'^updateuser/$', 'views.update.page', name="update"),
    url(r'^deleteuser/$', 'views.delete.page', name="delete"),


]