# views.py file
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from.forms import  CreateNewList
# Create your views here.

def index(response, id):
	ls = ToDoList.objects.get(id=id)
	if ls in response.user.todolist.all():

		if response.method =="POST":
			print(response.POST)
			if response.POST.get("save"):
				for item in ls.item_set.all():
					if response.POST.get("c" + str(item.id)) == "clicked":
						item.complete = True
					else:
						item.complete = False
					item.save()
			elif response.POST.get("newItem"):
				txt = response.POST.get("new")

				if len(txt) > 2:
					ls.item_set.create(text=txt, complete=False)
				else:
					print("invalid")

		return render(response, "main/list.html", {"ls":ls})
	return render(response, "main/view.html", {})

def home(response):
	return render(response, "main/home.html", {})

def create(response):
	if response.method == "POST":
		form = CreateNewList(response.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()
			response.user.todolist.add(t)

		return HttpResponseRedirect("/%i" %t.id)
	else:
		form = CreateNewList()
	return render(response, "main/create.html", {"form":form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
		
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to your home page
        else:
            # Handle invalid login
            return render(request, 'registration/login.html', {'error': 'Invalid login credentials'})

    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def views(response):
	return render(response,"main/view.html",{})