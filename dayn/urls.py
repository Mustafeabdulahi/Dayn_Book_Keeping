from django.urls import path
from .views import CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView, UserCustomerListView
from . import views

urlpatterns = [
    #path('', views.home, name='dayn-home'),
    path('', CustomerListView.as_view(), name='dayn-home'),
    path('user/<str:username>', UserCustomerListView.as_view(), name='user-customers'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('customer/new/', CustomerCreateView.as_view(), name='customer-create'),
    path('customer/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer-update'),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),
    path('about', views.about, name='dayn-about'),

]