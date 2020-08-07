# Generated by Django 3.1 on 2020-08-07 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0002_auto_20200807_1521'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productfilter',
            options={'verbose_name': 'Product variable name', 'verbose_name_plural': 'product variable names'},
        ),
        migrations.AddField(
            model_name='productfilter',
            name='value_type',
            field=models.CharField(choices=[('N', 'Number'), ('S', 'String'), ('B', 'Boolean')], default='S', max_length=1),
        ),
        migrations.AlterField(
            model_name='productfiltervalue',
            name='filter_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_filter_value', to='filters.productfilter'),
        ),
        migrations.DeleteModel(
            name='ProductFilterName',
        ),
    ]
