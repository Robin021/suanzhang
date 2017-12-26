from django.shortcuts import render
from grape.models import user
from .forms import LoginForm
from .forms import mingxiForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        return render(request, 'index.html')

# 做一些事情对于匿名未登录用户.

def Login(request):#登录
    next_to = request.GET.get('next', None)
    form = LoginForm(request.POST)
    if form.is_valid():  # 如果提交的数据合法
        u = form.cleaned_data['username']#表单用户名
        p = form.cleaned_data['password']#表单密码
        user = authenticate(username=u, password=p)#用户验证
        if user is not None and user.is_active:
            login(request, user)
            return redirect(next_to)
        else:
            return render(request, 'login.html', {'msg':'用户名或密码不匹配!'})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


@login_required(login_url='/login/')
def luru(request):
    mingxiform = mingxiForm(request.POST)
    return render(request, 'add.html', {'form': mingxiform})


def logout_view(request):
    logout(request)
    response = HttpResponseRedirect('/login')
    return response