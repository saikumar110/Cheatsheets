from django.contrib import admin
from cheats_app.models import Topic,SubTopic,Code_content,Language,compiler,Dashboard_menu,Documentation,books_module
# Register your models here.
"""
For the Admin Topic Model Display Content
"""
class Admintopic(admin.ModelAdmin):
    list_display=['topic_name']

"""
For the Admin Sub-Topic Model Display Content
"""
class AdminSub_topic(admin.ModelAdmin):
    list_display=['topic_name','sub_topic_name']


"""
For the Admin Language Model Display Content
"""
class AdminLanguage(admin.ModelAdmin):
    list_display=['Language']

"""
For the Admin Sub-Topic Model Display Content
"""
class AdminCode_content(admin.ModelAdmin):
    list_display=['topic_name','sub_topic_name','Language']


"""
For the Admin Sub-Topic Model Display Content
"""
class AdminCompilers(admin.ModelAdmin):
    list_display=['topic_name','editor_name']

class AdminLogo_Info(admin.ModelAdmin):
    list_display=['topic_name','images','back_color']
class AdminDoc(admin.ModelAdmin):
    list_display=['topic_name','link']
"""
Registering the display classes with models {(model_name,class_name)}
"""
admin.site.register(Topic,Admintopic)
admin.site.register(SubTopic,AdminSub_topic)
admin.site.register(Code_content,AdminCode_content)
admin.site.register(Language,AdminLanguage)
admin.site.register(compiler,AdminCompilers)
admin.site.register(Dashboard_menu,AdminLogo_Info)
admin.site.register(Documentation,AdminDoc)
admin.site.register(books_module)


