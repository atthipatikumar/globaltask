from application.models import AddExpenses
from django.shortcuts import render

def page(request):
    sort_model = AddExpenses.objects.filter(name="kumar", total_price="2000", upload_image="image1.jpg").order_by("id")
    sorting_query = sort_model[:1]
    addexpenses = sorting_query.get()
    addexpenses.save()

    edit_model = AddExpenses.objects.filter(name="kumar", total_price="2000", upload_image="image1.jpg").update(name="Global", total_price="5000", upload_image="globalimg.jpg")
    edit_model.save()
    return render(request, {'action': 'Update many model'})

