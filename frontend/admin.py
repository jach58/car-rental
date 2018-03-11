from django.contrib import admin


# Register your models here.
from django.contrib import admin
from .models import Car, Booking


class BookingModelAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'booking_start_date', 'booking_end_date', 'is_approved']
    list_filter = ['is_approved']
    search_fields = ['customer_name']
    list_editable = ['is_approved']

    actions = ['email_customers']

    def email_customers(self,request, queryset):

        for booking in queryset:
            if booking.is_approved:
                email_body = """Dear {},
                We are pleased to inform you that you booking has been approved.
                Tanks
                """.format(booking.customer_name)
            else:
                email_body = """Dear {},
                Unfortunately we do not have tha capacity right now to accept your booking.
                Tanks
                """.format(booking.customer_name)

            print(email_body)

        self.message_user(request, 'Emails were send successfully')

    email_customers.short_description = 'Send email about booking status to customers'

admin.site.register(Car)
admin.site.register(Booking, BookingModelAdmin)


