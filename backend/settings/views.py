from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserSettings
from .serializers import UserSettingsSerializer


class UserSettingsByUserView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            settings = UserSettings.objects.get(pk=pk)
        except UserSettings.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSettingsSerializer(settings, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        try:
            settings = UserSettings.objects.get(pk=pk)
        except UserSettings.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSettingsSerializer(settings, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            settings = UserSettings.objects.get(pk=pk)
        except UserSettings.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        settings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
