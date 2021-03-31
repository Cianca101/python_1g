from django.urls import path, include
# 6 DRF Generic Class Views
from .views import ListOwnersAPIView, RetrieveOwnersAPIView, CreateOwnersAPIView, UpdateOwnersAPIView, DestroyOwnersAPIView    
from .views import ListPetsAPIView, RetrievePetsAPIView, CreatePetsAPIView, UpdatePetsAPIView, DestroyPetsAPIView
from .views import ListOfficesAPIView, CreateOfficesAPIView

# from rest_framework import routers
# from .views import OwnersViewSet

urlpatterns = [
    # Owners #
    path("owners/", ListOwnersAPIView.as_view(), name="list-owners"),   # 7 DRF Generic Class Views
    path("owners/create/", CreateOwnersAPIView.as_view(), name="create-owners"),
    path("owners/<int:pk>/", RetrieveOwnersAPIView.as_view(), name="retrieve-owners"),
    path("owners/update/<int:pk>/", UpdateOwnersAPIView.as_view(), name="update-owners"),
    path("owners/destroy/<int:pk>/", DestroyOwnersAPIView.as_view(), name="destroy-owners"),
    # Pets #
    path("pets/", ListPetsAPIView.as_view(), name="list-pets"),   # 7 DRF Generic Class Views
    path("pets/create/", CreatePetsAPIView.as_view(), name="create-pets"),
    path("pets/<int:pk>/", RetrievePetsAPIView.as_view(), name="retrieve-pets"),
    path("pets/update/<int:pk>/", UpdatePetsAPIView.as_view(), name="update-pets"),
    path("pets/destroy/<int:pk>/", DestroyPetsAPIView.as_view(), name="destroy-pets"),
    # Office #
    path("offices/", ListOfficesAPIView.as_view(), name="list-offices"),   # 7 DRF Generic Class Views
    path("offices/create/", CreateOfficesAPIView.as_view(), name="create-office"),
]




# router = routers.DefaultRouter()
# router.register(r"owners", OwnersViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
# ]
