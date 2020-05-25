from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from tracker.models import MyUser
from tracker.models import Ticket
from tracker.forms import LoginForm
from tracker.forms import SubmitTicketForm
from tracker.forms import EditTicketForm

# Create your views here.


@login_required
def index(request):
    data = Ticket.objects.all()
    new_ticket = Ticket.objects.filter(status=Ticket.NEW)
    in_progress_ticket = Ticket.objects.filter(status=Ticket.IN_PROGRESS)
    completed_ticket = Ticket.objects.filter(status=Ticket.DONE)
    invalid_ticket = Ticket.objects.filter(status=Ticket.INVALID)

    return render(request, 'index.html',
                  {'data': data,
                   'new_ticket': new_ticket,
                   'in_progress_ticket': in_progress_ticket,
                   'completed_ticket': completed_ticket,
                   'invalid_ticket': invalid_ticket
                   })


def loginview(request):
    html = 'login_form.html'

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )

    form = LoginForm()

    return render(request, html, {'form': form})


def logoutview(request):
    if request.method == 'GET':
        logout(request)

    return HttpResponseRedirect(reverse('login'))


@login_required
def submitticket(request):
    html = 'submit_ticket_form.html'

    if request.method == 'POST':
        form = SubmitTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                filing_user=request.user,
                title=data['title'],
                description=data['description'],
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = SubmitTicketForm()

    return render(request, html, {'form': form})


@login_required
def ticketdetail(request, ticketdetail_id):
    # ticketid = Ticket.objects.get(id=ticketdetail_id)
    data = Ticket.objects.get(id=ticketdetail_id)
    return render(request, 'ticketdetail.html', {'data': data})


@login_required
def userdetails(request, user_id):
    user_ = MyUser.objects.get(id=user_id)
    submitted_tickets = Ticket.objects.filter(filing_user=user_)
    assigned_tickets = Ticket.objects.filter(assigned_user=user_)
    completed_tickets = Ticket.objects.filter(completing_user=user_)
    return render(request, 'user_detail.html',
                  {'user_': user_, 'submitted_tickets': submitted_tickets, 'assigned_tickets': assigned_tickets, 'completed_tickets': completed_tickets})


@login_required
def ticketedit(request, id):
    data = Ticket.objects.get(id=id)
    if request.method == 'POST':
        form = EditTicketForm(request.POST, instance=data)
        form.save()
        if form.is_valid():
            data.title = form.cleaned_data['title']
            data.description = form.cleaned_data['description']
            if data.status == 'DONE':
                data.completing_user = data.assigned_user
                data.assigned_user = None
            data.save()
            return HttpResponseRedirect(reverse('ticketdetail', args=(data.id,)))

    form = EditTicketForm(instance=data)
    return render(request, 'edit_ticket_form.html', {'form': form, 'data': data})


@login_required
def assignticket(request, id):
    data = Ticket.objects.get(id=id)
    data.status = 'IN_PROGRESS'
    data.assigned_user = request.user
    data.completing_user = None
    data.save()
    return HttpResponseRedirect(reverse('ticketdetail', args=(data.id,)))


@login_required
def completeticket(request, id):
    data = Ticket.objects.get(id=id)
    data.status = 'DONE'
    data.completing_user = data.assigned_user
    data.assigned_user = None
    data.save()
    return HttpResponseRedirect(reverse('ticketdetail', args=(data.id,)))


@login_required
def invalidticket(request, id):
    data = Ticket.objects.get(id=id)
    data.status = 'INVALID'
    data.completing_user = None
    data.assigned_user = None
    data.save()
    return HttpResponseRedirect(reverse('ticketdetail', args=(data.id,)))
