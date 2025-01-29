from django.urls import path
from . import views


urlpatterns = [
    path('createbook/', views.book_create, name='book_create'),
    path('listbook/', views.book_list, name='book_list'),
    path('bookdetail/<int:pk>/', views.book_detail, name='book_detail'),
    path('bookupdate/<int:pk>/', views.book_update, name='book_update'),
    path('bookdelete/<int:pk>/', views.book_delete, name='book_delete'),
]
# handler404 = 'function_based_view_01.views.notfound' # This is the function that will be called when a 404 error is raised
