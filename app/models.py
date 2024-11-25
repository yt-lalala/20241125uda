from django.db import models

class UploadImage(models.Model):
    class Meta:
        app_label = 'app'
    
    image = models.ImageField(upload_to='img')
   

class UploadImageUra(models.Model):
    class Meta:
        app_label = 'app'
    
    image = models.ImageField(upload_to='img_ura')
