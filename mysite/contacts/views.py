from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import ContactForm
from .forms import NameForm
from django.contrib.auth.decorators import login_required, permission_required

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            return HttpResponseRedirect(reverse("contacts:thanks", args=(name,)))
    else:
        form = NameForm()
    return render(request, "contacts/name.html", {"form": form})

def thanks(request, name):
    return HttpResponse(f'Obrigado {name}')

@permission_required("contacts.add_contact")
def create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['subject']
            form.save() #Commit por padrao é True
            return HttpResponseRedirect(reverse("contacts:thanks", args=(name,)))
    else:
        form = ContactForm()
    return render(request, "contacts/create.html", {"form": form})