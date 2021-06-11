from collections import namedtuple # insert all these header files in urls.py
from . import views
from django.urls import path

urlpatterns=[
    path('',views.home,name="home"),
    path('uhome/',views.uhome,name="uhome"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('profile/',views.profile,name="profile"),
    path('addprofile/',views.addprofile,name="addprofile"),
    path('signin/',views.signin,name="signin"),
    path('updated/',views.updateprofile,name="updateprofile"),
    path('upload/',views.updated,name="updated"),
    path('viewprofile/',views.viewprofile,name="viewprofile"),
    path('addrecord/',views.addrecord,name="addrecord"),
    path('rec/',views.rec,name="rec"),
    path('viewrecord/',views.viewrecord,name="viewrecord"),
    path('addprescription/',views.addprescription,name="addprescription"),
    path('pres/',views.pres,name="pres"),
    path('viewpres/',views.viewpres,name="viewpres"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('viewemergency/',views.viewemergency,name="viewemergency"),
    path('uviewemergency/',views.uviewemergency,name="uviewemergency"),
    path('addemer/',views.addemer,name="addemer"),
    path('addemergency/',views.addemergency,name="addemergency"),
    path('emerdelete/<int:id>',views.emerdelete,name="emerdelete"),
    path('emerupdate/<int:id>',views.emerupdate,name="emerupdate"),
    path('updateemergency/',views.updateemergency,name="updateemergency"),
    path('recordelete/<int:id>',views.recordelete,name="recordelete"),
    path('updaterecord/',views.updaterecord,name="updaterecord"),
    path('recordupdate/<int:id>',views.recordupdate,name="recordupdate"),
    path('presdelete/<int:id>',views.presdelete,name="presdelete"),
    path('updateprescription/',views.updateprescription,name="updateprescription"),
    path('presupdate/<int:id>',views.presupdate,name="presupdate"),
]


