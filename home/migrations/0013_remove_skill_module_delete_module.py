# Generated by Django 4.1.12 on 2024-05-04 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_module_skill_progress_completed_skill_module_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='module',
        ),
        migrations.DeleteModel(
            name='Module',
        ),
    ]
