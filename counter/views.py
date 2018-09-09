from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from collections import Counter

def home(request):
    print(request.META['REQUEST_METHOD'])
    return HttpResponse('yo')

def olivier(request):
    return render(request,'olivier.html', {'test':'incursion de python'}) #il faut séparer le

def compter(request):
    param = request.GET['parametre']
    splitparam= param.split()
    dictionnaire={}
    for word in splitparam:
        if word in dictionnaire :
            dictionnaire[word] += 1
            #on va rajouter 1 point à la clef deja existante
        else:
            #ajouter au dictionnaire une nouvelle entrée + 1 point
            dictionnaire[word] = 1
    print(dictionnaire)

    lensplit = len(splitparam)
    print(lensplit)
    return render(request,'compter.html',{'param1':param,'param2':lensplit,'param3':dictionnaire.items()})

def lol(request):
    a=1
    return render(request,'about.html',{'param8':a})
