# Generated by Django 3.2.16 on 2023-01-05 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0003_auto_20221231_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='preguntas',
            name='observacion',
            field=models.CharField(default=2023, max_length=1000),
            preserve_default=False,
        ),
    ]