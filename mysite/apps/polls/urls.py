from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'polls'),
    path("rooms/", views.allrooms),
    path("rooms/<str:room_id>/", views.room),
    path('objects/', views.check),
    path('<int:sub_id>/', views.subrooms),
    path('<str:sub_name>/', views.subredirect),
]
