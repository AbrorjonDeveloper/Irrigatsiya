from django.shortcuts import render
from .models import Profile
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'profile.html', {})


