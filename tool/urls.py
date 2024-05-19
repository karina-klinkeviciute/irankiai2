from django.urls import path

from tool.views import ToolsView, ToolView

urlpatterns = [
    path('', ToolsView.as_view(), name="tools_list"),
    path('<int:pk>', ToolView.as_view(), name="tools_detail"),
]
