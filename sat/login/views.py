from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F

from sat.login.models import MyUser


def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                
                # For checking type of user 
                User_Instance=MyUser.objects.get(email=username).get_category()
                if User_Instance == "TEACHER":
                    return HttpResponse("Teacher")
                else:
                    if User_Instance == "STUDENT":
                        return HttpResponse("Student")
                    else:
                        return HttpResponseRedirect('/admin/')    # redirect according to user type
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('auth.html',{'state':state, 'username': username}, context_instance=RequestContext(request))
