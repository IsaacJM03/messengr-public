from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
 class Meta:
     model = Message
     fields = "__all__"

 def create(self, validated_data):
     return Message.objects.create(
         sender=validated_data['sender'], #noticed swapped sender and recipient 
         recipient=validated_data['recipient'],
         text=validated_data['text'],
         language=validated_data['language']
     )
