from django.contrib import admin
from .models import Temp,Visitor_perma
import csv
from django_export_csv import render_csv_response

# def export_csv(Vistor_permaadmin, request, qu):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
#     writer = csv.writer(response, csv.excel)
#     response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
#     writer.writerow([
#         smart_str(u"name"),
#         smart_str(u"phone"),
#         smart_str(u"Date"),
#     ])
#     for obj in qu:
#         writer.writerow([
#             smart_str(obj.name),
#             smart_str(obj.phone),
#             smart_str(obj.date),
#         ])
#     return response
# export_csv.short_description = u"Export CSV"


# class Vistor_permaadmin(admin.ModelAdmin):
#     actions = [export_csv]

admin.site.register(Temp)
admin.site.register(Visitor_perma)
# admin.site.register(Visitor_perma, Vistor_permaadmin)



        
