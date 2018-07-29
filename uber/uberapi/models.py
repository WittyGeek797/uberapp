import uuid
from django.db import models

# Create your models here.

class Customer(models.Model):
    cust_id   = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    cust_name = models.CharField(max_length=100,null=False,blank=False)
    mobile_no = models.CharField(max_length=10,unique=True,null=False,blank=False)

    def __str__(self):
        return "{}".format(self.cust_name)

class Driver(models.Model):
    driver_id   = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    driver_name = models.CharField(max_length=100,null=False,blank=False)
    mobile_no   = models.CharField(max_length=10,unique=True,null=False,blank=False)
    car_no      = models.CharField(max_length=13,unique=True,null=False,blank=False)
    availablity = models.BooleanField(null=False,blank=False,default=True)

    def __str__(self):
        return self.driver_name

class BookCab(models.Model):
    booking_id   = models.BigAutoField(primary_key=True, editable=False)
    booking_time = models.DateTimeField(auto_now_add=True, editable=False)
    cust_id      = models.ForeignKey("Customer",on_delete=models.CASCADE,related_name="book_cust_id")
    cust_name    = models.ForeignKey("Customer",on_delete=models.CASCADE,related_name="book_cust_name")
    driver_id    = models.ForeignKey("Driver",on_delete=models.CASCADE,related_name="book_driver_id")
    driver_name  = models.ForeignKey("Driver",on_delete=models.CASCADE,related_name="book_driver_name")

    def __str__(self):
        return self.booking_id

class TravelHistory(models.Model):
    booking_id  = models.ForeignKey("BookCab",on_delete=models.CASCADE,related_name="travel_book_id")
    cust_id     = models.ForeignKey("Customer",on_delete=models.CASCADE,related_name="travel_cust_id")
    cust_name   = models.ForeignKey("Customer",on_delete=models.CASCADE,related_name="travel_cust_name")
    driver_id   = models.ForeignKey("Driver",on_delete=models.CASCADE,related_name="travel_driver_id")
    driver_name = models.ForeignKey("Driver",on_delete=models.CASCADE,related_name="travel_driver_name")
