from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, mixins, generics, permissions
from .models import Book
from .serializer import BookSerializer
from .permissions import IsUser,IsAdminUser


#Function Based Views
@api_view(['POST'])
@permission_classes([IsAdminUser,])
def AddBook(request):
    s=BookSerializer(data=request.data)
    s.is_valid(raise_exception=True)
    s.save()
    return Response(s.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsUser,])
def AllBooks(request):
    books = Book.objects.all()
    seridata=BookSerializer(books,many=True)
    return Response(seridata.data, status=status.HTTP_200_OK)

@api_view(['POST','GET'])
@permission_classes([IsAdminUser,])
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
@permission_classes([IsAdminUser,])
def DeleteBook(request, pk):
    b=Book.objects.get(id=pk)
    b.delete()
    return Response({'msg':'Book is deleted '},status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
@permission_classes([IsAdminUser,])
def GetBook(request, pk):
    b=Book.objects.get(id=pk)
    bs=BookSerializer(b)
    return Response(bs.data,status=status.HTTP_202_ACCEPTED)

# #Class Based Views
# class ListCreateView(mixins.ListModelMixin,
#                 mixins.CreateModelMixin,
#                 generics.GenericAPIView):
#
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (AllowAll,IsAdminUser)
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
#
# class RetriveUpdateDeleteView(mixins.RetrieveModelMixin,
#                 mixins.UpdateModelMixin,
#                 mixins.DestroyModelMixin,
#                 generics.GenericAPIView):
#
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (IsAdminUser,)
#
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
#
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
#
#     def delete(self,request,*a,**kwargs):
#         return self.destroy(request,*a,**kwargs)