from django.urls import path, include
from django.contrib.auth import views

from . import views as main_views

app_name = 'hrefs'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', main_views.index, name='list'),
    path('dash/', main_views.dashboard, name='dashboard'),

    # ex: /hrefs/5/view/
    path('add/', main_views.add, name='href-add'),

    # ex: /hrefs/5/view/
    path('<int:href_id>/', main_views.view, name='href-view'),

    # ex: /hrefs/6/edit/
    path('<int:href_id>/edit/', main_views.edit, name='href-edit'),

    # ex: /hrefs/6/edit/
    path('<int:href_id>/delete/', main_views.delete, name='href-delete'),

    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    #path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Обработчики восстановления пароля.
    #path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'), 
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), 
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('register/', main_views.register, name='register'),
    path('edit/', main_views.edit, name='edit'),
]