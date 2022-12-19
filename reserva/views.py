from django.shortcuts import render, redirect
from .models import Reserva, Institucion
from .form import FormReserva


# Create your views here.


def home(request):
    return render(request, "home.html")


# Registramos datos del formulario en la base de datos
def registrar(request):

    if request.method == "POST":
        form = FormReserva(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listado")
    else:
        form = FormReserva()
    data = {"form": form}
    return render(request, "registrar.html", data)


# funcion para listar los datos de la base de datos
def listado(request):
    reserva = Reserva.objects.all()
    data = {"reserva": reserva}
    return render(request, "listado.html", data)


# creamos la funcio para editar los datos de la base de datos
def editar(request, id):
    if request.method == "GET":
        reserva = Reserva.objects.get(id=id)
        form = FormReserva(instance=reserva)
        data = {"form": form}
        return render(request, "editar.html", data)
    else:
        try:
            reserva = Reserva.objects.get(id=id)
            form = FormReserva(request.POST, instance=reserva)
            if form.is_valid():
                form.save()
            return redirect("listado")
        except ValueError:
            return render(
                request,
                "editar.html",
                {"form": form, "error": "NO SE PUDO EDITAR EL REGISTRO"},
            )


def eliminar(request, id):
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    return redirect("listado")

