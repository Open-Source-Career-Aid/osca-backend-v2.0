# Generated by Django 3.2.4 on 2022-05-25 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0003_auto_20220525_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='superskill',
            name='superskill_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic_name',
            field=models.CharField(max_length=100),
        ),
    ]