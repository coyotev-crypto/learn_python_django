from django.urls import path

from .views import index, courses, course


urlpatterns = [
        path('', index),
        path('courses', courses),
        path('course/<int:id>', course)
]