from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add-homework/', homework_create, name='homework_create'),
    path('homework/<int:id>/', homework_instance, name='homework'),
    path('review/<int:id>/', review_homework, name='review_homework'),
    path('delete/<int:id>/', delete_model_instance, name='delete_object'),
    # path('delete/<str:model_name>/<int:id>/<str:redirect_url_name>/', delete_model_instance, name='delete_object'),
]