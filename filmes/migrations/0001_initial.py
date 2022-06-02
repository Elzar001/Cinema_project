# Generated by Django 4.0.5 on 2022-06-01 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('name', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='images')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filmes', to='filmes.genre')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmes',
                'ordering': ['title'],
            },
        ),
    ]
