from django.db import migrations
from tree.operations import CreateTreeTrigger

class Migration(migrations.Migration):
    dependencies = [
        ('tree', '0001_initial'),
        ('channels', '0001_initial'),
    ]

    operations = [
        CreateTreeTrigger('channels.Channel'),
    ]