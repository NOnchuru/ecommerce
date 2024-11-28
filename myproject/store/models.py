from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    """Model representing a customer."""
    name = models.CharField(max_length=100)  # Name of the customer
    email = models.EmailField(unique=True)    # Unique email for the customer

    def __str__(self):
        return self.name


class Order(models.Model):
    """Model representing an order placed by a customer."""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the order is created
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount for the order

    def __str__(self):
        return f'Order {self.id} by {self.customer.name}'