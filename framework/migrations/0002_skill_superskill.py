# Generated by Django 3.2.4 on 2022-05-23 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('subskills', models.ManyToManyField(blank=True, related_name='subskills_under_subskill', to='framework.Skill')),
                ('topics', models.ManyToManyField(blank=True, related_name='subskill_topics', to='framework.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='Superskill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('superskill_name', models.CharField(max_length=100)),
                ('Skills', models.ManyToManyField(blank=True, related_name='super_skill', to='framework.Skill')),
            ],
        ),
    ]