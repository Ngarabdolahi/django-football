from django.shortcuts import render
from django.http import JsonResponse
from app01 import models
# Create your views here.
def search(request):
    return render(request,"search.html")
def majores_get_all(request):
    majores = models.Major.objects.all()
    mjs = []
    for majore in majores:
        mjs.append({"id":majore.id,
                    "name":majore.name})
    return JsonResponse({"majores":mjs})
def teachers_search(request):
    teachers = models.Teacher.objects.filter(majore = models.Major.objects.get(id=request.POST["majore"]))
    tcs=[]
    for teacher in teachers:
        tcs.append({"id":teacher.id,
                    "name":teacher.name,
                    "family":teacher.family,
                    "majores":teacher.majore.name})
    return JsonResponse({"teachers":tcs})
def majores_store(request):
    pass
def teachers_search2(request):
    teachers = models.Teacher.objects.filter(majore = models.Major.objects.get(id=request.POST["major"])) & (models.Teacher.objects.filter(name__startswith = request.POST["search"]) | models.Teacher.objects.filter(family__startswith = request.POST["search"]))
    tcs=[]
    for teacher in teachers:
        tcs.append({"id":teacher.id,
                    "name":teacher.name,
                    "family":teacher.family,
                    "majores":teacher.majore.name
                    })
    return JsonResponse({"teachers":tcs})