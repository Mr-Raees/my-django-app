from django.contrib import admin

# Register your models here.
from .models import Chemistry,English,Physics,Maths,Graphics,IT,Chemistrylab,Sports,Languagelab,Physics2,Maths2,EVS,FEE,PSP,Workshop,FEElab,PSPlab,Physicslab,CSA,CProgram,CN1,DCF,Clab,SAlab,CHlab,ADlab,DCFlab,OOPS,CN2,ESRTOS,OOPSlab,NAlab,ESlab,CHlab2,Minorproject

#semester 1
admin.site.register(Chemistry)
admin.site.register(English)
admin.site.register(Physics)
admin.site.register(Maths)
admin.site.register(Graphics)
admin.site.register(IT)
admin.site.register(Chemistrylab)
admin.site.register(Sports)

#semester 2
sem2 = [Languagelab,Physics2,Maths2,EVS,FEE,PSP,Workshop,FEElab,PSPlab,Physicslab,]
for sub in sem2:
    admin.site.register(sub)

#semester 3
sem3 =[CSA,CProgram,CN1,DCF,Clab,SAlab,CHlab,ADlab,DCFlab]
for sub in sem3:
    admin.site.register(sub)

#semester 4
sem4 =[OOPS,CN2,ESRTOS,OOPSlab,NAlab,ESlab,CHlab2,Minorproject,]
for sub in sem4:
    admin.site.register(sub)
