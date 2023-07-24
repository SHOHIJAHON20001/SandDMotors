from django.urls import path
from .views import home, gallery, gallery_details, our_team, services, contact, mail_send


urlpatterns = [
   path('', home, name='home'),
   path('gallery/', gallery, name='gallery'),
   path('gallerys/<int:car_id>/', gallery_details, name='gallery_details'),
   path('our_team/', our_team, name='our_team'),
   path('services/', services, name='services'),
   path('contact/', contact, name='contact'),
   path('mail_send/', mail_send, name='mail_send'),
]