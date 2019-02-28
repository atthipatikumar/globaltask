from application.models import AddExpenses
from django.shortcuts import render

def page(request):
    delete_task = AddExpenses.objects.get(id=1)
    delete_task.delete()
    all_delete = AddExpenses.objects.all()
    all_delete.delete()
    return render(request, {'action': 'Delete my tasks'})