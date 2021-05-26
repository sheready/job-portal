# Generated by Django 3.2.3 on 2021-05-22 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=200, null=True)),
                ('jobinstruction', models.CharField(max_length=200, null=True)),
                ('jobsample', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='joballocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Job allocated', 'Job allocated'), ('Job allocated', 'Job allocated'), ('Job not allocated', 'Job not allocated')], max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='name',
            new_name='employeename',
        ),
    ]
