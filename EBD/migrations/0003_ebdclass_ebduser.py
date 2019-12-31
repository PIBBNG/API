# Generated by Django 3.0.1 on 2019-12-31 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_permissions'),
        ('EBD', '0002_classregister_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='EBDClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ebd_class',
            },
        ),
        migrations.CreateModel(
            name='EBDUser',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ebd_class', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ebd_class', to='EBD.EBDClass')),
            ],
            options={
                'db_table': 'ebd_user',
            },
            bases=('users.customuser',),
        ),
    ]
