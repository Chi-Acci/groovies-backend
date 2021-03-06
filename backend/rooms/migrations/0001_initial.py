# Generated by Django 2.1.5 on 2019-01-26 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=None, max_length=20, unique=True)),
                ('mood', models.CharField(choices=[('any', 'any'), ('happy', 'happy'), ('sad', 'sad')], default='any', max_length=5)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms_as_admin', to='users.User')),
                ('movies', models.ManyToManyField(related_name='rooms', to='movies.Movie')),
                ('users', models.ManyToManyField(related_name='rooms', to='users.User')),
            ],
        ),
    ]
