from django.urls import path
from blog.views import about_page,ContactView,faq

urlpatterns = [
    path('about_page/', about_page , name='about_page'),
    path('contact/', ContactView.as_view() , name='contact'),
    path('faq/', faq ,name='faq')
]
