# Generated by Django 3.0.3 on 2020-02-20 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acamps_questions', '0004_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='team',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='acamps_questions.Team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='session',
            name='acamps_questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions_set', to='acamps_questions.AcampsQuestions'),
        ),
    ]
