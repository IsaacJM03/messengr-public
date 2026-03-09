import pytest
from django.contrib.auth.models import User
from messaging.models import Message # ImportError: attempted relative import with no known parent package -> decided to use a more absolute path
from messaging.serializers import MessageSerializer


@pytest.mark.django_db
def test_translation():
 u1=User.objects.create(username='a')
 u2=User.objects.create(username='b')
 msg=Message.objects.create(sender=u1,recipient=u2,text='Hello',language='fr')
 assert msg.translated_text()=="FR_Hello"

@pytest.mark.django_db
def test_sender_recipient():
 u1=User.objects.create(username='a')
 u2=User.objects.create(username='b')
 msg=Message.objects.create(sender=u1,recipient=u2,text='Hi',language='en')
 assert msg.sender==u1

@pytest.mark.django_db
def test_translated_text_unknown_language():
 u1=User.objects.create(username='x')
 u2=User.objects.create(username='y')
 msg=Message.objects.create(sender=u1,recipient=u2,text='Hola',language='de')
 assert msg.translated_text()=="Hola"
 
@pytest.mark.django_db
def test_serializer_create_keeps_sender_recipient():
 u1=User.objects.create(username='sender1')
 u2=User.objects.create(username='recipient1')
 data={"sender": u1.id, "recipient": u2.id, "text": "Test", "language": "en"}
 serializer = MessageSerializer(data=data)
 assert serializer.is_valid()
 msg = serializer.save()
 assert msg.sender==u1 and msg.recipient==u2   