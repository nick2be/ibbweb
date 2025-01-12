# Generated by Django 4.2.7 on 2025-01-10 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_message_da_contact_message_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='recaptcha_token',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='contact',
            name='company',
            field=models.CharField(blank=True, max_length=100, verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message_da',
            field=models.TextField(null=True, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message_en',
            field=models.TextField(null=True, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=200, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject_da',
            field=models.CharField(max_length=200, null=True, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Subject'),
        ),
    ]
