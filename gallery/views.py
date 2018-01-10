# from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Group, Image


def index(request):
    all_groups = Group.objects.all()
    return render(request, 'gallery/index.html', {'all_groups': all_groups})


def info(request, group_id):
    # try:
    #     group = Group.objects.get(pk=group_id)
    # except Group.DoesNotExist:
    #     raise Http404("No Groups Exist")
    group = get_object_or_404(Group, pk=group_id)
    return render(request, 'gallery/info.html', {'group': group})


def fave(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    try:
        selected = group.image_set.get(pk=request.POST['image'])
    except (KeyError, Image.DoesNotExist):
        return render(request, 'gallery/info.html', {'group': group, 'error_msg': "no image selected"})
    else:
        selected.is_fave = True
        selected.save()
        return render(request, 'gallery/info.html', {'group': group})
