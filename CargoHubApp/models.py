from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return self.name


class ItemLine(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ItemType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ItemGroup(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    item_type = models.ForeignKey(ItemType, on_delete=models.SET_NULL, null=True, related_name='items')
    item_group = models.ForeignKey(ItemGroup, on_delete=models.SET_NULL, null=True, related_name='items')
    item_line = models.ForeignKey(ItemLine, on_delete=models.SET_NULL, null=True, related_name='items')

    def __str__(self):
        return self.name


class Inventory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='inventories')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='inventories')
    total_on_hand = models.IntegerField()
    total_ordered = models.IntegerField(default=0)
    total_allocated = models.IntegerField(default=0)

    def __str__(self):
        return f"Inventory for {self.item.name} at {self.location.name}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} for {self.client.name}"


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

    def __str__(self):
        return self.name


class Shipment(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='shipments')
    shipment_date = models.DateTimeField()

    def __str__(self):
        return f"Shipment #{self.id} from {self.supplier.name}"


class Transfer(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='transfers')
    from_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='transfers_out')
    to_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='transfers_in')
    amount = models.IntegerField()
    transfer_date = models.DateTimeField()

    def __str__(self):
        return f"Transfer #{self.id} for {self.item.name}"
