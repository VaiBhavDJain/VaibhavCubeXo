from django.http import HttpResponse
from django.shortcuts import render,redirect
from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from . models import Wallet,Transaction

def index(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
			return redirect('/trans')
				
		else:
			return render(request,'register.html')

	return render(request,'login.html')

def register(request):
	form = UserCreationForm()
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
	context = {'form': form}
	return render(request, 'register.html',context)


def amount_credit_debit(request):
	if request.method=='POST':
		amount=request.POST.get('amount')
		transaction=request.POST.get('credit-debit')
		allData = []
		data=Wallet.objects.filter(user_id=request.user)
		for cat in data:
			allData.append(cat)

		for i in allData: 
			if transaction=='Debit':
				i.balance=i.balance-(int(amount))
				i.save()
			
			if transaction=='Credit':
				i.balance=i.balance+(int(amount))
				i.save()
			
		if(transaction!=''):
			t = Transaction(user_id=request.user,transaction=transaction,amount=(int(amount)))
			t.save()
		return redirect('/trans')
	return render(request,'transaction.html')


def trans(request):
	allData = []
	data=Wallet.objects.filter(user_id=request.user)
	for cat in data:
		print(cat)
		allData.append(cat)
		params={'allData':allData}
	return render(request,'transaction.html',params)

def transHistory(request):
	allData=[]
	data=Transaction.objects.filter(user_id=request.user).order_by("-trans_date")
	for cat in data:
		print(cat)
		allData.append(cat)
		params={'allData':allData}
	return render(request,'transactionHistory.html',params)