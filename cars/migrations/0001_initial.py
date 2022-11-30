# Generated by Django 4.1.3 on 2022-11-25 01:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompilerModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('code', models.TextField()),
                ('success', models.CharField(blank=True, max_length=555, null=True)),
                ('fail', models.CharField(blank=True, max_length=250, null=True)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]