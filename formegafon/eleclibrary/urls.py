from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addbook/', views.addbook, name='addbook'),
    path('editbook/<int:book_id>/', views.editbook, name='editbook'),
    path('deletebook/<int:book_id>/', views.deletebook, name='deletebook'),
    path('addauthor/', views.addauthor, name='addauthor'),
    path('editauthor/<int:author_id>', views.editauthor, name='editauthor'),
    path('deleteauthor/<int:author_id>', views.deleteauthor, name='deleteauthor')
]