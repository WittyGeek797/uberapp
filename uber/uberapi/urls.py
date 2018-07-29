from .views import CreateCustomerView, CreateDriverView, CreateBookCabView, CreateTravelHistory
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = {
    url(r'^customer/$', CreateCustomerView.as_view(), name="create_user"),
    url(r'^driver/$', CreateDriverView.as_view(), name="create_driver"),
    url(r'^book-cab/$', CreateBookCabView.as_view(), name="book_cab"),
    url(r'^travel-history/$', CreateTravelHistory.as_view(), name="travel_history"),
}

urlpatterns = format_suffix_patterns(urlpatterns)

# urlpatterns = [
#     path(r'customer/$',CreateCustomerView.as_view(),name="create")
# ]