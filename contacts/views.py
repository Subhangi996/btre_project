from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    listings_id = request.POST['listings_id']
    listings = request.POST['listings']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

    #Check if user has already made an inquiry

    if request.user.is_authenticated:
          user_id = request.user.id
          has_contacted = Contact.objects.all().filter(listings_id=listings_id, user_id=user_id)
          if has_contacted:
                messages.error(request, 'You already have made an inquiry for this listing')
                return redirect('/listings/'+listings_id)

    contact = Contact(listings=listings, listings_id=listings_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    # Send email
    #send_mail(
    #  'Property Listing Inquiry',
    #  'There has been an inquiry for ' + listings + '. Sign into the admin panel for more info',
    #  'subhangi.parija@gmail.com',
    #  [realtor_email, 'subhangi.parija@gmail.com'],
    # fail_silently=False
    #)

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/listings/'+listings_id)