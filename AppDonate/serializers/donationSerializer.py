from AppDonate.models.donation import Donation
from rest_framework import serializers

class CreateDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id_donation','email','cardNumber','nameOnCard','amount','city'] #campos obligatorios para la creacion del objeto

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields =  ['id_donation','email','amount','city'] 