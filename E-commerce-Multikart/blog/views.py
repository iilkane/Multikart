from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Blog

from django.urls import reverse_lazy
from blog.forms import ContactForm
from django.contrib import messages
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _

# Create your views here.

def about_page(request):
    return render(request, 'about-page.html')


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.add_message(self.request, messages.SUCCESS, _("Successfully sent!"))
        return super().form_valid(form)
    
# def contact(request):
#     form = ContactForm()                              seyfe adi yuklenende form bos halda gorunsun
#     if request.method == 'POST':                       icindeki data ile birlikde gotursun
#         form = ContactForm(data = request.POST)
#         if form.is_valid():                            form validationdan kecirse formu save edir      
#             form.save()
#             messages.add_message(request, messages.SUCCESS, "Successfully sent!")
#             return redirect(reverse_lazy('contact'))
#     context = {
#         'form' : form
#     }
#     return render(request, 'contact.html', context)

def faq(request):
    return render(request, 'faq.html')

def blog(request):
    blog = Blog.objects.all()
    
    context = {
        'blog' : blog
    }
    return render(request, 'index.html' , context)
