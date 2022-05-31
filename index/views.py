from django.shortcuts import render
from blog.models import Blogs
from shop.models import Order, Shops

def index(request):
    some_blogs=Blogs.objects.all()[0:3]
    context={
        'some_blogs':some_blogs,
    }
    return render(request,'index.html',context=context)

def context_processor_for_items(request):

	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()

	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}
	
	context = {'orderr':order}
	return context