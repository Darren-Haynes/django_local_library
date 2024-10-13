# Generated by Django 4.2.16 on 2024-10-13 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='language',
            field=models.CharField(blank=True, help_text="Enter the book's language (e.g. English, Mandarin etc.)", max_length=20, unique=True),
        ),
    ]
