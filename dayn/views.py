from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Customer



# Create your views here.
def home(request):
	context = {

		'customers': Customer.objects.all()
	}
	return render(request,'dayn/home.html',context)


class CustomerListView(ListView):
	model = Customer
	template_name = 'dayn/home.html'
	context_object_name = 'customers'
	ordering = ['first_name']
	paginate_by = 5

class UserCustomerListView(ListView):
	model = Customer
	template_name = 'dayn/user_customer.html'
	context_object_name = 'customers'
	ordering = ['first_name']
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Customer.objects.filter(client=user).order_by('first_name')


class CustomerDetailView(LoginRequiredMixin, DetailView):
	model = Customer


class CustomerCreateView(LoginRequiredMixin, CreateView):
	model = Customer
	fields = ["first_name", "last_name", "amount_owed", "amount_paid", "date_paid"]
#addition code
	def form_valid(self, form):
		form.instance.client = self.request.user
		return super().form_valid(form)



class CustomerUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model = Customer
	fields = ["first_name", "last_name", "amount_owed", "amount_paid", "date_paid", ]

	def form_valid(self, form):
		form.instance.client = self.request.user
		return super().form_valid(form)

	def test_func(self):
		customer = self.get_object()
		if self.request.user == customer.client:
			return True
		return False

class CustomerDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
	model = Customer
	success_url = '/'

	def test_func(self):
		customer = self.get_object()
		if self.request.user == customer.client:
			return True
		return False

# This below code is not used any where in the program,
#  it is just an example of how to create function based html pages in django.
def about(request):
	return render(request,'dayn/about.html')

def admin(request):
	return render(request,'dayn/admin.html')










