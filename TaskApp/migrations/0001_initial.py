# Generated by Django 3.2.6 on 2021-08-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('text', models.TextField(null=True)),
            ],
        ),
    ]
