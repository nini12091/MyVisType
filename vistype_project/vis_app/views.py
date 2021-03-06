from django.shortcuts import render
from .models import Vis_test, Answer, Vis_Choice_Test, Choice
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
import time

# Create your views here.

def index(request):

    return render(request, 'index.html')

def test(request, test_id):
    if test_id <= 4:
        if request.method == "POST":
            termiate_time = time.time()
            result_time = int (termiate_time - request.session['start_time'])
            test = Vis_test.objects.get(pk=request.session['test_id'])
            answer = Answer()
            answer.answer_id = str(str(request.session['test_id']) + str(request.user))
            answer.user_id = request.user.username
            answer.test_id = test.test_id
            answer.v_type = test.v_type
            answer.v_task = test.v_task
            answer.answer = request.POST.get('answer','')

            if answer.answer == test.correct:
                answer.status = True
            else:
                answer.status = False
            
            answer.time = result_time
            answer.save()
            return HttpResponseRedirect(reverse('vis_app:test', args=(test_id,)))

        else:
            request.session['test_id'] = test_id
            start_time = time.time()
            request.session['start_time'] = start_time
            next_test_id = test_id + 1
            test_detail = get_object_or_404(Vis_test, pk=test_id)
            context = {'next_test_id':next_test_id, 'test_detail':test_detail}
            return render(request, 'test/test_100%.html', context)

    elif 4 < test_id <= 8:
        if request.method == "POST":
            termiate_time = time.time()
            result_time = int (termiate_time - request.session['start_time'])
            test = Vis_test.objects.get(pk=request.session['test_id'])
            answer = Answer()
            answer.answer_id = str(str(request.session['test_id']) + str(request.user))
            answer.user_id = request.user.username
            answer.test_id = test.test_id
            answer.v_type = test.v_type
            answer.v_task = test.v_task
            answer.answer = request.POST.get('answer','')

            if answer.answer == test.correct:
                answer.status = True
            else:
                answer.status = False
            
            answer.time = result_time
            answer.save()
            return HttpResponseRedirect(reverse('vis_app:test', args=(test_id,)))

        else:
            request.session['test_id'] = test_id
            start_time = time.time()
            request.session['start_time'] = start_time
            next_test_id = test_id + 1
            test_detail = get_object_or_404(Vis_test, pk=test_id)
            context = {'next_test_id':next_test_id, 'test_detail':test_detail}
            return render(request, 'test/test_bar.html', context)

    elif 8 < test_id <= 11:
        if request.method == "POST":
            termiate_time = time.time()
            result_time = int (termiate_time - request.session['start_time'])
            test = Vis_test.objects.get(pk=request.session['test_id'])
            answer = Answer()
            answer.answer_id = str(str(request.session['test_id']) + str(request.user))
            answer.user_id = request.user.username
            answer.test_id = test.test_id
            answer.v_type = test.v_type
            answer.v_task = test.v_task
            answer.answer = request.POST.get('answer','')

            if answer.answer == test.correct:
                answer.status = True
            else:
                answer.status = False
            
            answer.time = result_time
            answer.save()
            return HttpResponseRedirect(reverse('vis_app:test', args=(test_id,)))

        else:
            request.session['test_id'] = test_id
            start_time = time.time()
            request.session['start_time'] = start_time
            next_test_id = test_id + 1
            test_detail = get_object_or_404(Vis_test, pk=test_id)
            context = {'next_test_id':next_test_id, 'test_detail':test_detail}
            return render(request, 'test/test_pie.html', context)

    elif 11 < test_id <= 15:
        if request.method == "POST":
            termiate_time = time.time()
            result_time = int (termiate_time - request.session['start_time'])
            test = Vis_test.objects.get(pk=request.session['test_id'])
            answer = Answer()
            answer.answer_id = str(str(request.session['test_id']) + str(request.user))
            answer.user_id = request.user.username
            answer.test_id = test.test_id
            answer.v_type = test.v_type
            answer.v_task = test.v_task
            answer.answer = request.POST.get('answer','')

            if answer.answer == test.correct:
                answer.status = True
            else:
                answer.status = False
            
            answer.time = result_time
            answer.save()
            return HttpResponseRedirect(reverse('vis_app:test', args=(test_id,)))

        else:
            request.session['test_id'] = test_id
            start_time = time.time()
            request.session['start_time'] = start_time
            next_test_id = test_id + 1
            test_detail = get_object_or_404(Vis_test, pk=test_id)
            context = {'next_test_id':next_test_id, 'test_detail':test_detail}
            return render(request, 'test/test_stack_bar.html', context)

    elif 15 < test_id <= 17:
        if request.method == "POST":
            termiate_time = time.time()
            result_time = int (termiate_time - request.session['start_time'])
            test = Vis_test.objects.get(pk=request.session['test_id'])
            answer = Answer()
            answer.answer_id = str(str(request.session['test_id']) + str(request.user))
            answer.user_id = request.user.username
            answer.test_id = test.test_id
            answer.v_type = test.v_type
            answer.v_task = test.v_task
            answer.answer = request.POST.get('answer','')

            if answer.answer == test.correct:
                answer.status = True
            else:
                answer.status = False
            
            answer.time = result_time
            answer.save()
            return HttpResponseRedirect(reverse('vis_app:test', args=(test_id,)))

        else:
            request.session['test_id'] = test_id
            start_time = time.time()
            request.session['start_time'] = start_time
            next_test_id = test_id + 1
            test_detail = get_object_or_404(Vis_test, pk=test_id)
            context = {'next_test_id':next_test_id, 'test_detail':test_detail}
            return render(request, 'test/test_tree.html', context)

    elif 17 < test_id <= 19:
        if request.method == "POST":
            termiate_time = time.time()
            result_time = int (termiate_time - request.session['start_time'])
            test = Vis_test.objects.get(pk=request.session['test_id'])
            answer = Answer()
            answer.answer_id = str(str(request.session['test_id']) + str(request.user))
            answer.user_id = request.user.username
            answer.test_id = test.test_id
            answer.v_type = test.v_type
            answer.v_task = test.v_task
            answer.answer = request.POST.get('answer','')

            if answer.answer == test.correct:
                answer.status = True
            else:
                answer.status = False
            
            answer.time = result_time
            answer.save()
            
            if test_id == 19:
                return HttpResponseRedirect(reverse('vis_app:type', args=(1,)))
            else:
                return HttpResponseRedirect(reverse('vis_app:test', args=(test_id,)))

        else:
            request.session['test_id'] = test_id
            start_time = time.time()
            request.session['start_time'] = start_time
            next_test_id = test_id + 1
            test_detail = get_object_or_404(Vis_test, pk=test_id)
            context = {'next_test_id':next_test_id, 'test_detail':test_detail}
            return render(request, 'test/test_end.html', context)
    else:
       return HttpResponseRedirect(reverse('vis_app:type', args=(1,)))

