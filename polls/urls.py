from django.urls import include, path


from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('crudVoucher/', views.crudVoucher),
    path('base2/', views.base2), 
    path('<int:pk>',views.crudVoucher,name="voucher"),
    path('create_voucher/', views.createVoucher, name="create_voucher"),
    path('update_voucher/<str:pk>/', views.updateVoucher, name="update_voucher"),
    path('delete_voucher/<str:pk>/', views.deleteVoucher, name="delete_voucher"),
    #path('register/', views.registerPage, name="register"),
	#path('login/', views.loginPage, name="login"),  
	#path('logout/', views.logoutUser, name="logout"),
   # path('pbDashbord.html', views.pbDashbord),   
]


