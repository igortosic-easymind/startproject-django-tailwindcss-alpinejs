from django.shortcuts import render
from . import models
from .forms import ClientForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

# Create your views here.


def get_clients(request):
    clients = models.Client.objects.all()
    return render(request, "clients/clients.html", {"clients": clients})


def add_client(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Client has been successfully created")
            return redirect("/dashboard/clients")
    form.required_fields = [
        "company_name",
        "first_name",
        "first_name",
        "last_name",
        "position",
        "phone",
        "email",
        "website",
        "address" "city",
        "state",
        "zipcode",
    ]
    context = {"form": form}
    return render(request, "clients/add_client.html", context)


def view_client(request, pk):
    client = models.Client.objects.get(id=pk)
    field_labels = {field.name: field.verbose_name for field in client._meta.fields}

    context = {
        "client": client,
        "field_labels": field_labels,
    }
    return render(request, "clients/view_client.html", context)


# def update_client(request, pk):
#     client = models.Client.objects.get(id=pk)
#     form = ClientForm(request.POST, instance=client)
#     if form.is_valid():
#         form.save()
#         messages.success(request, "Client Has Been Updated!")
#         return redirect("/dashboard/clients")
#     context = {"form": form}
#     return render(request, "clients/update_client.html", context)


def update_client(request, pk):
    item = get_object_or_404(models.Client, id=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Client has been successfully updated")
            return redirect("/dashboard/clients")
    else:
        form = ClientForm(instance=item)

    form.required_fields = [
        "company_name",
        "first_name",
        "first_name",
        "last_name",
        "position",
        "phone",
        "email",
        "website",
        "address" "city",
        "state",
        "zipcode",
    ]
    return render(request, "clients/update_client.html", {"form": form})


def delete_client(request, pk):
    client = models.Client.objects.get(id=pk)
    client.delete()
    messages.success(request, "Client has been successfully deleted")
    return redirect("/dashboard/clients")
