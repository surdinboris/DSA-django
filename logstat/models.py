from django.db import models
import django.utils.timezone

# Create your models here.
class Source(models.Model):
    title=models.CharField(max_length=100,default=None,null=True)
    descr=models.CharField(max_length=300,default=None,null=True)
    def __str__(self):
        return self.descr

class Standalone(models.Model):
    source=models.ForeignKey(Source, null=True)
    date=models.DateField(null=False, default= django.utils.timezone.now())
    origfilename=models.CharField(max_length=500, default=None, null=True)
    descr=models.CharField(max_length=300, default=None, null=True)

    def __str__(self):
        return self.descr

    def serr(self):
        return self.serial

    def getattch(self):
        return Attach.objects.filter(std=self.id)

    def getxmlattch(self):
        return XmlAtt.objects.filter(std=self.id)


class Attach(models.Model):
    att=models.FileField(null=True)
    thumbnl=models.FileField(null=True)
    descr=models.CharField(max_length=300,default=None,null=True)
    std = models.ForeignKey(Standalone, null=False)
    def __str__(self):
        url=self.att.url
        return url

class XmlAtt(models.Model):
    xmlatt = models.FileField(null=True)
    xml_added_date=models.DateField(null=False, default= django.utils.timezone.now())
    std = models.ForeignKey(Standalone, null=False)
    xmlresult = models.FileField(null=True)
    def __str__(self):
        url = self.xmlatt.url
        return url