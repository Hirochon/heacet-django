from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Nogizaka,Message
from .forms import NogizakaForm,FindForm,CheckForm,MessageForm
from django.core.paginator import Paginator

def index(request, num=1):
	data = Nogizaka.objects.all()
	##page = Paginator(data,3)
	params = {
		"title":"やっはろー",
		"message":"",
		##"data":page.get_page(num)
	}
	return render(request, 'heacet/index.html', params)

def create(request):
	params = {
		"title":"くりえいとぺーじ。",
		"form":HeacetForm(),
	}
	if (request.method == "POST"):
		name = request.POST["name"]
		mail = request.POST["mail"]
		gender = 'gender' in request.POST
		age = int(request.POST["age"])
		birth = request.POST["birthday"]
		nogizaka = Nogizaka(name=name,mail=mail,gender=gender,age=age,birthday=birth)
		nogizaka.save()
		return redirect(to='/heacet')
	return render(request, 'heacet/create.html', params)

def newcreate(request):
	if (request.method == 'POST'):
		nogizaka = NogizakaForm(request.POST, instance=Nogizaka())
		nogizaka.save()
		return redirect(to="/heacet")
	params={
		'title':'くりえいとぺーじ。',
		'form':NogizakaForm(),
	}
	return render(request, 'heacet/create.html', params)

def edit(request,num):
	obj = Nogizaka.objects.get(id=num)
	if (request.method == 'POST'):
		nogizaka = NogizakaForm(request.POST, instance=obj)
		nogizaka.save()
		return redirect(to='/heacet')
	params = {
		'title':'へんしゅうぺーじ。',
		'id':num,
		'form':NogizakaForm(instance=obj),
	}
	
def delete(request,num):
	member = Nogizaka.objects.get(id=num)
	if (request.method == 'POST'):
		member.delete()
		return redirect(to='/heacet')
	params = {
		'title':'さくじょぺーじ。',
		'member':member,
	}
	return render(request, 'heacet/delete.html', params)

def find(request):
	if (request.method == 'POST'):
		msg = 'search result:'
		form = FindForm(request.POST)
		str = request.POST['find']
		val = str.split()
		member = Nogizaka.objects.all()[int(val[0]):int(val[1])]
	else:
		msg = 'serch words...'
		form = FindForm()
		member = Nogizaka.objects.all()
	params = {
		'title':msg,
		'data':member,
		'message':msg,
		'form':form,
	}
	return render(request, 'heacet/find.html', params)

def sql_find(request):
	if (request.method == 'POST'):
		msg = request.POST['find']
		form = FindForm(request.POST)
		sql = 'select * from heacet_nogizaka'
		if(msg != ''):
			sql += ' where ' + msg
		member = Nogizaka.objects.raw(sql)
		msg = sql
	else:
		msg = 'serch words...'
		form = FindForm()
		member = Nogizaka.objects.all()
	params = {
		'title':msg,
		'data':member,
		'msg':msg,
		'form':form,
	}
	return render(request, 'heacet/find.html', params)

def check(request):
	params = {
		'title':'Hello',
		'message':'check validation.',
		'form':NogizakaForm(),
	}
	if(request.method == "POST"):
		obj = Nogizaka()
		form = NogizakaForm(request.POST, instance=obj)
		params['form'] = form
		if (form.is_valid()):
			params['message'] = 'OK!'
		else:
			params['message'] = 'No good...'
	return render(request, 'heacet/check.html', params)

def message(request, page=1):
	if (request.method == 'POST'):
		obj = Message()
		form = MessageForm(request.POST, instance=obj)
		form.save()
	data = Message.objects.all().reverse()
	paginator = Paginator(data, 5)
	params = {
		'title':'Message',
		'form':MessageForm(),
		'data':paginator.get_page(page),
	}
	return render(request, 'heacet/message.html', params)
