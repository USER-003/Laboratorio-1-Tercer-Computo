from django.contrib import admin
from django.urls import path
from MiApp.views import home, cliente, venta, empleado, area

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cliente/', cliente, name='cliente'),
    path('venta/', venta, name='venta'),
    path('empleado/', empleado, name='empleado'),
    path('area/', area, name='area'),
]
