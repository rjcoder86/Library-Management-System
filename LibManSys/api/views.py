from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, mixins, generics, permissions
from .models import Book
from .serializer import BookSerializer
from .permissions import IsAdminUser ,AllowAll ,AllowAny


#Function Based Views
# @permission_classes([IsAdminUser,])
@api_view(['POST'])
def AddBook(request):
    s=BookSerializer(data=request.data)
    s.is_valid(raise_exception=True)
    s.save()
    return Response(s.data, status=status.HTTP_201_CREATED)

# @permission_classes([AllowAny,])
@api_view(['GET'])
def AllBooks(request):
    books = Book.objects.all()
    seridata=BookSerializer(books,many=True)
    return Response(seridata.data, status=status.HTTP_200_OK)

# @permission_classes([IsAdminUser,])
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

# @permission_classes([IsAdminUser,])
@api_view(['GET'])
def DeleteBook(request, pk):
    b=Book.objects.get(id=pk)
    b.delete()
    return Response({'msg':'Book is deleted '},status=status.HTTP_202_ACCEPTED)

#Class Based Views
class ListCreateView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAll,IsAdminUser)

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class RetriveUpdateDeleteView(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminUser,)

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*a,**kwargs):
        return self.destroy(request,*a,**kwargs)