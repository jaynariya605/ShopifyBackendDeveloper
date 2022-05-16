from django.contrib import admin
from Inventory.models import Warehouse, InventorySheet, InventoryDiscription

# Register your models here.
class Warehouseview(admin.ModelAdmin):
    list_display = ("WareHouseId", "Name")


class Inventorysheetview(admin.ModelAdmin):
    list_display = ("id", "get_id", "Date")

    def get_id(self, obj):
        return obj.Assigned_Warehouse.WareHouseId


class Inventorydiscriptionview(admin.ModelAdmin):
    list_display = (
        "Inventory_id",
        "Arrival",
        "Dispatch",
        "Item_Name",
        "Brand",
        "Quantity",
        "Unit_Price",
        "Total_Price",
    )


admin.site.register(Warehouse, Warehouseview)
admin.site.register(InventorySheet, Inventorysheetview)
admin.site.register(InventoryDiscription, Inventorydiscriptionview)
