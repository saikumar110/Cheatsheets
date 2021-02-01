from django.shortcuts import render,get_object_or_404,redirect
from urllib import request
from cheats_app.models import Topic,SubTopic,Language,Code_content,compiler,Dashboard_menu,Documentation,books_module
from django.http import HttpResponse,Http404



# Create your views here.
"""
Functions for Landing/Dashboard and Content templates
"""
def homepage(request):
    title="Dashboard"
    dash_data = Dashboard_menu.getAll_dashInfo()
    editors = compiler.get_compilers()
    documentations = Documentation.getall_docu()

    data={
        "tab_title":title,
         "datas":dash_data,
         "editors":editors,
         "documentations":documentations,
   }


    return render(request ,"dashboard.html", data)



def data_content(request ,id):
   
    #print(id)

    title=Topic.get_topicName_Byid(id)
    code = Code_content.get_contentBy_topic(id)
    
    """
    Creating the dictonary for sending data to template
    """
    data={
        "tab_title":title,
        "code_contents":code,
        #"compiler": editor ,
     }
    return render(request,"code.html",data)
    #return render(request,"Editor.html")

def content_edit(request,id):
    print(id)

    title=Topic.get_topicName_Byid(id)
    editor = compiler.get_compilerBy_topic_id(id)
    topic = Topic.get_topic()
    language = Language.get_languages()
    #print(editor)

    data={
        "title":title,
        "editor":editor,
        "topics":topic,
        "languages":language,

    }
   


    return render(request,"Editor.html",data)
    


def Update_content(request):
    if request.method=="POST":
        code_con = request.POST.get('program_content')
        dropdwn_lang = request.POST.get('drop_language')
        dropdwn_topic = request.POST.get('drop_topic')
        subtopic = request.POST.get("sub_topic")

        ids = Topic.getId_byname(dropdwn_topic)
        lang_id =Language.getid_byname(dropdwn_lang)
        #print(ids.id)
        #print(dropdwn_lang)
        #print(lang_id)

        #print(dropdwn_topic)
        print(subtopic)

        content = Code_content(
             topic_name_id = ids.id,
             sub_topic_name=subtopic,
             Language_id = lang_id.id,
             code=code_con,
        )
        content.save()

        return redirect('homepage')
    else:
        return redirect("content_edit")




def books_view(request):
    title="Books"
    dash_data = books_module.getAll_books()

    data={
         "tab_title":title,
         "datas":dash_data,
    }
    return render(request,"books_dashboard.html",data)


def read_book(request,id):
    book = books_module.getbook_byId(id)
    data={
        "book":book,
    }
    return render (request,"books.html",data)
