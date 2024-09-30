from lib2to3.fixes.fix_input import context
from django.contrib import messages
from tempfile import template
from wsgiref.util import request_uri

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.context_processors import request
from django.urls import reverse_lazy
from .models import Item
import os
from django.template import loader
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView

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

    def form_valid(self, form): # Store the old image path
        self.request.FILES.get('item_image')
        form.instance.username = self.request.user

        return super().form_valid(form)


@login_required
def editing(request, id):
    item = get_object_or_404(Item, pk=id)  # Fetch the item to edit

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)  # Pass the instance here
        if form.is_valid():
            form.save()  # Saves the changes to the existing item
            return redirect('details', id=id)
    else:
        form = ItemForm(instance=item)  # Pass the instance here for GET requests

    return render(request, 'edit_form.html', {'form': form, 'item': item})


class Editing(UpdateView):
    model = Item
    fields = ['item_name', 'item_des', 'price', 'item_image']
    template_name = 'edit_form.html'
    login_required = True
    success_url = reverse_lazy('items')  # redirect after success

    def form_valid(self, form):
        old_image = self.object.item_image.path  # Store the old image path
        if self.request.FILES.get('item_image'):  # Check if there's a new image
            if os.path.exists(old_image):  # If the old image exists, delete it
                os.remove(old_image)
        messages.success(self.request, "The item was updated successfully.")
        return super().form_valid(form)


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


