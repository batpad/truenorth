from models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from ox.django.shortcuts import render_to_json_response
import datetime

def home(request, user_type):
    return HttpResponse("you are a %s" % user_type)

# DO NOT USE THE FOLLOWING VIEW !
def students(request):
    return HttpResponse("We are students of true north")
def viewstafflist(request):
    staff = Staff.objects.all()

    return render_to_response('view_profile_staff.html',{'staff':staff}, context_instance=RequestContext(request))

def viewstudentlist(request):
    students = Student.objects.all()

    return render_to_response('view_profile_students.html',{'students':students}, context_instance=RequestContext(request))

def menu(request):
    return render_to_response('menu.html', context_instance=RequestContext(request))
    


def selectcenter(request):
    if request.GET:
        center = request.GET.get('center')
        request.session["center"] = center
        return HttpResponseRedirect("/menu/")
    return render_to_response('selectcenter.html', context_instance=RequestContext(request))


def checkin(request):
    user = request.GET.get("user", None)
    time_in = request.GET.get("time_in", None)
    time_out = request.GET.get("time_out", None)
    centre = request.GET.get("centre", None)
    if not user or not time_in or not centre:
        return render_to_json_response({'error': 'Insufficient data'})
    curr_user = request.user
    curr_user_type = curr_user.user_type
    if curr_user_type not in ['admin', 'staff', 'tutor']:
        return render_to_json_response({'error': 'Insufficient permissions'})
    if user.user_type == 'tutor' and curr_user_type == 'tutor':
        return render_to_json_response({'error': 'Tutors can only mark attendance for students'})
    today = datetime.datetime.now()
    if Checkin.objects.filter(user=user).filter(time_in__date=today).filter(centre=centre).count() > 0:
        return render_to_json_response({'error': 'Attendance already marked for today'})
    checkin = Checkin(user=user, time_in=time_in, time_out=time_out, marked_by=curr_user)
    checkin.save()
    return render_to_json_response({'success': 'Attendance marked'})



