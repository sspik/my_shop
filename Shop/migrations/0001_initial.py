# Generated by Django 3.1 on 2020-08-07 12:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('seo_title', models.CharField(max_length=255)),
                ('seo_description', models.CharField(max_length=255)),
                ('text', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.FileField(upload_to='catalog/%Y/%m/%d/')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Shop.catalog')),
            ],
            options={
                'verbose_name': 'Catalog',
                'verbose_name_plural': 'catalogs',
            },
        ),
        migrations.CreateModel(
            name='ProductFilterName',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Product variable name',
                'verbose_name_plural': 'product variable names',
            },
        ),
        migrations.CreateModel(
            name='ProductFilterValue',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=255)),
                ('value_type', models.CharField(choices=[('N', 'Number'), ('S', 'String')], default='S', max_length=1)),
            ],
            options={
                'verbose_name': 'Product variable value',
                'verbose_name_plural': 'product variable values',
            },
        ),
        migrations.CreateModel(
            name='ProductVariable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('var_name', models.CharField(max_length=255)),
                ('var_value', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'verbose_name': 'Product variable',
                'verbose_name_plural': 'product variables',
            },
        ),
        migrations.CreateModel(
            name='ProductFilter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('filter_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Shop.productfiltername')),
                ('filter_value', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Shop.productfiltervalue')),
            ],
            options={
                'verbose_name': 'Product filter',
                'verbose_name_plural': 'product filters',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('seo_title', models.CharField(max_length=255)),
                ('seo_description', models.CharField(max_length=255)),
                ('text', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('catalog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Shop.catalog')),
                ('variables', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.productvariable')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.AddField(
            model_name='catalog',
            name='product_filter',
            field=models.ManyToManyField(related_name='catalog', to='Shop.ProductFilter'),
        ),
    ]
