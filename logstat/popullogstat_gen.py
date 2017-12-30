import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
from faker import Factory
django.setup()
from logstat.models import Standalone, Source, Attach
#import numpy
from PIL import Image
from mysite import settings
from random import randint
#from PIL import ImageFilter

def getatt(att):
    return(getattr(fake, att)())

def last_std(modl):
    if modl.objects.last():
        l=modl.objects.last()
        l=l.id+1
    else:
        l = 0
    return(l)

def populate(y):
    d = Standalone.objects.get_or_create(id=last_std(Standalone), machine_type='77812', descr=getatt('paragraph'),
                                         serial=getatt('pyint'), source=Source.objects.get(id=1))[0]
    print(d.id)
    for t in range(5):
        a = Attach.objects.get_or_create(id=last_std(Attach), std=d, descr=getatt('paragraph'),att = imgen(y*10+t))[0]
        a.save()
    #print(a)

def imgen(y):
    #a = numpy.random.rand(930,930,3) * 255
    randval = randint(100, 1000)
    #im_out = Image.fromarray(a.astype('uint8')).convert('RGB').filter(ImageFilter.GaussianBlur(radius=randval)).filter(ImageFilter.CONTOUR)
    im_out=Image.new('RGB',(randval,randval),color=getatt('hex_color'))
    im_out.save(os.path.join(settings.MEDIA_ROOT,'out%000d.jpg' % y))
    return('out%000d.jpg' % y)


fake = Factory.create('ru')
if __name__ == "__main__":
    for y in range(100):
        populate(y)