from django.urls import path
from . import views

urlpatterns = [
    path("home",views.Home,name="home"),
    path("reg",views.get_reg,name="reg"),
    path("log",views.get_login,name="log"),
    # path("feedback",views.feed_back,name="feedback"),
    path("logout",views.log_out,name="logout"),
    path("feedback",views.get_feed,name="feedback"),
    path("feed2",views.feed_back2,name="feed2"),

    ]
