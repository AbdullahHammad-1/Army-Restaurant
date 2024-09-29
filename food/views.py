from lib2to3.fixes.fix_input import context
from tempfile import template
from wsgiref.util import request_uri

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import request

from .models import Item
from django.template import loader
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.


def items(request):
    item_list = Item.objects.all().values()
    template = loader.get_template('items.html')
    context = {
        'item_list': item_list,
    }
    return HttpResponse(template.render(context, request))


class ItemsView(ListView):
    model = Item
    template_name = 'items.html'
    context_object_name = 'item_list'


def details(request, id):
    item = Item.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'item': item
    }
    return HttpResponse(template.render(context, request))


class DetailsView(DetailView):
    model = Item
    template_name = 'details.html'


def main(request):
    return render(request, 'main.html')


@login_required
def adding(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('items')
    return render(request, 'item_form.html',{"form": form})


class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_des', 'price', 'item_image']
    login_required = True
    template_name = 'item_form.html'

    def form_valid(self, form):
        form.instance.username = self.request.user

        return super().form_valid(form)


@login_required
def editing(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('items')
    return render(request, 'item_form.html', {"form": form, "item": item})


@login_required
def deleting(request, id):
    item = Item.objects.get(id=id)
    if request.method =='POST':
        item.delete()
        return redirect('items')
    return render(request, 'item_delete.html', {'item': item})


def testing(request):
    template = loader.get_template("template.html")

    return HttpResponse(template.render())


