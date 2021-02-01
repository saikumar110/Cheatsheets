from django.contrib import admin
from django.urls import path,include
from cheats_app import views

urlpatterns = [
   
    path('',views.homepage,name="homepage"),#Homepage
    path('data_content/<int:id>',views.data_content,name="data_content"),
    path('content_edit/<int:id>',views.content_edit,name="content_edit"),
    path('Update_content/',views.Update_content,name="Update_content"),
    path('books_view/',views.books_view,name="books_view"),
    path('read_book/<int:id>',views.read_book,name="read_book"),
    
    

]