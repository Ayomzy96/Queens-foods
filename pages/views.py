from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views.generic import TemplateView, FormView
from .forms import ContactForm

#homepage
def home(request):
    return render(request, 'pages/home.html')

#contact us
class ContactView(FormView):
    form_class = ContactForm
    template_name = "pages/contact.html"

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        full_message = f"""
            Received message below from {email}, {subject}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )
        return super(ContactView, self).form_valid(form)

#services
def services(request):
   return render(request, 'pages/services.html')

#product
def product(request):
    return render(request, 'pages/product.html')

#about us
def about(request):
    return render(request, 'pages/about.html')