def type(request, vis_id):
    if vis_id <= 4:
        if request.method == "POST":
            termiate_time = time.time()
            result_time = int (termiate_time - request.session['start_time'])
            vis_choice_test = Vis_Choice_Test.objects.get(pk=request.session['vis_id'])
            choice = Choice()
            choice.choice_id = str(str(request.session['vis_id']) + str(request.user))
            choice.user_id = request.user.username
            choice.set_number = vis_choice_test.set_number
            select = request.POST.get('option-list','')
            if select == 'option1':
                choice.choice_type = vis_choice_test.vis_1
            else:
                choice.choice_type = vis_choice_test.vis_2
            choice.v_task = vis_choice_test.v_task
            choice.v_reason = request.POST.get('reason','')
            choice.time = result_time
            choice.save()
            return HttpResponseRedirect(reverse('vis_app:type', args=(vis_id,)))
        else:
            request.session['vis_id'] = vis_id
            start_time = time.time()
            request.session['start_time'] = start_time
            next_vis_id = vis_id + 1
            type_detail = get_object_or_404(Vis_Choice_Test, pk=vis_id)
            context = {'next_vis_id':next_vis_id, 'type_detail':type_detail}
            return render(request, 'type/type_stack_bar.html', context)

    elif 4 < vis_id <= 8:
        if request.method == "POST":
            termiate_time = time.time()
            result_time = int (termiate_time - request.session['start_time'])
            vis_choice_test = Vis_Choice_Test.objects.get(pk=request.session['vis_id'])
            choice = Choice()
            choice.choice_id = str(str(request.session['vis_id']) + str(request.user))
            choice.user_id = request.user.username
            choice.set_number = vis_choice_test.set_number
            select = request.POST.get('option-list','')
            if select == 'option1':
                choice.choice_type = vis_choice_test.vis_1
            else:
                choice.choice_type = vis_choice_test.vis_2
            choice.v_task = vis_choice_test.v_task
            choice.v_reason = request.POST.get('reason','')
            choice.time = result_time
            choice.save()
            return HttpResponseRedirect(reverse('vis_app:type', args=(vis_id,)))
        else:
            request.session['vis_id'] = vis_id
            start_time = time.time()
            request.session['start_time'] = start_time
            next_vis_id = vis_id + 1
            type_detail = get_object_or_404(Vis_Choice_Test, pk=vis_id)
            context = {'next_vis_id':next_vis_id, 'type_detail':type_detail}
            return render(request, 'type/type_stack_pie.html', context)

    elif 8 < vis_id <= 13: 
        if request.method == "POST":
            termiate_time = time.time()
            result_time = int (termiate_time - request.session['start_time'])
            vis_choice_test = Vis_Choice_Test.objects.get(pk=request.session['vis_id'])
            choice = Choice()
            choice.choice_id = str(str(request.session['vis_id']) + str(request.user))
            choice.user_id = request.user.username
            choice.set_number = vis_choice_test.set_number
            select = request.POST.get('option-list','')
            if select == 'option1':
                choice.choice_type = vis_choice_test.vis_1
            else:
                choice.choice_type = vis_choice_test.vis_2
            choice.v_task = vis_choice_test.v_task
            choice.v_reason = request.POST.get('reason','')
            choice.time = result_time
            choice.save()
            if vis_id == 13:
                return HttpResponseRedirect(reverse('vis_app:finish'))
            else:
                return HttpResponseRedirect(reverse('vis_app:type', args=(vis_id,)))
        else:
            request.session['vis_id'] = vis_id
            start_time = time.time()
            request.session['start_time'] = start_time
            next_vis_id = vis_id + 1
            type_detail = get_object_or_404(Vis_Choice_Test, pk=vis_id)
            context = {'next_vis_id':next_vis_id, 'type_detail':type_detail}
            return render(request, 'type/type_stack_tree.html', context)

    else:
       return HttpResponseRedirect(reverse('vis_app:finish'))

def finish(request):

    return render(request, 'finish.html')