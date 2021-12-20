from django.urls import path
from .views import Index, Problem, Rank, Login, logout

urlpatterns = [
    path('', Index.as_view(),),
    path('problems', Problem.as_view(),),
    path('rank', Rank.as_view(),),
    path('login', Login.as_view(),),
    path('logout', logout,),
]
