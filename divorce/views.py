from django.shortcuts import render
from .models import Divorce
from django.views.generic import CreateView
from divorce.models import Divorce
from django.shortcuts import redirect
from .forms import *
# Create your views here.
def form_1 (request):
    if request.method=="POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            State_issued_divorce_id = form.cleaned_data['State_issued_divorce_id']
            # Date_of_birth = request.POST['Date_of_birth'] 
            # Nationality = request.POST['Nationality']
            # Maritial_status = request.POST['Maritial_status']
            # Highest_education = request.POST['Highest_education']
        
            divorce = Divorce(name=name, State_issued_divorce_id=State_issued_divorce_id,
            #  Date_of_birth=Date_of_birth,
            # Nationality=Nationality,
            # Maritial_status=Maritial_status,
            # Highest_education=Highest_education 
            
            )

            divorce.save()
            request.session['formid']=divorce.sno
            return redirect('divorce:form_2')
        else:
            form = ApplicationForm()
            return render(request, "form_1.html",{'form':form,'error':'Enter valid captcha'})
    else:
        form = ApplicationForm()
        return render(request, "form_1.html",{'form':form})

def form_2(request):
    if request.method=="POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            Date_of_birth = request.POST['Date_of_birth']
            Nationality = request.POST['Nationality']
            formid = request.session.get('formid')
            Divorce.objects.filter(sno=formid).update(Date_of_birth=Date_of_birth,Nationality=Nationality)

            return redirect('divorce:form_3')
        else:
            form = ApplicatioForm()
            return render(request,'form_2.html',{'form':form,'error':'Enter valid captcha'})
    else:
        form = ApplicationForm()
        return  render(request,'form_2.html',{'form':form})
def form_3(request):
    if request.method=="POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            Maritial_status = request.POST['Maritial_status']
            Highest_education = request.POST['Highest_education']
            formid = request.session.get('formid')
            Divorce.objects.filter(sno=formid).update(Maritial_status=Maritial_status,Highest_education=Highest_education)
            return redirect('divorce:form_1')
        else:
            form = ApplicationForm()
            return render(request,'form_3.html',{'form':form,'error':'Enter valdi catpcha'})

    else:
        form = ApplicationForm()
        return render(request,'form_3.html',{'form':form})

# def form_2 (request):
#     return render(request, "form_2.html")
# def form_3 (request):
#     return render(request, "form_3.html")


# class Form_1(CreateView):
#     model = Divorce 
#     template_name = "form_1.html" 
#     fields = "name", "State_issued_divorce_id"