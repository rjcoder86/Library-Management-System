from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Book
from .serializer import BookSerializer


#Function Based Views
@api_view(['POST'])
def AddBook(request):
    s=BookSerializer(data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def AllBooks(request):
    books = Book.objects.all()
    seridata=BookSerializer(books,many=True)
    return Response(seridata.data, status=status.HTTP_200_OK)


@api_view(['POST','GET'])
def UpdateBook(request, pk):
    b=Book.objects.get(id=pk)
    if request.method=='POST':
        bs=BookSerializer(b,data=request.data)
        if bs.is_valid():
            bs.save()
            return Response({'msg':'object updated'},status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    bs = BookSerializer(b)
    return Response(bs.data)

@api_view(['GET'])
def DeleteBook(request, pk):
    b=Book.objects.get(id=pk)
    b.delete()
    return Response({'msg':'Book is deleted '},status=status.HTTP_202_ACCEPTED)
