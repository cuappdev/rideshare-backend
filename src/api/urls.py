from django.urls import include
from django.urls import path
from django.urls import re_path
from person.views import AuthenticateView
from person.views import DeveloperView
from person.views import MeView
from ride.views import RidesView
from ride.views import RideView
from ride.views import SearchView
from prompts.views import PromptsView
from prompts.views import PromptView


urlpatterns = [
    path("authenticate/", AuthenticateView.as_view(), name="authenticate"),
    path("dev/", DeveloperView.as_view(), name="dev"),
    path("me/", MeView.as_view(), name="me"),
    path("rides/<int:id>/", RideView.as_view(), name="ride"),
    path("rides/", RidesView.as_view(), name="rides"),
    path("search/", SearchView.as_view(), name="search"),
    re_path(r"^requests/", include("request.urls")),
    path("prompts/", PromptsView.as_view(), name="prompts"),
    path("prompts/<int:id>/", PromptView.as_view(), name="prompt")
]
