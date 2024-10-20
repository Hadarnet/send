from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserSettings
from .serializers import UserSettingsSerializer

class UserSettingsListView(APIView):
    def get(self, request, *args, **kwargs):
        settings = UserSettings.objects.all()
        serializer = UserSettingsSerializer(settings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
