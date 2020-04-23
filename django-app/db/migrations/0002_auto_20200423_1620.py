# Generated by Django 2.2.5 on 2020-04-23 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='address',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AddField(
            model_name='room',
            name='baths',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='bedrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='beds',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='check_in',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='check_out',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='city',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='room',
            name='country',
            field=django_countries.fields.CountryField(default='KR', max_length=2),
        ),
        migrations.AddField(
            model_name='room',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='room',
            name='guests',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='room',
            name='instant_book',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
