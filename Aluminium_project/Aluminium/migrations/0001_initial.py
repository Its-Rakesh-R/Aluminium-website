# Generated by Django 3.2 on 2024-03-23 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIRSTNAME', models.CharField(max_length=20)),
                ('LASTNAME', models.CharField(max_length=20)),
                ('USERNAME', models.CharField(max_length=20)),
                ('PASSWORD', models.CharField(max_length=20)),
                ('GENDER', models.CharField(max_length=20)),
                ('Status', models.BooleanField(default=False)),
            ],
        ),
    ]