# Generated by Django 2.2 on 2021-03-10 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notes',
            field=models.TextField(default='A Book'),
        ),
        migrations.AddField(
            model_name='books',
            name='desc',
            field=models.TextField(default={models.CharField(max_length=255)}),
        ),
    ]