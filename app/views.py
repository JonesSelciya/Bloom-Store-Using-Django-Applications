from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login,logout
from .models import Reg,bloom
from .forms import myform 
from django.shortcuts import render, get_object_or_404

# Create your views here.

def home(request):
    return render(request,'main.html')

def signup(request):
    if request.method == 'POST':
        # if form.is_valid():
           
            username = request.POST.get('pass')
            password = request.POST.get('hos')
            user = Reg.objects.create_user( username=username, password=password)
            user.save()
            auth_login(request, user)
            return redirect('home')
    return render(request,"registration.html")
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('nm')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('home')


def Addbloom(request):
    # nm=request.GET.get('flower')
    # print(nm)
  
    form = myform()
    if request.method == 'POST':  
        form = myform(request.POST, request.FILES)  
        if form.is_valid():  
            form.save() 
        return redirect('') 
        
    return render (request,'add.html', {'form': form})

def viewbloom(request,name):
    cate=bloom.objects.filter(category=name)
    return render(request,'view.html',{'form':cate})



    

def orderbloom(request, id):
    # Get the Flower object based on the provided name
    flower = get_object_or_404(bloom, id=id)

    # Access the attributes of the Flower object
    flower_name = flower.name
    flower_image = flower.image
    flower_price = flower.price

    # You can pass these variables to the template
    context = {
        'flower_name': flower_name,
        'flower_image': flower_image,
        'flower_price': flower_price,
    }

    return render(request, 'order.html', context)



def orderdetails(request):
    pass


