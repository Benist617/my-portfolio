from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . forms import CreatePollForm
from . models import Poll


def home(request):
    all_items = Poll.objects.all().order_by("id")
    context = {'all_items': all_items}
    return render(request, 'pollapp/home.html', context)


def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pollapp')
    else:
        form = CreatePollForm()
    context = {
        'form': form
    }
    return render(request, 'pollapp/create.html', context)


def vote(request, poll_id):
    pollobject = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'result_option1':
            pollobject.option_one_count += 1
        elif selected_option == 'result_option2':
            pollobject.option_two_count += 1
        elif selected_option == 'result_option3':
            pollobject.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')
        pollobject.save()
        return redirect('results', pollobject.id)

    context = {
        'poll': pollobject
    }
    return render(request, 'pollapp/vote.html', context)


def results(request, poll_id):
    pollobject = Poll.objects.get(pk=poll_id)

    context = {
        'poll': pollobject
    }
    return render(request, 'pollapp/results.html', context)




