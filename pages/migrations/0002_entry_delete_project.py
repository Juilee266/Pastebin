# Generated by Django 4.2.9 on 2024-05-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_id', models.CharField(max_length=20)),
                ('text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
