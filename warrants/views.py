from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def Warrant(request):

    if request.method == "GET":
        return JsonResponse({"status" : "ok"})
    
    elif request.method == "POST":
        return JsonResponse({"status" : "ok"})
    
    elif request.method == "PATCH":
        return JsonResponse({"status" : "ok"})
    
    else:
        return JsonResponse({"Error" : "Request method not allowed"}, status=405)

def Crime(request):

    if request.method == "GET":
        return JsonResponse({"status" : "ok"})
    
    elif request.method == "POST":
        return JsonResponse({"status" : "ok"})
    
    elif request.method == "PATCH":
        return JsonResponse({"status" : "ok"})
    
    else:
        return JsonResponse({"Error" : "Request method not allowed"}, status=405)
    

def Citizen(request):
    if request.method == "GET":
        return JsonResponse({"status" : "ok"})
    
    elif request.method == "POST":
        return JsonResponse({"status" : "ok"})
    
    elif request.method == "PATCH":
        return JsonResponse({"status" : "ok"})
    
    else:
        return JsonResponse({"Error" : "Request method not allowed"}, status=405)
    

def Vehicle(request):
    if request.method == "GET":
        return JsonResponse({"status" : "ok"})
    
    elif request.method == "POST":
        return JsonResponse({"status" : "ok"})
    
    elif request.method == "PATCH":
        return JsonResponse({"status" : "ok"})
    
    else:
        return JsonResponse({"Error" : "Request method not allowed"}, status=405)


