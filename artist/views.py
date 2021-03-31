from django.shortcuts import render
from .models import Services, Art, Booking, Contact

# Create your views here.

def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	if request.method == "POST":
		cname = request.POST['Name']
		cemail = request.POST['Email']
		cphone = request.POST['Phone']
		cmsg = request.POST['Message']

		con = Contact(c_name=cname, c_email=cemail, c_phone=cphone, c_msg=cmsg)
		con.save()
		yes = "yes"
		return render(request, 'contact.html', {
			'yes' : yes,
			'msg' : "Thank you for contacting us..."
			})
	else:
		yes = "no"
		return render(request, 'contact.html', {
			'yes' : yes
			})

def services(request):
	s = Services.objects.all()
	yes = "no"
	return render(request, 'services.html', {
		'service' : s,
		'yes' : yes,
		})

def subservice(request, myservice):
	subs = Art.objects.all()
	list1 = []
	for i in subs:
		if i.a_service.service == myservice:
			list1.append(i)
	
	return render(request, 'subservice.html', {
		'subservice' : list1,
		})

def checkout(request, myid):
	serve1 = Art.objects.filter(a_id=myid)
	return render(request, 'checkout.html', {
		's' : serve1[0],
		})

def booking(request, sid):
	booking_of = Art.objects.filter(a_id=sid)
	s = Services.objects.all()
	if request.method == "POST":
		bname = request.POST.get('uname', '')
		baddress = request.POST.get('uadd', '')
		bcontact = request.POST.get('ucontact', '')
		bdate = request.POST.get('udate', '')

		book = Booking(booking_user=bname, booking_phone=bcontact, booking_address=baddress, 
			booking_date_of_service=bdate, booking_service=booking_of[0])
		book.save()
		yes = "yes"
		return render(request, 'services.html', {
			'ss' : booking_of[0],
			'service' : s,
			'yes' : yes,
			'msg' : f"Thanks For Booking, You will get a call soon from the {booking_of[0].a_name}."
			})
