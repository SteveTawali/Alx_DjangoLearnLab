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
# Create your views here.
