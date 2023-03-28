from content.models import Content
from content.serializers import ContentSerializer, ContentSerializerMod

from rest_framework import viewsets

class ContentList(viewsets.ModelViewSet):
	serializer_class = ContentSerializer
	mod_serializer_class = ContentSerializerMod
	
	queryset = Content.objects.all()

	def get_serializer_class(self):
		if self.request.method in ['PUT', 'POST', 'PATCH']:
			return self.mod_serializer_class
		return self.serializer_class
