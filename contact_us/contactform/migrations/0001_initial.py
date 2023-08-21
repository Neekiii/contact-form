# Generated by Django 4.2.2 on 2023-06-19 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('mode_of_contact', models.CharField(max_length=50, verbose_name='Conatct by')),
                ('question_categories', models.CharField(max_length=50, verbose_name='How can we help you?')),
                ('message', models.TextField(max_length=3000)),
            ],
        ),
    ]