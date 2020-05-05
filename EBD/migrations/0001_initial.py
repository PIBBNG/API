# Generated by Django 3.0.6 on 2020-05-05 15:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EBDClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'ebd_class',
            },
        ),
        migrations.CreateModel(
            name='EBDUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=25, unique=True)),
                ('name', models.CharField(default='--', max_length=50)),
                ('ebd_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ebd_class', to='EBD.EBDClass')),
            ],
            options={
                'db_table': 'ebd_user',
            },
        ),
        migrations.AddField(
            model_name='ebdclass',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ebd_teacher', to='EBD.EBDUser'),
        ),
        migrations.CreateModel(
            name='EBD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lesson_theme', models.CharField(blank=True, default='', help_text='Tema da EBD', max_length=255)),
                ('lesson_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesson_class', to='EBD.EBDClass')),
            ],
            options={
                'db_table': 'ebd',
            },
        ),
        migrations.CreateModel(
            name='ClassRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('bible', models.BooleanField(default=False)),
                ('lesson', models.BooleanField(default=False)),
                ('presence', models.BooleanField(default=False)),
                ('reading', models.BooleanField(default=False)),
                ('cult', models.BooleanField(default=False)),
                ('visitor', models.BooleanField(default=False)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_register', to='EBD.EBDUser')),
            ],
            options={
                'db_table': 'class_register',
            },
        ),
    ]
