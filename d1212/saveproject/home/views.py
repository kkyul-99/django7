from django.shortcuts import render

def index(request):
    # 쿠키 검색 - request
    # 쿠키 저장 - response
    
    # 쿠키 검색: COOKIES - 모든 정보 / COOKIES.get() - 특정 정보
    cook_info = request.COOKIES
    print("쿠키 모든 정보: ",cook_info)
    cook_id = request.COOKIES.get("cook_id","") # 있으면 cook_id, 없으면 빈공백 처리
    print("cook_id 정보: ",cook_id)
    
    response = render(request,'index.html')
    # 쿠키 저장
    # cook_id = aaa
    # 유지시간 없으면 브라우저 종료시 사라짐 / 시간을 설정하면 해당 시간동안 유지
    # 쿠키 정보가 없을때만 쿠키 저장
    # if not cook_id:
    #     response.set_cookie("smsite_connect","ok")
    #     response.set_cookie("ip","127.0.0.1:8000",max_age=60*60*24) # 60초*60분*24시간*365일 = 1년
    return response
