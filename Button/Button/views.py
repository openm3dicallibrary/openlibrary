from django.shortcuts import render 
import requests

##############################################################################################################################################
import bpy
##############################################################################################################################################



from django.template import loader
from django.http import HttpResponse

from Button.forms import tweezer_form
from Button.forms import splint_form
from Button.forms import clip_form


############################################################################################################################
# TWEEZER
############################################################################################################################
def responseform_tweezer(request):
 #if form is submitted
     if request.method == 'POST':
        myForm = tweezer_form(request.POST)

        if myForm.is_valid():
            x1 = myForm.cleaned_data['x1']
            x2 = myForm.cleaned_data['x2']
            
        ############################################################################################################################
            bpy.data.objects.remove(bpy.data.objects["Cube"], do_unlink=True)
            bpy.ops.import_mesh.stl(filepath="static\Button\DefaultThumbClamp.stl")
            myClipImport = bpy.data.objects['DefaultThumbClamp']
            myClipImport.scale = (x1,x2,1)
            bpy.ops.export_mesh.stl(filepath="static\Button\myExportSTL.stl")
        ############################################################################################################################

           # context = {
           # 'x1': x1,
           # 'x2': x2,
           # 'sum': x1+x2,
           # }

            template = loader.get_template('submitted.html')

            return HttpResponse(template.render(context, request))

     else:
         form = tweezer_form()

     return render(request, 'Tweezers.html', {'form':form})
############################################################################################################################
# SPLINTS
############################################################################################################################
def responseform_splint(request):
 #if form is submitted
     if request.method == 'POST':
        myForm = splint_form(request.POST)

        if myForm.is_valid():
            x1 = myForm.cleaned_data['x1']
            x2 = myForm.cleaned_data['x2']
            x3 = myForm.cleaned_data['x3']
            
        ############################################################################################################################
            bpy.data.objects.remove(bpy.data.objects["Cube"], do_unlink=True)
            bpy.ops.import_mesh.stl(filepath="static\Button\DefaultThumbClamp.stl")
            myClipImport = bpy.data.objects['DefaultThumbClamp']
            myClipImport.scale = (x1,x2,1)
            bpy.ops.export_mesh.stl(filepath="static\Button\myExportSTL.stl")
        ############################################################################################################################

           # context = {
           # 'x1': x1,
           # 'x2': x2,
           # 'sum': x1+x2,
           # }

            template = loader.get_template('submitted.html')

            return HttpResponse(template.render(context, request))

     else:
         form = splint_form()

     return render(request, 'Splints.html', {'form':form})
############################################################################################################################
# CLIPS
############################################################################################################################
def responseform_clips(request):
 #if form is submitted
     if request.method == 'POST':
        myForm = clip_form(request.POST)

        if myForm.is_valid():
            x1 = myForm.cleaned_data['x1']
          
            
        ############################################################################################################################
            bpy.data.objects.remove(bpy.data.objects["Cube"], do_unlink=True)
            bpy.ops.import_mesh.stl(filepath="static\Button\DefaultThumbClamp.stl")
            myClipImport = bpy.data.objects['DefaultThumbClamp']
            myClipImport.scale = (x1,x2,1)
            bpy.ops.export_mesh.stl(filepath="static\Button\myExportSTL.stl")
        ############################################################################################################################

           # context = {
           # 'x1': x1,
           # 'x2': x2,
           # 'sum': x1+x2,
           # }

            template = loader.get_template('submitted.html')

            return HttpResponse(template.render(context, request))

     else:
         form = clip_form()

     return render(request, 'Clips.html', {'form':form})    
    
def general(request):
    return render(request, 'GHC.html', {})


"""
def button(request):
    return render(request,'Tweezers.html')
def output(request):
    
    #data=requests.get("https://www.google.com")
    data="acb"
    print(data)
    data=data
    return render(request,'Tweezers.html',{'data' :data })
"""

