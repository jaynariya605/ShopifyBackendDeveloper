from Inventory.models import InventorySheet, InventoryDiscription


def get_all(model, ID=None):
    if ID:
        return model.objects.filter(Inventory_sheet_id=ID)
    return model.objects.all()


def delete_inventory_sheet(ID):
    try:
        InventorySheet.objects.filter(id=ID).delete()
        InventoryDiscription.objects.filter(Inventory_id=ID).delete()
    except:
        pass


def delete_invetory_item(ID):
    try:
        InventoryDiscription.objects.filter(id=ID).delete()
    except:
        pass
