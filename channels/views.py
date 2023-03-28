from channels.models import Channel
from channels.serializers import ChannelSerializer, ChannelSerializerMod, ChannelSerializerAddParent
from content.serializers import ContentSerializer
from django.core.validators import ValidationError

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

import logging

class ChannelList(viewsets.ModelViewSet):

	queryset = Channel.objects.all()

	def get_serializer_class(self):
		if self.action == 'contents':
			return ContentSerializer

		if self.action == 'addParent':
			return ChannelSerializerAddParent

		if self.request.method in ['PUT', 'PATCH']:
			return ChannelSerializerMod

		return ChannelSerializer


	@action(detail=True, methods=['post'])
	def addParent(self, request, pk=None):
		channel = Channel.objects.get(id=pk)

		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid():
			new_parent = Channel(**serializer.data)
			new_parent.parent = channel.parent

			try:
				new_parent.save()
			except ValidationError as err:
				return Response(err.messages, stats=status.HTTP_404_NOT_FOUND)

			try:
				channel.parent = new_parent
				channel.save()
			except ValidationError as err:
				return Response(err.messages, stats=status.HTTP_404_NOT_FOUND)

		return Response(serializer.data)

	@action(detail=True, methods=['get'])
	def subchannels(self, request, pk=None):
		children = Channel.objects.get(id=pk).get_children()

		page = self.paginate_queryset(children)

		if page:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = self.get_serializer(children, many=True)
		return Response(serializer.data)

	@action(detail=True, methods=['get'])
	def subtree(self, request, pk=None):
		subtree = Channel.objects.get(id=pk).get_descendants(include_self=False)

		page = self.paginate_queryset(subtree)

		if page:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = self.get_serializer(subtree, many=True)
		return Response(serializer.data)

	@action(detail=True, methods=['get'])
	def ancestors(self, request, pk=None):
		ancestors = Channel.objects.get(id=pk).get_ancestors(include_self=False)

		page = self.paginate_queryset(ancestors)

		if page:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = self.get_serializer(ancestors, many=True)
		return Response(serializer.data)

	@action(detail=True, methods=['get'])
	def siblings(self, request, pk=None):
		siblings = Channel.objects.get(id=pk).get_siblings()

		page = self.paginate_queryset(siblings)

		if page:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = self.get_serializer(siblings, many=True)
		return Response(serializer.data)

	@action(detail=True, methods=['get'])
	def contents(self, request, pk=None):
		contents = Channel.objects.get(id=pk).content

		page = self.paginate_queryset(contents)

		if page:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = self.get_serializer(contents, many=True)
		return Response(serializer.data)
