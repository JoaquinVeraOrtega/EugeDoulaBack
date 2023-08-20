# Generated by Django 4.2.4 on 2023-08-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='facebook',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='instagram',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='quote',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='youtube',
            field=models.URLField(null=True),
        ),
    ]