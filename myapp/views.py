# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from rest_framework import generics
from .models import Jhumka
from .serializers import JhumkaSerializer

class JhumkaList(generics.ListAPIView):
    queryset = Jhumka.objects.all()
    serializer_class = JhumkaSerializer