# Generated by Django 4.1.5 on 2023-10-10 19:18

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
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small_string', models.CharField(default='Default value', max_length=64)),
                ('big_string', models.TextField()),
                ('data_post', models.DateField(auto_now_add=True)),
                ('categoryType', models.CharField(choices=[('TN', 'ТАНКИ'), ('HL', 'ХИЛЫ'), ('DD', 'ДД'), ('MR', 'ТОРГОВЦЫ'), ('GM', 'ГИЛДМАТЕРА'), ('QG', 'КВЕСТГИВЕРЫ'), ('BS', 'КУЗНЕЦЫ'), ('PM', 'ЗЕЛЬЕВАРЫ'), ('MK', 'МАСТЕРА ЗАКЛИНАНИЙ'), ('TR', 'КОЖЕВНИКИ')], default='ВЫБЕРИТЕ КАТЕГОРИЮ ОБЪЯВЛЕНИЯ', max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.category')),
                ('postThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='postCategory',
            field=models.ManyToManyField(through='accounts.PostCategory', to='accounts.category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('commentPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.post')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]