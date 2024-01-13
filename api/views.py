# from django.shortcuts import render
# from mobile.models import Mobile
# from rest_framework.viewsets import ViewSet
# from api.serializer import MobileSerializer
# from rest_framework.response import Response


# # Create your views here.


# class MobileView(ViewSet):

#     def create(self,request,*args,kwargs):
#         serializer=MobileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.data)
        

#     def list(self,request,*args,kwargs):
#         qs=Mobile.objects.all()
#         serialiser=MobileSerializer(qs,many=True)
#         return Response(data=serialiser.data)
    

#     def retrieve(self,request,*args,kwargs):
#         id=kwargs.get("pk")
#         qs=Mobile.objects.get(id=id)
#         serializers=MobileSerializer(qs,many=False)
#         return Response(data=serializers.data)
    
#     def update(self,request,*args,kwargs):
#         id=kwargs.get("pk")
#         Mobile_obj=Mobile.objects.get(id=id)
#         serializer=MobileSerializer(data=request.data,instance=Mobile_obj)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.data)
        

#     def destroy(self,request,*args,kwargs):
#         id=kwargs.get("pk")
#         qs=Mobile.objects.get(id=id).delete()
#         return Response(data={"message":"delete"})

    

        