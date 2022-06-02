# Generated by Django 3.2.4 on 2022-06-02 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('framework', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillThroughSuperskill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='framework.skill')),
            ],
            options={
                'ordering': ('superskill', 'order'),
            },
        ),
        migrations.CreateModel(
            name='Superskill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('superskillName', models.CharField(max_length=100)),
                ('relatedSkills', models.ManyToManyField(blank=True, through='framework.SkillThroughSuperskill', to='framework.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='skillthroughsuperskill',
            name='superskill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='superskill', to='framework.superskill'),
        ),
    ]