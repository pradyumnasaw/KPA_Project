from rest_framework import serializers
from .models import KPAForm

class KPAFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = KPAForm
        fields = '__all__'
    def validate_email(self, value):
        if not value.endswith('@example.com'):
            raise serializers.ValidationError("Email must be from the domain '@example.com'")
        return value
    def validate_phone(self, value):
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Phone number must be at least 10 digits long and contain only numbers")
        return value