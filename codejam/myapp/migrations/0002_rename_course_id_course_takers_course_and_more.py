# Generated by Django 4.1.3 on 2022-11-19 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course_takers',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='course_takers',
            old_name='user_id',
            new_name='user',
        ),
    ]
