from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home.models import ChartData

def index(request):
    return render(request, 'main.html')

def chart(request):
    return render(request, 'chart1.html')

def chart2(request):
    return render(request, 'chart2.html')

# @csrf_exempt # CSRF 토큰 예외 처리
# 단순데이터 처리
def chart_json(request):
    context = {'dd_data':[10, 5, 9, 8, 3, 6],'ll_data':['홍길동','유관순','이순신','강감찬','김구','김유신']}
    return JsonResponse(context)

# db데이터 처리
def chart_json2(request):
    qs = ChartData.objects.all()
    l_qs = list(qs.values())
    
    # dd_data = []    
    # ll_data = []
    
    # for item in qs:
    #     dd_data.append(item.cdata) # 값
    #     ll_data.append(item.cyear) # 이름
    
    # context = {'dd_data':dd_data,'ll_data':ll_data}
    context = {'list_data':l_qs}
    return JsonResponse(context)

# def chart_json2(request):
#     qs = chartData.objects.all().order_by('cyear')
#     return JsonResponse({
#         'dd2_data': list(qs.values_list('cdata', flat=True)),
#         'll2_data': list(qs.values_list('cyear', flat=True)),
#     })
