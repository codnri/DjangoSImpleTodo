from django.db import models

# Create your models here.

# class Blog(models.Model):
class Todo(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()    
    is_completed = models.BooleanField()
    
    def __str__(self):#admin画面で、インスタンス表示の際に、titleが表示される
        return self.subject
    
    def show_completed_box(self):
        return u"\u2611" if self.is_completed else u"\u2610" #u2610は☒なし
        
    def show_completed_on_off(self):
        return 'checked' if self.is_completed else ''