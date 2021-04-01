# Generated by Django 3.0.8 on 2020-07-29 17:17

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 7, 29, 17, 17, 38, 855375, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('comment', models.TextField()),
                ('image', models.CharField(blank=True, default='https://pluspng.com/img-png/user-png-icon-account-avatar-human-male-man-men-people-person-download-svg-download-png-edit-icon-512.png', max_length=200, null=True)),
                ('commented_at', models.DateTimeField(verbose_name=datetime.datetime(2020, 7, 29, 17, 17, 38, 855375, tzinfo=utc))),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
    ]