from django.http.response import HttpResponse
from django.shortcuts import render

import random

def home(request):

   characters = list("abcdefghijklmnopqrstuvwxyz")

   if request.GET.get("uppercase"):
      characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

   if request.GET.get('lowercase'):
      characters.extend(characters)
   
   if request.GET.get('digit'):
      characters.extend(list('1234567890'))
   
   if request.GET.get('specialcharacters'):
      characters.extend(list("@#$%^&*"))


   password = ''
   length = int(request.GET.get('length', 8 ))
   for i in range(length):
      password += random.choice(characters)

   

   return render(request,"generate_password/home.html", {'password': password})


def about(request):
   return render(request, "generate_password/about.html")
