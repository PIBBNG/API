from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from EBD.models import EBDUser, EBDClass, ClassRegister
from rest_framework.permissions import AllowAny
from django.http import JsonResponse

class EBDClassView(APIView):

    permissions_classes = (AllowAny,)

    def post(self, request):
        try:
            class_name = request.data['class_name']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            EBDClass.objects.create(name=class_name)
            print(f"[LOG] Classe da EBD: '{class_name}', criada com sucesso!")
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        try:
            ebd_class_data = EBDClass.objects.all()

            data = []
            for ebd_class in ebd_class_data:
                aux = {}
                aux["class_name"] = ebd_class.name
                aux["students_count"] = ebd_class.ebd_class.count()
                data.append(aux)
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)