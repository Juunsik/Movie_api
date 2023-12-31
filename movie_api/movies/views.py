from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from .models import Movie, Actor, Review
from .serializers import MovieSerializer, ActorSerializer, ReviewSerializer

# Create your views here.


# 개별 페이지네이션 설정
class MoviePageNumberPagination(PageNumberPagination):
    page_size = 2


class ActorPageNumberPagination(PageNumberPagination):
    page_size = 5


# Use ListCreateAPIView : 제네릭 뷰 - 데이터 생성, 조회
class MovieList(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePageNumberPagination


# Use RetrieveUpdateDestroyAPIView : 제네릭 뷰 - 데이터 조회, 수정, 삭제
class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReviewList(ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie = get_object_or_404(Movie, pk=self.kwargs.get("pk"))
        return Review.objects.filter(movie=movie)

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs.get("pk"))
        serializer.save(movie=movie)


class ActorList(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    pagination_class = ActorPageNumberPagination


class ActorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


# Use APIView
# class MovieList(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class MovieDetail(APIView):
#     def get_object(self, pk):
#         movie = get_object_or_404(Movie, pk=pk)
#         return movie

#     def get(self, request, pk):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     def patch(self, request, pk):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         movie = self.get_object(pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ActorList(APIView):
#     def get(self, request):
#         actors = Actor.objects.all()
#         serializer = ActorSerializer(actors, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ActorSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ActorDetail(APIView):
#     def get_object(self, pk):
#         actor = get_object_or_404(Actor, pk=pk)
#         return actor

#     def get(self, request, pk):
#         actor = self.get_object(pk)
#         serializer = ActorSerializer(actor)
#         return Response(serializer.data)

#     def patch(self, request, pk):
#         actor = self.get_object(pk)
#         serializer = ActorSerializer(actor, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.data()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         actor = self.get_object(pk)
#         actor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# ---------------------------------------------------------------------------------------


# Use api_view decorator
# @api_view(["GET", "POST"])
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         data = request.data
#         serializer = MovieSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PATCH", "DELETE"])
# def movie_detail(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#     if request.method == "GET":
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "PATCH":
#         serializer = MovieSerializer(movie, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "POST"])
# def review_list(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#     if request.method == "GET":
#         reviews = Review.objects.filter(movie=movie)
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(movie=movie)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "POST"])
# def actor_list(request):
#     if request.method == "GET":
#         actors = Actor.objects.all()
#         serializer = ActorSerializer(actors, many=True)
#         return Response(serializer.data, status=200)
#     elif request.method == "POST":
#         data = request.data
#         serializer = ActorSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PATCH", "DELETE"])
# def actor_detail(request, pk):
#     actor = get_object_or_404(Actor, pk=pk)
#     if request.method == "GET":
#         serializer = ActorSerializer(actor)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "PATCH":
#         serializer = ActorSerializer(actor, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == "DELETE":
#         actor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# ---------------------------------------------------------------------------------------
