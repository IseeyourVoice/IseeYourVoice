from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
from django.urls import reverse_lazy

from user.forms import UserForm, LoginForm


# Create your views here.
@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('isyv:index')
    else:
        return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)  ## 인증

            login(request, user)  ## 로그인
            return redirect('isyv:index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(email, password)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # 로그인 후 이동할 페이지 설정
                return redirect('isyv:index')
            else:
                # 인증 실패 처리
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'common/login.html', {'form': form})