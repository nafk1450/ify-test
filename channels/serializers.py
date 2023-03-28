from rest_framework import serializers
from channels.models import Channel
import logging

class ChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Channel
		fields = ['id', 'language', 'picture', 'name', 'parent', 'content']

class ChannelSerializerMod(serializers.ModelSerializer):
	class Meta:
		model = Channel
		fields = ['id', 'language', 'picture', 'name', 'content',]


class ChannelSerializerAddParent(serializers.ModelSerializer):
	class Meta:
		model = Channel
		fields = ['id', 'language', 'picture', 'name',]