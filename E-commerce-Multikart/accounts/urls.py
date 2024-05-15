from django.urls import path, re_path
from accounts.views import register,UserLoginView,ShippingView, logout,vendor_profile,forget,wishlist,activate,PasswordChangeView,password_success
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', register ,name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/',logout , name= 'logout'),
    path('profile/',ShippingView.as_view() , name='profile'),
    path('vendor_profile/', vendor_profile , name='vendor_profile'),
    path('forget/', forget ,name='forget'),
    path('wishlist/', wishlist ,name='wishlist' ),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,40})/$',
        activate, name='activate'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="forget_pwd.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),  name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), name="password_reset_complete"),
    path('change_password',PasswordChangeView.as_view(template_name="password_change.html"),name='change_password' ),
    path('password_success',password_success,name='password_success' ),


    
]
