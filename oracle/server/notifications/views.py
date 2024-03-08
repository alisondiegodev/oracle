from django.shortcuts import render
from .models import Token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import cx_Oracle
import uuid


def connect():
    host = "dbcrisdu.crisdulabs.com.br"
    port = "1521"
    service_name = "desenv.snprodcrisdupri.vcnprdcrisdu.oraclevcn.com"
    dsn = f"(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST={host})(PORT={port}))(CONNECT_DATA=(SERVICE_NAME={service_name})(SERVER=dedicated)))"

    return cx_Oracle.connect("roman", "desenv", dsn)
    

@api_view(['GET'])
def token(request):
    try:
        print("Pass trough the view")
        con = connect()
       

    
        return Response({'success': True}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'success': False, 'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
