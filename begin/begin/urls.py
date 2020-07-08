"""begin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path,include
from .views import (
	home_page,
	contact_page,
	about_page,
	smile_page,
    login_page,
    register_page,
    logout_view,
    gallery_page,    
    set_timezone,
	)
from account.views import (
    account_info_view,
    # account_update_info_view,
    user_profile,
    profile_page,
    account_detail_info_view,
    profile_create_view,
    )
from blog.views import blog_post_create_view
from searches.views import search_view 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page),
    re_path(r'^page/$',about_page),
    re_path(r'^pages/$',about_page),
    re_path(r'^about/$',about_page),
    path('contact/',contact_page),
    path('blog-new/',blog_post_create_view),
    path('blog/',include('blog.urls')), #by proving include('blog.urls') we give the location of the content that we have
    path('smile/',smile_page),
    path('search/',search_view),
    path('login/',login_page),
    path('logout/',logout_view),
    path('register/',register_page),
    path('avatar/',include('avatar.urls')),
    path('timezone/',set_timezone),
    path('account/',include('account.urls')),
    path('account-create/',profile_create_view),
    path('gallery/',gallery_page),
    # path('user-profile/',user_profile),
    # path('account-detail/<str:slug>/',account_detail_info_view),
    # path('account-update/',account_update_info_view)
]

if settings.DEBUG:
    #TEST MODE
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
