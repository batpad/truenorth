from models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
from ox.django.shortcuts import render_to_json_response
from sat.login.models import *
import datetime

# Do we need to filter tutors and staff according to centre?

def home(request, user_type):
    return HttpResponse("you are a %s" % user_type)

# DO NOT USE THE FOLLOWING VIEW !
def students(request):
    return HttpResponse("We are students of true north")

def attendance(request,iden):
    student = Student.objects.get(id=iden)
    return render_to_response('attendance_students.html',{'student':student},context_instance=RequestContext(request))


def viewstafflist(request):
    staff = Staff.objects.all()
    return render_to_response('view_profile_staff.html',{'staff':staff}, context_instance=RequestContext(request))

def viewstudentlist(request):
    if request.session['centre'] == "All":
        students = Student.objects.all()
    else:
        centre_obj = Centre.objects.get(name=request.session['centre'])
        students  = Student.objects.filter(centre=centre_obj)

    return render_to_response('view_profile_students.html',{'students':students}, context_instance=RequestContext(request))

def viewtutorlist(request):
    tutors = Tutor.objects.all()
    return render_to_response('view_profile_tutor.html',{'tutors':tutors}, context_instance=RequestContext(request))



def edit_student(request,iden):
    # Bloddy edit was such a *** ( oh forget it )
    student = Student.objects.get(id=iden)
    if request.POST:
       #Create a guardian
        if request.POST['guardian1_email'] and request.POST['guardian1_tel']:
            try:
                # Already  a guardian
                guardian1 = Guardian.objects.get(email=request.POST['guardian1_email'])
            except:
                # No Guardian
                guardian1_email = request.POST['guardian1_email']
                guardian1_tel = request.POST['guardian1_tel']
                guardian1_user = MyUser.objects.create_user(guardian1_email)
                guardian1_user.set_password(guardian1_tel)
                guardian1_user.save()
                guardian1 =Guardian()
                guardian1.user = guardian_user

            
            if request.POST['guardian1_full_name']:
                guardian1.full_name = request.POST['guardian1_full_name']
            else:
                guardian1.full_name = ""
            guardian1.number = request.POST["guardian1_tel"]
            guardian1.email = request.POST["guardian1_email"]
            
        
            guardian1.save()
        else:
            # No input from user
            guardian1 = None


        if request.POST['guardian2_email'] and request.POST['guardian2_tel']:
            try:
                # Already  a guardian
                guardian2 = Guardian.objects.get(email=request.POST['guardian2_email'])
            except:
                # No Guardian
                guardian2_email = request.POST['guardian2_email']
                guardian2_tel = request.POST['guardian2_tel']
                guardian2_user = MyUser.objects.create_user(guardian2_email)
                guardian2_user.set_password(guardian2_tel)
                guardian2_user.save()
                guardian2 =Guardian()
                guardian2.user = guardian2_user

            
            if request.POST['guardian2_full_name']:
                guardian2.full_name = request.POST['guardian2_full_name']
            else:
                guardian.full_name = ""
            guardian2.number = request.POST["guardian2_tel"]
            guardian2.email = request.POST["guardian2_email"]
            
        
            guardian2.save()
        else:
            # No input from user
            guardian2 = None

        if request.POST['is_active'] == 'inactive':
            student.is_active = False
        else:
            student.is_active = True

        
            
        student.title = request.POST['title']
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.mobile = request.POST['mobile']
        student.grade = request.POST['grade']

        # info_dict['full_name'] = student_first_name + " " + student_last_name

        student.school = request.POST['school']
        student.address = request.POST['address']
        student.office_number = request.POST['office_number']
        student.guardian_1 = guardian1
        student.guardian_2 = guardian2
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
        tutor.address = request.POST['address']
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
            tutor_user = MyUser.objects.create_user(tutor_email)
            tutor_user.set_password(tutor_mobile) 
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
            info_dict['address'] = request.POST['address']
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
            staff_user = MyUser.objects.create_user(staff_email)
            staff_user.set_password(staff_mobile)
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
        student_user = MyUser.objects.create_user(student_email)
        student_user.set_password(student_mobile)
        student_user.save()

        
       #Create guardian 1
        if request.POST['guardian1_email'] and request.POST['guardian1_tel']:
            guardian1_email = request.POST['guardian1_email']
            guardian1_tel = request.POST['guardian1_tel']
            guardian1_user = MyUser.objects.create_user(guardian1_email)
            guardian1_user.set_password(guardian1_tel)
            guardian1_user.save()


            guardian1 =Guardian()

            
            if request.POST['guardian1_full_name']:
                guardian1.full_name = request.POST['guardian1_full_name']
            else:
                guardian1.full_name = ""
            guardian1.number = request.POST["guardian1_tel"]
            guardian1.email = request.POST["guardian1_email"]
            guardian1.user = guardian1_user
        
            guardian1.save()
        else:
            guardian1 = None

        if request.POST['guardian2_email'] and request.POST['guardian2_tel']:
            guardian2_email = request.POST['guardian2_email']
            guardian2_tel = request.POST['guardian2_tel']
            guardian2_user = MyUser.objects.create_user(guardian2_email)
            guardian2_user.set_password(guardian2_tel)
            guardian2_user.save()


            guardian2 =Guardian()

            
            if request.POST['guardian2_full_name']:
                guardian2.full_name = request.POST['guardian2_full_name']
            else:
                guardian2.full_name = ""
            guardian2.number = request.POST["guardian2_tel"]
            guardian2.email = request.POST["guardian2_email"]
            guardian2.user = guardian2_user
        
            guardian2.save()
        else:
            guardian2 = None

            
        
            
        #Create a student
        info_dict={}
        if request.POST['is_active'] == 'active':
            info_dict['is_active'] = True
        else:
            info_dict['is_active'] = False
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
        info_dict['guardian_1'] = guardian1
        info_dict['guardian_2'] = guardian2

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

