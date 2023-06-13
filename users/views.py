from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import CustomPermission


# Create your views here.
class UserView(APIView):
    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserByIdView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, CustomPermission]

    def get(self, req: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(req, user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, req: Request, user_id: int):
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(req, user)
        serializer = UserSerializer(user, req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
