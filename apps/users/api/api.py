from rest_framework.views import APIView
from rest_framework.response import Response
from apps.users.api.serializers import UserSerializer
from apps.users.models import User

class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        user_serializer = UserSerializer( users, many = True )
        return Response( user_serializer.data )