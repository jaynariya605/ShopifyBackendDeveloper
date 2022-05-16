from Inventory.models import InventorySheet, InventoryDiscription, Warehouse
from django import forms


def InventoryDiscriptionForm(data, id):
    Inventory_sheet = InventorySheet.objects.get(id=id)

    obj = InventoryDiscription(
        Inventory_sheet=Inventory_sheet,
        Arrival=data["Arrival"] if data["Arrival"] else None,
        Dispatch=data["Dispatch"] if data["Dispatch"] else None,
        Item_Name=data["Item_Name"],
        Brand=data["Brand"],
        Desciprion=data["Description"] if data["Description"] else None,
        Quantity=data["Quantity"],
        Unit_Price=data["Unit_Price"],
    )
    obj.save()
