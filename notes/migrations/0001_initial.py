# Generated by Django 3.0.6 on 2020-05-12 10:40

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import sajibnotes.helper


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True, null=True)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240)),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('photo', models.ImageField(upload_to='notes/')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('is_delete', models.BooleanField(default=False)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(default=sajibnotes.helper.get_current_user, on_delete=django.db.models.deletion.CASCADE, to='account.Profile')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.Category')),
                ('comment', models.ManyToManyField(blank=True, to='notes.Comment')),
                ('tag', models.ManyToManyField(to='notes.Tag')),
            ],
        ),
    ]