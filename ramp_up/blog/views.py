from rest_framework import generics
from rest_framework import mixins
from .serializers import AuthorSerializer, BlogSerializer
from .models import Author, Blog
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class GenericBlogAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
                     , mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id):
        return self.update(request, id)
    
    def delete(self, request, id):
        return self.destroy(request, id)



class GenericAuthorAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
                     , mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id):
        return self.update(request, id)
    
    def delete(self, request, id):
        return self.destroy(request, id)
    



class AuthorBlogsListAPIView(generics.ListAPIView):
    serializer_class = BlogSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        author_id = self.kwargs['author_id']
        queryset = Blog.objects.filter(author_id=author_id)
        return queryset