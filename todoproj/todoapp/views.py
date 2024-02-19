from django.shortcuts import render,redirect
from .models import Name


# Create your views here.


def Home(req):
    # return render(req,'index.html')
    names=Name.objects.all()
   
    if req.method=="POST":
        
        name=req.POST.get('name','')
        mark=req.POST.get('mark','')
        
        date=req.POST.get('date','')
        image=req.FILES['image']
        
        todo=Name(name=name,mark=mark,date=date,image=image)
        todo.save()
    return render(req,'index.html',{"names":names})


def Update(req,id):
    names=Name.objects.get(id=id)
    if req.method=="POST":
        name=req.POST.get('name','')
        mark=req.POST.get('mark','')
        date=req.POST.get('date','')
        Name.objects.filter(id=id).update(name=name,mark=mark,date=date)
        return redirect("home")
    return render(req,'update.html',{"names":names})
    
    
  

    

def Delete(req,id):
    names=Name.objects.filter(id=id)
    
    names.delete()
    return redirect("home")



def View(req,id):
    names=Name.objects.all()
    if req.method=="POST":
        
        name=req.POST.get('name','')
        mark=req.POST.get('mark','')
        date=req.POST.get('date','')
        image=req.FILES['image']        
        todo=Name(name=name,mark=mark,date=date,image=image)
        todo.save()


    return render(req,'view.html',{"name ":names})