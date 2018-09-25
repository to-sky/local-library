# Generated by Django 2.1.1 on 2018-09-25 11:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7cfb45bc-d8e1-47f1-8134-a6af73a43232'), help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False),
        ),
    ]
