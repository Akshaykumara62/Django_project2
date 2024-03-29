from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import ContactForm,MasterForm,AttForm, CheckAttForm
from .models import Masterdata5 as md,Mark_Attendance2
from django.contrib.auth.decorators import login_required
from users_app.decorators import allowed_users
from django.contrib import messages
import time
from att_app.forms import CheckByDate
# Create your views here.
posts = [
{
	'name' : 'sabiha',
	'roll_number' : 8809,
	'class' : 'CSE'
},

{
	'name' : 'Ravana',
	'roll_number' : 8806,
	'class' : 'BSE'
}]

def home(request):
	#return HttpResponse("<h1> Hello Everyone </h1>")
	context = {'data': posts, 'title':'Game over'}
	return render (request, 'att_app/home.html',context)

def about(request):
	#return HttpResponse("<h1> This is all about the django </h1>")
	return render (request, 'att_app/about.html')

def form_test(request):
	form = ContactForm()
	context = {'form':form}
	return render (request, 'att_app/display_form.html',context)

def display_master(request):
	data = md.objects.all()
	context = {'data' : data}
	return render (request, 'att_app/display_data.html',context)
@login_required(login_url='login')
def master_data(request):
	form=MasterForm()
	context = {'form':form}

	if request.method =='POST':
		form1 = MasterForm(request.POST)
		if form1.is_valid():
			form1.save()
			messages.success(request, 'Record is added.')
			return redirect('display-master')

	return render (request, 'att_app/display_form.html',context)
def e_h(t1):
	t9 = time.localtime(t1)
	return time.strftime('%d-%m-%Y %H:%M')
	

def display_att(request,roll_number):
	context= {
	'data': Mark_Attendance2.objects.filter(roll_number = roll_number)
	}
	return render(request,'att_app/display_att.html',context)

def mark_att(request):
	form1 = AttForm()
	context = {'form':form1}
	if request.method =='POST':
		form1 = AttForm(request.POST)
		if form1.is_valid():
			try:
				mark1 = form1.save(commit=False)
				print(request.META.items())
				mark1.ip_address = request.META.get('REMOTE_ADDR')
				mark1.platform = request.META.get('HTTP_USER_AGENT')
				mark1.time1 = int(time.time())
				mark1.date1 = e_h(mark1.time1)
				mark1.Master = get_object_or_404(md, roll_number=mark1.roll_number)
				form1.save()
				messages.success(request, 'Attendance Marked:)')
				return redirect('display-att', roll_number=mark1.roll_number)
			except Exception as e:
				messages.warning(request, str(e))

	return render (request, 'att_app/display_form.html',context)
################################# Display things ###########################

@login_required(login_url='login')
@allowed_users(allowed_roles=['class10'])
def CheckAttAll(request):
	context = {'data':Mark_Attendance2.objects.all()}
	return render(request, 'att_app/display_att.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['class10','class5'])
def CheckAtt(request):
	form = CheckAttForm()
	context = {'form':form}
	if request.method=='POST':
		form = CheckAttForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			d1 = form.cleaned_data['roll_number']
			data = Mark_Attendance2.objects.filter(roll_number=d1)
			context = {'data': data}
			return render(request,'att_app/display_att.html', context)


	return render(request, 'att_app/display_form.html',context)


def CheckDate(request):
	form = CheckByDate()
	context = {'form':form}
	if request.method=='POST':
		fromdate = request.POST.get('fromdate')
		todate = request.POST.get('todate')
		
	
		form = CheckByDate(request.POST)
		#if form.is_valid():
			#print(form)
			#d1 = form.cleaned_data['date1']
		
		data = Mark_Attendance2.objects.all()
		#return render(request,'att_app/attend.html', context)
		context = {'data': data}
		#return render(request,'att_app/display_att.html', context)
	#return render(request, 'att_app/display_form.html', context)
	return render(request, 'att_app/attend.html', context)
	