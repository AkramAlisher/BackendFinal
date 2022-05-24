from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from main.models import Book, Journal
from main.serializers import JournalSerializer, BookSerializer


class BooksViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def update(self, request, *args, **kwargs):
        if request.user.profile.role == 'S' or request.user.is_superuser:
            return self.update(request, *args, **kwargs)
        else:
            return Response(
                {'error': 'You have no access to modify the objects'},
                status=status.HTTP_403_FORBIDDEN
            )


class JournalViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()

    def update(self, request, *args, **kwargs):
        if request.user.profile.role == 'S' or request.user.is_superuser:
            return self.update(request, *args, **kwargs)
        else:
            return Response(
                {'error': 'You have no access to modify the objects'},
                status=status.HTTP_403_FORBIDDEN
            )
