"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from multi.views import BoardView, CreatePostView, DeleteBoardView, DeletePostView, HomeView, CreateBoardView, UpdateBoardView, DeleteBoardView, UpdatePostView, DeletePostView

urlpatterns = [
    path('admin/', admin.site.urls),

    # you need to import the views.py for usage as in DeletePostView.as_view()
    path('', HomeView.as_view(), name='home' ),
    path('board/<int:pk>', BoardView.as_view(), name='board-panel' ),

    # board related things
    path('board/create', CreateBoardView.as_view(), name='create-board' ),
    path('board/update/<int:pk>', UpdateBoardView.as_view(), name='update-board' ),
    path('board/delete/<int:pk>', DeleteBoardView.as_view(), name='delete-board' ),
    # the <int:pk> makes reference to said pk for the loading page so it load the content related to such
    # posts related things
    path('post/create/<int:pk>', CreatePostView.as_view(), name='create-post' ),
    path('post/update/<int:pk>', UpdatePostView.as_view(), name='update-post' ),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete-post' ),

    path('registration/', include('django.contrib.auth.urls')),
    path('registration/', include('accounts.urls'))

]
