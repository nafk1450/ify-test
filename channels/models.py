from django.db.models import Model, TextField, CharField, IntegerField, BooleanField, ForeignKey, ImageField, CASCADE, ManyToManyField
from tree.fields import PathField
from tree.models import TreeModelMixin
from django.core.validators import validate_image_file_extension, RegexValidator
from django.core.files.storage import FileSystemStorage
from django.core.validators import ValidationError
from content.models import Content
import logging

fs = FileSystemStorage(location='/media/channel_photo')

class Channel(Model, TreeModelMixin):

	language = CharField(max_length=2, default="ZZ", validators=[RegexValidator(regex='^[A-Z]{2}$', message='Not a valid language'),])
	picture = ImageField(storage=fs, default="placeholder.png", validators=[validate_image_file_extension,])
	
	name = CharField(max_length=30)
	parent = ForeignKey('self', null=True, blank=True, on_delete=CASCADE, related_name='children')
	position = IntegerField(default=1)
	path = PathField(order_by=['position', 'name',])
	public = BooleanField(default=False)

	content = ManyToManyField(Content, related_name='channel', blank=False)

	class Meta:
		ordering = ('path',)

	def clean(self, *args, **kwargs):

		if not self.id: # Creating
			if self.parent:
				if self.parent.content.all():
					raise ValidationError(f"Channel {self.parent.name} already has content, you cannot add a channel")

	def save(self, *args, **kwargs):

		self.full_clean()

		super(Channel, self).save(*args, **kwargs)

'''
class Group(Model):
	name = TextField(max_length=20)
'''