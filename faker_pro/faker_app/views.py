from django.shortcuts import render,HttpResponse,redirect
from .models import person
from faker import Faker

# Create your views here.
fake=Faker()

def faker_view(request):
    for i in range(50):
        fake_name=fake.name()
        fake_mobile=fake.random_int(min=12345, max=89078)
        fake_location=fake.address()
    data=person(
        name=fake_name,
        mobile=fake_mobile,
        location=fake_location,
    )

    data.save()
    return redirect('data')

def display_data(request):
    data=person.objects.all()
    return render(request,'display.html',{'data':data})
