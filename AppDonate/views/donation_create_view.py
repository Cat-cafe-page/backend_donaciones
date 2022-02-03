from rest_framework                                  import serializers, status, views
from rest_framework.response                         import Response
from rest_framework_simplejwt.serializers            import TokenObtainPairSerializer
from AppDonate.serializers.donationSerializer        import CreateDonationSerializer, DonationSerializer

class DonationCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreateDonationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializers_mostrar = DonationSerializer(data = serializer.data) 
        serializers_mostrar.is_valid()
        return Response(serializers_mostrar.data) 