from rest_framework.viewsets import ModelViewSet
from shoes.models import ShoeColor,  ShoeType, Shoe, Manufacturer
from shoes.serializers import ManufacturerSerializer, ShoeColorSerializer, ShoeSerializer, ShoeTypeSerializer

# Create your views here.
class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()

class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    queryset =  ShoeColor.objects.all()

class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    queryset = ShoeType.objects.all()

class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    queryset = Shoe.objects.all()