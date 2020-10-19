from django.shortcuts import render,redirect,get_object_or_404
from .forms import*
from .models import*

def read(request):
    dicio = {}
    dicio['Alunos']  = Aluno.objects.all()
    return render(request,'read.html',dicio)
def insert(request):
    dicio = {}
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_read')
    else:
        dicio['form'] = form
        return render(request,'insert.html',dicio)
def update(request,id):
    dicio = get_object_or_404(Aluno,pk=id)
    formulario = AlunoForm(request.POST or None, instance=dicio)

    if formulario.is_valid():
       formulario.save()
       return redirect('url_read')

    else:
        dicio={"form":formulario}
        return render(request,'insert.html',dicio)      
        
def delete(request,id):
    dicio = get_object_or_404(Aluno,pk=id)
    formulario = AlunoForm(request.POST or None, instance=dicio)

    if request.method=="POST":
        dicio.delete()
        return redirect('url_read')

    else:
        dicio = {"form":formulario,"delete":dicio}
        return render(request,'deleting.html',dicio)