from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.FloatField()
    rating = models.FloatField()
    discount = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price
    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='products', null=True)
    product = models.ForeignKey('app.Product', on_delete=models.CASCADE)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
