from django.contrib import admin
from .models import User, VanOperator, UserVehicle, ChargingVan, Request, Booking, Payment, Feedback

# ======================
# User Admin
# ======================
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'email', 'user_phone', 'role', 'created_at')
    search_fields = ('user_name', 'email', 'user_phone')
    list_filter = ('role',)

# ======================
# VanOperator Admin
# ======================
@admin.register(VanOperator)
class VanOperatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'operator_name', 'operator_email', 'operator_phone', 'operator_status', 'created_at')
    search_fields = ('operator_name', 'operator_email')
    list_filter = ('operator_status',)

# ======================
# UserVehicle Admin
# ======================
@admin.register(UserVehicle)
class UserVehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'vehicle_company', 'vehicle_name', 'vehicle_model', 'vehicle_number', 'created_at')
    search_fields = ('vehicle_name', 'vehicle_number')
    list_filter = ('vehicle_company',)

# ======================
# ChargingVan Admin
# ======================
@admin.register(ChargingVan)
class ChargingVanAdmin(admin.ModelAdmin):
    list_display = ('id', 'van_number', 'operator', 'battery_capacity', 'created_at')
    search_fields = ('van_number',)
    list_filter = ('battery_capacity',)

# ======================
# Request Admin
# ======================
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'operator', 'vehicle', 'user_location', 'request_time', 'completion_time')
    search_fields = ('user__user_name', 'vehicle__vehicle_number', 'user_location')
    list_filter = ('operator',)

# ======================
# Booking Admin
# ======================
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'request', 'operator', 'booking_status', 'start_time', 'end_time', 'created_at')
    search_fields = ('request__id', 'operator__operator_name')
    list_filter = ('booking_status',)

# ======================
# Payment Admin
# ======================
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'request', 'user', 'operator', 'amount', 'p_method', 'p_status', 'payment_time')
    search_fields = ('user__user_name', 'operator__operator_name')
    list_filter = ('p_status', 'p_method')

# ======================
# Feedback Admin
# ======================
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'operator', 'rating', 'comments', 'created_at')
    search_fields = ('user__user_name', 'operator__operator_name', 'comments')
    list_filter = ('rating',)
