from rest_framework.routers import SimpleRouter

from django.urls import include, path

from cats.views import CatViewSet

router = SimpleRouter()
router.register('cats', CatViewSet)
urlpatterns = [
    path('', include(router.urls)),
] 

# urlpatterns = [
#     path('cats/', CatList.as_view()),
#     path('cats/<int:pk>/', CatDetail.as_view()),
# ]

# urlpatterns = [
#     path('cats/', APICat.as_view()),
# ]

# urlpatterns = [
#    path('cats/', cat_list),
# ]
