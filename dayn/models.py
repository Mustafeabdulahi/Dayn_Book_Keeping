from django.db import models
from django.db.models.fields import CharField, DecimalField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    amount_owed = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    date_owed= models.DateTimeField(default=timezone.now)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    date_paid= models.DateTimeField(default=timezone.now)
    total_owed = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_total_owed(self):
        if self.amount_owed > 0:
            result = self.amount_owed - self.amount_paid
            return result
        else:
            self.amount_owed == 0

    def get_amount_paid(self):
         temp = Customer.objects.all()[0]
         while True:
            if self.amount_paid >= 0:
                temp =+ self.amount_paid
            return temp
                    # override the save method
    def save(self, *args, **kwargs):
        self.amount_paid = self.get_amount_paid()
        self.total_owed = self.get_total_owed()
        super(Customer, self).save(*args, **kwargs)


    def __str__(self):
        return self.first_name


    def get_absolute_url(self):
        return reverse("customer-detail", kwargs={'pk':self.pk})