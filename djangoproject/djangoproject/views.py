from django.shortcuts import render

import pyrebase

config = {
    "apiKey": "AIzaSyBYm7w0kt_NvWmH9GE1vI9ckN9SrXdHJgw",
    "authDomain": "loginauth-80e28.firebaseapp.com",
    "databaseURL": "https://loginauth-80e28.firebaseio.com",
    "projectId": "loginauth-80e28",
    "storageBucket": "loginauth-80e28.appspot.com",
    "messagingSenderId": "1018199481520"

}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def login(request):
    return render(request,"login.html")