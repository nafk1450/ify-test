from rest_framework import serializers
from content.models import Content

class ContentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Content
		fields = ['id', 'file', 'rating', 'description', 'author', 'genre', 'channel']

class ContentSerializerMod(serializers.ModelSerializer):
	class Meta:
		model = Content
		fields = ['id', 'file', 'rating', 'description', 'author', 'genre']