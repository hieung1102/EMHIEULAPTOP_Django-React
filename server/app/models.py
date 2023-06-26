from django.db import models

# Create your models here.
class SANPHAM(models.Model):
    TenSP = models.CharField(max_length=255)
    GiaSP = models.IntegerField(10)
    MoTa = models.CharField(max_length=255)
    Image = models.ImageField(upload_to = r'D:\EMHIEULAPTOP_Django-React\server\app\statics\images\macbook.jpg', default = r'D:\EMHIEULAPTOP_Django-React\server\app\statics\images\macbook.jpg')

    def __str__(self) -> str:
        return "{} {}".format(self.TenSP, self.MoTa)


