from django.db import models

# Create your models here.
class Warehouse(models.Model):

  WareHouseId = models.IntegerField(primary_key=True)
  Name = models.CharField(max_length= 215)
  Address = models.TextField(unique=False, blank=False)


class InventorySheet(models.Model):

  Assigned_Warehouse = models.ForeignKey(Warehouse, blank= True, on_delete=models.CASCADE, null=True)
  Date = models.DateTimeField(auto_now_add= True)

class InventoryDiscription(models.Model):

  Inventory_sheet = models.ForeignKey(InventorySheet, blank= False,on_delete=models.CASCADE)
  Arrival = models.DateTimeField(blank= True, null= True)
  Dispatch = models.DateTimeField(blank =True, null= True)
  Item_Name = models.CharField(max_length= 215, blank=False)
  Brand = models.CharField(max_length= 215, blank= False)
  Desciprion = models.CharField(max_length= 215,blank=True, null= True)
  Quantity = models.IntegerField()
  Unit_Price = models.DecimalField(verbose_name='USD$', decimal_places = 2, max_digits = 215)

  @property
  def Total_Price(self):
    return self.Quantity * self.Unit_Price

  @property
  def Inventory_id(self):
    return self.Inventory_sheet.id
  
  
  