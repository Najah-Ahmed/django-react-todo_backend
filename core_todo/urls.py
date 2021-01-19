
from django.contrib import admin


from django.urls import path, include                 # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),             # add this
]
