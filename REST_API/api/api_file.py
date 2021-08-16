from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from .mypaginations import MyPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


#GET requests, which are typically sent by clients when they'd like to receive some information.

#localhost:1200:/api/users?page=1&limit=10&name=James&ordering=-age
class users_list(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    filter_backends=[OrderingFilter,SearchFilter]
    ordering_fields=['age']
    search_fields=['first_name','last_name']
    pagination_class=MyPageNumberPagination


      #POST requests are used to send data to the server.Typically, they contain data in their body that's supposed to be stored.

    def post(self,request):                  #   post() method that receives a POST request
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class UserDetail(APIView):
    def get(self,request,id):              #Sample query looks like:- localhost:1200/api/users/1         It will show all record of id=1

        try:
            model=User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(f'User with {id} is Not Found in database',status=status.HTTP_404_NOT_FOUND)
        serializer=UserSerializer(model)
        return Response(serializer.data,status=status.HTTP_200_OK)

#PUT request modifies a part of the given resource.
    def put(self,request,id):
        try:
            model=User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(f'User with {id} is Not Found in database',status=status.HTTP_404_NOT_FOUND)

        serializer=UserSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





#delete() method ,it takes the ID of the item we'd like to remove.

    def delete(self,request,id):
        try:
            model=User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(f'User with {id} is Not Found in database',status=status.HTTP_404_NOT_FOUND)

        model=User.objects.get(id=id)

        model.delete()
        return Response(f'User with {id} Successfully Delete',status=status.HTTP_200_OK)
