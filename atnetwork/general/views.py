from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, TOM. You're at the general homepage index.")