from django.shortcuts import render
from Family_Data.models import FamilyData
from django.http import HttpResponse
from django.template import loader


def FamilyDataViews(request):
    dataFamily = FamilyData.objects.all()
    
    return render( request, 'index.html', { 'data': dataFamily } )