from django.shortcuts import render
from django.views.generic import ListView, DetailView

from user.models import User


# Create your views here.
# class UserView(DetailView):
#     template_name = "user/user_detail.html"
#     model = User

def current_user_profile(request):

    return render(request, template_name="user/user_detail.html")
