# Generated by Django 3.2.4 on 2022-05-27 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0014_auto_20220526_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='resources',
        ),
        migrations.AddField(
            model_name='resource',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='framework.topic'),
        ),
    ]