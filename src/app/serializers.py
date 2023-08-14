from rest_framework import serializers

from app.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'foreign_id',
            'location_from',
            'location_to',
            'status',
            'datetime_created',
            'datetime_changed'
        )
        read_only_fields = (
            'id',
            'status',
            'datetime_created',
            'datetime_changed',
        )