from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate,logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import * 
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

# Create your views here.
def index(request):
    return render(request, 'index.html')


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        
        context = {
            'user': user,
            'profile': profile,
        }

        return render(request, 'profile.html', context)
    
class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = UserProfile
    fields = ['neighborhood','email', 'bio', 'birth_date','picture']
    template_name = 'profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})
        

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False

   
# def search_business(request):
#     current_user= request.user
#     if request.method == 'GET':
#         name = request.GET.get("name")
#         businesses = Business.objects.filter(name__icontains=name).all()
#         return render(request, 'search.html', {'businesses': businesses,'current_user':current_user})

# def register_request(request,):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
  
#     if form.is_valid():
#         user = form.save()
#         login(request, user)
#         messages.success(request, "Registration successful." )
#         return redirect("main:home")

#     messages.error(request, "Unsuccessful registration. Invalid information.")
#     form = NewUserForm()
#     return render (request=request, template_name="main/register.html", context={"register_form":form})

# def login_request(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}.")
#                 return redirect("main:home")
#             else:
#                 messages.error(request,"Invalid username or password.")
#     else:
#         messages.error(request,"Invalid username or password.")
#     return render(request,"login.html")
#     # form = AuthenticationForm()
#     # return render(request=request, template_name="main/login.html", context={"login_form":form})


# def logout_request(request):
#     logout(request)
#     messages.info(request, "You have successfully logged out.") 
#     return redirect("main:home")

