from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError

from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        return add_item(request, list_id)
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
    except ValidationError:
        list_.delete()
        error_msg = "You can't have an empty list item"
        return render(request, 'home.html', {'error': error_msg})
    return redirect('view-list', list_.id)


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    try:
        item = Item.objects.create(text=request.POST['item_text'], list=list_)
        item.full_clean()
        item.save()
        return redirect(list_)
    except ValidationError:
        error_msg = "You can't have an empty list item"
        return render(request, 'list.html', {'list': list_, 'error': error_msg})
