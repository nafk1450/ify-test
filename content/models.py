from django.db.models import Model, FileField, DecimalField, TextField, CharField
from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/content')

class Content(Model):

	file = FileField(
		storage=fs,
		validators = [FileExtensionValidator(['pdf', 'txt', 'mp4',]),])

	rating = DecimalField(
		max_digits = 3,
		decimal_places = 1,
		validators = [
			MinValueValidator(0.0),
			MaxValueValidator(10.0),
		])
	
	description = TextField(max_length=200, default='Without description')
	author = CharField(max_length=30, default='Unknown author')
	genre = CharField(max_length=30, default='Unknown genre')
