import os
from os import listdir
from os.path import isfile, join
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
from faker import Factory
django.setup()
from logstat.models import Standalone, Source, Attach
from PIL import Image
from mysite import settings
from random import randint, choice
from django.core.exceptions import  ObjectDoesNotExist

mypath="/Images/"

def getatt(att):
    return(getattr(fake, att)())

def last_id(modl):
    try:
        l=modl.objects.last()
        l=l.id+1
    except (ObjectDoesNotExist, AttributeError):
        l = 0
    return(l)

def populate(y):
    d = Standalone.objects.get_or_create(id=last_id(Standalone), machine_type='77812', descr=getatt('paragraph'),
                                         serial=getatt('pyint'), source=Source.objects.get(id=1))[0]
    print(d.id)
    for t in range(randint(0, 10)):
        imgnum=y*10+t
        if t:
            a = Attach.objects.get_or_create(id=last_id(Attach), std=d, descr=getatt('paragraph'),att = imgen(imgnum))[0]
            a.thumbnl = imgen(imgnum, resize=True, imgpath=a.att.path)
            a.save()


def imgen(y,resize=False,imgpath=''):
   if resize==True:
       imm_out = Image.open(os.path.join(settings.MEDIA_ROOT,imgpath))
       try:
           imm_out.thumbnail((50,50), resample=0)
           imm_out.save(os.path.join(settings.MEDIA_ROOT, 'mout%000d.jpg' % y))
       except OSError:
            return('notfound.png')
       else:
            return ('mout%000d.jpg' % y)
   else:
    randval = randint(100, 1000)
    onlyfiles = [join(mypath,f) for f in listdir(mypath) if isfile(join(mypath, f))]
    im_out=Image.open(choice(onlyfiles))
    im_out.save(os.path.join(settings.MEDIA_ROOT,'out%000d.jpg' % y))
    return('out%000d.jpg' % y)


fake = Factory.create('ru')
if __name__ == "__main__":
    for y in range(30):
        populate(y)

def handle_uploaded_file(ufile, y,ext):
    filepath=os.path.join(settings.MEDIA_ROOT, str('out%000d' % y)+ext)

    with open(filepath, 'wb+') as destination:
        for chunk in ufile.chunks():
            destination.write(chunk)

    return (str('out%000d' % y)+ext)