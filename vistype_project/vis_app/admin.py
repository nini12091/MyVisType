from django.contrib import admin
from .models import Vis_test,Answer,Choice, Vis_Choice_Test,User_info,Vis_prefer

# Register your models here.
admin.site.register(Vis_test)
admin.site.register(Answer)
admin.site.register(Vis_Choice_Test)
admin.site.register(Choice)
admin.site.register(User_info)
admin.site.register(Vis_prefer)