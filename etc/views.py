from django.shortcuts import render

# Create your views here.


def etcList(request):

    return render(request, 'main.html')