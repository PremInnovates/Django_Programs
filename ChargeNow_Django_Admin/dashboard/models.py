from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# ======================
# Custom User Manager
# ======================
class CustomUserManager(BaseUserManager):
    def create_user(self, email, user_name, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address is required')
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, user_name, password, **extra_fields)


# ======================
# User Model
# ======================
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=30)
    user_phone = models.BigIntegerField()
    user_address = models.CharField(max_length=100)
    role = models.CharField(max_length=10, default='user')  # user/admin
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # admin panel access
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'         # login via email
    REQUIRED_FIELDS = ['user_name']  # required for superuser

    def __str__(self):
        return self.user_name


# ======================
# VanOperator Model
# ======================
class VanOperator(models.Model):
    operator_name = models.CharField(max_length=30)
    operator_email = models.EmailField(unique=True)
    operator_password = models.CharField(max_length=15)
    operator_phone = models.BigIntegerField()
    operator_license_doc = models.CharField(max_length=100)
    operator_status = models.CharField(max_length=10, choices=(('online','online'),('offline','offline')), default='offline')
    van = models.ForeignKey('ChargingVan', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.operator_name


# ======================
# UserVehicle Model
# ======================
class UserVehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_company = models.CharField(max_length=30)
    vehicle_name = models.CharField(max_length=30)
    vehicle_model = models.CharField(max_length=30)
    vehicle_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_number


# ======================
# ChargingVan Model
# ======================
class ChargingVan(models.Model):
    van_number = models.CharField(max_length=15, unique=True)
    operator = models.ForeignKey(VanOperator, on_delete=models.SET_NULL, null=True, blank=True)
    battery_capacity = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.van_number


# ======================
# Request Model
# ======================
class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    operator = models.ForeignKey(VanOperator, on_delete=models.SET_NULL, null=True, blank=True)
    vehicle = models.ForeignKey(UserVehicle, on_delete=models.CASCADE)
    user_location = models.CharField(max_length=255)
    request_time = models.DateTimeField(auto_now_add=True)
    completion_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Request {self.id} by {self.user.user_name}"


# ======================
# Booking Model
# ======================
class Booking(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    operator = models.ForeignKey(VanOperator, on_delete=models.CASCADE)
    booking_status = models.CharField(
        max_length=15,
        choices=(
            ('pending','pending'),
            ('accepted','accepted'),
            ('rejected','rejected'),
            ('inprogress','inprogress'),
            ('completed','completed'),
            ('canceled','canceled')
        ),
        default='pending'
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id}"


# ======================
# Payment Model
# ======================
class Payment(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    operator = models.ForeignKey(VanOperator, on_delete=models.CASCADE)
    amount = models.FloatField()
    p_method = models.CharField(max_length=10, choices=(('upi','upi'),('card','card'),('wallet','wallet')))
    p_status = models.CharField(max_length=10, choices=(('success','success'),('failed','failed'),('pending','pending')), default='pending')
    payment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id}"


# ======================
# Feedback Model
# ======================
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    operator = models.ForeignKey(VanOperator, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.id} - {self.rating}⭐"
