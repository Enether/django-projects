from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from lists.models import Item


def home_page(request: HttpRequest):
    return render(request, 'home.html')


def view_list(request: HttpRequest):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request: HttpRequest):
    new_item_text = request.POST['item_text']
    Item.objects.create(text=new_item_text)
    return redirect('/lists/the-only-list-in-the-world')
