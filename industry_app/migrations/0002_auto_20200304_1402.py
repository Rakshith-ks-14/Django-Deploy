# Generated by Django 3.0.3 on 2020-03-04 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industry_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='price',
            field=models.IntegerField(),
        ),
    ]