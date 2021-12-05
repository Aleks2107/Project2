# Generated by Django 3.2.9 on 2021-12-05 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('auther', models.CharField(max_length=50)),
                ('genre', models.TextField(blank=True, null=True)),
                ('status', models.CharField(max_length=50)),
                ('data', models.CharField(max_length=50)),
                ('give_out', models.CharField(max_length=50)),
                ('give_in', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
    ]