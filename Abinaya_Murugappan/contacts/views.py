from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from django.contrib import messages
from django.utils import timezone
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.
#Home Page rendering all contacts list 
def contacts_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def contact_create(request):
    if request.method == 'POST':
        name=request.POST['name']
        email = request.POST.get('email')
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, f"Enter a valid email address", extra_tags='validemail_error')
        if Contact.objects.filter(name=name).exists():
            # Add an error message using Django's messages framework
            messages.error(request, f"Contact with this name already exists", extra_tags='name_error')
        if Contact.objects.filter(email=email).exists():
            # Add an error message for email using Django's messages framework
            messages.error(request, f"Contact with this email already exists", extra_tags='email_error')
        if messages.get_messages(request):
            return redirect('contact_create')
        else:
            contact = Contact(name=name, email=request.POST['email'], notes=request.POST['notes'], created_time=timezone.now())
            contact.save()
            return redirect('contacts_list')
    return render(request, 'contacts/contact_create.html')

def contact_details(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    return render(request, "contacts/contact_detail.html", {"contact": contact})

def contact_update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        name=request.POST['name']
        email = request.POST.get('email')
        check_contacts = Contact.objects.exclude(id=contact_id)
        if not validate_email(email):
            # Add an error message for invalid email format
            messages.error(request, f"Enter a valid email address", extra_tags='validemail_error')
        if check_contacts.filter(name=name).exists():
            # Add an error message using Django's messages framework
            messages.error(request, f"Contact with this name already exists in other contacts", extra_tags='name_error')
        if check_contacts.filter(email=email).exists():
            # Add an error message for email using Django's messages framework
            messages.error(request, f"Contact with this email already exists in other contacts", extra_tags='email_error')
        if messages.get_messages(request):
            return redirect('contact_update', contact_id=contact_id)
        else:
            contact.name = request.POST['name']
            contact.email = request.POST['email']
            contact.notes = request.POST['notes']
            contact.save()
        return redirect('contacts_list')
    return render(request, 'contacts/contact_update.html', {'contact': contact})





