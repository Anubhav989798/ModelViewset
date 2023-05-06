from django.shortcuts import render
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .Validations import *
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import login
from .send_mail import mailsend



# Create your views here.
class UserRegistrationView(ModelViewSet):
    queryset=RegistrationModel.objects
    serializer_class=UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        data=request.data
        #validating all the data
        try:
            validation_for_profile(data['profile'])
            validation_for_address(data['address'])
            validation_for_username(data['username'])
            validation_for_email(data['email'])
            validation_for_first_name(data['first_name'])
            validation_for_last_name(data['last_name'])
            validation_for_password(data['password'],data['cpassword'])
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
        #checking for username exist or not
        try:
            user=User.objects.get(username=data['username'])
            if user:
                return Response({'msg':'username already exist'},status=status.HTTP_302_FOUND)
            e_mail=User.objects.get(email=data['email'])
            if e_mail:
                return Response({'msg':'Email already exist'},status=status.HTTP_302_FOUND)
        except:
            pass
        #creating entry into database
        try:
            user=User.objects.get(email=data['email'])
            if user:
                return Response({'msg':'Email already exist'},status=status.HTTP_302_FOUND)
        except:
            pass
        try:
            user=User.objects.create_user(username=data['username'],email=data['email'],first_name=data['first_name'],last_name=data['last_name'])
            user.set_password(data['password'])
            user.save()
            register=self.queryset.create(profile=data['profile'],address=data['address'],user_id_id=user.id)
            register.save()
            token,_=Token.objects.get_or_create(user=user)
            data=User.objects.get(id=user.id)
            serializers=self.serializer_class(data)
            return Response({'msg':'user registration successfully','token':token.key,'data':serializers.data},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_406_NOT_ACCEPTABLE)

class Userlogin(ModelViewSet):
    queryset=User.objects
    serializer_class=UserRegistrationSerializer
    permission_classes=[AllowAny]
    def create(self,request,*args, **kwargs):
        data=request.data
        try:
            validation_for_username(data['username'])
            validation_for_password1(data['password'])
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
        try:
            user=authenticate(username=data['username'],password=data['password'])
            if not user:
                return Response({'msg':'user not Register'},status=status.HTTP_401_UNAUTHORIZED)
            user=self.queryset.get(id=user.id)
            token=Token.objects.get(user_id=user.id)
            data=User.objects.get(id=user.id)
            serializers=self.serializer_class(data)
            login(request,user)
            return Response({'msg':'user login successfully','token':token.key,'data':serializers.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_406_NOT_ACCEPTABLE)
        
class UserLogout(ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=User.objects
    def create(self,request,*args, **kwargs):
        try:
            user=User.objects.get(id=request.user.id)
            Token.objects.get(user=user).delete()
            return Response({'msg':'user logout successfully'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e),'msg':'some error occured for the logout'},status=status.HTTP_400_BAD_REQUEST)

class PostView(ModelViewSet):
    queryset=PostModel.objects
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    serializer_class=PostSerializer
    
    def list(self,request,*args, **kwargs):
        try:
         data=self.queryset.all()
         data=self.serializer_class(data,many=True).data
         return Response({'data':data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_304_NOT_MODIFIED)


    def create(self,request,*args,**kwargs):
        data=request.data
        try:
            post=self.queryset.create(Title=data['title'],description=data['description'],user_id_id=request.user.id)
            return Response({'msg':'post created sucessfully'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_406_NOT_ACCEPTABLE)
        
class RepportedpostView(ModelViewSet):
    queryset=ReportedbyPostModel.objects.all()
    serializer_class=ReportedbyPostSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def create(self,request,*args, **kwargs):
        data=request.data
        try:
            report=ReportedbyPostModel.objects.create(comment=data['comment'],post_id_id=data['id'],user_id_id=request.user.id)
            report.save()
            return Response({'msg':'Reported successfully'},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_406_NOT_ACCEPTABLE)
    
class CommentView(ModelViewSet):
    queryset=CommentModel.objects.all()
    serializer_class=CommentSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def list(self,request,*args, **kwargs):
        try:
            data=CommentModel.objects.filter(parent_id__isnull=True)
            serializers=self.serializer_class(data,many=True).data
            return Response({'data':serializers},status=status.HTTP_200_OK)
        except Exception as e:
             return Response({'error':str(e)},status=status.HTTP_406_NOT_ACCEPTABLE)

class likedbyView(ModelViewSet):
    queryset=likedModel.objects.all()
    serializer_class=likedSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

class ReportedcommentView(ModelViewSet):
    queryset=ReportedbyCommentModel.objects.all()
    serializer_class=ReportedCommentSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

