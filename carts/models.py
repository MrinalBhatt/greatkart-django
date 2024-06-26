from django.db import models
from store.models import Product,VariationProduct
from accounts.models import Accounts
# Create your models here.
class Cart(models.Model):
    cart_id     = models.CharField(max_length=500, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    user        = models.ForeignKey(Accounts, on_delete=models.CASCADE, null = True)
    def __str__(self) -> str:
        return self.cart_id

class CartItem(models.Model):
    product     = models.ForeignKey(Product, on_delete = models.CASCADE)
    variation   = models.ManyToManyField(VariationProduct, blank=True)
    cart        = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity    = models.IntegerField()
    is_active   = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product

