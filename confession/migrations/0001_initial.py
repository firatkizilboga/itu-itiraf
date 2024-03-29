# Generated by Django 4.0 on 2022-12-23 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Confession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('author', models.CharField(default='Anonim', max_length=80)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Anonim', max_length=80)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('confession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='confession.confession')),
            ],
        ),
    ]
