# Generated by Django 5.1.1 on 2024-09-30 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flaticon.com%2Ffree-icon%2Fplaceholder_1377194&psig=AOvVaw33ZI-EobWzE6fbzuZVhkRQ&ust=1726661043871000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCJCv1uP3yYgDFQAAAAAdAAAAABAt', max_length=500, upload_to='foods'),
        ),
    ]
