from django.shortcuts import render, get_object_or_404, redirect
from .models import ServiceTicket, UserProfile
from django.http import JsonResponse


#Home page
def home(request):
    return render(request, 'home.html')


def submit_ticket(request):
    if request.method == "POST":
        # Fetch or create user
        user, _ = UserProfile.objects.get_or_create(
            email=request.POST['email'],
            defaults={
                'full_name': request.POST['name'],
                'contact_number': request.POST['contact_number']
            }
        )
        # Create service ticket
        ticket = ServiceTicket.objects.create(
            user=user,
            category=request.POST['category'],
            description=request.POST['description']
        )
        return JsonResponse({'message': 'Ticket created successfully!', 'ticket_id': ticket.id})
    return render(request, 'submit_ticket.html')

def track_ticket(request, ticket_id):
    ticket = get_object_or_404(ServiceTicket, id=ticket_id)
    return render(request, 'track_ticket.html', {'ticket': ticket})
