# Generated by Django 4.0 on 2022-12-24 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_user_email_alter_user_first_name_and_more'),
        ('confession', '0006_comment_image_confession_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfessionIdentityRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confession.confession')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
            options={
                'unique_together': {('user', 'confession')},
            },
        ),
    ]