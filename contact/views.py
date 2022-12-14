from django.shortcuts import render, redirect
from .models import Contact


# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ""
    context = {'contacts': contacts, 'search_input': search_input}
    return render(request, "index.html", context)

def addContact(request):
    if request.method == 'POST':
        new_contact = Contact(
            full_name = request.POST['fullname'],
            relationship = request.POST['relationship'],
            phone_number = request.POST['phone-number'],
            email = request.POST['email'],
            address = request.POST['address']
        )
        new_contact.save()
        return redirect('/')
    return render(request, "new.html")

def contactProfile(request, pk):
    contact = Contact.objects.get(pk=pk)
    context = {'contact': contact}
    return render(request, "contact-profile.html", context)

def editProfile(request, pk):
    contact = Contact.objects.get(pk=pk)
    
    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['e-mail']
        contact.phone_number = request.POST['phone-number']
        contact.address = request.POST['address']
        contact.save()

        return redirect('/profile/'+str(contact.pk))
    
    context = {'contact': contact}
    return render(request, "edit.html", context)


def deleteProfile(request, pk):
    contact = Contact.objects.get(pk=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    context = {'contact': contact}
    return render(request, "delete.html", context)