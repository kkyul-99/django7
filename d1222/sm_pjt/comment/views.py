from django.shortcuts import render
from comment.models import Comment
from board.models import Board
from django.http import JsonResponse

# 하단댓글 리스트
def clist(request):
    bno = request.GET.get('bno')
    print("bno 확인: ",bno)
    board = Board.objects.get(bno=bno)
    qs = Comment.objects.filter(board=board)
    list_qs = list(qs.values())
    context = {'result':'success','list':list_qs}
    return JsonResponse(context)
