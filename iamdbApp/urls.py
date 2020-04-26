from django.urls import path
from .views import *


app_name='iamdbApp'

urlpatterns=[
    path('',index,name='index'),

    path('search/',search,name='search'),
    path('wishlist-add/',addToWishList,name='wishlist-add'),
    path('watchlist-add/',addToWatchList,name='watchlist-add'),


    path('user-profile/',userProfile,name='user-profile'),
    path('user-profile/backend/<int:pk>/',UserDetailAndUpdate.as_view(),name='user-profile-backend'),
]