from models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from ox.django.shortcuts import render_to_json_response
from sat.login.models import *
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

def add_student(request):
    if request.POST:
        #Create a user for Student 
        student_email = request.POST['email']
        student_mobile = request.POST['mobile']
        student_user = MyUser.objects.create_user(student_email,student_mobile)
        student_user.save()
        #Create user for guardian
        guardian_email = request.POST['guardian_email']
        guardian_tel = request.POST['guardian_tel']
        guardian_user = MyUser.objects.create_user(guardian_email,guardian_tel)
        guardian_user.save()
       #Create a guardian
        guardian =Guardian()


        if request.POST['guardian_full_name']:
            guardian.full_name = request.POST['guardian_full_name']
        else:
            guardian.full_name = ""
        guardian.user = guardian_user
            
        guardian.save()
            
        #Create a student
        info_dict={}
        
        student_first_name = request.POST['first_name']
        student_last_name = request.POST['last_name']
        info_dict['user'] = student_user
        info_dict['full_name'] = student_first_name + " " + student_last_name
        info_dict['centre'] = request.POST['centre']
        info_dict['school'] = request.POST['school']
        info_dict['address'] = request.POST['address']
        info_dict['office_number'] = request.POST['office_number']
        info_dict['guardian'] = guardian
        student = Student.objects.create(**info_dict)
        student.save()
        
        #Rdirect ot the display page( hopefully we should see it there )
        return HttpResponseRedirect('/students/')
        #PHEWW :-/
    return render_to_response('add_student.html',context_instance=RequestContext(request))


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



