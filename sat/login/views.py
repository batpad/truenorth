from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
import pdb

from sat.login.models import MyUser
from sat.truenorth.models import *

def redirect_user(user,username):
    user_type = user.user_type
    if user_type != 'unknown':
       
               # # For checking type of user 
        User_Instance=MyUser.objects.get(email=username).get_category()
        import pdb
        pdb.set_trace()
        return HttpResponse("test")
    #     if (User_Instance == "superuser" or User_Instance == "admin"):
    #         return HttpResponseRedirect("/redirectcentre/")
    #     # return HttpResponse("Teacher")
    #     if (User_Instance == "STUDENT"):
    #         return HttpResponseRedirect("/attendance/"+user.id+"/")
    # raise Http404


def login_user(request):
    state = None
    username = password = ''
    print username 
    print password 
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # state = "You're successfully logged in!"
                # redirect_user(user,username)
               #  user_type = user.user_type
               #  if user_type != 'unknown':
               #      # redirect_url = "/home/%s" % user_type
               #      state = "You have logged in"
                
                    
               
               # # For checking type of user 
                User_Instance=MyUser.objects.get(email=username).get_category()
                if (User_Instance == "superuser" or User_Instance == "admin" or User_Instance == 'tutor'):
                    
                    return HttpResponseRedirect("/redirectcentre/")
                   # return HttpResponse("Teacher")
                else:
                    if User_Instance == "student":
                        u = MyUser.objects.get(id=user.id)
                        student = Student.objects.get(user=u)
                        return HttpResponseRedirect("/attendance/"+str(student.id)+"/")
               #     else:
               #  	if User_Instance == "GAURDIAN":
               #  		return HttpResponse("Gaurdian")
			
               #  	else: 	
               #                  return HttpResponseRedirect('/admin/')    # redirect according to user type 

            else:
                # return HttpResponse("You are osama !")
                usename = ""
                state = "Your account is not active, please contact the site admin."
        else:
            username = ""
            # return HttpResponse("Oops sorry")
            state = "Your username and/or password were incorrect."




    return render_to_response('login.html',{'state':state, 'username': username}, context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/login/")
    
