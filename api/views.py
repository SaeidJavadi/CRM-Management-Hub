from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from api.permissions import IsCommonOrReadOnly, IsSuperUser
from django.contrib.auth import get_user_model
from crm import models as crmmod
from api import serializers


class UserList(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAdminUser, IsSuperUser)


class UsereDetail(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAdminUser, IsSuperUser)


class RevokeToken(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        request.auth.delete()
        return Response({"msg": "Token Revoked."})


class Common60View(ListCreateAPIView):
    queryset = crmmod.Common60.objects.all()
    serializer_class = serializers.Common60Serializer
    permission_classes = (IsCommonOrReadOnly,)


class Common60ViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = crmmod.Common60.objects.all()
    serializer_class = serializers.Common60Serializer
    permission_classes = (IsCommonOrReadOnly, IsSuperUser)

class Common60ViewSet(ModelViewSet):
    pass







class Common61View(ListCreateAPIView):
    queryset = crmmod.Common61.objects.all()
    serializer_class = serializers.Common61Serializer
    permission_classes = (IsCommonOrReadOnly, IsSuperUser)


class Common61ViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = crmmod.Common61.objects.all()
    serializer_class = serializers.Common61Serializer
    permission_classes = (IsCommonOrReadOnly, IsSuperUser)


class Common70View(ListCreateAPIView):
    queryset = crmmod.Common70.objects.all()
    serializer_class = serializers.Common70Serializer
    permission_classes = (IsCommonOrReadOnly, IsSuperUser)


class Common70ViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = crmmod.Common70.objects.all()
    serializer_class = serializers.Common70Serializer
    permission_classes = (IsCommonOrReadOnly, IsSuperUser)


class CommonDeadView(ListCreateAPIView):
    queryset = crmmod.CommonDead.objects.all()
    serializer_class = serializers.CommonDeadSerializer
    permission_classes = (IsCommonOrReadOnly, IsSuperUser)


class CommonDeadViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = crmmod.CommonDead.objects.all()
    serializer_class = serializers.CommonDeadSerializer
    permission_classes = (IsAdminUser, IsSuperUser)


class JudiciaryDeadView(ListCreateAPIView):
    queryset = crmmod.JudiciaryDead.objects.all()
    serializer_class = serializers.JudiciaryDeadSerializer
    permission_classes = (IsAdminUser, IsSuperUser)


class JudiciaryDeadViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = crmmod.JudiciaryDead.objects.all()
    serializer_class = serializers.JudiciaryDeadSerializer
    permission_classes = (IsAdminUser, IsSuperUser)


class DoingDeadView(ListCreateAPIView):
    queryset = crmmod.DoingDead.objects.all()
    serializer_class = serializers.DoingDeadSerializer
    permission_classes = (IsAdminUser, IsSuperUser)


class DoingDeadViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = crmmod.DoingDead.objects.all()
    serializer_class = serializers.DoingDeadSerializer
    permission_classes = (IsAdminUser, IsSuperUser)


class PublicAssistanceView(ListCreateAPIView):
    queryset = crmmod.PublicAssistance.objects.all()
    serializer_class = serializers.PublicAssistanceSerializer
    permission_classes = (IsAdminUser, IsSuperUser)


class PublicAssistanceViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = crmmod.PublicAssistance.objects.all()
    serializer_class = serializers.PublicAssistanceSerializer
    permission_classes = (IsAdminUser, IsSuperUser)
