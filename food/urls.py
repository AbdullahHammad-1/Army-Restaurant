from django.urls import path
from . import views


urlpatterns = [
    path('items', views.ItemsView.as_view(), name='items'),
    path('details/<int:pk>', views.DetailsView.as_view(), name='details'),
    path('', views.main, name="main"),
    path('testing', views.testing, name='testing'),
    path('adding', views.CreateItem.as_view(), name='adding'),
    path('editing/<int:id>', views.editing, name='editing'),
    path('deleting/<int:id>', views.deleting, name='deleting'),
]