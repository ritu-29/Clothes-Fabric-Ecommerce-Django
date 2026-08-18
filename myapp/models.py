from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone

# Create your models here.

class Login(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, default="admin@123")
    phone = models.CharField(max_length=20, null=True, blank=True)

    ROLE = (
        ("Seller", "Seller"),
        ("User", "User"),
    )
    role = models.CharField(max_length=10, choices=ROLE, default='User')

    STATUS = (
        ("0", "unapproved"),
        ("1", "approved")
    )
    status = models.CharField(max_length=10, choices=STATUS, default='0')

    id_proof = models.FileField(upload_to='id_proofs/', null=True, blank=True, default=None)

    def pic(self):
        return mark_safe('<img src = "{}" width = "100">'.format(self.id_proof.url))
    pic.allow_tags = True

    def __str__(self):
        return self.name

class Contact_detail(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    address = models.TextField()
    date_of_birth = models.DateField(blank=True, null=True)
    profession = models.CharField(max_length=100)  # User's profession
    bio = models.TextField(blank=True, null=True)  # Brief introduction
    userprofile_image = models.ImageField(upload_to='media/', blank=True, null=True)

    def user_image(self):
        return mark_safe('<img src = "{}" width = "100">'.format(self.userprofile_image.url))
    user_image.allow_tags = True

    def __str__(self):
        return self.user.name

class SellerProfile(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=True)
    sellerprofile_image = models.ImageField(upload_to='seller_profiles/', blank=True, null=True)
    shop_name = models.CharField(max_length=255, blank=True, null=True)
    shop_address = models.TextField(blank=True, null=True)
    years_of_experience = models.FloatField(blank=True, null=True)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    rating = models.FloatField(default=0.0)  # Changed to FloatField
    availability = models.CharField(max_length=40, choices=[('Available', 'Available'), ('Not Available', 'Not Available')], default='Available')

    def seller_image(self):
        return mark_safe('<img src = "{}" width = "100">'.format(self.sellerprofile_image.url))
    seller_image.allow_tags = True

    def __str__(self):
        return f"{self.user.name}'s Seller Profile"

class ProductCategory(models.Model):
    cateName = models.CharField(max_length=25)

    def __str__(self):
        return self.cateName

class Product(models.Model):
    seller = models.ForeignKey('Login', on_delete=models.CASCADE, limit_choices_to={'role': 'Seller'}, default='')
    Cate = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=25)
    type = models.CharField(choices=[("fabric","fabric"),("embllishments","embllishments")],null=True,max_length=40)
    measure = models.CharField(choices=[("meter","meter"),("Pack of 10 pcs","Pack of 10 pcs")],null=True,max_length=40)
    desc = models.TextField()
    price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=True)
    image1 = models.ImageField(upload_to='product_images/', blank=True, default='')
    status = models.CharField(max_length=40, choices=[('Available', 'Available'), ('Not Available', 'Not Available')], default='Available')


    def pic(self):
        return mark_safe('<img src = "{}" width = "100">'.format(self.image1.url))
    pic.allow_tags = True

    def __str__(self):
        return self.name

class productCart(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Price = models.IntegerField(default=100)
    Quantity = models.PositiveIntegerField(default=1)
    total = models.FloatField()
    Order_id = models.IntegerField(default=0)
    Order_status = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.user.name} - {self.product.name}"

    def save(self, *args, **kwargs):
        if not self.pk:
            product = self.product
            if product.quantity >= int(self.Quantity):  # Convert self.Quantity to an integer
                product.quantity -= int(self.Quantity)
                product.save()
                self.total = int(self.Quantity) * product.price  # Convert self.Quantity to an integer
            else:
                raise ValueError("Insufficient quantity available")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        product = self.product
        product.quantity += self.Quantity
        product.save()
        super().delete(*args, **kwargs)

class Order(models.Model):
    PAYMENT_MODE_CHOICES = [
        ('online', 'Online Payment'),
        ('offline', 'Offline Payment'),
    ]

    PAYMENT_STATUS = (
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("Failed", "Failed"),
    )

    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    amount = models.FloatField()  # Store the total order amount
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=255, blank=True, null=True)
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODE_CHOICES)  # Payment mode
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default="Pending")
    offline_reference = models.CharField(max_length=255, blank=True, null=True)  # Reference number for offline payment
    offline_remarks = models.TextField(blank=True, null=True)  # Optional remarks for offline payments
    address = models.TextField(blank=True, null=True)  # Optional remarks for offline payments
    timestamp = models.DateTimeField(default=timezone.now)


    def get_total_amount(self):
        return self.amount

class Feedback(models.Model):
    user = models.ForeignKey('Login', on_delete=models.CASCADE, default="")
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, blank=True, default='')
    ratings = models.IntegerField()
    comment = models.CharField(max_length=300, default="")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Feedback from {self.user.name}"

class Complaint(models.Model):
    user = models.ForeignKey('Login', on_delete=models.CASCADE, default="")
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, blank=True, default='')
    subject = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Complaint from {self.user.name} - {self.subject}"

