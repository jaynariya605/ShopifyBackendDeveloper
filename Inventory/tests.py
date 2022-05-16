from django.test import TestCase, Client
from datetime import datetime

# Create your tests here.
from Inventory.models import Warehouse, InventorySheet, InventoryDiscription
from Inventory.views import Home_view


class WarehouseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Warehouse.objects.create(WareHouseId=1, Name="Test", Address="TestAddress")
        InventorySheet.objects.create(
            Assigned_Warehouse=Warehouse.objects.get(WareHouseId=1)
        )

    def test_name_warehouse(self):
        obj = Warehouse.objects.get(WareHouseId=1)
        field_label = obj._meta.get_field("Name").verbose_name
        self.assertEqual(field_label, "Name")

    def test_Address_warehouse(self):
        obj = Warehouse.objects.get(WareHouseId=1)
        field_label = obj._meta.get_field("Address").verbose_name
        self.assertEqual(field_label, "Address")

    def test_Assigned_warehouse_label(self):
        obj = InventorySheet.objects.get(id=1)
        field_label = obj._meta.get_field("Assigned_Warehouse").verbose_name
        self.assertEqual(field_label, "Assigned Warehouse")

    def test_Assigned_warehouse_inventorysheet(self):
        obj1 = InventorySheet.objects.get(id=1)
        obj2 = Warehouse.objects.get(WareHouseId=1)
        self.assertEqual(obj1.Assigned_Warehouse, obj2)


class InventoryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        InventorySheet.objects.create()

    def test_Assigned_warehouse(self):
        obj = InventorySheet.objects.get(id=1)
        self.assertEqual(obj.Assigned_Warehouse, None)

    def test_Date_creation(self):
        obj = InventorySheet.objects.get(id=1)
        obj.Date = datetime.now()
        obj.save()
        self.assertLessEqual(obj.Date, datetime.now())

    def test_date_lable_inventorysheet(self):
        obj = InventorySheet.objects.get(id=1)
        field_label = obj._meta.get_field("Date").verbose_name
        self.assertEqual(field_label, "Date")


class InvenoryDescriptionTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        InventoryDiscription.objects.create(
            Inventory_sheet=InventorySheet.objects.create(),
            Item_Name="Test",
            Brand="DjangoTest",
            Desciprion="Testcase writing",
            Quantity=5,
            Unit_Price=200,
        )

    def test_Inventorysheet_label_InventoryDiscription(self):
        obj = InventoryDiscription.objects.get(id=1)
        field_label = obj._meta.get_field("Inventory_sheet").verbose_name
        self.assertEqual(field_label, "Inventory sheet")

    def test_arrival_date_lable_InventoryDiscription(self):
        obj = InventoryDiscription.objects.get(id=1)
        field_label = obj._meta.get_field("Arrival").verbose_name
        self.assertEqual(field_label, "Arrival")

    def test_dispatch_date_lable_InventoryDiscription(self):
        obj = InventoryDiscription.objects.get(id=1)
        field_label = obj._meta.get_field("Dispatch").verbose_name
        self.assertEqual(field_label, "Dispatch")

    def test_item_name_lable_InventoryDiscription(self):
        obj = InventoryDiscription.objects.get(id=1)
        field_label = obj._meta.get_field("Item_Name").verbose_name
        self.assertEqual(field_label, "Item Name")

    def test_brand_lable_InventoryDiscription(self):
        obj = InventoryDiscription.objects.get(id=1)
        field_label = obj._meta.get_field("Brand").verbose_name
        self.assertEqual(field_label, "Brand")

    def test_description_lable_InventoryDiscription(self):
        obj = InventoryDiscription.objects.get(id=1)
        field_label = obj._meta.get_field("Desciprion").verbose_name
        self.assertEqual(field_label, "Desciprion")

    def test_quantity_lable_InventoryDiscription(self):
        obj = InventoryDiscription.objects.get(id=1)
        field_label = obj._meta.get_field("Quantity").verbose_name
        self.assertEqual(field_label, "Quantity")

    def test_unit_price_lable_InventoryDiscription(self):
        obj = InventoryDiscription.objects.get(id=1)
        field_label = obj._meta.get_field("Unit_Price").verbose_name
        self.assertEqual(field_label, "USD$")

    def test_total_price_InventoryDiscription(self):
        obj = InventoryDiscription.objects.get(id=1)
        Total = obj.Total_Price
        self.assertEqual(Total, 1000)


class HomeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Warehouse.objects.create(WareHouseId=1, Name="Test", Address="TestAddress")
        InventorySheet.objects.create(
            Assigned_Warehouse=Warehouse.objects.get(WareHouseId=1)
        )
        InventoryDiscription.objects.create(
            Inventory_sheet=InventorySheet.objects.get(id=1),
            Item_Name="Test",
            Brand="DjangoTest",
            Desciprion="Testcase writing",
            Quantity=5,
            Unit_Price=200,
        )

    def test_home_get_view(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        I = response.context["Inventories"][0]
        self.assertEqual(I.id, (InventorySheet.objects.get(id=1)).id)
        self.assertTemplateUsed(response, "home.html")

    def test_home_post_view(self):

        response = self.client.post("", {"ID": 1}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.redirect_chain, "edit/")

        response = self.client.post("", {"DID": 1}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

        response = self.client.post("", {"CID": 1}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.redirect_chain, "create/")


class Editviewtest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Warehouse.objects.create(WareHouseId=1, Name="Test", Address="TestAddress")
        InventorySheet.objects.create(
            Assigned_Warehouse=Warehouse.objects.get(WareHouseId=1)
        )
        InventoryDiscription.objects.create(
            Inventory_sheet=InventorySheet.objects.get(id=1),
            Item_Name="Test",
            Brand="DjangoTest",
            Desciprion="Testcase writing",
            Quantity=5,
            Unit_Price=200,
        )

    def test_edit_get_view(self):

        response = self.client.get("/edit/1/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Inventory.html")

    def test_edit_post_view(self):

        response = self.client.post("/edit/1/", {"AID": 1}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.redirect_chain, "item/")

        response = self.client.post("/edit/1/", {"Save": 1, "WID": 1}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.redirect_chain, "edit/")

        response = self.client.post("/edit/1/", {"DID": 1}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.redirect_chain, "edit/")


class ItemviewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Warehouse.objects.create(WareHouseId=1, Name="Test", Address="TestAddress")
        InventorySheet.objects.create(
            Assigned_Warehouse=Warehouse.objects.get(WareHouseId=1)
        )
        InventoryDiscription.objects.create(
            Inventory_sheet=InventorySheet.objects.get(id=1),
            Item_Name="Test",
            Brand="DjangoTest",
            Desciprion="Testcase writing",
            Quantity=5,
            Unit_Price=200,
        )

    def test_item_get_view(self):
        response = self.client.get("/item/1/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "item.html")

    def test_item_post_view(self):
        response = self.client.post(
            "/item/1/",
            {
                "Arrival": "",
                "Dispatch": "",
                "Item_Name": "Phone",
                "Brand": "Apple",
                "Description": "siudhskdf",
                "Quantity": 2,
                "Unit_Price": 400,
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.redirect_chain, "edit/")


class WarehouseViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Warehouse.objects.create(WareHouseId=1, Name="Test", Address="TestAddress")
        InventorySheet.objects.create(
            Assigned_Warehouse=Warehouse.objects.get(WareHouseId=1)
        )
        InventoryDiscription.objects.create(
            Inventory_sheet=InventorySheet.objects.get(id=1),
            Item_Name="Test",
            Brand="DjangoTest",
            Desciprion="Testcase writing",
            Quantity=5,
            Unit_Price=200,
        )

    def test_warehose_get_view(self):
        response = self.client.get("/ware/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ware.html")

    def test_warehouse_post_view(self):
        response = self.client.post(
            "/ware/",
            {"WareHouseId": 5454, "Name": "Shopify", "Address": "Canada"},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.redirect_chain, "")


class createViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Warehouse.objects.create(WareHouseId=1, Name="Test", Address="TestAddress")
        InventorySheet.objects.create(
            Assigned_Warehouse=Warehouse.objects.get(WareHouseId=1)
        )
        InventoryDiscription.objects.create(
            Inventory_sheet=InventorySheet.objects.get(id=1),
            Item_Name="Test",
            Brand="DjangoTest",
            Desciprion="Testcase writing",
            Quantity=5,
            Unit_Price=200,
        )

    def test_create_get_view(self):
        response = self.client.get("/create")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "create.html")

    def test_create_post_view(self):
        response = self.client.post(
            "/create", {"Date": datetime.now(), "WID": "None"}, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.redirect_chain, "edit/")
