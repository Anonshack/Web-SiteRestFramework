from django.db import models


class mijoz(models.Model):
    name = models.CharField(max_length=200)
    lastname =  models.CharField(max_length=200)
    age = models.IntegerField()
    bio = models.TextField()
    image = models.ImageField(upload_to='static/')

    def __str__(self):
        return self.name


class aboutpage(models.Model):
    companiya = models.CharField(max_length=200) #kompnaiya haqida
    social = models.CharField(max_length=200) #ijtimoiytarmoq
    otzv = models.CharField(max_length=200) #otzvlar 
    info = models.TextField() #kompaniya haqida ma'lumot


class Director(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    date = models.DateField()
    position = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    img = models.ImageField('static/')


class Asoschi(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    date = models.DateField()
    position = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    img = models.ImageField('static/')