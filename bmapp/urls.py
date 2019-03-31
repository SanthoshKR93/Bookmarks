from django.conf.urls import url
from bmapp.views import Get_Link_List,LoginView,LogoutView,UserCreate

urlpatterns = [
   url(r'^linksapi/$', Get_Link_List.as_view()),
   url(r'^login/$', LoginView.as_view()),
   url(r'^logout/$', LogoutView.as_view()),
   url(r'^register/$',UserCreate.as_view()),

]

