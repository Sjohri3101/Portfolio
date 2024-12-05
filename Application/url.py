from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
path('admin/', admin.site.urls),
path('',views.indexpage,name='indexpage'),
path('all_portfolio',views.all_portfolio,name='all_portfolio'),
path('employee_portfolio',views.employee_portfolio,name='employee_portfolio'),
path('display_employee_portfolio',views.display_employee_portfolio,name='display_employee_portfolio'),
path('create_portfolio',views.create_portfolio,name='create_portfolio'),
]
