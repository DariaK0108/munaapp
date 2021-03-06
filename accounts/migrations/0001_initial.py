# Generated by Django 3.1.1 on 2020-09-14 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('age', models.PositiveIntegerField(null=True)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('O', 'Other'), ('', 'Prefer not to say')], max_length=2, null=True)),
                ('education', models.CharField(choices=[('0', 'No schooling completed'), ('1', 'Nursery school to 8th grade'), ('2', 'Some high school, no diploma'), ('3', 'High school graduate, diploma or the equivalent'), ('4', 'Some college credit, no degree'), ('5', 'Trade/technical/vocational training'), ('6', 'Associate degree'), ('7', 'Bachelor’s degree'), ('8', 'Master’s degree'), ('9', 'Professional degree'), ('10', 'Doctorate degree'), ('', 'Prefer not to say')], max_length=30, null=True)),
                ('interests', models.ManyToManyField(default=None, related_name='user_interests', to='accounts.Interest')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
