from django.shortcuts import render
from .models import Vis_test, Answer, Vis_Choice_Test, Choice
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
import timeit

# Create your views here.

def index(request):

    return render(request, 'index.html')

def test(request, test_id):
    if test_id <= 4:
        if request.method == "POST":
            termiate_time = timeit.default_timer()
            test = Vis_test.objects.get(pk=request.session['test_id'])
            return HttpResponseRedirect(reverse('vis_app:test', args=(test_id,)))

        else:
            request.session['test_id'] = test_id
            start_time = timeit.default_timer()
            next_test_id = test_id + 1
            test_detail = get_object_or_404(Vis_test, pk=test_id)
            context = {'next_test_id':next_test_id, 'test_detail':test_detail}
            return render(request, 'test/test_100%.html', context)

    elif 4 < test_id <= 8:
        if request.method == "POST":
            termiate_time = timeit.default_timer()
            test = Vis_test.objects.get(pk=request.session['test_id'])
            return HttpResponseRedirect(reverse('vis_app:test', args=(test_id,)))

        else:
            request.session['test_id'] = test_id
            start_time = timeit.default_timer()
            next_test_id = test_id + 1
            test_detail = get_object_or_404(Vis_test, pk=test_id)
            context = {'next_test_id':next_test_id, 'test_detail':test_detail}
            return render(request, 'test/test_bar.html', context)

    elif 8 < test_id <= 11:
        if request.method == "POST":
            termiate_time = timeit.default_timer()
            test = Vis_test.objects.get(pk=request.session['test_id'])
            return HttpResponseRedirect(reverse('vis_app:test', args=(test_id,)))

        else:
            request.session['test_id'] = test_id
            start_time = timeit.default_timer()
            next_test_id = test_id + 1
            test_detail = get_object_or_404(Vis_test, pk=test_id)
            context = {'next_test_id':next_test_id, 'test_detail':test_detail}
            return render(request, 'test/test_pie.html', context)

    elif 11 < test_id <= 15:
        if request.method == "POST":
            termiate_time = timeit.default_timer()
            test = Vis_test.objects.get(pk=request.session['test_id'])
            return HttpResponseRedirect(reverse('vis_app:test', args=(test_id,)))

        else:
            request.session['test_id'] = test_id
            start_time = timeit.default_timer()
            next_test_id = test_id + 1
            test_detail = get_object_or_404(Vis_test, pk=test_id)
            context = {'next_test_id':next_test_id, 'test_detail':test_detail}
            return render(request, 'test/test_stack_bar.html', context)

    elif 15 < test_id <= 18:
        if request.method == "POST":
            termiate_time = timeit.default_timer()
            test = Vis_test.objects.get(pk=request.session['test_id'])
            return HttpResponseRedirect(reverse('vis_app:test', args=(test_id,)))

        else:
            request.session['test_id'] = test_id
            start_time = timeit.default_timer()
            next_test_id = test_id + 1
            test_detail = get_object_or_404(Vis_test, pk=test_id)
            context = {'next_test_id':next_test_id, 'test_detail':test_detail}
            return render(request, 'test/test_tree.html', context)

    else:
        return render(request, "index.html")