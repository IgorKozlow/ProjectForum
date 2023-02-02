from django.urls import path, include
from .views import *

urlpatterns = [

    path('', index, name='home'),
    path('register/', userRegistration, name='register'),
    path('login/', userLogin, name='login'),
    path('forum/', forum, name='forum'),
    path('logout/', userLogout, name='logout'),
    path('profile/<int:user_id>', profile, name="profile"),
    path('thread/', thread, name='thread'),
    path('forum/<slug:thread_id>/', show_thread, name='show_thread'),
    path('add_page/', add_page, name='add_page'),
    path('edit_page/<slug:thread_id>', edit_page, name='edit_page'),
    path('delete_page/<slug:thread_id>', delete_page, name='delete_page'),
    path('delete_comment/<int:comment_id>', delete_comment, name='delete_comment'),
]
