from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def my_first_view(request):
#     return HttpResponse("""<a href='http://127.0.0.1:8000/myname'> Имя </a> </br>
#                         <a href='http://127.0.0.1:8000/mysurname'> Фамилия </a> </br>
#                         <a href='http://127.0.0.1:8000/mynumber'> Номер </a>""")

# def myname(request):
#     return HttpResponse("""<h1> Ansar </h1> </br>
#                         <a href='http://127.0.0.1:8000/'> Назад </a>""")

# def mysurname(request):
#     return HttpResponse("""<h1> Ashirbekov </h1> </br>
#                         <a href='http://127.0.0.1:8000/'> Назад </a>""")

# def mynumber(request):
#     return HttpResponse("""<h1> 87774713028 </h1> </br>
#                         <a href='http://127.0.0.1:8000/'> Назад </a>""")

# def my_view(request):
#     if request.method == 'GET':
#         return HttpResponse("""GET запрос
#         <!DOCTYPE html>
# <html lang="ru">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Пример HTTP-запросов</title>
# </head>
# <body>
#     <h1>Отправка HTTP-запросов</h1>
    
#     <button onclick="sendGetRequest()">GET</button>
#     <button onclick="sendPostRequest()">POST</button>
#     <button onclick="sendPutRequest()">PUT</button>
#     <button onclick="sendDeleteRequest()">DELETE</button>

#     <script>
#         const url = 'https://jsonplaceholder.typicode.com/posts';

#         function sendGetRequest() {
#             fetch(url)
#                 .then(response => response.json())
#                 .then(data => console.log('GET Response:', data))
#                 .catch(error => console.error('Ошибка GET:', error));
#         }

#         function sendPostRequest() {
#             fetch(url, {
#                 method: 'POST',
#                 headers: {
#                     'Content-Type': 'application/json'
#                 },
#                 body: JSON.stringify({ title: 'foo', body: 'bar', userId: 1 })
#             })
#             .then(response => response.json())
#             .then(data => console.log('POST Response:', data))
#             .catch(error => console.error('Ошибка POST:', error));
#         }

#         function sendPutRequest() {
#             fetch(`${url}/1`, {
#                 method: 'PUT',
#                 headers: {
#                     'Content-Type': 'application/json'
#                 },
#                 body: JSON.stringify({ id: 1, title: 'updated title', body: 'updated body', userId: 1 })
#             })
#             .then(response => response.json())
#             .then(data => console.log('PUT Response:', data))
#             .catch(error => console.error('Ошибка PUT:', error));
#         }

#         function sendDeleteRequest() {
#             fetch(`${url}/1`, {
#                 method: 'DELETE'
#             })
#             .then(response => {
#                 if (response.ok) {
#                     console.log('DELETE успешен');
#                 } else {
#                     console.error('Ошибка DELETE');
#                 }
#             })
#             .catch(error => console.error('Ошибка DELETE:', error));
#         }
#     </script>
# </body>
# </html>""")
#     elif request.method == 'POST':
#         return HttpResponse('Это POST запрос')
#     elif request.method == 'PUT':
#         return HttpResponse('Это PUT запрос')
#     elif request.method == 'DELETE':
#         return HttpResponse('Это DELETE запрос')
#     else:
#         return HttpResponse('Метод не поддерживается', status=405)

# def contact_view(request):
#     if request.method == 'GET':
#         return render(request, 'index.html')
#     elif request.method == 'POST':
#         name = request.POST.get('name')
#         message = request.POST.get('message')
#         return HttpResponse(f'Спасибо за ваше сообщение, {name}: {message}')
#     elif request.method == 'PUT':
#         message = request.PUT.get('message')
#         return HttpResponse(f'ваше новое сообщение: {message}')
#     elif request.method == 'DELETE':
#         name = request.DELETE.get('name')
#         return HttpResponse(f'имя {name} удалено')

# def article_detail(request, id):
#     return HttpResponse(f'Статья с ID: {id}')

def myapp_view(request):
    
    data = {
        'name':'Ansar Ashirbekov',
        'age': 28,
        'knowledge': ['Математика', 'Химия', 'C++'],
        'aboutme': """<h1>Привет</h1><strong>мир!</strong>
        <script>alert('Вас взломали')</script>"""
    }

    # context = {
    #     'students' : [
    #         {'name' :'Ansar',
    #         'lastname' :'Ashirbekov'},
    #         {'name' :'Danara',
    #         'lastname' :'Magomedova'},
    #         {'name' :'Nurlan',
    #         'lastname' :'Azhigalin'},
    #         {'name' :'Aben',
    #         'lastname' :'Baktygulov'},
    #         {'name' :'Mansur',
    #         'lastname' :'Karim'}
    #     ]
    # }

    return render(request, 'ansarapp/index.html', data)

