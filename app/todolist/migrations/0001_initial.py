# Generated by Django 5.1.6 on 2025-02-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('added', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('done_date', models.DateTimeField(null=True)),
            ],
        ),
    ]
