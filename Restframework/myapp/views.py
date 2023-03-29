from django.shortcuts import render
from .models import userinfo
from rest_framework.decorators import api_view
from .serializers import userserializers
from rest_framework.response import Response
from rest_framework  import status



# Create your views here.
#SELECT DATA
@api_view(['GET'])
def getalldata(request):
    user=userinfo.objects.all()
    userserial=userserializers(user,many=True)
    return Response(userserial.data)

#ID ThROUGH GET
@api_view(['GET'])
def getid(request,id):
    try:
          stid=userinfo.objects.get(id=id)
    except userinfo.DoesNotExist:
          return Response(status=status.HTTP_404_NOT_FOUND)
    userserial=userserializers(stid) 
    return Response(userserial.data)
    
#INSERT DATA
@api_view(['POST'])
def  saveuser(request):
    if request.method=='POST':
          userserial=userserializers(data=request.data)
          if userserial.is_valid():
               userserial.save()
               return Response(status=status.HTTP_201_CREATED)
          else:
               return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#DELETE ID 
@api_view(['GET','DELETE'])
def deleteuser(request,id):
    try:
          stid=userinfo.objects.get(id=id)
    except userinfo.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
         userserial=userserializers(stid)
         return Response(userserial.data)
    if request.method=='DELETE':
        userinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED) 

#UPDATE DATA
@api_view(['GET','PUT'])
def updatedata(request,id):
    try:
          stid=userinfo.objects.get(id=id)
    except userinfo.DoesNotExist:
          return Response(status=status.HTTP_404_NOT_FOUND) 
    if request.method=='GET':
         userserial=userserializers(stid)
         return Response(userserial.data)    
    if  request.method=='PUT':
         userserial=userserializers(data=request.data,instance=stid)
         if userserial.is_valid():
              userserial.save()
              return Response(status=status.HTTP_202_ACCEPTED)
         else:
              return Response(status=status.HTTP_400_BAD_REQUEST)
     


