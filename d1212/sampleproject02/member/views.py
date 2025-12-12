from django.shortcuts import render
from .models import Member
from django.http import HttpResponse

# 로그인 부분
def login(request):
    if request.method == 'GET':
        cook_id = request.COOKIES.get('cook_id','')
        context = {'cook_id':cook_id}
        return render(request,'member/login.html',context)
    elif request.method == 'POST':
        # 맨 앞 id,pw - 변수 / 괄호 안 "id","pw" - login.html에서 input(아이디/비밀번호)의 name
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        login_keep = request.POST.get("login_keep")
        qs = Member.objects.filter(id=id,pw=pw)
        if qs:
            print("id,pw 일치")
            request.session['session_id'] = id
            request.session['session_name'] = qs[0].name
            context = {"state_code":"1"}
            response = render(request,'member/login.html',context)
        else:
            print("id,pw 불일치")
        
# 로그인 부분
def logout(request):
    return render(request,'member/login.html')
