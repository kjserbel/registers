# Generated by Django 4.2.6 on 2023-10-28 22:09

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
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namecompleted', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=250)),
                ('man', models.BooleanField(default=False)),
                ('women', models.BooleanField(default=False)),
                ('education', models.CharField(max_length=200)),
                ('questionOne', models.CharField(max_length=250)),
                ('questionTwo', models.CharField(max_length=250)),
                ('questionTree', models.CharField(max_length=250)),
                ('questionFour', models.CharField(max_length=250)),
                ('questionFive', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datecompleted', models.DateTimeField(null=True, blank=True)),
                ('important', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]