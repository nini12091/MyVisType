import re
from django.shortcuts import render
from .models import User_info, Vis_test, Answer, Vis_Choice_Test, Choice, Vis_prefer
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
import time
import logging
import csv

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

    elif 8 < test_id <= 12:
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

    elif 12 < test_id <= 16:
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

    elif 16 < test_id <= 19:
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

    elif 19 < test_id <= 21:
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
            
            if test_id == 21:
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
    if vis_id <= 1:
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
            return HttpResponseRedirect(reverse('vis_app:prefer', args=(1,)))
        else:
            request.session['vis_id'] = vis_id
            vis_id
            start_time = time.time()
            request.session['start_time'] = start_time
            type_detail = get_object_or_404(Vis_Choice_Test, pk=vis_id)
            context = {'vis_id':vis_id, 'type_detail':type_detail}
            return render(request, 'type/type_stack_bar.html', context)

    elif 1 < vis_id <= 4:
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
            request.session['prefer_id'] = request.session['prefer_id'] + 1
            return HttpResponseRedirect(reverse('vis_app:prefer', args=(request.session['prefer_id'],)))

        else:
            request.session['vis_id'] = vis_id
            vis_id
            start_time = time.time()
            request.session['start_time'] = start_time
            type_detail = get_object_or_404(Vis_Choice_Test, pk=vis_id)
            context = {'vis_id':vis_id, 'type_detail':type_detail}
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
            request.session['prefer_id'] = request.session['prefer_id'] + 1
            return HttpResponseRedirect(reverse('vis_app:prefer', args=(request.session['prefer_id'],)))
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
            request.session['prefer_id'] = request.session['prefer_id'] + 1
            return HttpResponseRedirect(reverse('vis_app:prefer', args=(request.session['prefer_id'],)))
        else:
            request.session['vis_id'] = vis_id
            start_time = time.time()
            request.session['start_time'] = start_time
            next_vis_id = vis_id + 1
            type_detail = get_object_or_404(Vis_Choice_Test, pk=vis_id)
            context = {'next_vis_id':next_vis_id, 'type_detail':type_detail}
            return render(request, 'type/type_stack_tree.html', context)

    else:
       return HttpResponseRedirect(reverse('vis_app:user_info'))

