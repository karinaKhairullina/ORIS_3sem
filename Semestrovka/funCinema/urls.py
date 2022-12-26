from django.urls import path
from . import views


urlpatterns = [
    path("serials_list/", views.SerialsView.as_view(), name='serials_list'),
    path('list/', views.add_list, name='list'),
    path('form/', views.serials_form, name='insert'),
    path('form/<int:id>/', views.serials_form, name='update'),
    path('delete/<int:id>/', views.delete_list, name='delete'),
    path("single_serial/", views.SerialDetailView.as_view(), name='single_serial'),
    path("<int:id>/", views.SingleSerial.as_view(), name='detail_serial'),
    path("actor/<int:id>/", views.ActorView.as_view(), name='actor_detail'),
    path('login/', views.Login, name='login'),
    path('sign/', views.Register, name='sign')
]

