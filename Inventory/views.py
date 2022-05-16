from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from Inventory.utils import get_all, delete_inventory_sheet, delete_invetory_item
from Inventory.models import Warehouse, InventorySheet, InventoryDiscription
from Inventory.forms import InventoryDiscriptionForm

# Create your views here.


def Home_view(request):
    context = {}
    if request.POST and "ID" in request.POST:
        ID = request.POST.get("ID")
        return redirect("edit", pk=ID)

    if request.POST and "DID" in request.POST:
        ID = request.POST.get("DID")
        delete_inventory_sheet(ID)
        context["Inventories"] = get_all(InventorySheet)
        return render(request, "home.html", context)
    
    if request.POST and "CID" in request.POST:
        return redirect("create")

    else:
        context["Inventories"] = get_all(InventorySheet)
        return render(request, "home.html", context)


def Edit_view(request, pk):

    if request.POST and "AID" in request.POST:
        return redirect("item", pk=pk)
    
    if request.POST and "DID" in request.POST:
        delete_invetory_item(request.POST.get("DID"))
        return redirect("edit", pk=pk)

    if request.POST and "Save" in request.POST:
        obj = InventorySheet.objects.get(id=pk)
        if request.POST.get("WID") == "None":
            obj.Assigned_Warehouse = None

        else:
            obj.Assigned_Warehouse = Warehouse.objects.get(
                WareHouseId=request.POST.get("WID")
            )
        obj.save()
        return redirect("edit", pk=pk)
    context = {}
    context["ItemList"] = get_all(InventoryDiscription, ID=pk)
    context["WareHouses"] = get_all(Warehouse)
    obj = InventorySheet.objects.get(id=pk)

    context["current_W"] = obj.Assigned_Warehouse

    context["id"] = pk
    return render(request, "Inventory.html", context)


def Create_view(request):
    if request.POST:
        date = request.POST.get("date")
        WID = request.POST.get("WID")
        if WID != "None":
            W = Warehouse.objects.get(WareHouseId=WID)
            obj = InventorySheet(Date=date, Assigned_Warehouse=W)
        else:
            obj = InventorySheet(Date=date)
        obj.save()

        return redirect("edit", pk=obj.id)
    context = {}

    context["Warehouse"] = get_all(Warehouse)
    return render(request, "create.html", context)


def item_view(request, pk):
    if request.POST:
        InventoryDiscriptionForm(request.POST.dict(), pk)

        return redirect("edit", pk=pk)

    context = {}
    context["id"] = pk

    return render(request, "item.html", context)


def Warehouse_view(request):
    if request.POST:
        data = request.POST.dict()
        obj = Warehouse(
            WareHouseId=data["WareHouseId"], Name=data["Name"], Address=data["Address"]
        )
        obj.save()
        return redirect("home")
    return render(request, "ware.html")
