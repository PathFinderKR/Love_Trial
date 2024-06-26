import uuid
from django.shortcuts import render, redirect

def home(request):
    return redirect('welcome')

def welcome(request):
    if request.method == 'POST':
        if 'new_room' in request.POST:
            room_code = str(uuid.uuid4())  # UUID를 사용하여 고유한 방 번호 생성
            request.session['room_code'] = room_code
            return redirect('nickname')
        elif 'enter_room' in request.POST:
            room_code = request.POST.get('room_code')
            request.session['room_code'] = room_code
            return redirect('chat')
    return render(request, 'welcome.html')

def nickname(request):
    room_code = request.session.get('room_code')
    if request.method == 'POST':
        nickname = request.POST['nickname']
        request.session['nickname'] = nickname
        return redirect('player')
    return render(request, 'nickname.html', {'room_code': room_code})

def player(request):
    if request.method == 'POST':
        if 'single' in request.POST:
            return redirect('chat')
        elif 'double' in request.POST:
            return redirect('room')
    return render(request, 'player.html')

def room(request):
    room_code = request.session.get('room_code')
    return render(request, 'room.html', {'room_code': room_code})

def chat(request):
    room_code = request.session.get('room_code')
    nickname = request.session.get('nickname', 'Anonymous')
    return render(request, 'chat.html', {'room_code': room_code, 'nickname': nickname})
