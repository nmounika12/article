# Generated by Django 5.1.3 on 2024-12-05 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('article', models.CharField(max_length=32)),
                ('prize', models.IntegerField()),
                ('genre', models.CharField(max_length=32)),
                ('objective', models.CharField(max_length=500)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]