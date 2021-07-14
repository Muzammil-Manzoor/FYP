from django.shortcuts import render
from rest_framework.response import Response
from .models import product,product_type,brands
from django.http import HttpResponse,JsonResponse
from .serializers import productSerializer,product_typeSerializer,brandsSerializer
from rest_framework import status
from rest_framework import viewsets

class productViewSet(viewsets.ViewSet):

    def list(self, request):
        from rest_framework.pagination import PageNumberPagination
        item = product.objects.all()
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(item, request)
        if page is not None:
            serializer = productSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = productSerializer(item, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)



    def retrieve(self,request,*args,**kwargs):
        params=kwargs
        print(params)
        print('*******************')
        params_list=params['pk'].split('-')
        #id=params['pk']
        size=len(params_list)
        print(f'**************************{params_list}****{size}********')
        
        if(size==1):
            item=product.objects.filter(brand_name=params_list[0])
        elif(size==2):
            item=product.objects.filter(brand_name=params_list[0],gender_category=params_list[1] )  
        elif(size==3):
            item=product.objects.filter(brand_name=params_list[0],gender_category=params_list[1],category_name=params_list[2] )
        if(size==4):
            item=product.objects.filter(gender_category=params_list[0])
        if(size==5):
            item=product.objects.filter(gender_category=params_list[0],category_name=params_list[1])
        
            
            
        #pagination_class=MyPageNumberPagiation
        from rest_framework.pagination import PageNumberPagination
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(item, request)
        if page is not None:
            serializer = productSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = productSerializer(item, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer=productSerializer(stu,many=True)
        return Response(serializer.data)

class product_typeViewSet(viewsets.ViewSet):
    def list(self,request):
        item=product_type.objects.all()
        serializer=product_typeSerializer(item,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        

    def retrieve(self,request,*args,**kwargs):
        pharms=kwargs
        print(pharms)
        print('*******************')

        id=pharms['pk']

        stu=product_type.objects.get(product_type_id=id)
        serializer=product_typeSerializer(stu,many=True)
        return Response(serializer.data)

    
class brandViewSet(viewsets.ViewSet):
    def list(self,request):
        item=brands.objects.all()
        serializer=brandsSerializer(item,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        

    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            stu=brands.objects.get(name=id)
            serializer=brandsSerializer(stu)
            print(serializer.data['name'])
            return Response(serializer.data)

    
    
    
        
