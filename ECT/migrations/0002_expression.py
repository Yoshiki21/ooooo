# Generated by Django 3.0.5 on 2020-04-21 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ECT', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression_text', models.CharField(max_length=200)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ECT.Meeting')),
            ],
        ),
    ]
