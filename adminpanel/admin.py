from django.contrib import admin
from django.http import HttpResponse
from django.contrib.auth.models import Group
from .models import Pending_deliverie
from .models import Completed_deliverie
from .models import Pending_payment
from .models import Deliverie
from .models import Payment
from .models import Completed_payment
from django.db import models
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_user_model
from django.db import connection
connection.queries

admin.site.site_header = 'Orders'




    
def export_Completed_deliveries_as_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Completed_deliveries.csv'
    writer = csv.writer(response,csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"tracking_id"),
        smart_str(u"user_name"),
        smart_str(u"sender_name"),
        smart_str(u"sender_phn_number"),
        smart_str(u"sender_email"),
        smart_str(u"pick_country"),
        smart_str(u"pick_state"),
        smart_str(u"pick_town"),
        smart_str(u"pick_house_number"),
        smart_str(u"pick_street_name"),
        smart_str(u"pick_apartment_number"),
        smart_str(u"pick_zip_code"),
        smart_str(u"recipient_name"),
        smart_str(u"recipient_email_1"),
        smart_str(u"recipient_email_2"),
        smart_str(u"recipient_phone"),
        smart_str(u"country"),
        smart_str(u"state"),
        smart_str(u"town"),
        smart_str(u"house_number"),
        smart_str(u"street_name"),
        smart_str(u"apartment_number"),
        smart_str(u"zip_code"),
        smart_str(u"product_details"),
        smart_str(u"delivery_type"),
        smart_str(u"pickup_date_start"),
        smart_str(u"pickup_date_end"),
        smart_str(u"delivery_status"),
        smart_str(u"payment_status"),
        smart_str(u"estimated_weight"),
        smart_str(u"estimated_cost"),
        smart_str(u"volumetric_weight"),
        smart_str(u"payment_URL"),
        smart_str(u"po_box"),
        smart_str(u"payment_done"),
        ])

    for obj in queryset:
        writer.writerow([
        smart_str(obj.tracking_id),
        smart_str(obj.user_name),
        smart_str(obj.sender_name),
        smart_str(obj.sender_phn_number),
        smart_str(obj.sender_email),
        smart_str(obj.pick_country),
        smart_str(obj.pick_state),
        smart_str(obj.pick_town),
        smart_str(obj.pick_house_number),
        smart_str(obj.pick_street_name),
        smart_str(obj.pick_apartment_number),
        smart_str(obj.pick_zip_code),
        smart_str(obj.recipient_name),
        smart_str(obj.recipient_email_1),
        smart_str(obj.recipient_email_2),
        smart_str(obj.recipient_phone),
        smart_str(obj.country),
        smart_str(obj.state),
        smart_str(obj.town),
        smart_str(obj.house_number),
        smart_str(obj.street_name),
        smart_str(obj.apartment_number),
        smart_str(obj.zip_code),
        smart_str(obj.product_details),
        smart_str(obj.delivery_type),
        smart_str(obj.pickup_date_start),
        smart_str(obj.pickup_date_end),
        smart_str(obj.delivery_status),
        smart_str(obj.payment_status),
        smart_str(obj.estimated_weight),
        smart_str(obj.estimated_cost),
        smart_str(obj.volumetric_weight),
        smart_str(obj.payment_URL),
        smart_str(obj.po_box),
        smart_str(obj.payment_done),
        ])
    return response
    export_csv.short_description = u"Export CSV"

def export_completed_payments_as_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Completed_payments.csv'
    writer = csv.writer(response,csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"tracking_id"),
        smart_str(u"user_name"),
        smart_str(u"sender_name"),
        smart_str(u"sender_phn_number"),
        smart_str(u"sender_email"),
        smart_str(u"pick_country"),
        smart_str(u"pick_state"),
        smart_str(u"pick_town"),
        smart_str(u"pick_house_number"),
        smart_str(u"pick_street_name"),
        smart_str(u"pick_apartment_number"),
        smart_str(u"pick_zip_code"),
        smart_str(u"recipient_name"),
        smart_str(u"recipient_email_1"),
        smart_str(u"recipient_email_2"),
        smart_str(u"recipient_phone"),
        smart_str(u"country"),
        smart_str(u"state"),
        smart_str(u"town"),
        smart_str(u"house_number"),
        smart_str(u"street_name"),
        smart_str(u"apartment_number"),
        smart_str(u"zip_code"),
        smart_str(u"product_details"),
        smart_str(u"delivery_type"),
        smart_str(u"pickup_date_start"),
        smart_str(u"pickup_date_end"),
        smart_str(u"delivery_status"),
        smart_str(u"payment_status"),
        smart_str(u"estimated_weight"),
        smart_str(u"estimated_cost"),
        smart_str(u"volumetric_weight"),
        smart_str(u"payment_URL"),
        smart_str(u"po_box"),
        smart_str(u"payment_done"),
        ])

    for obj in queryset:
        writer.writerow([
        smart_str(obj.tracking_id),
        smart_str(obj.user_name),
        smart_str(obj.sender_name),
        smart_str(obj.sender_phn_number),
        smart_str(obj.sender_email),
        smart_str(obj.pick_country),
        smart_str(obj.pick_state),
        smart_str(obj.pick_town),
        smart_str(obj.pick_house_number),
        smart_str(obj.pick_street_name),
        smart_str(obj.pick_apartment_number),
        smart_str(obj.pick_zip_code),
        smart_str(obj.recipient_name),
        smart_str(obj.recipient_email_1),
        smart_str(obj.recipient_email_2),
        smart_str(obj.recipient_phone),
        smart_str(obj.country),
        smart_str(obj.state),
        smart_str(obj.town),
        smart_str(obj.house_number),
        smart_str(obj.street_name),
        smart_str(obj.apartment_number),
        smart_str(obj.zip_code),
        smart_str(obj.product_details),
        smart_str(obj.delivery_type),
        smart_str(obj.pickup_date_start),
        smart_str(obj.pickup_date_end),
        smart_str(obj.delivery_status),
        smart_str(obj.payment_status),
        smart_str(obj.estimated_weight),
        smart_str(obj.estimated_cost),
        smart_str(obj.volumetric_weight),
        smart_str(obj.payment_URL),
        smart_str(obj.po_box),
        smart_str(obj.payment_done),
        ])
    return response
    export_csv.short_description = u"Export CSV"


