from rest_framework.routers import SimpleRouter  # new

app_name = 'posts'

# from .views import PostList, PostDetail, UserList, UserDetail
# urlpatterns = [
#     path('<int:pk>', PostDetail.as_view()),
#     path('', PostList.as_view()),
#     path('users/', UserList.as_view()),  # new
#     path('users/<int:pk>/', UserDetail.as_view()),
# ]

from .views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register('users', UserViewSet)
router.register('', PostViewSet)
urlpatterns = router.urls
