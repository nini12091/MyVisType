from django.contrib import admin
from .models import Vis_test,Answer,Choice, Vis_Choice_Test

# Register your models here.
admin.site.register(Vis_test)
admin.site.register(Answer)
admin.site.register(Vis_Choice_Test)
admin.site.register(Choice)