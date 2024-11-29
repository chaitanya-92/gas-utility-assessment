from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    
    path('tickets/submit/', views.submit_ticket, name='submit_ticket'),
    
    path('tickets/track/<int:ticket_id>/', views.track_ticket, name='track_ticket'),
]
