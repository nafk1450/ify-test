from django.db.models.signals import pre_delete
from django.dispatch import receiver
from rest_framework.serializers import ValidationError

from channels.models import Channel


@receiver(pre_delete, sender=Channel)
def channel_pre_delete(sender: Channel, instance: Channel, *args, **kwargs) -> None:
	if not instance.get_siblings():
		raise ValidationError(f"Channel {instance.name} doesn't have siblings hence it can't be deleted since it would result in an opened branch")
