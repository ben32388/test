from django.shortcuts import render, redirect, get_object_or_404
from .models import Space
from .models import Planargraph
from .forms import SpaceForm
from .forms import PlanargraphForm
from django.contrib import messages

from .forms import DeleteConfirmForm

def space_show(request,pk):
    space = Space.objects.filter(planargraph_id=pk)

    form = SpaceForm(request.POST or None)
    pk=pk
    planargraph = Planargraph.objects.get(planargraphId=pk)
    if form.is_valid():
        form.save()
    return render(request,'planargraphs/space_show.html', {
        'spaces' : space,'form' : form, 'pk' :pk ,'planargraphs' : planargraph
    })

def space_edit(request,spk,pk):
    space = get_object_or_404(Space, pk=spk,planargraph=pk)
    form = SpaceForm(request.POST or None,instance=space)
    if form.is_valid():
        form.save()
        messages.success(request,'編輯成功')
        return redirect('../../')
    return render(request,'planargraphs/space_edit.html', {
        'spaces' : space,'form' : form,
    })

def space_delete(request,spk,pk):
    space = get_object_or_404(Space, pk=spk,planargraph=pk)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid():
        space.delete()
        messages.success(request,'刪除成功')
        return redirect('../../')
    return render(request,'planargraphs/space_delete.html', {
        'spaces' : space,'form' : form,
    })

def space_add(request,pk):
    space = Space.objects.filter(planargraph_id=pk)
    form = SpaceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('../')
        # space = form.save(commit=False)
        # space.image = 'aaaaa'
        # space.jj = db,get*
        # space.save()
    return render(request,'planargraphs/space_add.html', {
        'spaces' : space,
        'form' : form,
        'images': Space.IMAGE_CHOICES,
    })

def planargraph_show(request):
    planargraph = Planargraph.objects.all()
    form = PlanargraphForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'planargraphs/planargraph_show.html', {
        'planargraphs' : planargraph, 'form' : form,
    })

def planargraph_edit(request,pk):
    planargraph = get_object_or_404(Planargraph, pk=pk)
    form = PlanargraphForm(request.POST or None, instance=planargraph)
    if form.is_valid():
        form.save()
        messages.success(request,'編輯成功')
        return redirect('/planargraphs/planargraph_show/')
    return render(request,'planargraphs/planargraph_edit.html', {
        'planargraphs' : planargraph, 'form' : form,
    })

def planargraph_delete(request,pk):
    planargraph = get_object_or_404(Planargraph, pk=pk)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid():
        planargraph.delete()
        messages.success(request,'刪除成功')
        return redirect('/planargraphs/planargraph_show/')
    return render(request,'planargraphs/planargraph_delete.html', {
        'planargraphs' : planargraph, 'form' : form,
    })