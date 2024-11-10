from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
# Create a router instance
router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'catalogs', CatalogViewSet)
router.register(r'tests', TestViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
urlpatterns = [
    # Custom Login API
    path('login/', CustomLoginAPIView.as_view(), name='login'),
    
    # User-related endpoints
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserListCreateAPIView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    
    # Catalog-related endpoints
    path('catalogs/', CatalogListCreateAPIView.as_view(), name='catalog-list'),
    path('catalogs/create/', CatalogListCreateAPIView.as_view(), name='catalog-create'),
    path('catalogs/<int:pk>/', CatalogRetrieveUpdateDestroyAPIView.as_view(), name='catalog-detail'),
    
    # Test-related endpoints
    path('tests/', TestListCreateAPIView.as_view(), name='test-list'),
    path('tests/create/', TestListCreateAPIView.as_view(), name='test-create'),
    path('tests/<int:pk>/', TestRetrieveUpdateDestroyAPIView.as_view(), name='test-detail'),
    
    # Question-related endpoints
    path('questions/', QuestionListCreateAPIView.as_view(), name='question-list'),
    path('questions/create/', QuestionListCreateAPIView.as_view(), name='question-create'),
    path('questions/<int:pk>/', QuestionRetrieveUpdateDestroyAPIView.as_view(), name='question-detail'),
    
    # Answer-related endpoints
    path('answers/', AnswerListCreateAPIView.as_view(), name='answer-list'),
    path('answers/create/', AnswerListCreateAPIView.as_view(), name='answer-create'),
    path('answers/<int:pk>/', AnswerRetrieveUpdateDestroyAPIView.as_view(), name='answer-detail'),
    
    # Submit test endpoint
    path('test/<int:test_id>/', test_view, name='test_view'),
    path('submit_test/<int:test_id>/', submit_test, name='submit_test'),
]


urlpatterns += router.urls
