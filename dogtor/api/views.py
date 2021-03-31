# from rest_framework import viewsets   # Vistas con viewsets
from rest_framework import generics # vistas generic class  # 1 DRF Generic Class Views

from vet.models import PetOwner, Pet, BranchOffice
# 4 DRF Generic Class Views
from .serializers import OwnersListSerializer, OwnersSerializer, OwnersUpdateSerializer, OwnersDestroySerializer  
from .serializers import PetsListSerializer, PetsSerializer, PetsUpdateSerializer, PetsDestroySerializer
from .serializers import OfficesListSerializer, OfficesSerializer

# Create your views here.
# class OwnersViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet del modelo PetOwners.
#     """

#     queryset = PetOwner.objects.all()
#     serializer_class = OwnersSerializer

# CRUD Owners #
class ListOwnersAPIView(generics.ListAPIView):  # 2 DRF Generic Class Views
    queryset = PetOwner.objects.all()
    serializer_class = OwnersListSerializer # 5 DRF Generic Class Views

class CreateOwnersAPIView(generics.CreateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class RetrieveOwnersAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class UpdateOwnersAPIView(generics.UpdateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersUpdateSerializer

class DestroyOwnersAPIView(generics.DestroyAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersDestroySerializer

# CRUD Pets #
class ListPetsAPIView(generics.ListAPIView):  # 2 DRF Generic Class Views
    queryset = Pet.objects.all()
    serializer_class = PetsListSerializer # 5 DRF Generic Class Views

class CreatePetsAPIView(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class RetrievePetsAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class UpdatePetsAPIView(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsUpdateSerializer

class DestroyPetsAPIView(generics.DestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsDestroySerializer

# CRUD Office #
class ListOfficesAPIView(generics.ListAPIView):  # 2 DRF Generic Class Views
    queryset = BranchOffice.objects.all()
    serializer_class = OfficesListSerializer # 5 DRF Generic Class Views

class CreateOfficesAPIView(generics.CreateAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = OfficesSerializer

