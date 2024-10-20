from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StreetSerializer, CitySerializer, CountrySerializer, ContinentSerializer
from .models import Street, City, Country, Continent

# Views for Continent model
class ContinentListCreateAPIView(APIView):
    """
    List all continents or create a new continent.
    """
    def get(self, request):
        """
        List all continents.
        """
        continents = Continent.objects.all()
        serializer = ContinentSerializer(continents, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new continent.
        """
        serializer = ContinentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContinentDetailAPIView(APIView):
    """
    Retrieve, update, or delete a specific continent.
    """
    def get_object(self, pk):
        """
        Get a continent by primary key.
        """
        try:
            return Continent.objects.get(pk=pk)
        except Continent.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieve a specific continent.
        """
        continent = self.get_object(pk)
        serializer = ContinentSerializer(continent)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a specific continent.
        """
        continent = self.get_object(pk)
        serializer = ContinentSerializer(continent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific continent.
        """
        continent = self.get_object(pk)
        continent.delete()
        continents = Continent.objects.all()
        serializer = ContinentSerializer(continents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Views for Country model
class CountryListCreateAPIView(APIView):
    """
    List all countries or create a new country.
    """
    def get(self, request):
        """
        List all countries.
        """
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new country.
        """
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CountryDetailAPIView(APIView):
    """
    Retrieve, update, or delete a specific country.
    """
    def get_object(self, pk):
        """
        Get a country by primary key.
        """
        try:
            return Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieve a specific country.
        """
        country = self.get_object(pk)
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a specific country.
        """
        country = self.get_object(pk)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific country.
        """
        country = self.get_object(pk)
        country.delete()
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Views for City model
class CityListCreateAPIView(APIView):
    """
    List all cities or create a new city.
    """
    def get(self, request):
        """
        List all cities.
        """
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new city.
        """
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CityDetailAPIView(APIView):
    """
    Retrieve, update, or delete a specific city.
    """
    def get_object(self, pk):
        """
        Get a city by primary key.
        """
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieve a specific city.
        """
        city = self.get_object(pk)
        serializer = CitySerializer(city)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a specific city.
        """
        city = self.get_object(pk)
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific city.
        """
        city = self.get_object(pk)
        city.delete()
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StreetListCreateAPIView(APIView):
    """
    List all streets or create a new street.
    """
    def get(self, request):
        """
        List all streets.
        """
        streets = Street.objects.all()
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new street.
        """
        serializer = StreetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreetDetailAPIView(APIView):
    """
    Retrieve, update, or delete a specific street.
    """
    def get_object(self, pk):
        """
        Get a street by primary key.
        """
        try:
            return Street.objects.get(pk=pk)
        except Street.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Retrieve a specific street.
        """
        street = self.get_object(pk)
        serializer = StreetSerializer(street)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a specific street.
        """
        street = self.get_object(pk)
        serializer = StreetSerializer(street, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific street.
        """
        street = self.get_object(pk)
        street.delete()
        streets = Street.objects.all()
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)