from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views import View
from todo.form import  *
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
# Create your views here.


def login_required(fn):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Please Login to Access the data....")
            return redirect('auth_login')
        else:
            return fn(request, *args, **kwargs)
    return wrapper


decs = [login_required, never_cache]

# Create your views here.


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user_object = authenticate(request, username=uname, password=pwd)
            if user_object:
                login(request, user_object)
                print("login sucess")
                return redirect("home")
        print("invalid")
        return render(request, "login.html", {"form": form})



class LogoutView(View):
    def get(self, request, *args, **kwargs):
        print(request.user)
        logout(request)
        print(request.user)
        return redirect('auth_login')


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'register.html', {'form': form})
    def post(self, request, *args, **kwargs):
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            print("Success")
            messages.success(request, " Account Created Successfully..")
            return redirect('auth_login')
        else:
            print("error")
            return render(request, 'register.html',{'form':form})

@method_decorator(decs, name="dispatch")
class IndexView(View):
   def get(self, request, *args, **kwargs):
       form=TodoForm()
       todos=Todos.objects.filter(user=request.user)
       return render(request, "index.html", {"form": form,"todos":todos})
   def post(self, request, *args, **kwargs):
       form=TodoForm(request.POST)
       if form.is_valid():
           form.instance.user=request.user
           form.save()
           print("Todo Added")
           return redirect("home")
       else:
           print("Error")
           return redirect('home')


@method_decorator(decs, name="dispatch")
class CheckView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        Todos.objects.filter(id=id).update(status=True)
        return redirect("home")


@method_decorator(decs, name="dispatch")
class UncheckView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        Todos.objects.filter(id=id).update(status=False)
        return redirect("home")

@method_decorator(decs, name="dispatch")
class UpdateView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        id = kwargs.get("pk")
        obj=Todos.objects.get(id=id)

        form=TodoForm(request.POST,instance=obj)
        print(name,id)
        if form.is_valid():
            form.save()
        return redirect("home")
    
@method_decorator(decs, name="dispatch")
class DeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Todos.objects.filter(id=id).delete()
        return redirect("home")