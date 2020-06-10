# Generated by Django 3.0.6 on 2020-06-09 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_auto_20200609_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaimAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(upload_to='claims/')),
                ('claim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Claim')),
            ],
        ),
    ]