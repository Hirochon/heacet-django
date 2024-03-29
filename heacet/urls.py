from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:num>/', views.index, name='index'),
	path('create/', views.newcreate, name='create'),
	path('edit/<int:num>', views.edit, name='edit'),
	path('delete/<int:num>', views.delete, name='delete'),
	## path('find/', views.find, name='find'),
	path('sfind/', views.sql_find, name='sfind'),
	path('check/', views.check, name="check"),
	path('message/', views.message, name="message"),
	path('message/<int:page>/', views.message, name="message"),
]