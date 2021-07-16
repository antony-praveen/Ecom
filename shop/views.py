from django.core import paginator
from django.shortcuts import render
from .models import order, products
from django.core.paginator import Paginator
# Create your views here.

def index(request):

    product_objects = products.objects.all()
    template_name = 'shop/index.html'
    # Search funtionality
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:                             #For querysets questions please view the page
        product_objects =product_objects.filter(title__icontains = item_name) #https://sodocumentation.net/django/topic/1235/querysets

    #Paginator code & link 
    #https://docs.djangoproject.com/en/3.2/topics/pagination/
    paginator = Paginator(product_objects,4)
    page_number = request.GET.get('page')
    product_objects = paginator.get_page(page_number)

    return render(request,template_name,{'product_objects': product_objects})


def detail(request,obj_id):
    product_objects = products.objects.get(id=obj_id)
    return render(request,'shop/detail.html',{'product_objects':product_objects})

def checkout(request):

    if request.method == 'POST':

        items =request.POST.get('items',"") #allow the null value thats why put the empty string ""
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total','')
        order_list = order( items = items,name = name, email = email, address = address, city = city, state = state, zipcode = zipcode,total = total)
        order_list.save()

    return render(request,'shop/checkout.html')
