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

def viewtutorlist(request):
    tutors = Tutor.objects.all()
    return render_to_response('view_profile_tutor.html',{'tutors':tutors}, context_instance=RequestContext(request))



def edit_student(request,iden):
    # Bloddy edit was such a *** ( oh forget it )
    student = Student.objects.get(id=iden)
    if request.POST:
       #Create a guardian
        if request.POST['guardian_email'] and request.POST['guardian_tel']:
            try:
                # Already  a guardian
                guardian = Guardian.objects.get(email=request.POST['guardian_email'])
            except:
                # No Guardian
                guardian_email = request.POST['guardian_email']
                guardian_tel = request.POST['guardian_tel']
                guardian_user = MyUser.objects.create_user(guardian_email,guardian_tel)
                guardian_user.save()
                guardian =Guardian()
                guardian.user = guardian_user

            
            if request.POST['guardian_full_name']:
                guardian.full_name = request.POST['guardian_full_name']
            else:
                guardian.full_name = ""
            guardian.number = request.POST["guardian_tel"]
            guardian.email = request.POST["guardian_email"]
            
        
            guardian.save()
        else:
            # No input from user
            guardian = None
        
        
            
        student.title = request.POST['title']
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.mobile = request.POST['mobile']
        student.grade = request.POST['grade']

        # info_dict['full_name'] = student_first_name + " " + student_last_name

        student.school = request.POST['school']
        student.address = request.POST['address']
        student.office_number = request.POST['office_number']
        student.guardian = guardian
        # Get the centre
        centre = Centre.objects.get(id=request.POST['centre'])
        student.centre = centre

        
        
        student.save()
        
        #Rdirect to the display page( hopefully we should see it there )
        return HttpResponseRedirect('/students/')
    
        #PHEWW :-/



    centres = Centre.objects.all()
    return render_to_response('edit_student.html',{'student':student,'centres':centres}, context_instance=RequestContext(request))

    # return HttpResponse(student)
def edit_staff(request,iden):
    staff = Staff.objects.get(id=iden)
    if request.POST:
        staff.title = request.POST['title']
        staff.first_name = request.POST['first_name']
        staff.last_name = request.POST['last_name']
        staff.cell_number = request.POST['mobile']
        staff.landline = request.POST['landline'] 
        staff.pan_number = request.POST['pan_number']
        staff.save()
        return HttpResponseRedirect("/staff/")

    return render_to_response('edit_staff.html',{'staff':staff}, context_instance=RequestContext(request))

def edit_tutor(request,iden):
    tutor = Tutor.objects.get(id=iden)
    if request.POST:
        tutor.title = request.POST['title']
        tutor.first_name = request.POST['first_name']
        tutor.last_name = request.POST['last_name']
        tutor.cell_number = request.POST['mobile']
        tutor.landline = request.POST['landline'] 
        tutor.pan_number = request.POST['pan_number']
        tutor.office_number = request.POST['office_num']
        tutor.save()
        return HttpResponseRedirect("/tutors/")

    return render_to_response('edit_tutor.html',{'tutor':tutor}, context_instance=RequestContext(request))

    
def add_tutor(request):
        if request.POST:

        #Create a user for tutor
            tutor_email = request.POST['email']
            tutor_mobile = request.POST['mobile']
            tutor_user = MyUser.objects.create_user(tutor_email,tutor_mobile)
            tutor_user.save()
        # Create a tutor
            info_dict={}
            info_dict['user'] = tutor_user
            info_dict['title'] = request.POST['title']
            info_dict['first_name'] = request.POST['first_name']
            info_dict['last_name'] = request.POST['last_name']
            info_dict['pan_number'] = request.POST['pan_number']
            info_dict['cell_number'] = request.POST['mobile']
            info_dict['landline'] = request.POST['landline']
            info_dict['office_number'] = request.POST['office_num']
            tutor = Tutor.objects.create(**info_dict)
            tutor.save()
            return HttpResponseRedirect('/tutors/')

        return render_to_response('add_tutor.html', context_instance=RequestContext(request))
    

def add_staff(request):
        if request.POST:

        #Create a user for Staff
            staff_email = request.POST['email']
            staff_mobile = request.POST['mobile']
            staff_user = MyUser.objects.create_user(staff_email,staff_mobile)
            staff_user.save()
        # Create a staff
            info_dict={}
            info_dict['user'] = staff_user
            info_dict['title'] = request.POST['title']
            info_dict['first_name'] = request.POST['first_name']
            info_dict['last_name'] = request.POST['last_name']
            info_dict['pan_number'] = request.POST['pan_number']
            info_dict['cell_number'] = request.POST['mobile']
            info_dict['landline'] = request.POST['landline']
            staff = Staff.objects.create(**info_dict)
            staff.save()
            return HttpResponseRedirect('/staff/')

        return render_to_response('add_staff.html', context_instance=RequestContext(request))




    
