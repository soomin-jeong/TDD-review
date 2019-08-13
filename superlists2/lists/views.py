from django.shortcuts import render
from django.http import HttpResponse

from .models import Item


# Create your views here.
def HomePageView(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
    else:
        new_item_text = ''
    return render(request, 'home.html', {'new_item_text': request.POST.get('item_text', '')})
