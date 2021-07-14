from django.db import models
# Create your models here.



class brands(models.Model):
    brand_id = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100,blank=True)
    link=models.URLField(blank=True)   
    class Meta:
        db_table='brands'
    def __str__(self):
        return self.name


class gender(models.Model):
    gender_id= models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50,blank=True)
    class Meta:
        db_table='gender'
    def __str__(self):
        return self.name

class product_type(models.Model):
    product_type_id= models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=150,blank=True)
    
    class Meta:
        db_table='product_type'
    def __str__(self):
        return self.name
    


class product(models.Model):
    product_id= models.BigAutoField(primary_key=True)
    brand=models.ForeignKey(brands, on_delete=models.CASCADE)
    gender=models.ForeignKey(gender, on_delete=models.CASCADE)
    category=models.ForeignKey(product_type, on_delete=models.CASCADE)

    brand_name=models.CharField(max_length=50,blank=True)
    gender_category=models.CharField(max_length=50,blank=True)
    category_name=models.CharField(max_length=50,blank=True)
    title=models.CharField(max_length=50,blank=True)
    price=models.CharField(max_length=50,blank=True)
    sale_price=models.CharField(max_length=50,blank=True)
    product_link=models.URLField(blank=True)   
    image_link=models.URLField(blank=True)
    image_link2=models.URLField(blank=True)

    rating=models.CharField(max_length=50,blank=True)
    status=models.CharField(max_length=50,blank=True)
    datee= models.DateField()
    detail=models.CharField(max_length=50,null=True)

    class Meta:
        db_table='product'
    def __str__(self):
        return self.brand_name
    




