# Model view template (MVP)
# WHEN WE WANT TO make a page we satrt with a view not html
from django.http import HttpResponse 
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,get_user_model
from django.template.loader import get_template
from .forms import ContactForm, RegisterForm, LoginForm
from blog.models import BlogPost
from django.contrib import auth

def home_page(request): #we request something and then we return the response 
	# return render(request, "hello_world.html")
	
	my_title = "Hello world..."
	qs = BlogPost.objects.all()#[:5]
	context = {"title":"Welcome to try django" ,'blog_list':qs}
	# if request.user.is_authenticated:
	# 	context = {"title":my_title, "my_list":[1,2,3,4,5]}

	# template_name = "title.txt"
	# template_obj = get_template(template_name)
	# rendered_string = template_obj.render(context)
	# # doc = "<h1>{title}</h1>".format(title=my_title)
	# # django_rendered_doc = "<h1>{{title}}</h1>".format(title=my_title)
	return render(request, "home.html",context)

def about_page(request): #we request something and then we return the response 
	return render(request, "about.html",{"title":"About us"})

def contact_page(request):
	# print(request.POST)
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm()
	context = {
	"title":"Contact us",
	"form":form
	}
	return render(request, "contact.html",context)

def gallery_page(request):
	return render(request,'gallery.html')

def smile_page(request): #we request something and then we return the response 
	context = {"title":"Smile"}
	template_name = "hello_world.html"
	template_obj = get_template(template_name)
	rendered_item = template_obj.render(context)
	return HttpResponse(template_obj.render(context))


def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		'form':form
		}
	
	print("User logged in")
	if form.is_valid():# is_valid holds if the input has an appropriate data type.
		print(form.cleaned_data)
		username = form.cleaned_data.get('username')#we use cleaned_data when we need to know where the validation data is. of the method is valid then it will return true
		password = form.cleaned_data.get('password')#cleaned_data is an object not a function
		# form.save() #so when we make save() it will save in admin of models that we created
		form = LoginForm()
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			context['form'] = LoginForm()
			return redirect('/')

		else:
			print("Error")
	# if form.is_valid(form.cleaned_data):
	# 	print(form.cleaned_data)
	return render(request,'auth/login.html',context)



User = get_user_model()

def logout_view(request):
	auth.logout(request)

	return redirect('/login')

	# return render(request,'logout.html')


def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		'form':form
		}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get('username')#we use cleaned_data when we need to know where the validation data is. of the method is valid then it will return true
		email    = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		new_user = User.objects.create_user(username,email,password)
		print(new_user)
		if new_user is not None:
			login(request,new_user)
			context['form'] = LoginForm()
			return redirect('/')

	return render(request,'auth/register.html',context)




def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'timezone.html', {'timezones': pytz.common_timezones})