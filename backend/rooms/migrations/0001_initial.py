# Generated by Django 2.1.5 on 2019-01-20 01:25

from django.db import migrations, models
import django.db.models.deletion
import rooms.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=None, max_length=20, unique=True)),
                ('mood', models.CharField(choices=[('any', 'any'), ('happy', 'happy'), ('sad', 'sad')], default='any', max_length=5)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms_as_admin', to='users.User')),
                ('users', models.ManyToManyField(related_name='rooms', to='users.User')),
            ],
            managers=[
                ('objects', rooms.managers.RoomManager()),
            ],
        ),
    ]