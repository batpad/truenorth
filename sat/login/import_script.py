from sat.login.models import *
import datetime
import csv

# WARNING: THIS SCRIPT MUST BE RUN AFTER ADDING ATLEAST ONE CENTRE !

def import_things():
    with open('/home/anshu/dev/truenorth/sat/login/list_final.csv','rb') as import_list:
        somereader = csv.reader(import_list,delimiter=',')

        for row in somereader:
            # print row[0]
            
            student_email = row[0]
            student_mobile = row[14]
            student_user = MyUser.objects.create_user(student_email)
            student_user.set_password(student_mobile)
            student_user.save()
        
        # Create Guardian

            guardian1_email = row[16]
            guardian1_tel = row[17]
            guardian1_user = MyUser.objects.create_user(guardian1_email)
            guardian1_user.set_password(guardian1_tel)
            guardian1_user.save()
            guardian1 =Guardian()
            guardian1.user = guardian1_user
            guardian1.full_name = row[18]
            guardian1.number = row[17]
            guardian1.email = row[16]
            guardian1.save()
            guardian2 = None # For the time being
            
        # Now the student
            info_dict = {}
            info_dict['user'] = student_user
            info_dict['title'] = row[18]
            info_dict['first_name'] = row[10]
            info_dict['last_name'] = row[13]
            info_dict['mobile'] = row[14]
            info_dict['landline'] = row[12]
            info_dict['grade'] = row[11]

        # info_dict['full_name'] = student_first_name + " " + student_last_name

            info_dict['school'] = row[15]
            info_dict['guardian_1'] = guardian1
            info_dict['guardian_2'] = guardian2
        # Get the centre
            centre = Centre.objects.all()[0] # Fixme: Set to take colaba
            info_dict['centre'] = centre
            student = Student.objects.create(**info_dict)
            student.save()
        

 


        

    
