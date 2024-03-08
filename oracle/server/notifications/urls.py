from django.urls import path
from notifications import views
urlpatterns = [
    path('token/', views.token)
    # path('get_token/<int>id>', views.get_token ) # Passar id como um argumento na função
    # path('get_token/<str:representante>', views.get_token ) # Passer como argumento (request, representante)
]