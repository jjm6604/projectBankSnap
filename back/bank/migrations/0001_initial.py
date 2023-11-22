# Generated by Django 4.2.7 on 2023-11-21 23:49

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
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_co_no', models.CharField(max_length=20)),
                ('kor_co_nm', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DepositProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('fin_prdt_nm', models.TextField(default='none')),
                ('etc_note', models.TextField(default='none')),
                ('join_deny', models.IntegerField(default=-1)),
                ('join_member', models.TextField(default='none')),
                ('join_way', models.TextField(default='none')),
                ('spcl_cnd', models.TextField(default='none')),
                ('deposit_type', models.IntegerField(default=-1)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.bank')),
                ('like_users', models.ManyToManyField(related_name='like_products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DepositOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(default='none')),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('intr_rate', models.FloatField(default=-1, null=True)),
                ('intr_rate2', models.FloatField(default=-1, null=True)),
                ('save_trm', models.IntegerField(default=-1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.depositproduct')),
            ],
        ),
    ]
