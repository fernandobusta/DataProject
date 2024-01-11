# Generated by Django 4.1.5 on 2023-03-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_place_mydate'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mydate', models.DateTimeField(auto_now_add=True)),
                ('place_id', models.CharField(max_length=500)),
            ],
        ),
    ]