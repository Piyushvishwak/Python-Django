from django.contrib import admin
from django.urls import path
# from jsonResponse.views import my_view, list_view, error_view, ajax_view
from jsonResponse import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('my-view/', views.my_view, name='my_view'),
    path('list-view/', views.list_view, name='list_view'),
    path('error-view/', views.error_view, name='error_view'),
    path('ajax-test/', views.ajax_test_page, name='ajax_test'),
    path('ajax-view/', views.ajax_view, name='ajax_view'),
]
