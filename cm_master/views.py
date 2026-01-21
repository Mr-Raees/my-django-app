from django.shortcuts import render

# Create your views here.
from django.shortcuts import render 
from django.http import HttpResponse
from .models import Chemistry,English,Physics,Maths,Graphics,IT,Chemistrylab,Sports,Languagelab,Physics2,Maths2,EVS,FEE,PSP,Workshop,FEElab,PSPlab,Physicslab,CSA,CProgram,CN1,DCF,Clab,SAlab,CHlab,ADlab,DCFlab


def index(request):
    return render(request, 'index.html')

def s1(request):
    Chem = Chemistry.objects.all()
    Eng = English.objects.all()
    Phy = Physics.objects.all()
    Mat = Maths.objects.all()
    Gra = Graphics.objects.all()
    I = IT.objects.all()
    Chemlab = Chemistrylab.objects.all()
    Sport = Sports.objects.all()
    a={'Chem':Chem, 'Eng':Eng, 'Phy':Phy, 'Mat':Mat,'Gra':Gra, 'I':I, 'Chemlab':Chemlab, 'Sport':Sport}
    return render(request, 's1.html', a)

def s2(request):
    lan = Languagelab.objects.all()
    evs = EVS.objects.all()
    phy2 = Physics2.objects.all()
    phylab = Physicslab.objects.all()
    mat2 = Maths2.objects.all()
    fee = FEE.objects.all()
    psp = PSP.objects.all()
    feelab = FEElab.objects.all()
    psplab = PSPlab.objects.all()
    work = Workshop.objects.all()
    a = { 'lan':lan, 'evs':evs, 'phy2':phy2, 'mat2':mat2, 'fee':fee, 'psp':psp, 'feelab':feelab, 'psplab':psplab, 'work':work, 'phylab':phylab }
    return render(request, 's2.html', a)
def s3(request):
    csa = CSA.objects.all()
    cp = CProgram.objects.all()
    cn1 = CN1.objects.all()
    dcf = DCF.objects.all()
    cl = Clab.objects.all()
    sa = SAlab.objects.all()
    ch = CHlab.objects.all()
    dcflab = DCFlab.objects.all()
    ad = ADlab.objects.all()
    a ={'csa':csa, 'cp':cp, 'cn1':cn1, 'dcf':dcf, 'cl':cl, 'sa':sa, 'ch':ch, 'dcflab':dcflab, 'ad':ad}
    return render(request, 's3.html', a)
def s4(request):
    return render(request, 's4.html')
def s5(request):
    return render(request, 's5.html')
def s6(request):
    return render(request, 's6.html')

def base(request):
    return render(request, 'base.html')
