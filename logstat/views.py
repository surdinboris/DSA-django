from django.shortcuts import render, HttpResponseRedirect
from .models import Standalone, Attach, XmlAtt
from django.views.generic import UpdateView, CreateView
from .forms import Form_create
from logstat.filehandling import last_id, getatt, imgen, handle_uploaded_file
from logstat.xmlparse import report
import os

def home(request):
    standalone=Standalone.objects.all()

    return render(request,'home.html',{'standalone':standalone},)

class UpdStd(UpdateView):
    model = Standalone
    fields = ('source','origfilename',)
    template_name = 'updstd.html'

class CrtStd(CreateView):
    model = Standalone
    fields = ('source','serial','machine_type','descr',)
    template_name = 'updstd.html'

def getimg(request):
    if request.GET:
        print(request.GET.keys())
    return render(request,'home.html')

def create_std(request):
    if request.POST:
        form = Form_create(request.POST,request.FILES)
        attachs=request.FILES.getlist('attachs')
        attachsstr=[]
        for att in attachs:
            attachsstr.append(att.name)
        if form.is_valid():
            new_id = form.cleaned_data['new_id']
            new_std = Standalone(id=new_id, origfilename=attachsstr)
            new_std.save()
            for idx, val in enumerate(attachs):
                fn, ext = os.path.splitext(val.name)
                fs_file=handle_uploaded_file(ufile=val, y=int(new_id)*100+idx, ext=ext)
                if ext == '.jpg' or ext == '.jpeg':
                    print('jpg detected')
                    i = Attach.objects.get_or_create(id=last_id(Attach), std=new_std, descr=getatt('paragraph'), att=fs_file)[0]
                    i.thumbnl = imgen(y=int(new_id)*100+idx, resize=True, imgpath=fs_file)
                    i.save()

                if ext =='.xml':
                    print('xml detected', fs_file)
                    x = XmlAtt.objects.get_or_create(id=last_id(XmlAtt), std=new_std, xmlatt=fs_file, )[0]
                    print(fs_file)
                    x.xmlresult = report(fs_file,ident=new_id)
                    x.save()


            return HttpResponseRedirect('home.html')
        else:
            print('form is invalid')
            return render(request, 'updstd.html', {'form': form})
    else:
        form = Form_create()


        return render(request, 'updstd.html', {'form': form})