from django.conf                         import settings
from rest_framework                      import generics, status

from AppDonate.models.donation import Donation
from AppDonate.serializers.donationSerializer import CreateDonationSerializer, DonationSerializer

class DonationDetailView(generics.RetrieveAPIView):
    queryset            = Donation.objects.all()
    serializer_class    = DonationSerializer
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

class AllDonationDetailView(generics.ListAPIView):
    queryset         = Donation.objects.all()
    serializer_class = DonationSerializer

#get donation by user email
class DonationByUserEmailView(generics.ListAPIView):
    queryset         = Donation.objects.all()
    serializer_class = DonationSerializer  
    def get_queryset(self):
        queryset = Donation.objects.filter(email=self.kwargs["email"])
        return queryset

#get donation by city
class DonationByCityView(generics.ListAPIView):
    queryset         = Donation.objects.all()
    serializer_class = DonationSerializer  
    def get_queryset(self):
        queryset = Donation.objects.filter(city=self.kwargs["city"])
        return queryset

