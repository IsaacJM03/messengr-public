from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
 class Meta:
     model = Message
     fields = "__all__"

     def validate(self, data):
        sender = data.get("sender")
        recipient = data.get("recipient")
        if sender and recipient and sender == recipient:
            raise serializers.ValidationError("sender and recipient must be different")
        return data

     def create(self, validated_data):
        return Message.objects.create(**validated_data)