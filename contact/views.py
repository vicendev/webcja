from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            job = request.POST.get('jobs','')
            content = request.POST.get('content','')

            # Enviamos correo y redireccionamos
            email = EmailMessage(
                "José Aranda Construcciones: Nuevo mensaje de contacto",
                "De {} <{}>\n\nPara un trabajo de {}./n/nEscribe:\n\n{}".format(name, email, job,content),
                "no-contestar@jaconstrucciones.org",
                ['adminjac@jaconstrucciones.org'],
                reply_to=[email] 
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form': contact_form})