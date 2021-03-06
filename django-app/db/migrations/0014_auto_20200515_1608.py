# Generated by Django 2.2.5 on 2020-05-15 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0013_auto_20200428_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guests',
            field=models.IntegerField(default=0, help_text='총 인원 수를 입력하세요.'),
        ),
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('usd', 'USD'), ('krw', 'KRW')], default='krw', max_length=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('kr', 'Korean')], default='kr', max_length=2),
        ),
    ]
