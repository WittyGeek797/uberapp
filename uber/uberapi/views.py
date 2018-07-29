from rest_framework import generics, serializers
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from .models import Customer, Driver, BookCab
from.serializers import CustomerSerializer, DriverSerializer, BookCabSerializer, TravelHistorySerializer

# Create your views here.
class CreateCustomerView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()

class CreateDriverView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()

class CreateBookCabView(generics.ListCreateAPIView):
    queryset = BookCab.objects.all()
    serializer_class = BookCabSerializer

    def perform_create(self,serializer):        
        customer = Customer.objects.all().filter(cust_id=self.request.POST["cust_name"])
        if len(customer) == 0 or len(customer) > 1:
            raise APIException("Could not find the customer with given name")
        drivers = Driver.objects.all().filter(availablity=True)
        if len(drivers) == 0:
            raise APIException("Could not find the customer with given name")
        driver = drivers[0]
        if serializer.is_valid():
            serializer.save()
        Driver.objects.filter(driver_id=driver.driver_id).update(availablity=False)

class CreateTravelHistory(generics.ListCreateAPIView):
    queryset = BookCab.objects.all()
    serializer_class = BookCabSerializer
