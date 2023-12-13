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



