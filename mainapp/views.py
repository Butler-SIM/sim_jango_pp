from django.shortcuts import render

# Create your views here.
from mainapp.models import MainappModel


def main(request):

    main_model = MainappModel.objects.get(id=1)

    item = {'main_intro':main_model.main_intro}
    return render(request, 'index.html',item)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def portfolio_details(request):
    id = request.GET['id']
    print(request.GET['id'])
    return render(request, 'portfolio-details.html')

def resume(request):
    return render(request, 'resume.html')

def services(request):
    return render(request, 'services.html')

