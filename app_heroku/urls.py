from django.urls import path
from . import views as logic


urlpatterns = [
    # path('', my_home, ""),

    path(route='get_currency/', view=logic.get_currency, name="get_currency"),
]

