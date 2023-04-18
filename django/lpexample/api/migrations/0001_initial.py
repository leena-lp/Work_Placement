# Generated by Django 4.1.5 on 2023-04-06 05:22

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
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=100)),
                ('salary', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('female', 'female'), ('male', 'male')], max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('address', models.CharField(max_length=100)),
                ('profilepic', models.ImageField(blank=True, null=True, upload_to='images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]