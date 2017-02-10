from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.shortcuts import render
from .forms import UserLoginForm
import http.client

# Create your views here.

def login_view(request):
    # title = "login"
    # form = UserLoginForm(request.POST or None)

    # conn = http.client.HTTPSConnection("")

    # payload = "{\"client_id\": \"uxqlKBGtq1DDOHgCCtZx0bH1O7GgDhrR\",\"email\": \"$('#signup-email').val()\",\"password\": \"$('#signup-password').val()\",\"user_metadata\": {\"name\": \"john\",\"color\": \"red\"}}"

    # headers = { 'content-type': "application/json" }

    # conn.request("POST", "/sitesalt.auth0.com/dbconnections/signup", payload, headers)

    # res = conn.getresponse()
    # data = res.read()

    # print(data.decode("utf-8"))


    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

    return render (request, "Accounts/forms.html", {"form":form, "title":title})
