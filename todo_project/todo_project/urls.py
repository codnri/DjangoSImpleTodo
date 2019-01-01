"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
import todo_app.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',todo_app.views.index, name='index'),
    path('todos/',todo_app.views.index, name='index'),
    path('todos/new',todo_app.views.new, name='new'),
    path('todos/<int:todo_id>/',todo_app.views.show, name='show'),
    path('todos/<int:todo_id>/edit',todo_app.views.edit, name='edit'),
    path("todos/<int:todo_id>/delete",todo_app.views.delete,name="delete"),

    # path('<int:blog_id>/',views.detail, name='detail')

]
