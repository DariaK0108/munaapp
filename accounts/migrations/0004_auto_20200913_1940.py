# Generated by Django 3.1.1 on 2020-09-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200913_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interest',
            name='interest_id',
        ),
        migrations.AddField(
            model_name='interest',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='interests',
            field=models.ManyToManyField(default=None, related_name='user_interests', to='accounts.Interest'),
        ),
    ]