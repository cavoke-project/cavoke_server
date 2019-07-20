# Generated by Django 2.2.3 on 2019-07-20 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cavoke_app', '0007_auto_20190715_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_type_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('creator', models.CharField(max_length=100)),
                ('git_url', models.CharField(max_length=100)),
                ('description', models.CharField(default='No description', max_length=1000)),
                ('timesPlayed', models.IntegerField(default=0)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='gamesession',
            name='game_type_id',
        ),
        migrations.AddField(
            model_name='gamesession',
            name='game_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cavoke_app.GameType'),
        ),
    ]
