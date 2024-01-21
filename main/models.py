from typing import Any
from django.db import models


class Logo(models.Model):
    img = models.ImageField('Logo', upload_to='media' )

    def __str__(self) -> str:
        return f"Logo"
    
    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logos'


class Design(models.Model):
    image = models.ImageField('Design Image', upload_to='media')
    title = models.CharField('Title', max_length= 50)
    text = models.TextField('About Design')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Design'
        verbose_name_plural = 'Design'


class AboutTeam(models.Model):
    image = models.ImageField('Image', upload_to='meia')
    title = models.CharField('Title', max_length= 50)
    text1 = models.TextField('First Text')
    text2 = models.TextField('Second Text')
    text3 = models.TextField('Third Text')


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'About Team'
        verbose_name_plural = 'About Team'


class GalleryOne(models.Model):
    image1 = models.ImageField('First Image', upload_to='media', null= True)
    image2 = models.ImageField('Second Image', upload_to='media', null= True)
    image3 = models.ImageField('Third Image', upload_to='media', null= True)
    image4 = models.ImageField('Fourth Image', upload_to='media', null= True)
    image5 = models.ImageField('Fifth Image', upload_to='media', null= True)

    def __str__(self) -> str:
        return f"Gallery One"
    

    class Meta:
        verbose_name = "Gallery One"
        verbose_name_plural = "Gallery One"


class SecondGallery(models.Model):
    image1 = models.ImageField('First Image', upload_to='media', null= True)
    image2 = models.ImageField('Second Image', upload_to='media', null= True)
    image3 = models.ImageField('Third Image', upload_to='media', null= True)
   

    def __str__(self) -> str:
        return f"Second Gallery"
    

    class Meta:
        verbose_name = "Second Gallery"
        verbose_name_plural = "Second Gallery"


class ThirdGallery(models.Model):
    image1 = models.ImageField('First Image', upload_to='media', null= True)
    image2 = models.ImageField('Second Image', upload_to='media', null= True)
    image3 = models.ImageField('Third Image', upload_to='media', null= True)
    image4 = models.ImageField('Fourth Image', upload_to='media', null= True)
   

    def __str__(self) -> str:
        return f"Third Gallery"
    

    class Meta:
        verbose_name = "Third Gallery"
        verbose_name_plural = "Third Gallery"


class ContactUs(models.Model):
    name = models.CharField("Name", max_length=50)
    email = models.EmailField("E-mail Address", max_length=75)
    message = models.TextField("Message")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

class ContactText(models.Model):
    text = models.TextField('Text')
    address = models.CharField('Address', max_length= 200)

    def __str__(self) -> str:
        return f"Address"
    

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Address'


    