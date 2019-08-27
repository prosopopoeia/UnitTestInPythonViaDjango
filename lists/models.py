from django.db import models



class List(models.Model):
    pass
    # list = models.TextField(default='')
     
    # def save(self):
        # models.save()
        
class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)