from django.shortcuts import render


from .forms import SimpleForm

def demo(request):
	obj = SimpleForm()
	if request.method=="POST":
		a = request.POST	
		return render(request, 'register.html', {'form':obj,'data':a})
	context = {"form":obj}
	return render(request, 'register.html', context)


def index(request):
	if request.method == "POST":
		n = request.POST['fullname']
		data = {"name":n}
		return render(request, 'index.html', data)
	return render(request,'index.html')    

# Create your views here.
