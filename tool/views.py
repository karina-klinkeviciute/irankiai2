from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from tool.models import Tool


# Create your views here.
class ToolsView(ListView):
    template_name = "tool/tools_list.html"
    model = Tool


class ToolView(DetailView):
    template_name = "tool/tools_detail.html"
    model = Tool
