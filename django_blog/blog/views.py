from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserUpdateForm

@login_required
def profile_view(request):
    if request.method == 'POST':
        # Create a form instance with POST data and the current user as the instance
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            # Save the updated user details
            form.save()
            # Redirect to the profile page after successful update
            return redirect('profile')
    else:
        # For GET requests, pre-populate the form with the current user's details
        form = CustomUserUpdateForm(instance=request.user)

    return render(request, 'registration/profile.html', {'form': form})


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

# ListView to display all blog posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# DetailView to show a single blog post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# CreateView for creating new blog posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user  # Automatically set the current user as the author
        return super().form_valid(form)

# UpdateView for editing existing posts
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        # Ensure that only the post author can edit
        if self.request.user != form.instance.author:
            raise PermissionError("You do not have permission to edit this post.")
        return super().form_valid(form)

# DeleteView for deleting posts
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        # Ensure that only the post author can delete it
        return Post.objects.filter(author=self.request.user)
# Create your views here.
