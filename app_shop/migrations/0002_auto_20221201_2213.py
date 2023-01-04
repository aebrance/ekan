# Generated by Django 3.2.5 on 2022-12-02 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorias',
            name='nombre',
            field=models.CharField(db_index=True, default='Categoria', max_length=100),
        ),
        migrations.AddField(
            model_name='categorias',
            name='slug',
            field=models.SlugField(default='url', max_length=100),
        ),
        migrations.AddField(
            model_name='productos',
            name='articulo',
            field=models.CharField(default='0000', max_length=4),
        ),
        migrations.AddField(
            model_name='productos',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_shop.categorias'),
        ),
        migrations.AddField(
            model_name='productos',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de publicación'),
        ),
        migrations.AddField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='producto/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='productos',
            name='precio_mayor',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='productos',
            name='precio_menor',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='productos',
            name='producto',
            field=models.CharField(default='Producto', max_length=50),
        ),
        migrations.AddField(
            model_name='productos',
            name='stock_disonible',
            field=models.IntegerField(default=0),
        ),
    ]
