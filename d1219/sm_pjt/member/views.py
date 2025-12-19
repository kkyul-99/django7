from django.shortcuts import render
from .models import Member

def login(request):
    if request.method == 'GET':
        return render(request,'member/login.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.post.get('pw')
        
        qs = Member.objects.filter(id=id,pw=pw)
        if qs:
            request.session['session_id'] = id
            request.session['session_name'] = qs[0].name
            context = {'flag':'1'}
        else:
            context = {'flag':'0','id':id,'pw':pw}
        
        return render(request,'member/login.html',context)

def logout(request):
    return
