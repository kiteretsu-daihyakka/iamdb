from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from imdbpie import Imdb
from .forms import UserForm
from .models import *
from django.views import generic,View
from django.urls import reverse_lazy

# Create your views here..
imdb = Imdb()

@login_required
def index(request):
    return render(request,'iamdbApp/index.html',context={})

def search(request):
    txt = request.GET.get('srch_txt')
    # movie_details = None
    print(txt)
    movie_details = imdb.search_for_title(txt)

    print(movie_details)
    return JsonResponse(data={'rslt':txt,'movie_details_list':movie_details})

def addToWishList(request):
    imdbId = request.GET.get('imdbId')
    print(imdbId)
    rslt=1
    try:
        if imdbId in WatchList.objects.filter(user=AuthUser.objects.get(id=request.user.id)).values('contentId'):
            rslt=-1
        else:
            WatchList(user=AuthUser.objects.get(id=request.user.id),contentId=imdbId).save()
    except:
        rslt=0
    print(rslt)
    return JsonResponse(data={'rslt': rslt})

def addToWatchList(request):
    imdbId = request.GET.get('imdbId')
    print(imdbId)
    rslt = 1
    try:
        if imdbId in WishList.objects.filter(user=AuthUser.objects.get(id=request.user.id)).values('contentId'):
            rslt = -1
        else:
            WishList(user=AuthUser.objects.get(id=request.user.id), contentId=imdbId).save()
    except:
        rslt = 0
    print(rslt)
    return JsonResponse(data={'rslt': rslt})

@login_required
def userProfile(request):
    return UserDetailAndUpdate.as_view()(request,pk=request.user.id)

# class UserDetailView(generic.DetailView):
#     model=AuthUser
#     template_name = 'iamdbApp/user-profile.html'

class UserDetailAndUpdate(generic.UpdateView):
    model = AuthUser
    fields = ['username', 'first_name', 'last_name', 'email', 'date_joined']
    success_url = reverse_lazy('iamdbApp:user-profile')
    # fields = '__all__'

# thas was for registration which i wss using in show and update details
# class UserProfileForm(View):
#     def get(self, request):
#         usr_form = UserForm(instance=AuthUser())
#         template = 'iamdbApp/user-profile.html'
#         context = {'usr_form': usr_form}
#         return render(request, template, context)
#
#     def post(self, request):
#         # context = {}
#         usr_form  = UserForm(request.POST, instance=AuthUser())
#
#         if usr_form.is_valid():
#             new_adv = usr_form.save(commit=False)
#             new_adv.auth_user = User.objects.get(email=request.user.email)
#             print(new_adv.auth_user.email)
#             print(cart_forms)
#             new_adv.save()
#             for cart_form in cart_forms:
#                 new_cart = cart_form.save(commit=False)
#                 new_cart.id = new_adv
#                 # new_cart.auth_user=User.objects.get(id=1)
#                 new_cart.save()
#                 # print(new_cart.noofdays)
#             return redirect("/adminsite/list/Cartdetail")
#         context = {'adv_form': adv_form, 'cart_forms': cart_forms}
#         return render(request, 'admm/new_cart.html', context)
#     # return render(request,'iamdbApp/user-profile.html',context={})
