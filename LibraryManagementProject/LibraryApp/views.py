from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from LibraryApp.models import Student, Course, Book, Issue_Book


# Create your views here.

def log_fun(request):
    return render(request,'login.html',{'data':''})

def readlog_fun(request):
    user_name=request.POST['txtname']
    user_password=request.POST['txtpwd']
    u = authenticate(username=user_name,password=user_password)
    if u is not None:
        if u.is_superuser:
            return render(request,'AdminHome.html')
        else:
            return render(request,'login.html',{'data':'Invalid Username or Password '})
    else:
        s = Student.objects.filter(Q(Student_Name=user_name) | Q(Student_Password=user_password)).exists()
        if s:
            return render(request,'StudentHome.html')
        else:
            return render(request, 'login.html', {'data': 'Invalid Username or Password '})

def studentReg_fun(request):
    c = Course.objects.all()
    return render(request,'Studentregistration.html',{'data':'','course':c})

def adminReg_fun(request):
    return render(request,'Adminregistration.html',{'data':""})


def readstdreg_fun(request):
    user = Student.objects.filter(Q(Student_Name=request.POST['txtname']) | Q(Student_Password=request.POST['txtpwd'])).exists()
    if user:
        return render(request,'Studentregistration.html',{'data':'UserName And Password Already Exist'})
    else:
        s = Student()
        s.Student_Name=request.POST['txtname']
        s.Student_PhoneNo=request.POST['txtmobile']
        s.Student_Sem=request.POST['txtsem']
        s.Student_Password=request.POST['txtpwd']
        s.Course=Course.objects.get(Course_Name=request.POST['ddlcourse'])
        s.save()
        return redirect('log')


def readadminreg_fun(request):
    u = authenticate(username=request.POST['txtname'], password=request.POST['txtpwd'])
    if u is not None:
        if u.is_superuser:
            return render(request, 'Adminregistration.html',{'data':'Username and Password Already Exist'})
        else:
            u = User.objects.create_superuser(username=request.POST['txtname'], password=request.POST['txtpwd'])
            u.save()
            return redirect('log')
    else:
        u = User.objects.create_superuser(username=request.POST['txtname'], password=request.POST['txtpwd'])
        u.save()
        return redirect('log')


def addbook_fun(request):
    c = Course.objects.all()
    return render(request,'addbook.html',{'courses':c,'msg':''})


def readaddbook_fun(request):
    b = Book()
    b.Book_Name = request.POST['txtname']
    b.Author_Name = request.POST['txtAname']
    b.Course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
    b.save()
    c = Course.objects.all()
    return render(request,'addbook.html',{'courses':c,'msg':'One Book Added Successfully'})


def displaybooks_fun(request):
    b = Book.objects.all()


    return render(request,'display.html',{'books':b})

def update_fun(request,bid):
    b = Book.objects.get(id=bid)
    c = Course.objects.all()
    if request.method=='POST':
        b.Book_Name = request.POST['txtname']
        b.Author_Name = request.POST['txtAname']
        b.Course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        b.save()
        c = Course.objects.all()
        return render(request, 'update.html', {'book': b, 'courses': c, 'msg': 'One Book Updated'})

    return render(request,'update.html',{'book':b,'courses':c, 'msg':''})


def delete_fun(request,bid):
    b = Book.objects.get(id=bid)
    b.delete()
    return redirect('dis')


def assignbook(request):
    c = Course.objects.all()
    return render(request,'AssignBook.html',{'Courses':c})


def readsemcourse(request):
    stdsem = request.POST['txtsem']
    course = request.POST['ddlcourse']
    students = Student.objects.filter(Q(Student_Sem=stdsem) | Q(Course=Course.objects.get(Course_Name=course)))
    print(students)
    books = Book.objects.filter(Course=Course.objects.get(Course_Name=course))
    print(books)
    return render(request,'AssignBook.html',{'students':students,'books':books})


def readstdbook(request):
    ib = Issue_Book()
    ib.Student_Name = Student.objects.get(Student_Name=request.POST['ddlstdname'])
    ib.Book_Name = Book.objects.get(Book_Name=request.POST['ddlbookname'])
    ib.Start_Date = request.POST['startdate']
    ib.End_Date = request.POST['enddate']
    ib.save()
    c = Course.objects.all()
    return render(request,'AssignBook.html',{'Courses':c,'msg':'Book Assigned Successfully'})


def disIssuedBk(request):
    Ibooks = Issue_Book.objects.all()
    return render(request,'DisplayIssuedBooks.html',{'Ibooks':Ibooks})


def updateIbook(request,id):
    ib=Issue_Book.objects.get(id=id)
    bk = Book.objects.all()
    # s = Student.objects.get(id=ib.Student_Name_id)
    # c = Course.objects.get(Q(Course_Name=s.Course) &
    if request.method == 'POST':
        ib.Student_Name = Student.objects.get(Student_Name=request.POST['txtstdname'])
        ib.Book_Name= Book.objects.get(Book_Name=request.POST['ddlbkname'])
        ib.Start_Date= request.POST['startdate']
        ib.End_Date= request.POST['enddate']
        ib.save()
        return redirect('IssuedBooks')

    return render(request,'UpdateIssuedBook.html',{'ib':ib,'books':bk})


def delIbook(request,id):
    ib = Issue_Book.objects.get(id=id)
    ib.delete()
    return redirect('IssuedBooks')
