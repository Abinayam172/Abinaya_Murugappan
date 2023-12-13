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

