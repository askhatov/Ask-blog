from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path,include


from account.views import (
    account_info_view,
    # account_update_info_view,
    user_profile,
    profile_page,
    account_detail_info_view,
    )

urlpatterns = [
	path('',profile_page), 
    # path('user-profile/',user_profile),
    # path('<str:slug>',account_detail_info_view),
    # path('<str:slug>/info/',account_info_view),
    # path('<str:slug>/update/',account_update_info_view)
]