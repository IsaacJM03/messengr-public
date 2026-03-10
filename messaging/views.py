from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Message
from .serializers import MessageSerializer

class MessageCreateView(APIView):
 def post(self, request):
    #  print(User.objects.all()) #no user exist -> <QuerySet []>, had to create two users
    #  sender = User.objects.first()
    #  recipient = User.objects.last()
    #  print(sender.id,recipient.id)
     user_list = User.objects.all()
     if (request.data.get("sender") not in user_list) or (request.data.get("recipient") not in user_list):
         return Response({"error": "Sender and recipient must exist"})
     data = {"sender": request.data.get("sender"), "recipient": request.data.get("recipient"), "text": request.data.get("text"), "language": request.data.get("language")}
     serializer = MessageSerializer(data=data)
     serializer.is_valid(raise_exception=True)
     msg = serializer.save()
     return Response({"message": msg.translated_text()})

class InboxView(APIView):
 def get(self, request):
     user = User.objects.first()
     msgs = Message.objects.filter(recipient=user)
     return Response([m.translated_text() for m in msgs])
