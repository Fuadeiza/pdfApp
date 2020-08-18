from django.db import models

# Create your models here.

class pdf_files(models.Model):
    file_name=models.CharField(max_length=256)
    pdf_file=models.FileField(upload_to='media/pdf')

    def __str__(self):
        return self.file_name