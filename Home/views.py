from django.shortcuts import render
import string
import random

# Create your views here.
def home(request):
    ucase= string.ascii_uppercase
    lcase=string.ascii_lowercase
    num = string.digits
    scas = string.punctuation
    password = ''
    char=[]
    if request.method == 'GET':
        length = request.GET.get('length')
        if request.GET.get('Ucase'):
            char.extend(ucase)
        if request.GET.get('Lcase'):
            char.extend(lcase)
        if request.GET.get('number'):
            char.extend(num)
        if request.GET.get('Schar'):
            char.extend(scas)

        int_len = int(length)

        print(length)
        
        for i in range(int_len):
           password += random.choice(char)

        context= {'pass': password}
        
        print(password)

    

    return render(request, "index.html",context)