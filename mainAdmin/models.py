from django.db import models

# Create your models here.
import datetime
import os


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)


class productItems(models.Model):
    name = models.TextField(max_length=191)
    price = models.TextField(max_length=150)
    quantity = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)

    def __str__(self):
        return self.name


class cart(models.Model):
    name = models.TextField(max_length=120)
    user = models.TextField(max_length=120, null=True)
    price = models.TextField(max_length=200)
    total = models.IntegerField(null=True, default=0)
    quantity = models.TextField(max_length=100, null=True, default=1)
    qtyInSt = models.TextField(max_length=100, null=True, default=0)
    description = models.TextField(max_length=500, null=True)
    image = models.TextField(max_length=120, null=True)

    def __str__(self):
        return self.name


class orderItem(models.Model):
    order_id = models.TextField(max_length=120, null=True)
    name = models.TextField(max_length=120, null=True)
    user = models.TextField(max_length=120, null=True)
    price = models.TextField(max_length=200, null=True)
    total = models.IntegerField(null=True, default=0)
    quantity = models.TextField(max_length=100, null=True, default=1)
    image = models.TextField(max_length=120, null=True)

    def __str__(self):
        return self.order_id+' ------  '+self.name+' ------  '+self.user+' ------  '+self.price


class CheckOut(models.Model):
    firstName = models.TextField(max_length=120, null=True)
    lastName = models.TextField(max_length=120, null=True)
    userName = models.TextField(max_length=120, null=True)
    city = models.TextField(max_length=120, null=True)
    state = models.TextField(max_length=120, null=True)
    zip = models.IntegerField(max_length=50, null=True)
    paymentMethod = models.TextField(max_length=200, null=True)
    totalCheck = models.TextField(max_length=100, null=True)
    checkoutId = models.TextField(max_length=130, null=True)

    def __str__(self):
        return self.firstName+'-------------'+self.totalCheck
