# Generated by Django 3.2.4 on 2022-05-26 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0012_auto_20220526_1852'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resource',
            options={'ordering': ('sort_order',)},
        ),
        migrations.RemoveField(
            model_name='resource',
            name='relatedTopic',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='subtopics',
        ),
        migrations.CreateModel(
            name='ResourceToTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='framework.resource')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='framework.topic')),
            ],
            options={
                'ordering': ('topic',),
            },
        ),
    ]