def export_Pending_deliveries_as_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Pending_deliveries.csv'
    writer = csv.writer(response,csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"tracking_id"),
        smart_str(u"user_name"),
        smart_str(u"sender_name"),
        smart_str(u"sender_phn_number"),
        smart_str(u"sender_email"),
        smart_str(u"pick_country"),
        smart_str(u"pick_state"),
        smart_str(u"pick_town"),
        smart_str(u"pick_house_number"),
        smart_str(u"pick_street_name"),
        smart_str(u"pick_apartment_number"),
        smart_str(u"pick_zip_code"),
        smart_str(u"recipient_name"),
        smart_str(u"recipient_email_1"),
        smart_str(u"recipient_email_2"),
        smart_str(u"recipient_phone"),
        smart_str(u"country"),
        smart_str(u"state"),
        smart_str(u"town"),
        smart_str(u"house_number"),
        smart_str(u"street_name"),
        smart_str(u"apartment_number"),
        smart_str(u"zip_code"),
        smart_str(u"product_details"),
        smart_str(u"delivery_type"),
        smart_str(u"pickup_date_start"),
        smart_str(u"pickup_date_end"),
        smart_str(u"delivery_status"),
        smart_str(u"payment_status"),
        smart_str(u"estimated_weight"),
        smart_str(u"estimated_cost"),
        smart_str(u"volumetric_weight"),
        smart_str(u"payment_URL"),
        smart_str(u"po_box"),
        smart_str(u"payment_done"),
        ])

    for obj in queryset:
        writer.writerow([
        smart_str(obj.tracking_id),
        smart_str(obj.user_name),
        smart_str(obj.sender_name),
        smart_str(obj.sender_phn_number),
        smart_str(obj.sender_email),
        smart_str(obj.pick_country),
        smart_str(obj.pick_state),
        smart_str(obj.pick_town),
        smart_str(obj.pick_house_number),
        smart_str(obj.pick_street_name),
        smart_str(obj.pick_apartment_number),
        smart_str(obj.pick_zip_code),
        smart_str(obj.recipient_name),
        smart_str(obj.recipient_email_1),
        smart_str(obj.recipient_email_2),
        smart_str(obj.recipient_phone),
        smart_str(obj.country),
        smart_str(obj.state),
        smart_str(obj.town),
        smart_str(obj.house_number),
        smart_str(obj.street_name),
        smart_str(obj.apartment_number),
        smart_str(obj.zip_code),
        smart_str(obj.product_details),
        smart_str(obj.delivery_type),
        smart_str(obj.pickup_date_start),
        smart_str(obj.pickup_date_end),
        smart_str(obj.delivery_status),
        smart_str(obj.payment_status),
        smart_str(obj.estimated_weight),
        smart_str(obj.estimated_cost),
        smart_str(obj.volumetric_weight),
        smart_str(obj.payment_URL),
        smart_str(obj.po_box),
        smart_str(obj.payment_done),
        ])
    return response
    export_csv.short_description = u"Export CSV"

