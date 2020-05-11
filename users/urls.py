from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^login/',views.User.as_view(),name='login'),
    # url(r'^register/',views.register,name='register'),
]