def add_student(request):
    if request.POST:

        #Create a user for Student 
        student_email = request.POST['email']
        student_mobile = request.POST['mobile']
        student_user = MyUser.objects.create_user(student_email,student_mobile)
        student_user.save()

        
       #Create a guardian
        if request.POST['guardian_email'] and request.POST['guardian_tel']:
            guardian_email = request.POST['guardian_email']
            guardian_tel = request.POST['guardian_tel']
            guardian_user = MyUser.objects.create_user(guardian_email,guardian_tel)
            guardian_user.save()


            guardian =Guardian()

            
            if request.POST['guardian_full_name']:
                guardian.full_name = request.POST['guardian_full_name']
            else:
                guardian.full_name = ""
            guardian.number = request.POST["guardian_tel"]
            guardian.email = request.POST["guardian_email"]
            guardian.user = guardian_user
        
            guardian.save()
        else:
            guardian = None
            
        
            
        #Create a student
        info_dict={}
        

        info_dict['user'] = student_user
        info_dict['title'] = request.POST['title']
        info_dict['first_name'] = request.POST['first_name']
        info_dict['last_name'] = request.POST['last_name']
        info_dict['mobile'] = request.POST['mobile']
        info_dict['landline'] = request.POST['landline']
        info_dict['grade'] = request.POST['grade']

        # info_dict['full_name'] = student_first_name + " " + student_last_name

        info_dict['school'] = request.POST['school']
        info_dict['address'] = request.POST['address']
        info_dict['office_number'] = request.POST['office_number']
        info_dict['guardian'] = guardian

        # Get the centre
        centre = Centre.objects.get(id=request.POST['centre'])
        info_dict['centre'] = centre

        
        student = Student.objects.create(**info_dict)
        student.save()
        
        #Rdirect ot the display page( hopefully we should see it there )
        return HttpResponseRedirect('/students/')

    
        #PHEWW :-/
    centres = Centre.objects.all()
    return render_to_response('add_student.html',{'centres':centres}, context_instance=RequestContext(request))


def menu(request):
    return render_to_response('menu.html', context_instance=RequestContext(request))
    


def selectcenter(request):
    if request.GET:
        center = request.GET.get('center')
        request.session["center"] = center
        return HttpResponseRedirect("/menu/")
    return render_to_response('selectcenter.html', context_instance=RequestContext(request))


def checkin(request):
    if request.GET:
        user = request.GET.get("user", None)
        user = MyUser.objects.get(pk=user)
        time_in = request.GET.get("time_in", None)
        time_out = request.GET.get("time_out", None)
        date = request.GET.get("date", '')
        is_present = request.GET.get("is_present", True)
        if is_present == 'false':
            is_present = False
        centre = request.GET.get("centre", None)
        centre_obj = Centre.objects.get(id=centre)
        if not user or not time_in or not centre:
            return render_to_json_response({'error': 'Insufficient data'})
        curr_user = request.user
        if not curr_user.is_authenticated():
            return render_to_json_response({'error': 'Please log-in'})
        curr_user_type = curr_user.user_type
        if curr_user_type not in ['admin', 'staff', 'tutor']:
            return render_to_json_response({'error': 'Insufficient permissions'})
        if user.user_type == 'tutor' and curr_user_type == 'tutor':
            return render_to_json_response({'error': 'Tutors can only mark attendance for students'})
        if date == '':
            today = datetime.datetime.now()
        else:
            today = datetime.datetime.strptime(date, "%d %b, %Y")
        hours,mins = (int(t) for t in time_in.split(":"))
        time_obj = datetime.time(hours,mins)
        time_in_obj = datetime.datetime.combine(today,time_obj)
        today_min = datetime.datetime.combine(today, datetime.time.min)
        today_max = datetime.datetime.combine(today, datetime.time.max)
        today_qset = Checkin.objects.filter(user=user).filter(time_in__range=(today_min, today_max)).filter(centre=centre)
        if today_qset.count() > 0:
            if is_present:
                today_qset[0].time_in = time_in_obj
                today_qset[0].save()
                return render_to_json_response({'success': 'Attendance updated'})
            else:
                today_qset.delete()
                return render_to_json_response({'success': 'Attendance removed'})
        if is_present:        
            checkin = Checkin(user=user, time_in=time_in_obj, time_out=time_out, marked_by=curr_user,centre=centre_obj)
            checkin.save()
        else:
            return render_to_json_response({'error': 'Present not marked'})
        return render_to_json_response({'success': 'Attendance marked'})
  
    

def has_attendance(request):
    if not request.user.is_authenticated():
        return render_to_json_response({'error': 'not logged in'})
    user_id = request.GET.get('id', None)
    date = request.GET.get('date', '')
    if date == '':
        date = datetime.datetime.today()
    else:
        date = datetime.datetime.strptime(date, "%d %b, %Y")
    
    today_min = datetime.datetime.combine(date, datetime.time.min)
    today_max = datetime.datetime.combine(date, datetime.time.max)
    user = MyUser.objects.get(id=user_id)
    today_qset = Checkin.objects.filter(user=user).filter(time_in__range=(today_min, today_max))
    if today_qset.count() > 0:
        time_in = today_qset[0].time_in.strftime("%H:%m")
        return render_to_json_response({'success': time_in})
    else:
        return render_to_json_response({'success': 'no'})

def view_attendance(request):
    date = request.GET.get('date', '')
    if date == '':
        today = datetime.datetime.today()
    else:
        today = datetime.datetime.strptime(date, "%d %b, %Y")
    students = Student.objects.all()
    students = [student.user.get_attendance_data(today) for student in Student.objects.all()]
    return render_to_response('view_attendance.html',{'students':students, 'date': date}, context_instance=RequestContext(request))

    
