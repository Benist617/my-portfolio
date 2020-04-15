from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from todoapp.models import ToDo


def home(request):
    all_items = ToDo.objects.all().order_by("-added_date")
    return render(request, 'todoapp/index.html', {"all_items": all_items})


@csrf_exempt
def add_item(request):
    created_obj = ToDo.objects.create(added_date=timezone.now(), text=request.POST['content'])
    print(created_obj)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@csrf_exempt
def delete_item(request, item_id):
    ToDo.objects.get(id=item_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@csrf_exempt
def delete_all(request):
    ToDo.objects.all().delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


