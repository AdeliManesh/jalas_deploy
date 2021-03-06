# Generated by Django 3.0 on 2019-12-13 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('email', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_url', models.CharField(max_length=264)),
                ('title', models.CharField(max_length=264)),
                ('participants', models.ManyToManyField(to='first_app.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_id', models.IntegerField(default=0)),
                ('val', models.IntegerField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Participant')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_id', models.IntegerField(default=0)),
                ('start', models.CharField(max_length=264)),
                ('end', models.CharField(max_length=264)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=264)),
                ('end', models.CharField(max_length=264)),
                ('meeting_url', models.CharField(max_length=264)),
                ('creator', models.CharField(max_length=264)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Poll')),
            ],
        ),
    ]
