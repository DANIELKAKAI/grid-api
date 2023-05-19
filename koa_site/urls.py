from django.contrib import admin
from django.urls import path
from main.views import calculate_closest_points

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate-closest-points/', calculate_closest_points, name='calculate_closest_points')
]
