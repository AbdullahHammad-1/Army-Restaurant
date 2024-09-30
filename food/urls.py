from django.contrib.auth import login
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('items', views.ItemsView.as_view(), name='items'),
    path('details/<int:pk>', views.DetailsView.as_view(), name='details'),
    path('', views.main, name="main"),
    path('testing', views.testing, name='testing'),
    path('adding', login_required(views.CreateItem.as_view()), name='adding'),
    path('editing/<int:pk>', login_required(views.Editing.as_view()), name='editing'),
    path('deleting/<int:id>', views.deleting, name='deleting'),
]