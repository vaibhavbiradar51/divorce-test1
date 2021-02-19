from django.contrib import admin
from django.urls import path
from divorce import views

admin.site.site_header = "Vibhor Anand"
admin.site.site_title = "Welcome to the Portal "

app_name="divorce"
# from divorce.views import 
urlpatterns = [
    path('', views.form_1, name='form_1'),
    path('form_2', views.form_2, name='form_2'),
    path('form_3', views.form_3, name='form_3'),
]
