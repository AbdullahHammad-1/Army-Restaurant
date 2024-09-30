from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Item(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=80)
    item_des = models.CharField(max_length=80)
    price = models.FloatField()
    item_image = models.ImageField(max_length=500, default="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flaticon.com%2Ffree-icon%2Fplaceholder_1377194&psig=AOvVaw33ZI-EobWzE6fbzuZVhkRQ&ust=1726661043871000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCJCv1uP3yYgDFQAAAAAdAAAAABAt", upload_to='foods')

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})