def redirectcentre(request):
    if request.COOKIES.has_key('centre'):
        request.session["centre"] = request.COOKIES['centre']
        return HttpResponseRedirect("/menu/")
    else:
        return HttpResponseRedirect("/selectcenter/")
        
    


def selectcenter(request):
    if request.POST:
        centre = request.POST['centre']
        # I dont know why it does not update centre on assignment.It updates correctly if the key is made blank ...
        request.session["centre"] = ""
        request.session["centre"] = centre
        return HttpResponseRedirect("/menu/")
        # # Wat da F** x-(
        # response.set_cookie( 'centre', centre)
        # # return HttpResponse("centre:" +centre + "session: " + request.session["centre"])
        # return response
    centres = Centre.objects.all()
    return render_to_response('selectcenter.html',{'centres':centres},context_instance=RequestContext(request))


def checkin(request):
    if request.GET:
        user = request.GET.get("user", None)
        user = MyUser.objects.get(pk=user)
        time_in = request.GET.get("time_in", None)
        time_out = request.GET.get("time_out", '')
        if time_out == '':
            time_out = None
        date = request.GET.get("date", timezone.now().strftime("%d %b, %Y"))
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
            today = timezone.now()
        else:
            today = datetime.datetime.strptime(date, "%d %b, %Y")
        time_in_hours,time_in_mins = (int(t) for t in time_in.split(":"))
        time_in_obj = datetime.time(time_in_hours,time_in_mins)
        time_in = datetime.datetime.combine(today,time_in_obj)
        if time_out:
            time_out_hours,time_out_mins = (int(t) for t in time_out.split(":"))
            time_out_obj = datetime.time(time_out_hours,time_out_mins)
            time_out = datetime.datetime.combine(today,time_out_obj)
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
            checkin = Checkin(user=user, time_in=time_in, time_out=time_out, marked_by=curr_user,centre=centre_obj)
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
        date = timezone.now()
    else:
        date = datetime.datetime.strptime(date, "%d %b, %Y")
    
    today_min = datetime.datetime.combine(date, datetime.time.min)
    today_max = datetime.datetime.combine(date, datetime.time.max)
    user = MyUser.objects.get(id=user_id)
    today_qset = Checkin.objects.filter(user=user).filter(time_in__range=(today_min, today_max))
    now = timezone.now().strftime("%H:%m")
    if today_qset.count() > 0:
        checkin_dict = today_qset[0].get_dict()
        #time_in = today_qset[0].time_in.strftime("%H:%m")
        return render_to_json_response({'success': 'yes', 'checkin': checkin_dict, 'now': now})
    else:
        return render_to_json_response({'success': 'no', 'now': now})

def view_attendance(request):
    date = request.GET.get('date', '')
    if date == '':
        today = timezone.now()
    else:
        today = datetime.datetime.strptime(date, "%d %b, %Y")
    students = Student.objects.all()
    students = [student.user.get_attendance_data(today) for student in Student.objects.all()]
    return render_to_response('view_attendance.html',{'students':students, 'date': today}, context_instance=RequestContext(request))

def view_attendance_tutor(request):
    date = request.GET.get('date', '')
    if date == '':
        today = timezone.now()
    else:
        today = datetime.datetime.strptime(date, "%d %b, %Y")
    # Is this line needed ?
    tutors = Tutor.objects.all()

    tutors = [tutor.user.get_attendance_data(today) for tutor in Tutor.objects.all()]
    return render_to_response('attendance_tutors.html',{'tutors':tutors, 'date': today}, context_instance=RequestContext(request))
    
