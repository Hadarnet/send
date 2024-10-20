from django.http import HttpResponse
from rest_framework.views import APIView
# from asset.models import DigitalAsset
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


# @permission_classes([AllowAny])
# class RobotsTxtView(APIView):
#     def get(self, request):
#         lines = [
#             "User-agent: *",
#             "Disallow: /admin/",
#         ]        
#         assets = DigitalAsset.objects.all() 
#         for asset in assets:
#             lines.append(f"Disallow: /{asset.domain}/")

#         lines.append(f"Sitemap: http://localhost:8000{request.build_absolute_uri('/asset/sitemap.xml')}")

#         return HttpResponse("\n".join(lines), content_type="text/plain")
