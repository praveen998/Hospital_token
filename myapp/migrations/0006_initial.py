# Generated by Django 5.0.7 on 2024-07-31 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0005_delete_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
            ],
            options={
                'db_table': 'author',
            },
        ),
    ]
