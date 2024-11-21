from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required

@permission_required('app_name.can_edit', raise_exception=True)
def edit_view(request, id):
    # Edit logic
    pass
