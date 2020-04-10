"""alumni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from posts import views as post_view
from teach import views as teach_view
from users import views as user_views
from django.contrib.auth import views as auth_views
from projects import views as project_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',post_view.create_view,name='create'),
    path('profile/', user_views.profile, name='profile'),
    path('list/',post_view.list_view,name='list'),
    path('blog/<str:slug>',post_view.detail_view,name='details'),
    path('class',teach_view.list_view,name='class-list'),
    path('<str:slug>',teach_view.detail_view,name='class-details'),
    path('<str:slug>/booked',teach_view.booked_view,name="class-booked"),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('front/',teach_view.front_view,name='front'),

    #Projects
    path('procreate/',project_view.create_view,name="project-create"),
    path("prolist/",project_view.list_view,name="project-list"),
    path("project/<str:slug>",project_view.detail_view,name="project-detail"),

    #
    path("project/<str:slug>/like",project_view.PostLikeToggle.as_view(),name="likes"),
    path("project/api/<str:slug>/like",project_view.PostLikeAPIToggle.as_view(),name="apilikes")
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,     document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
