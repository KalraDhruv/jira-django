from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.home, name='jira-home'),
        path('bug/<int:pk>/', views.BugDetailView.as_view(), name='bug-detail'),
        path('bug/<int:pk>/update/', views.update_bug, name='update-bug'),
]
