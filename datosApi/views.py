from django.shortcuts import render
from reserva.models import Institucion, Reserva
from .serializers import InstitucionSerializer, ReservaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.


@api_view(["GET", "POST"])
def listar_institucion(request):
    if request.method == "GET":
        ins = Institucion.objects.all()
        serializer = InstitucionSerializer(ins, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serial = InstitucionSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def institucion_detalle(request, pk):
    try:
        ins = Institucion.objects.get(pk=pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serial = InstitucionSerializer(ins)
        return Response(serial.data)

    if request.method == "PUT":
        serial = InstitucionSerializer(ins, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        ins.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReservaList(APIView):
    def get(self, request):
        reserva = Reserva.objects.all()
        serial = ReservaSerializer(reserva, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = ReservaSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservaDetalle(APIView):
    def get_object(self, pk):
        try:
            return Reserva.objects.get(pk=pk)
        except Reserva.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        reserva = self.get_object(pk)
        serial = ReservaSerializer(reserva)
        return Response(serial.data)

    def put(self, request, pk):
        reserva = self.get_object(pk)
        serial = ReservaSerializer(reserva, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reserva = self.get_object(pk)
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# json sin ningun tipo de serializacion
def api_json_institucion(request):
    reservas = Reserva.objects.all()
    data = {
        "reservas": list(
            reservas.values(
                "id",
                "nombre",
                "telefono",
                "fecha",
                "hora",
                "inscripcion",
                "institucion",
                "observaciones",
                "estado_de_reserva",
            )
        )
    }
    return JsonResponse(data)
