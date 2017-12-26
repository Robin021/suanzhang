from django.shortcuts import render
from grape.models import user
from .forms import LoginForm
from .forms import mingxiForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import redirect


# Create your views here.
def index(request):
    context = {}
    context['title'] = 'Login'
    return render(request, 'index.html', context)

def Login(request):#登录
    if request.method == 'POST':#POST请求才处理
        form = LoginForm(request.POST)
        if form.is_valid():  # 如果提交的数据合法
            u = form.cleaned_data['username']#表单用户名
            p = form.cleaned_data['password']#表单密码
            user = authenticate(username=u, password=p)#验证
            if user is not None and user.is_active:
                login(request, user)
                response = HttpResponseRedirect('/luru/', {'username': user.username})
                # response.set_cookie('username', user.name, 3600)
                return response
            else:
                HttpResponseRedirect('/')
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html', {'msg': 'invaild method'})


def luru(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    mingxiform = mingxiForm(request.POST)
    return render(request, 'add.html', {'form': mingxiform})

def logout_view(request):
    logout(request)