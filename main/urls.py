from rest_framework.routers import DefaultRouter

from main.views import JournalViewSet, BooksViewSet

router = DefaultRouter()
router.register(r'books', BooksViewSet, basename='books')
router.register(r'journals', JournalViewSet, basename='journals')

urlpatterns = router.urls