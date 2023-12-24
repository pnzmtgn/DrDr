from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import speciality, doctor
# Create your views here.

def List(request):
    specialty_list = speciality.objects.all()
    specialty_json = []
    for item in specialty_list:
        specialty_json.append({
            'Specialty' : item.Name
        })
    return JsonResponse(specialty_json, safe=False)

def List_html(request):
    specialities = speciality.objects.all()
    specialities_json = {'Specialty':specialities}
    return render(request, 'Specialty/index.html', specialities_json)

def cardio_list(request):
    doctor_list = doctor.objects.all()
    cardio_doctor_list = []
    for doci in doctor_list:
        if doci.Specialty.Name == 'Cardiology':
            cardio_doctor_list.append({
                'Name' : doci.Name,
                'Specialty' : doci.Specialty.Name
            })
    return JsonResponse(cardio_doctor_list, safe=False)

def cardio_filt(request):
    specialty = specialty.objects.filter(specialty='cardiology')


def dermato_list(request):
    doctor_list = doctor.objects.all()
    derma_doctor_list = []
    for doci in doctor_list:
        if doci.Specialty.Name == 'Dermatology':
            derma_doctor_list.append({
                'Name' : doci.Name,
                'Speciality' : doci.Specialty.Name
            })
    return JsonResponse(derma_doctor_list, safe=False)  


def dermato_filt(request):
    specialty = specialty.objects.filter(specialty='dermatology')  

def hemato_list(request):
    doctor_list = doctor.objects.all()
    hemato_doctor_list = []
    for doci in doctor_list:
        if doci.Specialty.Name == 'Hematology':
            hemato_doctor_list.append({
                'Name' : doci.Name,
                'Specialty' : doci.Specialty.Name
            })
    return JsonResponse(hemato_doctor_list, safe=False)

    

