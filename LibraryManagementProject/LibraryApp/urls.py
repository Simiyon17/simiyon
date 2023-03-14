from django.urls import path

from LibraryApp import views


urlpatterns=[
    path('',views.log_fun,name='log'),
    path('readlog',views.readlog_fun),
    path('studentreg',views.studentReg_fun,name="sreg"),
    path('adminreg',views.adminReg_fun,name='areg'),
    path('readstdreg',views.readstdreg_fun),
    path('readadminreg',views.readadminreg_fun),
    path('addbook',views.addbook_fun,name='addbook'),
    path('readaddbook',views.readaddbook_fun),
    path('display',views.displaybooks_fun,name='dis'),
    path('update/<int:bid>',views.update_fun,name='up'),
    path('delete/<int:bid>',views.delete_fun,name='del'),
    path('assignbook',views.assignbook,name='assign'),
    path('readsemcourse',views.readsemcourse),
    path('readstdbook',views.readstdbook),
    path('disIssuedBk',views.disIssuedBk,name='IssuedBooks'),
    path('updateIbook/<int:id>',views.updateIbook,name='upib'),
    path('delIbook/<int:id>',views.delIbook,name='ibdel')


]