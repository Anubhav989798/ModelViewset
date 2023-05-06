from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserDetailsSserializer(serializers.ModelSerializer):
    class Meta:
        model=RegistrationModel
        fields='__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    details=serializers.SerializerMethodField()
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','details']
    
    def get_details(self,obj):
        try:
            data=UserDetailsSserializer(RegistrationModel.objects.get(user_id_id=obj.id)).data
        except:
            data="no data"
        return data
    
class ReportedbyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReportedbyPostModel
        fields='__all__'
    
class PostSerializer(serializers.ModelSerializer):
    reported_by=serializers.SerializerMethodField()
    class Meta:
        model=PostModel
        fields='__all__'

    def get_reported_by(self,obj):
        try:
            data=ReportedbyPostSerializer(ReportedbyPostModel.objects.filter(post_id_id=obj.id),many=True).data
        except:
            data="No report on this post"
        return data
    
class likedSerializer(serializers.ModelSerializer):
    class Meta:
        model=likedModel
        fields='__all__'

class ReportedCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReportedbyCommentModel
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    liked_by=serializers.SerializerMethodField()
    comment_by=serializers.SerializerMethodField()
    reported_by=serializers.SerializerMethodField()
    class Meta:
        model=CommentModel
        fields='__all__'

    def get_comment_by(self,obj):
        try:
            data=CommentSerializer(CommentModel.objects.filter(parent_id=obj.id),many=True).data
        except:
            data=[]
        return data
    
    def get_liked_by(self,obj):
        try:
            data=likedSerializer(likedModel.objects.filter(comment_id_id=obj.id),many=True).data
        except:
            data=[]
        return data
    
    def get_reported_by(self,obj):
        try:
            data=ReportedCommentSerializer(ReportedbyCommentModel.objects.filter(comment_id_id=obj.id),many=True).data
        except:
            data=[]
        return data



    