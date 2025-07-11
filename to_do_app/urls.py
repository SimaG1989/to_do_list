from django.urls import path,include
from django.contrib import admin
from .views import *
from .api import url_patterns
from .token import CustomTokenView
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('tasks/', task_list_view, name='task_list'),
    path('tasks/<int:task_id>/update/', task_update_view, name='task_update'),
    path('toggle/<int:task_id>/', toggle_task_view, name='toggle_task'),
    path('delete/<int:task_id>/', delete_task_view, name='delete_task_view'),
    path('api/', include(url_patterns)),

    path('', RegisterFormView.as_view(), name='register_form'),
    path('api/register/', RegisterAPIView.as_view(), name='api_register'),
    # path('api/token/', CustomTokenView.as_view(), name='token'),
    path('login/', auth_views.LoginView.as_view(template_name='to_do_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tasks/<int:task_id>/update/', task_update_view, name='task_update'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/<int:task_id>/', task_detail_view, name='task-detail'),
]
