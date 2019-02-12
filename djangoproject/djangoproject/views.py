from django.shortcuts import render, redirect
import pyrebase
from .forms import *
from .config import config
from .database import *
from Crypto.Hash import SHA256
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def login(request):
    if (request.method == 'POST'):
        #Data has been submitted
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = auth.sign_in_with_email_and_password(form.cleaned_data['user'], form.cleaned_data['passcode'])
                uuid = user['localId']
                udata = retrieveUserData(uuid)
                userTheme = udata['themeID']
                request.session['uid'] = uuid
                request.session['themeCSS'] = userTheme+ ".css"
            except:
                error = "Invalid Credentials Entered, Please Try Again"
                form = LoginForm()
                return render(request, './login.html', {'form' : form}, {'error' : error})
            return redirect(appInterface)
        else:
            return redirect(login)
    else:
        form = LoginForm()
    return render(request, './login.html', {'form' : form})
def newuser(request):
    if (request.method == 'POST'):
        form = NewUser(request.POST)
        if form.is_valid():
            if(form.cleaned_data['password'] != form.cleaned_data['confirmPassword']):   #Is this secure?
                return redirect(newuser)
            else:
                #Valid data probably
                try:
                    user = auth.create_user_with_email_and_password(form.cleaned_data['email'], form.cleaned_data['password'])
                    addData(user['localId'], form.cleaned_data['username'], form.cleaned_data['email'], 0)
                    print("Added data")
                except:
                    form = NewUser()
                    return render(request, './registeruser.html', {'form': form})
                return redirect(appInterface)
        else:
            return redirect(newuser)
    else:
        form = NewUser()
    return render(request, './registeruser.html', {'form': form})
def resetpassword(request):
    return render(request, './resetpassword.html')
def rootToLogin(request):
    return redirect(login)

def appInterface(request):
    if(request.method =='POST'):
        form = NewConv(request.POST)
        if(form.is_valid()):
            encKey = SHA256.new(form.cleaned_data['key'].encode('utf-8')).hexdigest()
            addConv(request.session['uid'], form.cleaned_data['title'], encKey)
        return redirect(appInterface)
    else:
        form = NewConv()
    return render(request,'./appInterface.html', {'form': form, 'themeCSS': request.session['themeCSS']})

def settings(request):
    if(request.method== 'POST'):
        form = ThemeSelect(request.POST)
        if form.is_valid():
            print(form.cleaned_data['id'])
            updateThemeID(request.session['uid'], form.cleaned_data['id'])
            request.session['theme'] = form.cleaned_data['id']
            request.session['themeCSS'] = request.session['theme'] +".css"
            request.session.modified = True
    else:
        form = ThemeSelect()

    return render(request, './settings.html', {'form': form, 'themeCSS': request.session['themeCSS']})
