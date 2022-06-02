# Generated by Django 3.2.4 on 2022-06-01 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0004_resourcethroughtopic'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='relatedResources',
            field=models.ManyToManyField(through='framework.ResourceThroughTopic', to='framework.Resource'),
        ),
    ]