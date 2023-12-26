from django.db import models


# Create your models here.
class hodim(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()
    bio = models.TextField()
    image = models.ImageField(upload_to='static/')

    def __str__(self):
        return self.name


class Aboutpage(models.Model):
    name = models.CharField(max_length=200) #pereparat nomi
    about = models.CharField(max_length=200) #fikir mulohaza
    info = models.CharField(max_length=200) #ma'lumotlar
    contact = models.CharField(max_length=200) #aloqa


class fikir(models.Model):
    title = models.CharField(max_length=200) #sarlavha
    link = models.CharField(max_length=200) #youtube link


class info(models.Model):
    bio = models.TextField


class contact(models.Model):
    tel = models.CharField(max_length=200) #telefon raqam
    insta = models.CharField(max_length=200) #insta manzil
    tg = models.CharField(max_length=200) #tg manzil
    email = models.CharField(max_length=200) #email manzil
