# from pyexpat import model
# from turtle import textinput
from distutils.command.upload import upload
from django.db import models
from django.urls import reverse

# Create your models here.
class Board(models.Model):
    class BoardCategory(models.TextChoices):
        Opsfw= "SFW" , "sfw"
        Opnsfw= "NSFW" , "nsfw"


    tag = models.CharField(
            max_length=12,
            choices=BoardCategory.choices,
            default=BoardCategory.Opsfw
        )

    image = models.ImageField( null=True, blank=True, upload_to="images/") # this field is from Pillow 

    name = models.CharField(default="Pick a name", max_length=50)
    # title = name

    description = models.TextField(default="Pick a description")

    newadd = models.TextField(default="Hola que pasa")

    adminPost= models.TextField(default="Hola soy el admin")

    def __str__(self): # this function defines a name as identifier for the objects, if you don't do this they will be displayed as object(1) and such
        return self.name

    def get_absolute_url(self): # mandatory, it is set to redirect you to another page after interacting with a form
        return reverse('home')

class Post(models.Model):
    
    board =  models.ForeignKey(Board, related_name='posts', on_delete=models.CASCADE) # sets foreign key # parameter
    # on_delete=models.CASCADE deletes every post related to said board on board deletion.

    description = models.TextField(default="post text")
    date = models.DateTimeField(auto_now_add=True) # displays creation time

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('home')