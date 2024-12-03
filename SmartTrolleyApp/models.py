from django.db import models

# Create your models here.

class LoginTable(models.Model):
    Username=models.CharField(max_length=30, blank=True, null=True)
    Password=models.CharField(max_length=30, blank=True, null=True)
    Type=models.CharField(max_length=30, blank=True, null=True)
class ProductTable(models.Model):
    Image =models.FileField(blank=True, null=True)
    Name=models.CharField(max_length=30, blank=True, null=True)
    Price=models.FloatField(blank=True, null=True)
    ManufacturingDate=models.DateTimeField(blank=True, null=True)
    ExpiryDate=models.DateTimeField(blank=True, null=True)
    BrandName=models.CharField(max_length=300, blank=True, null=True)
class StaffTable(models.Model):
    Login=models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name=models.CharField(max_length=30, blank=True, null=True)
    Age=models.IntegerField(blank=True, null=True)
    Area=models.CharField(max_length=300, blank=True, null=True)
    PhoneNumber=models.BigIntegerField(blank=True, null=True)
    Qualification=models.CharField(max_length=30, blank=True, null=True)
    Salary=models.FloatField(blank=True, null=True)
    Address=models.CharField(max_length=300, blank=True, null=True)
class UserTable(models.Model):
    Login=models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name=models.CharField(max_length=30, blank=True, null=True)
    Address=models.CharField(max_length=30, blank=True, null=True)
    PhoneNumber=models.BigIntegerField(blank=True, null=True)
class RatingTable(models.Model):
    User=models.ForeignKey(UserTable,on_delete=models.CASCADE)
    Rating=models.FloatField(blank=True, null=True)
    Date=models.DateTimeField(blank=True, null=True)
class FeedbackTable(models.Model):
    User=models.ForeignKey(UserTable,on_delete=models.CASCADE)
    Feedback=models.CharField(max_length=300, blank=True, null=True)
    Date=models.DateTimeField(blank=True, null=True)
class OffersTable(models.Model):
    Product=models.ForeignKey(ProductTable, on_delete=models.CASCADE)
    Offer=models.CharField(max_length=30, blank=True, null=True)
    StartDate=models.DateTimeField(blank=True, null=True)
    EndDate=models.DateTimeField(blank=True, null=True)
class CartTable(models.Model):
    Product=models.IntegerField(blank=True, null=True)
    User=models.ForeignKey(UserTable,on_delete=models.CASCADE)
    Quantity=models.IntegerField(blank=True, null=True) 
    Date=models.DateTimeField(blank=True, null=True)

    











    