def prefer(request, prefer_id):
        if prefer_id == 1 or prefer_id == 4 or prefer_id == 7 or prefer_id == 10:
            if request.method == "POST":
                vis_choice_test = Vis_Choice_Test.objects.get(pk=request.session['vis_id'])
                vis_prefer = Vis_prefer()
                vis_prefer.vis_prefer_id = str(str(prefer_id) + str(request.user))
                vis_prefer.prefer_id = prefer_id
                vis_prefer.user_id = request.user.username
                vis_prefer.prefer = request.POST.get('option-list','')
                vis_prefer.v_task = vis_choice_test.v_task
                vis_prefer.vis_type = vis_choice_test.vis_1
                vis_prefer.save()
                request.session['prefer_id'] = prefer_id + 1
            
                return HttpResponseRedirect(reverse('vis_app:prefer', args=(request.session['prefer_id'],)))

            else:
                request.session['prefer_id'] = prefer_id - 1
                next_prefer_id = request.session['prefer_id'] + 1
                type_detail = get_object_or_404(Vis_Choice_Test, pk=request.session['vis_id'])
                context = {'next_prefer_id':next_prefer_id, 'type_detail':type_detail}
                return render(request, 'prefer_stacked.html', context)

        elif prefer_id == 2 or prefer_id == 5 or prefer_id == 8 or prefer_id == 11:
            if request.method == "POST":
                vis_choice_test = Vis_Choice_Test.objects.get(pk=request.session['vis_id'])
                vis_prefer = Vis_prefer()
                vis_prefer.vis_prefer_id = str(str(prefer_id) + str(request.user))
                vis_prefer.prefer_id = prefer_id
                vis_prefer.user_id = request.user.username
                vis_prefer.prefer = request.POST.get('option-list','')
                vis_prefer.v_task = vis_choice_test.v_task
                vis_prefer.vis_type = vis_choice_test.vis_2
                vis_prefer.save()
                request.session['prefer_id'] = prefer_id + 1
            
                return HttpResponseRedirect(reverse('vis_app:prefer', args=(request.session['prefer_id'],)))

            else:
                request.session['prefer_id'] = prefer_id - 1
                next_prefer_id = request.session['prefer_id'] + 1
                type_detail = get_object_or_404(Vis_Choice_Test, pk=request.session['vis_id'])
                context = {'next_prefer_id':next_prefer_id, 'type_detail':type_detail}
                return render(request, 'prefer_multi_bar.html', context)

        elif prefer_id == 13 or prefer_id == 16 or prefer_id == 19 or prefer_id == 22:
            if request.method == "POST":
                vis_choice_test = Vis_Choice_Test.objects.get(pk=request.session['vis_id'])
                vis_prefer = Vis_prefer()
                vis_prefer.vis_prefer_id = str(str(prefer_id) + str(request.user))
                vis_prefer.prefer_id = prefer_id
                vis_prefer.user_id = request.user.username
                vis_prefer.prefer = request.POST.get('option-list','')
                vis_prefer.v_task = vis_choice_test.v_task
                vis_prefer.vis_type = vis_choice_test.vis_1
                vis_prefer.save()

                request.session['prefer_id'] = prefer_id + 1 
            
                return HttpResponseRedirect(reverse('vis_app:prefer', args=(request.session['prefer_id'],)))

            else:
                request.session['prefer_id'] = prefer_id - 1
                next_prefer_id = request.session['prefer_id'] + 1
                type_detail = get_object_or_404(Vis_Choice_Test, pk=request.session['vis_id'])
                context = {'next_prefer_id':next_prefer_id, 'type_detail':type_detail}
                return render(request, 'prefer_stacked_100.html', context)

        elif prefer_id == 14 or prefer_id == 17 or prefer_id == 20 or prefer_id == 23:
            if request.method == "POST":
                vis_choice_test = Vis_Choice_Test.objects.get(pk=request.session['vis_id'])
                vis_prefer = Vis_prefer()
                vis_prefer.vis_prefer_id = str(str(prefer_id) + str(request.user))
                vis_prefer.prefer_id = prefer_id
                vis_prefer.user_id = request.user.username
                vis_prefer.prefer = request.POST.get('option-list','')
                vis_prefer.v_task = vis_choice_test.v_task
                vis_prefer.vis_type = vis_choice_test.vis_2
                vis_prefer.save()
                request.session['prefer_id'] = prefer_id + 1
            
                return HttpResponseRedirect(reverse('vis_app:prefer', args=(request.session['prefer_id'],)))

            else:
                request.session['prefer_id'] = prefer_id - 1
                next_prefer_id = request.session['prefer_id'] + 1
                type_detail = get_object_or_404(Vis_Choice_Test, pk=request.session['vis_id'])
                context = {'next_prefer_id':next_prefer_id, 'type_detail':type_detail}
                return render(request, 'prefer_multi_pie.html', context)

        elif prefer_id == 25 or prefer_id == 27 or prefer_id == 29 or prefer_id == 31:
            if request.method == "POST":
                vis_choice_test = Vis_Choice_Test.objects.get(pk=request.session['vis_id'])
                vis_prefer = Vis_prefer()
                vis_prefer.vis_prefer_id = str(str(prefer_id) + str(request.user))
                vis_prefer.prefer_id = prefer_id
                vis_prefer.user_id = request.user.username
                vis_prefer.prefer = request.POST.get('option-list','')
                vis_prefer.v_task = vis_choice_test.v_task
                vis_prefer.vis_type = vis_choice_test.vis_2
                vis_prefer.save()
                request.session['prefer_id'] = prefer_id + 1
            
                return HttpResponseRedirect(reverse('vis_app:prefer', args=(request.session['prefer_id'],)))

            else:
                request.session['prefer_id'] = prefer_id - 1
                next_prefer_id = request.session['prefer_id'] + 1
                type_detail = get_object_or_404(Vis_Choice_Test, pk=request.session['vis_id'])
                context = {'next_prefer_id':next_prefer_id, 'type_detail':type_detail}
                return render(request, 'prefer_tree.html', context)
        
        elif prefer_id == 32:
            return HttpResponseRedirect(reverse('vis_app:user_info'))

        else:
            request.session['vis_id'] = request.session['vis_id'] + 1
            return HttpResponseRedirect(reverse('vis_app:type', args=(request.session['vis_id'],)))

def user_info(request):
    if request.method == "POST":
        user_info = User_info()
        user_info.user_id = request.user.username
        user_info.sex = request.POST.get('sex','')
        user_info.age = request.POST.get('user-age','')
        user_info.major = request.POST.get('user-major','')
        user_info.education = request.POST.get('user-education','') 
        user_info.save()
        return HttpResponseRedirect(reverse('vis_app:finish'))
    else:
        return render(request, 'user_info.html')

def finish(request):

    return render(request, 'finish.html')

def exportcsv_user(request):
    resultdata = User_info.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=user_data.csv'
    writer = csv.writer(response)
    writer.writerow(['user_id', 'sex', 'age', 'major', 'education'])
    results = resultdata.values_list('user_id', 'sex', 'age', 'major', 'education')
    for rlt in results:
        writer.writerow(rlt)
    return response

def exportcsv_test(request):
    resultdata = Answer.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=test_data.csv'
    writer = csv.writer(response)
    writer.writerow(['answer_id', 'user_id', 'test_id', 'v_type', 'v_task','answer','status','time'])
    results = resultdata.values_list('answer_id', 'user_id', 'test_id', 'v_type', 'v_task','answer','status','time')
    for rlt in results:
        writer.writerow(rlt)
    return response

def exportcsv_type(request):
    resultdata = Choice.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=type_data.csv'
    writer = csv.writer(response)
    writer.writerow(['choice_id', 'user_id', 'set_number', 'choice_type', 'v_task','v_reason','time'])
    results = resultdata.values_list('choice_id', 'user_id', 'set_number', 'choice_type', 'v_task','v_reason','time')
    for rlt in results:
        writer.writerow(rlt)
    return response

def exportcsv_prefer(request):
    resultdata = Vis_prefer.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=prefer_data.csv'
    writer = csv.writer(response)
    writer.writerow(['vis_prefer_id', 'prefer_id', 'user_id', 'vis_type', 'v_task','prefer'])
    results = resultdata.values_list('vis_prefer_id', 'prefer_id', 'user_id', 'vis_type', 'v_task','prefer')
    for rlt in results:
        writer.writerow(rlt)
    return response

