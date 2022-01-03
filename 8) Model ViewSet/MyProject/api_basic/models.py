from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    author =models.CharField(max_length=100)
    email = models.EmailField(max_length=100)           # Email field ko lagi EmailField use gareko
    date = models.DateTimeField(auto_now_add=True)      # Date field ko lagi DateTimeField use gareko
 
 
    def __str__(self):                                  # yo Article vanni class ko property or attribute lai use garna cha vani, definition ma self as parameter pass garna parcha
        return self.title                               # yo Article class ko object or instance dekhauda title dekhaucha (i.ed in django providedadmin panel)