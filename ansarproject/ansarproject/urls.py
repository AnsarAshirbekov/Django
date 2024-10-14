"""
URL configuration for ansarproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
# from ansarapp.views import my_first_view, myname, mysurname, mynumber
# from ansarapp.views import my_view
# from ansarapp.views import contact_view
from ansarapp.views import article_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', my_first_view),
    # path('myname', myname),
    # path('mysurname', mysurname),
    # path('mynumber', mynumber)
    # path('', my_view)
    # path('', contact_view)
    # re_path(r"^article/(?P<id>\d{4})/$", article_detail),
    path('article/<int:id>/', article_detail, name= 'list_post')
]
