# Generated by Django 2.1 on 2019-06-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredient', '0003_auto_20190628_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='content',
            field=models.CharField(max_length=1000),
        ),
    ]
