from django.shortcuts import render
from django.urls import reverse_lazy # import for the deleteview thingy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # imports for crud

from multi.models import Board,Post
# Create your views here.

class HomeView(ListView): # listview makes a list of the boards
    model = Board # makes reference to which model you wanna use.
    template_name = 'home.html' # references the template
    ordering = ['-id'] # orders from id in reverse (latest added)

class BoardView(DetailView): # detailview shows the details of each board and its contents, ofc you need to reference in html temp
    model = Board
    template_name = 'board.html'

# CREATE

class CreatePostView(CreateView):
    model = Post
    template_name = 'cr-post.html'
    fields = '__all__' #selects every field from the model to use it in a form, you can pick them individualy too, 
    # the fields parameter is mandatory for create and update because they use forms duh!.

class CreateBoardView(CreateView):
    model = Board
    template_name = 'cr-board.html'
    fields = '__all__'

# UPDATE

class UpdateBoardView(UpdateView):
    model = Board
    template_name = 'up-board.html'
    fields = '__all__' # same as in create

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'up-post.html'
    fields = '__all__'
    
# DELETE

class DeleteBoardView(DeleteView):
    model = Board
    template_name = 'rm-board.html' 
    success_url = reverse_lazy('home') #redirects to home on success the "success_url" variable is obligatory. because deleteview cannot use the model reverse().

class DeletePostView(DeleteView):
    model = Post
    template_name = 'rm-post.html' 
    success_url = reverse_lazy('home') #redirects to home on success the "success_url" variable is obligatory. because deleteview cannot use the model reverse().

# all of this classes except the delete board, use a function specified in their model, to redirect you to other page after interacting with a form
# the function is:

    # def get_absolute_url(self):
    #     return reverse('home')

# which is mandatory for those clases