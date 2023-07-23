from django.urls import path
from .views import home, gallery, contact

urlpatterns = [
   path('', home, name='home'),
   path('gallery/', gallery, name='gallery'),
   path('contact/', contact, name='contact'),
]