from django.shortcuts import render

# Create your views here.
from mainapp.models import MainappModel


def main(request):
    #db데이터 가져오기
    main_model = MainappModel.objects.get(id=1) # Mainapp테이블에서 id가 1인 로우 가져오기

    item = {'main_intro':main_model.main_intro}   #딕셔너리 형식으로 담아줘야함

    return render(request, 'index.html',item)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def resume(request):
    return render(request, 'resume.html')

def services(request):
    return render(request, 'services.html')

