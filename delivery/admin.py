from django.contrib import admin
from delivery.models import neww_order_info,delivery_rate,products,additional_charges,currency_rate,payment,order_info
from django.http import HttpResponse
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_user_model
from django.db import connection
connection.queries



# Register your models here.




class delivery_rateAdmin(admin.ModelAdmin):
    list_filter=('country',)


def export_csv_of_delivery_rates(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Delivery_rates.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"id"),
        smart_str(u"country"),
        smart_str(u"weight"),
        smart_str(u"amount"),
        smart_str(u"delivery_type"),
    ])
    for obj in queryset:
        writer.writerow([
        smart_str(obj.id),
        smart_str(obj.country),
        smart_str(obj.weight),
        smart_str(obj.amount),
        smart_str(obj.delivery_type),   
        ])
    return response
    export_csv.short_description = u"Export CSV"


class drate(admin.ModelAdmin):
    list_display = ('id','country','weight','amount','delivery_type',)
    actions = [export_csv_of_delivery_rates,]
    search_fields = ['id','country','weight','amount','delivery_type',]


def export_csv_of_additional_charges(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Additional_charges.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"id"),
        smart_str(u"scheme_name"),
        smart_str(u"scheme_type"),
        smart_str(u"charge_per_transaction"),
    ])
    for obj in queryset:
        writer.writerow([
        smart_str(obj.id),
        smart_str(obj.scheme_name),
        smart_str(obj.scheme_type),
        smart_str(obj.charge_per_transaction),
        ])
    return response
    export_csv.short_description = u"Export CSV"

class additional(admin.ModelAdmin):
    list_display = ('id','scheme_name','scheme_type','charge_per_transaction',)
    actions = [export_csv_of_additional_charges,]
    search_fields = ['id','scheme_name','scheme_type','charge_per_transaction',]

admin.site.register(delivery_rate,drate)
admin.site.register(additional_charges,additional)
admin.site.register(products)
admin.site.register(currency_rate)
admin.site.register(order_info)
#admin.site.register(new_order_info)
admin.site.register(payment)
admin.site.register(neww_order_info)




