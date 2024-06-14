from django.db import models

class User(models.Model):

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    USER_CHOICE=[
        (1,'Librarian'),
        (2,'Patron')]
    usertype = models.CharField(max_length=15,choices=USER_CHOICE)
    image = models.ImageField(upload_to='bookhub/', null=True, blank=True)

    def __str__(self):
        return self.firstname,self.lastname

class Book(models.Model):

    BookName = models.CharField(max_length=300)
    AuthorName = models.CharField(max_length=100)
    BookDescription= models.CharField(max_length=5000)
    Price = models.IntegerField()
    image = models.ImageField(upload_to='bookhub/', null=True, blank=True)

    def __str__(self):
        return self.BookName,self.AuthorName