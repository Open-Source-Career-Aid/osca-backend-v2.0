# Generated by Django 3.2.4 on 2022-05-25 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0006_auto_20220525_0632'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resource',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='resource',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=True, verbose_name='order'),
            preserve_default=False,
        ),
    ]
