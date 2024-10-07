from account.forms import LoginForm
from django.shortcuts import render

def user_login(request):
    if request.method == 'POST':
        pass
    else:
        form = LoginForm()
    return render(request,'account/login.html',{'form':form})
