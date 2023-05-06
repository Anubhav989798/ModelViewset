from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'signup',UserRegistrationView,basename='signup')
router.register(r'login',Userlogin,basename='login')
router.register(r'post',PostView,basename='post')
router.register(r'reportpost',RepportedpostView,basename='reportpost')
router.register(r'liked',likedbyView,basename='liked')
router.register(r'reportcomment',ReportedcommentView,basename='reportcomment')
router.register(r'comment',CommentView,basename='comment')
router.register(r'logout',UserLogout,basename='logout')


urlpatterns = [
    
]

urlpatterns+=router.urls