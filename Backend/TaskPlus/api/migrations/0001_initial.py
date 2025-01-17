# Generated by Django 5.0.2 on 2024-02-22 00:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Workspace Name')),
                ('sector', models.CharField(max_length=255)),
                ('invite_code', models.CharField(max_length=5, verbose_name='Invite Code')),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('priority', models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], max_length=10)),
                ('ordered', models.BooleanField(default=False)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.workspace')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('priority', models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], max_length=10)),
                ('state', models.CharField(choices=[('missed', 'Missed'), ('complete', 'Complete'), ('incomplete', 'Incomplete')], max_length=10)),
                ('deadline', models.DateTimeField()),
                ('file_attachment', models.FileField(blank=True, null=True, upload_to='')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('order_position', models.IntegerField()),
                ('time_to_alert', models.DurationField(blank=True, null=True)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mission')),
                ('task_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_owned', to='api.member')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('time_posted', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.member')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.task')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='workspace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='api.workspace'),
        ),
    ]
