# Generated by Django 4.0 on 2021-12-13 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_description', models.TextField()),
                ('question_answer', models.CharField(max_length=200)),
            ],
        ),
    ]