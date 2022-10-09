from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status
from datetime import date, datetime, timedelta
from django.http import HttpResponse
import xlwt

@api_view(['GET'])
def getCountry(request):
    countri = Countries.objects.all()
    con = request.query_params.get('country', None)
    print("test")
    if con:
        c = []
        for i in Countries.objects.all():
            # print("tessstttt --->",con)
            if str(i).lower() == str(con).lower():
                c.append(i)
            # print(c)
        countri = c

    serializer = CountriesSerializer(countri , many=True)
    # print(serializer.data[0])
    return Response(serializer.data)

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/country/all/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of countries withs capitals , region and some informations'
        },
        {
            'Endpoint': 'country/all?country=neme_of_country',
            'method': 'GET',
            'body': None,
            'description': 'Returns a Country withs capitals , region and some informations'
        },
    ]
    return Response(routes)

def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="countries.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Countrise')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Country' , 'Capital' , 'Region' , 'Geography']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    
    rows = Countries.objects.all().values_list('country' , 'capital' , 'region' , 'geography')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response
'''
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Username', 'First name', 'Last name', 'Email address', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
'''