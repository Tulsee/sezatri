from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


def upload_thumbnail(instance, filename):
    return 'product/thumbnail/{product_name}/{file_name}'.format(
        product_name=instance.name, file_name=filename
    )


def upload_picture(instance, filename):
    return 'product/{product_name}/{file_name}'.format(
        product_name=instance.name, file_name=filename
    )


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=100, help_text=(
        'Please enter any one category listed as: '
        'Gurung ' 'Newar ' 'Magar ' 'Rai ' 'Sherpa ' 'Tamang '
    ))
    available = models.BooleanField(default=True, null=True, blank=True)
    quantity = models.IntegerField()
    size = models.CharField(max_length=200, help_text=(
        'Enter the available size seperated by comma ie , '
    ))
    views = models.IntegerField(blank=True, null=True)
    listed_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to=upload_thumbnail, help_text=(
        'recommendate size is 500x775'
    ))
    picture_1 = models.ImageField(
        upload_to=upload_picture, blank=True, null=True,  help_text=(
            'recommendate size is 1000x1358'
        ))
    picture_2 = models.ImageField(
        upload_to=upload_picture, blank=True, null=True,  help_text=(
            'recommendate size is 1000x1358'
        ))
    picture_3 = models.ImageField(
        upload_to=upload_picture, blank=True, null=True,  help_text=(
            'recommendate size is 1000x1358'
        ))

    def __str__(self):
        return self.name

    @property
    def product_size(self):
        size = self.size
        size = size.split(',')
        return size
