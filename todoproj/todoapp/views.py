from django.shortcuts import render,redirect
from .models import Name
from .forms import TodoForm

# Create your views here.


def Home(req):
    # return render(req,'index.html')
    names=Name.objects.all()
    print(req.method)
    if req.method=="POST":
        
        name=req.POST.get('name','')
        
        date=req.POST.get('date','')
        img=req.FILES['image']
        
        todo=Name(name=name,date=date,image=img)
        todo.save()
    return render(req,'index.html',{"name":names})


def Update(req,id):
    names=Name.objects.get(id=id)
    # if req.method=="POST":
    #    task=req.POST.get('task','')
    #    priority=req.POST.get('priority','')
    #    Task.objects.filter(id=id).update(task=task,priority=priority)
    #    return redirect("home")
    
    
    
    f=TodoForm(req.POST or None,instance=names)
    if f.is_valid():
        f.save()
        return redirect("home")
        
    return render(req,'formUpdate.html',{"name":names,'f':f})

    

def Delete(req,id):
    names=Name.objects.get(id=id)
    if req.method=="POST":
       name=req.POST.get('name','')
       priority=req.POST.get('prority','')
       Name.objects.filter(id=id).delete()
       
       return redirect("home")
    return render(req,'delete.html',{"name":names})