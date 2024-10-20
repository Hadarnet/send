from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Business
from .serializers import BusinessSerializer, MyBusinessSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from django.db import models
import uuid
from rest_framework.pagination import PageNumberPagination
from django.db.models import F, Func, FloatField


User = get_user_model()


class BusinessSearchView(APIView):
    """
    View to search businesses by name and category.
    """
    def get(self, request, *args, **kwargs):
        name = request.query_params.get('name', None)
        category_name = request.query_params.get('category', None)

        # Initial queryset
        queryset = Business.objects.all()

        # Filter by name if provided
        if name:
            queryset = queryset.filter(name__icontains=name)

        # Filter by category if provided
        if category_name:
            queryset = queryset.filter(category__name__iexact=category_name)

        if not name and not category_name:
            return Response({"detail": "At least one of 'name' or 'category' parameters is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Pagination
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset, request)
        serializer = BusinessSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)

class Distance(Func):
    function = 'ST_DistanceSphere'
    template = '%(function)s(%(expressions)s)'

    def __init__(self, *expressions, **extra):
        super().__init__(*expressions, output_field=FloatField(), **extra)



class BusinessRadiusFilterView(APIView):
    """
    View to filter businesses by a radius from a given point.
    """
    def get(self, request, *args, **kwargs):
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        radius = request.query_params.get('radius')

        if not latitude or not longitude or not radius:
            return Response({"detail": "Latitude, longitude, and radius are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            latitude = float(latitude)
            longitude = float(longitude)
            radius = float(radius)
        except ValueError:
            return Response({"detail": "Invalid input for latitude, longitude, or radius."}, status=status.HTTP_400_BAD_REQUEST)

        # Calculate the distance and filter the queryset
        businesses = Business.objects.annotate(
            distance=Distance(
                F('longitude'),
                F('latitude'),
                longitude, latitude
            )
        ).filter(distance__lte=radius).order_by('distance')  # Ensure ordering

        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BusinessListView(APIView):
    """
    View to list all businesses.
    """
    def get(self, request):
        """
        Return a list of all businesses.
        """
        businesses = Business.objects.all()
        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)

class BusinessCreateView(APIView):
    def post(self, request):
        """
        Create a new business.
        """
        serializer = BusinessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BusinessDetailView(APIView):
    """
    View to retrieve, update, or delete a business instance.
    """
    def get_object(self, pk):
        """
        Get a business instance by primary key.
        """
        try:
            return Business.objects.get(pk=pk)
        except Business.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Return a single business instance.
        """
        business = self.get_object(pk)
        serializer = BusinessSerializer(business)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update an existing business instance.
        """
        business = self.get_object(pk)
        serializer = BusinessSerializer(business, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a business instance.
        """
        business = self.get_object(pk)
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserBusinessListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id, *args, **kwargs):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        businesses = user.get_businesses()
        print(f"Businesses found: {businesses}")  # הוסף הדפסה לדיבוג

        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MyBusinessListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, business_id, *args, **kwargs):
        try:
            business = Business.objects.get(id=business_id)
        except Business.DoesNotExist:
            return Response({"detail": "Business not found."}, status=status.HTTP_404_NOT_FOUND)

        my_businesses = business.user_businesses.all()
        serializer = MyBusinessSerializer(my_businesses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BusinessFilterView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        category_name = request.query_params.get('category')
        city_name = request.query_params.get('city')
        country_name = request.query_params.get('country')

        queryset = Business.objects.all()

        if category_name:
            queryset = queryset.filter(category__name__iexact=category_name)
        if country_name:
            queryset = queryset.filter(country__name__iexact=country_name)
        if city_name:
            queryset = queryset.filter(city__name__iexact=city_name)

        # Paginate the results
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset, request)
        serializer = BusinessSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)

