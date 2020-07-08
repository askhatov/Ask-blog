from django.shortcuts import render
from blog.models import BlogPost
from django.shortcuts import render,get_object_or_404
# Create your views here.
from .models import Account
from .forms import AccountModelForm

def account_info_view(request):
	form = AccountModelForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		print(form.cleaned_data)
		# title = forms.cleaned_data['title']
		# obj   = BlogPost.objects.create(**form.cleaned_data)
		obj = form.save(commit=False)
		obj.user = request.user
		obj.name = form.cleaned_data.get('name')
		obj.save()

		form = AccountModelForm

	context = {
	'form':form
	}
	template_name = 'account/account_info.html'
	return render(request,template_name,context)


def account_detail_info_view(request,slug):
	instance = get_object_or_404(Account,slug=slug)
	template_name = 'account/account_detail_info.html'
	context = {
	'object':instance
	}
	return render(request,template_name,context)


# def account_update_info_view(request,slug):
	obj = get_object_or_404(Account, slug=slug)
	form = AccountModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	template_name = 'form.html'
	context = {'form':form,'title':f"Update {obj.title}"}

	return render(request,template_name,context)

def profile_create_view(request):
	form = AccountModelForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.user = request.user
		# obj = form.cleaned_data('image')
		obj.save()
		print(obj.image)
		form = AccountModelForm
	template_name="blog/form.html"
	context={'form':form}
	return render(request,template_name,context)

def profile_page(request):
	# instance = get_object_or_404(Account,slug=slug)
	instance = Account.objects.all()
	if request.user.is_authenticated:
		my_ins = Account.objects.filter(user=request.user)
		ins = (instance | my_ins).distinct()
	

	qs = BlogPost.objects.all().published() #queryset -> list of python objects
	if request.user.is_authenticated:
		my_qs = BlogPost.objects.filter(user=request.user)
		qs = (qs | my_qs).distinct() # we used distinct so the same post would not be posted twice
	# qs = BlogPost.objects.filter(publish_date__lte=now)# video number 53
	template_name = 'account/profile.html'
	context = {
	'object_list':qs,
	'object':instance
	}
	

	return render(request,template_name,context)


def user_profile(request):
	qs = BlogPost.objects.all()
	if request.user.is_authenticated:
		my_qs = BlogPost.objects.filter(user=request.user)
		context = {
		'object_list':my_qs
		}
	

	return render(request,'account/user_profile.html',context) 