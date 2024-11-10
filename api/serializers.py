from rest_framework import serializers
from quiz.models import Catalog, Test, Question, Answer
from user.models import CustomUser
from django.contrib.auth import authenticate






class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'surname', 'username', 'email', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data.get('name', ''),
            surname=validated_data.get('surname', ''),
            phone_number=validated_data.get('phone_number', ''),
        )
        return user




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text','question', 'is_correct']  
class QuestionSerializer(serializers.ModelSerializer):
    test = serializers.PrimaryKeyRelatedField(queryset=Test.objects.all())

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'test'] 

class TestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Test
        fields = ['id', 'title', 'description','catalog'] 

class CatalogSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Catalog
        fields = ['id', 'name', 'description']  
