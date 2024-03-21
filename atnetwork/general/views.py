from django.http import HttpResponse
from django.template import loader

from .models import Product

def index(request):
    product_list = Product.objects.order_by('-price')[:5]
    template = loader.get_template("general/index.html")
    context = {
        "product_list": product_list
    }
    return HttpResponse(template.render(context, request))