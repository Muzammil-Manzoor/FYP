from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


import pandas as pd

# Create your views here.

class UserViewSet(viewsets.ViewSet):

    def list(self,request):
        stu=User.objects.all()
        serializer=UserSerializer(stu,many=True)
        return Response(serializer.data)
        print(serializer.data)

    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            stu=User.objects.get(username=id)
            serializer=UserSerializer(stu)
            print(serializer.data['user_interest_brands'])
            return Response(serializer.data)
    # pick rules row for recommendation system
    def pick_rules(self,row, user_interest_list):
        
        consider_antecedents = True
        consider_consequents = True

        # Loop through all antecedents and find is this antecedents are
        # related to user intersts or not?.
        for item in row.antecedents:
            if item not in user_interest_list:
                consider_antecedents = False

            if  consider_antecedents:
            # Antecedents are matched

            # Now check if consequents of this rule is not in users Interests
            # then this rule is for this user.
                for item in row.consequents:
                    if item in user_interest_list:
                        consider_consequents = False
                    
                if(consider_consequents):
                # This rule is matched with the user.
                    return True
                else:
                    return False

            else:
                return False

    def create(self,request):

        serializer=UserSerializer(data=request.data)

        rul_df=pd.read_csv('./users_api/brands_recommendation.csv',converters={'antecedents': eval, 'consequents': eval})            # get user name and interests of new user.
        userinterests = request.data['user_interest_brands']
            # convert user interest into list.
        u_i_list = userinterests.split(',')

        applied_rul_df =  pd.DataFrame(columns=rul_df.columns)
            
        for index, row in  rul_df.iterrows():
            if(self.pick_rules(row,u_i_list)):
                applied_rul_df = applied_rul_df.append(row)
                    
            # get a rule which have higest lift 
            if(applied_rul_df.shape[0] >= 1):
                columns_names = ['antecedents', 'consequents', 'antecedent support', 'consequent support', 'support', 'confidence', 'lift', 'leverage', 'conviction']    
                selected_rule= applied_rul_df.iloc[applied_rul_df.lift.argmax()]
                userSeleted_Interest = selected_rule.consequents
                my_string = ','.join(userSeleted_Interest)
                new_user = {
                    
                    "user_recommend_brands": my_string
                }
            
            else:
                # In case no rule is matched with the user Interests.
                new_user = {
                    
                    "user_recommend_brands": "GULAHMED"
                        }
            dict3=request.data.update(new_user)
        print(request.data)

        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response({'msj':'data creates'},status=status.HTTP_201_CREATED)
            print("**************Creates**********")
        return Response(serializer.errors)
 
    def update(self,request,pk=None):
        id=pk
        stu=User.objects.get(username=id)
        serializer=UserSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msj':'Dta update'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    def partial_update(self,request,pk=None):
        id=pk
        stu=User.objects.get(id=id)
        serializer=UserSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msj':'partial  update'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
