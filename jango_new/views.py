from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={ 
        "title":"home page",
        "mydata" : "welcome to Microlearnig",
        "clist": ["Java","python","PHP"],
        "numbers":[10,20,30,40,50],
        "student_details":[
            {"name":"Parag nemade","contact": 9049170354},
            {"name":"Akash Irawade","contact": 8275708710}
        ]


    }
    return render(request, 'index.html',data)


def aboutus(request):
    return HttpResponse('welcome to Microlearning')

def course(request):
    return HttpResponse('Java')

def coursedetails(request,courseid):
    return HttpResponse(courseid)