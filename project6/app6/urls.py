from django.urls import path
from .import views
#from .views import frontpage,home,about,ulogin,register,wardenlogin,studentpage,wardenpage,notification

urlpatterns = [

     
    path('',views.frontpage),
    path('home',views.home),
    path('about',views.about),
    path('ulogin',views.ulogin),
    path('register',views.register),
    path('wardenlogin',views.wardenlogin),
    path('studentpage',views.studentpage),
    path('wardenpage',views.wardenpage),
    path('notifications',views.notification),
    path('wardenreg',views.wardenreg),
    path('wardenlogin',views.wardenlogin),
    path('sgatepass',views.sgatepass),
    path('sgprequest',views.sgprequest),
    path('sgpdisplay',views.sgpdisplay),
    path('sgpin',views.sgpin),
    path('viewgatepass',views.viewsgatepass),
    path('newgatereq',views.newgatereq),
    path('view<str:wk>',views.view,name="view"),
    path('accepted',views.accepted),
    path('rejected',views.rejected),
    path('gatepassin<str:gi>',views.gatepassin,name="gatepassin"),

    

]