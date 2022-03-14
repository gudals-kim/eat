from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

import board
from .models import Board
from .serializers import BoardSerializer
from board import serializers


# Create your views here.

def viewjson(request):
    return JsonResponse("REST API end point", safe=False)
        
@api_view(['GET'])
def index(request):
    api_urls = {
        'List' : '/boardlist',
        'Detail' : '/boardlist/<str:pk>/',
        'Create' : '/boardinsert',
        'Update' : '/boardupdate/<str:pk>/',
        'Delete' : '/boarddelete/<str:pk>/',
    }
    
    return Response(api_urls)

@api_view(['GET'])
def boardList(request):
    boards = Board.objects.all()
    serializers = BoardSerializer(boards, many=True)
    
    return Response(serializers.data)

@api_view(['GET'])
def boardview(request,pk):
    boards = Board.objects.get(id=pk)
    serializers = BoardSerializer(boards, many=False)
    
    return Response(serializers.data)

@api_view(['POST'])
def boardInsert(request):
    serializers = BoardSerializer(data=request.data)
    
    if serializers.is_valid():
        serializers.save()
    
    return Response(serializers.data)

@api_view(['PUT'])
def boardUpdate(request, pk):
    boards = Board.objects.get(id=pk)
    serializers = BoardSerializer(instance=boards,data=request.data)
    
    if serializers.is_valid():
        serializers.save()
    
    return Response(serializers.data)

@api_view(['DELETE'])
def boardDelete(request, pk):
    board = Board.objects.get(id=pk)
    
    if board:
        board.delete()
    
    return Response("delete..")