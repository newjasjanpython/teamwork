from django.http import JsonResponse, HttpResponse
import logging
from django.shortcuts import render,get_object_or_404
from quiz.models import Catalog, Test, Question, Answer
from user.models import CustomUser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets,generics,status,permissions
from django.contrib.auth.hashers import PBKDF2PasswordHasher, make_password
from .serializers import CustomUserSerializer, LoginSerializer, CatalogSerializer, TestSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated

class CustomLoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            print(username)
            print(password)
            try:
                user = CustomUser.objects.get(username=username)
            except CustomUser.DoesNotExist:
                return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
            
            hasher = PBKDF2PasswordHasher()
            password_hash = hasher.encode(password, user.password.split('$')[-1])
            print(user.password)
            print(password_hash)
            if user.password == password:
                user_data = {
                    'name': user.name,
                    'surname': user.surname,
                    'email': user.email,
                    'phone_number': user.phone_number,
                }
                print(user_data)
                request.user = user
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer




class CatalogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

class CatalogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

class TestListCreateAPIView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

# Logger setup
logger = logging.getLogger(__name__)

def test_view(request, test_id):
    # Retrieve the test object, or return 404 if not found
    test = get_object_or_404(Test, id=test_id)
    
    # Get questions related to the test
    questions = test.questions.all()

    # Render the template and pass the test and questions
    return render(request, 'submit_test.html', {
        'test': test,
        'questions': questions
    })

@api_view(['POST'])
def submit_test(request, test_id):
    """
    Handles the test submission, calculates the score, and returns the result.
    """
    try:
        # Retrieve the test based on the test_id
        test = Test.objects.get(id=test_id)
        logger.info(f"Test retrieved: {test.name}")

        # Get the submitted answers from the request (assumed to be in the body of the request)
        submitted_answers = request.data.get('answers', {})
        logger.info(f"Submitted answers: {submitted_answers}")

        # Make sure that answers were provided
        if not submitted_answers:
            return JsonResponse({"error": "No answers submitted"}, status=400)

        score = 0
        total_questions = 0

        # Loop through each question in the test
        for question in test.questions.all():
            total_questions += 1
            correct_answer = question.correct_answer
            logger.info(f"Question: {question.text}, Correct Answer: {correct_answer.text}")

            # Check if the answer provided by the user matches the correct one
            if str(question.id) in submitted_answers and submitted_answers[str(question.id)] == str(correct_answer.id):
                score += 1

        # Log the score and total questions
        logger.info(f"Score: {score}, Total Questions: {total_questions}")
        # Return the score with total number of questions
        return JsonResponse({
            "score": score,
            "total_questions": total_questions,
            "message": f"You scored {score} out of {total_questions}"
        }, status=200)
        
    except Test.DoesNotExist:
        return JsonResponse({"error": "Test not found"}, status=404)