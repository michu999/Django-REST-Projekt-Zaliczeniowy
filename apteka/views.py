from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.translation import gettextlazy as
from .models import Lek
from .serializers import LekSerializer
from .permissions import CzyTechnik, CzyLicencjat, CzyMagister

class LekViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lek.objects.all()
    serializer_class = LekSerializer

    def get_permissions(self):
        if self.action == 'lista_bez_recepty':
            return [CzyTechnik()]
        elif self.action == 'lista_na_recepte':
            return [CzyLicencjat()]
        elif self.action == 'lista_rpkw':
            return [CzyMagister()]
        return super().get_permissions()

    @action(detail=False, methods=['get'], urlpath='bez-recepty', name=('Leki bez recepty'))
    def lista_bez_recepty(self, request):
        leki = self.queryset.filter(kategoria='OTC')
        serializer = self.get_serializer(leki, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], urlpath='na-recepte', name=('Leki na receptę'))
    def lista_na_recepte(self, request):
        leki = self.queryset.filter(kategoria='PRESCRIPTION')
        serializer = self.get_serializer(leki, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], urlpath='rpkw', name=('Leki Rpw'))
    def lista_rpkw(self, request):
        leki = self.queryset.filter(kategoria='RPKW')
        serializer = self.get_serializer(leki, many=True)
        return Response(serializer.data)
