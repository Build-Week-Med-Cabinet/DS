# Generated by Django 2.2.5 on 2019-09-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrating',
            name='strain_name',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AlterField(
            model_name='userrating',
            name='userclass',
            field=models.CharField(blank=True, choices=[(0, 'default'), (1, 'recreational'), (2, 'medical')], default='default', max_length=100),
        ),
    ]