# Generated by Django 3.2.19 on 2023-08-04 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_weight'),
        ('blog', '0002_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cross_sell',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.product'),
        ),
    ]