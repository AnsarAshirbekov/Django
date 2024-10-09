from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my_first_view(request):
    return HttpResponse("""<a href='http://127.0.0.1:8000/myname'> Имя </a> </br>
                        <a href='http://127.0.0.1:8000/mysurname'> Фамилия </a> </br>
                        <a href='http://127.0.0.1:8000/mynumber'> Номер </a>""")

def myname(request):
    return HttpResponse("""<h1> Ansar </h1> </br>
                        <a href='http://127.0.0.1:8000/'> Назад </a>""")

def mysurname(request):
    return HttpResponse("""<h1> Ashirbekov </h1> </br>
                        <a href='http://127.0.0.1:8000/'> Назад </a>""")

def mynumber(request):
    return HttpResponse("""<h1> 87774713008 </h1> </br>
                        <a href='http://127.0.0.1:8000/'> Назад </a>""")
