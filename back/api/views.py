import json
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Courier, Mail, ApiUser


# Create your views here.

@login_required(login_url="/login")
def index(request):
    return render(request, 'index.html')


@login_required(login_url="/login")
def list(request):
    return render(request, 'list.html')


@login_required(login_url="/login")
def couriers(request):
    return render(request, 'couriers.html', {'items': Courier.objects.all()})


@login_required(login_url="/login")
def mail(request):
    ans = []
    for i in Mail.objects.all().filter(user=request.user):
        ans.append({
            'ticket_id': i.id,
            'answer': i.answer,
            'question': i.question,
            'is_answer': bool(i.answer),
        })

        print(bool(i.answer))

    return render(request, 'mails.html', context={'items': ans})


@login_required(login_url="/login")
def ticket(request):
    data = json.loads(request.body)
    question = data.get('question')
    Mail.objects.create(user=request.user, question=question)
    ans = []
    for i in Mail.objects.all().filter(user=request.user):
        ans.append({
            'ticket_id': i.id,
            'answer': i.answer,
            'question': i.question,
            'is_answer': bool(i.answer),
        })

    return render(request, 'mails.html', context={'items': ans})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        User = get_user_model()
        if User.objects.filter(username=username).exists():
            user1 = ApiUser.objects.get(username=username)
            user1.set_password(password)
            user1.save()

            # Попробуем аутентифицировать
            user = authenticate(request, username=username, password=password)
            print(user)
            print(username, password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                # Если аутентификация не удалась, отобразим сообщение об ошибке
                messages.error(request, "Wrong username or password")
                print("Authentication error: username or password are wrong.")
        else:
            messages.error(request, "Wrong username or password")
            print("Authentication error: username or password are wrong.")

    return render(request, 'login.html')
