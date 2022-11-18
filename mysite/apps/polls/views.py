from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Subject, Timetable


def index(request):
    data = {"subjects": Subject.objects.all(), "title": "Предметики"}
    return render(request, "polls/index.html", context = data)

def subrooms(request, sub_id):
    try:
        t_table = Timetable.objects.filter(subject_id = sub_id)
        name = Subject.objects.filter(id = sub_id)[0]
        subs = Subject.objects.all()
    except:
        return Http404("Что-то пошло не так")
    return render(request, 'polls/subrooms.html', context = {'subs': subs,'t_table': t_table,'sub_name': name , 'title': "РасПисьАние"})


def allrooms(request):
    try:
        roo = [*Timetable.objects.values_list('room')]
        rooms = []
        for i in range(len(roo)):
            rooms.append(*roo[i])
        rooms = set(rooms)
        return render(request, 'polls/allrooms.html', context = {'rooms': rooms, 'title': "РасПисьАние"})
    except:
        return Http404("Что-то пошло не так")
    

def room(request, room_id):
    # try:
    subs = []
    stt = set()
    for item in Timetable.objects.filter(room = room_id):
        subs.append({'lecture_practice': item.subject.lecture_practice,'name': Subject.objects.values_list('name').get(name = item.subject.name, lecture_practice = item.subject.lecture_practice)[0],'time':item.time,'week':item.weekday})
    rooms = [x for x in Timetable.objects.values('room').distinct()][1::]
    return render(request, 'polls/room_sub.html', context = {'subs': subs,"room": room_id,'rooms': rooms,  'title': 'РасПисьАние'})
    # except:
    #     return Http404(request)

def subredirect(request, sub_name):
    nm = sub_name.split(",,")[0]
    # return HttpResponse(nm)
    try:
        l_p = sub_name.split(",,")[-1]
    except:
        l_p = ''
    if l_p == '1':
        l_p = 'л/п'
    subs = Subject.objects.filter(lecture_practice = l_p).get(name = nm)
    return redirect(subs,permanent= True)

def check(request):
    subs = [x.__dict__ for x in Subject.objects.all()]
    return render(request, 'home.html', context={'sub':subs})