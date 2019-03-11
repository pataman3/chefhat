# Generated by Django 2.1.7 on 2019-03-11 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20190311_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='type',
            field=models.CharField(choices=[('tsp', 'teaspoon'), ('tbsp', 'tablespoon'), ('c', 'cup'), ('oz', 'ounce'), ('lb', 'pound'), ('cl', 'clove')], max_length=32),
        ),
    ]
