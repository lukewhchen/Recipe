from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('delete/<ingredient_id>', views.delete, name="delete" ),
    path('update/<ingredient_id>', views.update, name="update"),
]

# use regexp can create flexible url
