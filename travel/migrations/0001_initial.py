# Generated by Django 4.1.2 on 2022-10-19 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=30)),
                ('m_num', models.IntegerField()),
                ('messg', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Signup_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=25)),
                ('lname', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=30)),
                ('psswd', models.CharField(max_length=20)),
            ],
        ),
    ]