def export_Pending_payments_as_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Pending_payments.csv'
    writer = csv.writer(response,csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"tracking_id"),
        smart_str(u"user_name"),
        smart_str(u"sender_name"),
        smart_str(u"sender_phn_number"),
        smart_str(u"sender_email"),
        smart_str(u"pick_country"),
        smart_str(u"pick_state"),
        smart_str(u"pick_town"),
        smart_str(u"pick_house_number"),
        smart_str(u"pick_street_name"),
        smart_str(u"pick_apartment_number"),
        smart_str(u"pick_zip_code"),
        smart_str(u"recipient_name"),
        smart_str(u"recipient_email_1"),
        smart_str(u"recipient_email_2"),
        smart_str(u"recipient_phone"),
        smart_str(u"country"),
        smart_str(u"state"),
        smart_str(u"town"),
        smart_str(u"house_number"),
        smart_str(u"street_name"),
        smart_str(u"apartment_number"),
        smart_str(u"zip_code"),
        smart_str(u"product_details"),
        smart_str(u"delivery_type"),
        smart_str(u"pickup_date_start"),
        smart_str(u"pickup_date_end"),
        smart_str(u"delivery_status"),
        smart_str(u"payment_status"),
        smart_str(u"estimated_weight"),
        smart_str(u"estimated_cost"),
        smart_str(u"volumetric_weight"),
        smart_str(u"payment_URL"),
        smart_str(u"po_box"),
        smart_str(u"payment_done"),
        ])

    for obj in queryset:
        writer.writerow([
        smart_str(obj.tracking_id),
        smart_str(obj.user_name),
        smart_str(obj.sender_name),
        smart_str(obj.sender_phn_number),
        smart_str(obj.sender_email),
        smart_str(obj.pick_country),
        smart_str(obj.pick_state),
        smart_str(obj.pick_town),
        smart_str(obj.pick_house_number),
        smart_str(obj.pick_street_name),
        smart_str(obj.pick_apartment_number),
        smart_str(obj.pick_zip_code),
        smart_str(obj.recipient_name),
        smart_str(obj.recipient_email_1),
        smart_str(obj.recipient_email_2),
        smart_str(obj.recipient_phone),
        smart_str(obj.country),
        smart_str(obj.state),
        smart_str(obj.town),
        smart_str(obj.house_number),
        smart_str(obj.street_name),
        smart_str(obj.apartment_number),
        smart_str(obj.zip_code),
        smart_str(obj.product_details),
        smart_str(obj.delivery_type),
        smart_str(obj.pickup_date_start),
        smart_str(obj.pickup_date_end),
        smart_str(obj.delivery_status),
        smart_str(obj.payment_status),
        smart_str(obj.estimated_weight),
        smart_str(obj.estimated_cost),
        smart_str(obj.volumetric_weight),
        smart_str(obj.payment_URL),
        smart_str(obj.po_box),
        smart_str(obj.payment_done),
        ])
    return response
    export_csv.short_description = u"Export CSV"



class Pending_deli_filter(admin.ModelAdmin):
    list_display = ('id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',)
    actions = [export_Pending_deliveries_as_csv,]
    readonly_fields = ('id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',
)
    search_fields = ['id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',]
    
    def get_queryset(self, request):
        queryset = Pending_deliverie.objects.filter(delivery_status="Pending")
        return queryset

class Completed_deli_filter(admin.ModelAdmin):
    list_display = ('id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',)
    actions = [export_Completed_deliveries_as_csv,]
    readonly_fields = ('id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',
)
    search_fields = ['id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',]

    def get_queryset(self, request):
        queryset = Pending_deliverie.objects.filter(delivery_status="Completed")
        return queryset


class Pending_pay_filter(admin.ModelAdmin):
    list_display = ('id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',)
    actions = [export_Pending_payments_as_csv,]
    readonly_fields = ('id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',
)
    search_fields = ['id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',]

    def get_queryset(self, request):
        queryset = Pending_deliverie.objects.filter(payment_status="Pending")
        return queryset


class Completed_pay_filter(admin.ModelAdmin):
    list_display = ('id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',)
    actions = [export_completed_payments_as_csv,]
    readonly_fields =('id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',
)
    search_fields = ['id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',]

    def get_queryset(self, request):
        queryset = Completed_deliverie.objects.filter(payment_status="Completed")
        return queryset













class All_Payment(admin.ModelAdmin):
    list_display = ('id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',)
    actions = [export_completed_payments_as_csv,]
    readonly_fields =('id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',
)
    search_fields = ['id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',]

class All_deliverie(admin.ModelAdmin):
    list_display = ('id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',)
    actions = [export_completed_payments_as_csv,]
    readonly_fields =('id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',
)
    search_fields = ['id','tracking_id','user_name','sender_name','sender_phn_number','sender_email','pick_country','pick_state','pick_town','pick_house_number','pick_street_name','pick_apartment_number','pick_zip_code','recipient_name','recipient_email_1','recipient_email_2','recipient_phone','country','state','town','house_number','street_name','apartment_number','zip_code','product_details','delivery_type','pickup_date_start','pickup_date_end','delivery_status','payment_status','estimated_weight','estimated_cost','volumetric_weight','payment_URL','po_box','payment_done',]

   

admin.site.register(Pending_deliverie,Pending_deli_filter)
admin.site.register(Completed_deliverie,Completed_deli_filter)
admin.site.register(Pending_payment,Pending_pay_filter)
admin.site.register(Completed_payment,Completed_pay_filter)
admin.site.register(Payment,All_Payment)
admin.site.register(Deliverie,All_deliverie)
admin.site.unregister(Group)
