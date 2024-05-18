from django.db import models
from accounts.models import Accounts
from store.models import Product, VariationProduct
# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.payment_id
    
class Order(models.Model):
    STATUS = (
        ("New", "New"),
        ("Accepted", "Accepeted"),
        ("Inprogress", "Inprogress"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled") 
    )

    user            = models.ForeignKey(Accounts, on_delete=models.SET_NULL, null=True)
    payment         = models.ForeignKey(Payment, on_delete= models.SET_NULL, null= True, blank= True)
    order_number    = models.CharField(max_length=20)
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    phone           = models.CharField(max_length=15)
    email           = models.CharField(max_length=50)
    address_line1   = models.CharField(max_length=50)
    address_line2   = models.CharField(max_length=50, blank=True)
    country         = models.CharField(max_length=50)
    state           = models.CharField(max_length=50)
    city            = models.CharField(max_length=50)
    pincode         = models.CharField(max_length=10, blank=True)
    order_note      = models.CharField(max_length=100, blank=True)
    order_total     = models.FloatField()
    tax             = models.FloatField(default=0,blank=True)
    order_status    = models.CharField(max_length=10, choices=STATUS, default="New")
    ip              = models.CharField(blank=True, max_length=20)
    is_ordered      = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def full_address(self):
        return f'{self.address_line1}, {self.address_line2}'

class OrderProduct(models.Model):
    order           = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment         = models.ForeignKey(Payment, on_delete= models.SET_NULL, null= True, blank= True)
    user            = models.ForeignKey(Accounts, on_delete= models.CASCADE)
    product         = models.ForeignKey(Product, on_delete= models.CASCADE)
    variation       = models.ForeignKey(VariationProduct, on_delete= models.CASCADE)
    color           = models.CharField(max_length=50)
    size            = models.CharField(max_length=50)
    quantity        = models.IntegerField()
    product_price   = models.FloatField()
    ordered         = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name


