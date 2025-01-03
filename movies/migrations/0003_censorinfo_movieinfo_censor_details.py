# Generated by Django 5.1.4 on 2024-12-27 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movieinfo_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Censorinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=10, null=True)),
                ('certified_by', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='censor_details',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movie', to='movies.censorinfo'),
        ),
    ]
