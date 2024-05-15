from django.urls import path
from core.views import HomeView,SearchListView,notFound

urlpatterns = [
    path('home/', HomeView.as_view() , name='home'),
    path('search/', SearchListView.as_view(), name='search'),
    path('notFound/', notFound,name='notFound')
 
]