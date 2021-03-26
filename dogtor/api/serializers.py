from rest_framework import serializers

from vet.models import PetOwner, Pet

# # Serializers define the API representation.
# Owners #
class OwnersListSerializer(serializers.ModelSerializer):  # 3 DRF Generic Class Views
    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name",]

class OwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = "__all__"

class OwnersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = "__all__"

class OwnersDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = "__all__"

# Pets #
class PetsListSerializer(serializers.ModelSerializer):  # 3 DRF Generic Class Views
    class Meta:
        model = Pet
        fields = ["id", "name", "type", "owner",]

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"

class PetsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"
    
class PetsDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"

# class OwnersSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = PetOwner
#         fields = [
#             "id",
#             "first_name",
#             "last_name",
#             "email",
#             "phone",
#             "address",
#             "created_at",
#         ]
    

