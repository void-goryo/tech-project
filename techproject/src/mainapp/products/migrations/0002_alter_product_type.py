# Generated by Django 4.0.3 on 2022-04-06 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('entrees', 'entrees'), ('treats', 'treats'), ('drinks', 'drinks')], max_length=60),
        ),
    ]