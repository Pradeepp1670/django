from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("<int:id>/",views.v1, name="view 1"),
    path("create/",views.create, name="create"),
    path("view/",views.view, name="view")

]