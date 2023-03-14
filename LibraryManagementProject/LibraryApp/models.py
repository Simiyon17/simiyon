from django.db import models

# Create your models here.
class Course(models.Model):
    Course_Name=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.Course_Name}"
class Book(models.Model):
    Book_Name=models.CharField(max_length=50)
    Author_Name=models.CharField(max_length=50)
    Course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Book_Name}"
class Student(models.Model):
    Student_Name=models.CharField(max_length=50)
    Student_Password=models.CharField(max_length=50)
    Student_PhoneNo = models.BigIntegerField()
    Student_Sem = models.CharField(max_length=50)
    Course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Student_Name}"
class Issue_Book(models.Model):
    Student_Name=models.ForeignKey(Student,on_delete=models.CASCADE)
    Book_Name=models.ForeignKey(Book,on_delete=models.CASCADE)
    Start_Date=models.DateField()
    End_Date=models.DateField()