from rest_framework import generics
from rest_framework import mixins
from .serializers import AuthorSerializer, BlogSerializer
from .models import Author, Blog


class GenericBlogAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
                     , mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)
    
    def delete(self, request, id=None):
        return self.destroy(request, id)



class GenericAuthorAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
                     , mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)
    
    def delete(self, request, id=None):
        return self.destroy(request, id)