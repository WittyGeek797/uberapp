from rest_framework import serializers
from .models import Customer,Driver,BookCab,TravelHistory

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ("cust_name","mobile_no",)
        read_only_fields = ("cust_id",)

class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = ("driver_name","mobile_no","car_no",)
        read_only_fields = ("driver_id","availablity",)

class BookCabSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookCab
        fields = ("cust_name","driver_name",)
        read_only_fields = ("cust_id","driver_id",)
    
    def to_internal_value(self, data):
        customer = Customer.objects.all().filter(cust_id=self.request.POST["cust_name"])
        driver = Driver.objects.all().filter(driver_id=self.request.POST["driver_name"])
        return {
                "cust_id": customer[0].cust_id,
                "cust_name":customer[0].cust_name,
                "driver_id":driver[0].driver_id,
                "driver_name":driver[0].driver_name
            }

class TravelHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TravelHistory
        fields = ("booking_id","cust_name","driver_name",)
        read_only_fields = ("cust_id","driver_id",)
