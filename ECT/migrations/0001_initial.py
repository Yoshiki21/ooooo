# Generated by Django 3.0.5 on 2020-04-20 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_text', models.CharField(max_length=200)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ECT.Meeting')),
            ],
        ),
    ]
