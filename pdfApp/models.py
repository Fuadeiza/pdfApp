from django.db import models
from .pdfscript import get_pdf_info, split, rotate, watermarker, rotate_all_page
from django.db.models.signals import post_delete
# Create your models here.

class pdf_files(models.Model):
    file_name=models.CharField(max_length=256, default='file')
    pdf_file=models.FileField(upload_to='media/pdf')

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('create')

    # def save(self, *args, **kwargs):
    #     super(pdf_files, self).save(*args, **kwargs)
    #     filename=self.pdf_file.url
    #     rotate_all_page(r"C:\Users\DELL\Desktop\MyDjangoEnv\pdf_App\pdfpdf" +filename)
    #     return filename

    