from django.db import models
from django.contrib import admin

# Create your models here.
"""
 Model for the Topic i.e Name of the topic
"""
class Topic(models.Model):
    topic_name = models.CharField(max_length=200)

    # This is to display the Topic name in admin panel
    def __str__(self):
        return self.topic_name
    """
    Static method which wil be used in the views.py to fetch from the database
    """
    @staticmethod
    def get_topic():
        return Topic.objects.all()
    @staticmethod
    def get_topicName_Byid(id):
        return Topic.objects.get(id=id)
    @staticmethod
    def getId_byname(name):
        return Topic.objects.get(topic_name=name)






"""
 Model for the Sub-Topic i.e Name of the stub-topic
"""
class SubTopic(models.Model):
    topic_name = models.ForeignKey('Topic', on_delete=models.CASCADE)
    sub_topic_name = models.CharField(max_length=200)

    # This is to display the Topic name and sub topic  in admin panel
    def __str__(self):
        return self.sub_topic_name
    """
    Static method which wil be used in the views.py to fetch from the database
    """
    @staticmethod
    def get_subtopic():
        return SubTopic.objects.all()





"""
 Model for the language i.e Language of Code
"""
class Language(models.Model):
    Language = models.CharField(max_length=200)
    

    def __str__(self):
        return self.Language
    """
    Static method which wil be used in the views.py to fetch from the database
    """
    @staticmethod
    def get_languages():
        return Language.objects.all()

    @staticmethod
    def getid_byname(name):
        return Language.objects.get(Language=name)





"""
 Model for the Content i.e code content
"""

class Code_content(models.Model):
    topic_name = models.ForeignKey('Topic',on_delete=models.CASCADE)
    sub_topic_name = models.CharField(max_length=200)
    Language=models.ForeignKey("Language", on_delete=models.CASCADE)
    code = models.TextField()

    """
    Static method which wil be used in the views.py to fetch from the database
    """
    @staticmethod
    def get_contentBy_topic(topic_name_id):
       return Code_content.objects.filter(topic_name_id=topic_name_id)
       

"""
 Model for the Compilers i.e Online Editors
"""
class compiler(models.Model):
    topic_name = models.ForeignKey('Topic',on_delete=models.CASCADE)
    compiler = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=200)
    documentation = models.ForeignKey("Documentation" ,on_delete=models.CASCADE,default="1")

    

    """
    Static method which wil be used in the views.py to fetch from the database
    """
    @staticmethod
    def get_compilerBy_topic_id(topic_name_id):
       return compiler.objects.get(topic_name_id=topic_name_id)

    @staticmethod
    def get_compilers():
        return compiler.objects.all()
       
""" 
Model For the Dashboard Content
"""
class Dashboard_menu(models.Model):

    colors = [
    ( 'card-header-warning','Warning'),
    ( 'card-header-success','Success'),
    ( 'card-header-info','Info'),
    ( 'card-header-secondary','Secondary'),
    ( 'card-header-white','White'),
]


    topic_name = models.ForeignKey('Topic',on_delete=models.CASCADE)
    images = models.ImageField(upload_to="uploads/languages_logo")
    back_color = models.CharField(max_length=49, choices=colors)

    @staticmethod
    def getAll_dashInfo():
        return Dashboard_menu.objects.all()

class Documentation(models.Model):
     topic_name = models.ForeignKey('Topic',on_delete=models.CASCADE)
     link = models.CharField(max_length=200)
    
     def __str__(self):
        return str(self.topic_name)

     @staticmethod
     def getall_docu():
         return Documentation.objects.all()


""" ------------------------------------------------------------------------------------------------------------- """

class books_module (models.Model):
    topic_name = models.ForeignKey('Topic',on_delete=models.CASCADE)
    book_images = models.ImageField(upload_to="uploads/books_logo")
    book_name = models.CharField(max_length=200)
    book_link = models.CharField(max_length=200)

    @staticmethod
    def getAll_books():
        return books_module.objects.all()    


    @staticmethod
    def getbook_byId(book_id):
        return books_module.objects.get(id=book_id)

    def __str__(self):

        return str(self.topic_name)