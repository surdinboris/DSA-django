from django.contrib import admin
from .models import Standalone, Source, Attach,XmlAtt
admin.site.register(Standalone)
admin.site.register(Source)
admin.site.register(Attach)
admin.site.register(XmlAtt)

# Register your models here.
