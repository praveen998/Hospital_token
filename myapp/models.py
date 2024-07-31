from django.db import models

# Create your models here.

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    dob=models.DateField()

    class Meta:
        db_table = 'author'
    
    def __str__(self):
        return self.name
    
    