# Generated by Django 3.2.19 on 2023-07-05 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]