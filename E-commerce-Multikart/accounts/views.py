from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from accounts.models import ShippingAdress
from accounts.froms import RegisterForm, LoginForm,ShippingAdressForm,PasswordChangingForm
from django.contrib.auth import authenticate,login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from accounts.tokens import account_activation_token

from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from accounts.tokens import account_activation_token
from django.contrib.auth.views import LoginView,PasswordChangeView
from django.views.generic import CreateView,UpdateView
from accounts.models import Wishlist
from django.utils.translation import gettext_lazy as _

# Create your views here.

class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(False)
            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect(reverse_lazy('login'))

    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

def activate(request, uidb64, token):
    try:

        uid = force_str(urlsafe_base64_decode(uidb64))
        print(uid)
        user = User.objects.get(id=uid)
      
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    print(user,account_activation_token.check_token(user, token))
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        django_login(request, user,backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')

# def login(request):
#     form = LoginForm()
#     if request.method == "POST":                             
#         next = request.GET.get('next', reverse_lazy('home'))
#         form = LoginForm(data=request.POST)                            
#         if form.is_valid():
#             user = authenticate(                                      
#                 request=request,
#                 username=form.cleaned_data["username"],
#                 password=form.cleaned_data["password"],
#             )
#             if not user:
#                 messages.add_message(request, messages.ERROR, "User not found!")
#             else:
#                 django_login(request,user)
#                 return redirect(next)
#     context = {
#         'form' : form
#     }
#     return render(request, 'login.html' , context)
    
    

class ShippingView(UpdateView):
    template_name = 'profile.html'
    form_class = ShippingAdressForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return ShippingAdress.objects.filter(user=self.request.user).first()

    def get_initial(self):
        
        initial = super().get_initial()
        shipping_address = self.get_object()
        if shipping_address:
            initial['flat'] = shipping_address.flat
            initial['address'] = shipping_address.address
            initial['zip_code'] = shipping_address.zip_code
            initial['country'] = shipping_address.country
            initial['city'] = shipping_address.city
            initial['region'] = shipping_address.region
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        shipping_address = self.get_object()
        if shipping_address:
    
            shipping_address.flat = form.cleaned_data['flat']
            shipping_address.address = form.cleaned_data['address']
            shipping_address.zip_code = form.cleaned_data['zip_code']
            shipping_address.country = form.cleaned_data['country']
            shipping_address.city = form.cleaned_data['city']
            shipping_address.region = form.cleaned_data['region']
            shipping_address.save()
            messages.add_message(self.request, messages.SUCCESS, _("Successfully updated shipping address!"))
        else:
            
            form.save()
            messages.add_message(self.request, messages.SUCCESS, _("Successfully added shipping address!"))
        return super().form_valid(form)



def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('login'))

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

def vendor_profile(request):
    return render(request, 'vendor-profile.html')

def forget(request):
    return render(request, 'forget_pwd.html')


@login_required
def wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    
    context = {
        'wishlist' : wishlist
    }
    return render(request, 'wishlist.html' , context)


# change password

class PasswordChangeView(PasswordChangeView):
    form_class=PasswordChangingForm
    success_url=reverse_lazy("password_success")

def password_success(request):
    return render(request, 'password_change_success.html')

