# Generated by Django 2.2.6 on 2019-10-20 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0012_auto_20191018_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.CharField(default='Agregue Cliente', max_length=50),
        ),
        migrations.AddField(
            model_name='pedido',
            name='observacion',
            field=models.CharField(default='Ninguna..', max_length=20),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='precio',
            field=models.CharField(default=0, max_length=200),
        ),
    ]