# Generated by Django 4.1.3 on 2022-11-19 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_users_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
        migrations.RenameModel(
            old_name='Course_takers',
            new_name='Course_taker',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
