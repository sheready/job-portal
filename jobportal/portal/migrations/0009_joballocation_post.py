# Generated by Django 3.2.3 on 2021-05-22 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20210522_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='joballocation',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.jobs'),
        ),
    ]