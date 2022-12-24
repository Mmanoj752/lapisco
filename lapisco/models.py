from django.db import models

# Create your models here.
class brand(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)
class LaptopData(models.Model):
    id=models.IntegerField(primary_key=True)
    brand=models.ForeignKey(brand,on_delete=models.CASCADE)
    # brand=models.CharField(max_length=50)
    RAM=models.CharField(max_length=20)
    SSD=models.CharField(max_length=20)
    HDD=models.CharField(max_length=20)
    Processer=models.CharField(max_length=20)
    Colour=models.CharField(max_length=20)
    Price=models.CharField(max_length=20)
    def __str__(self):
        return str(self.brand)
    
class discription(models.Model):
    p_id=models.ForeignKey(LaptopData,on_delete=models.CASCADE)
    p_discription=models.TextField()
    display_size=models.CharField(max_length=10)
    keyboard_type=models.CharField(max_length=20)
    warrenty=models.CharField(max_length=50)
    def __str__(self):
        return str(self.p_id)
    
    