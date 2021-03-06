# Generated by Django 3.2.4 on 2021-10-22 13:13

from django.db import migrations, models
import geo.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AeroPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drone_id', models.CharField(default='0', max_length=500, verbose_name='Идентификатор дрона')),
                ('system_name', models.CharField(default='', max_length=500, verbose_name='Имя дрона')),
                ('center_freq', models.FloatField(default=0, verbose_name='Несущая частота')),
                ('brandwidth', models.FloatField(default=0, verbose_name='Пропускная способность')),
                ('detection_time', models.CharField(max_length=500, verbose_name='Время обнаружения')),
                ('comment_string', models.CharField(default='', max_length=500, verbose_name='Комментарии')),
                ('drone_lat', models.FloatField(default=0, max_length=10)),
                ('drone_lon', models.FloatField(default=0, max_length=10)),
                ('remote_lat', models.FloatField(default=0, verbose_name='Широта пульта')),
                ('remote_lon', models.FloatField(default=0, verbose_name='Долгота пульта')),
                ('azimuth', models.CharField(default='', max_length=500, verbose_name='Азимут')),
                ('area_sector_start_grad', models.FloatField(default=0, verbose_name='Внутренний радиус сектора')),
                ('area_sector_end_grad', models.FloatField(default=0, verbose_name='Внешний радиус сектора')),
                ('area_radius_m', models.FloatField(default=0, verbose_name='Радиус сектора (м)')),
                ('ip', models.CharField(default='', max_length=500, verbose_name='IP-адрес стрижа')),
                ('current_time', models.CharField(default='', max_length=500, verbose_name='Время засечки')),
                ('height', models.FloatField(default=0, verbose_name='Высота (м)')),
                ('strig_name', models.CharField(default='', max_length=500, verbose_name='Имя устройства')),
            ],
            options={
                'verbose_name': 'Аэропуп',
                'verbose_name_plural': 'Аэропупы',
            },
        ),
        migrations.CreateModel(
            name='ApemsConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strizh_name', models.CharField(default='стриж 0 (по умолчанию)', error_messages={'required': ''}, max_length=500, verbose_name='Имя стрижа')),
                ('freq_podavitelya', geo.models.IntegerRangeField(default=2400, error_messages={'required': ''}, verbose_name='Частота подавителя')),
                ('deg_podavitelya', geo.models.IntegerRangeField(default=60, error_messages={'required': ''}, verbose_name='Номер подавителя (60, 120 ...)')),
                ('type_podavitelya', models.CharField(choices=[('АПЕМ (Многоканальный)', 'АПЕМ (Многоканальный)'), ('Тестовый модуль', 'Тестовый модуль'), ('Шелест', 'Шелест'), ('Шелест (Многоканальный)', 'Шелест (Многоканальный)'), ('BarGen (Enter Morph)', 'BarGen (Enter Morph)'), ('BarGen (Плата Б)', 'BarGen (Плата Б)')], error_messages={'required': ''}, max_length=500, verbose_name='Тип подавителя')),
                ('ip_podavitelya', models.GenericIPAddressField(default='192.168.2.121', error_messages={'required': ''}, verbose_name='IP-адрес подавителя')),
                ('canal_podavitelya', geo.models.IntegerRangeField(default=0, error_messages={'required': ''}, verbose_name='Канал подавителя')),
                ('usileniye_db', geo.models.IntegerRangeField(default=0, error_messages={'required': ''}, verbose_name='Усиление')),
            ],
            options={
                'verbose_name': 'Конфигурация АПЕМ',
                'verbose_name_plural': 'АПЕМы',
                'ordering': ['-freq_podavitelya'],
            },
        ),
        migrations.CreateModel(
            name='DroneJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drone_id', models.CharField(default='0', max_length=500, verbose_name='Идентификатор дрона')),
                ('system_name', models.CharField(default='', max_length=500, verbose_name='Имя дрона')),
                ('center_freq', models.FloatField(default=0, verbose_name='Несущая частота')),
                ('brandwidth', models.FloatField(default=0, verbose_name='Пропускная способность')),
                ('detection_time', models.CharField(max_length=500, verbose_name='Время обнаружения')),
                ('comment_string', models.CharField(default='', max_length=500, verbose_name='Комментарии')),
                ('drone_lat', models.FloatField(default=0, max_length=10)),
                ('drone_lon', models.FloatField(default=0, max_length=10)),
                ('remote_lat', models.FloatField(default=0, verbose_name='Широта пульта')),
                ('remote_lon', models.FloatField(default=0, verbose_name='Долгота пульта')),
                ('azimuth', models.CharField(default='', max_length=500, verbose_name='Азимут')),
                ('area_sector_start_grad', models.FloatField(default=0, verbose_name='Внутренний радиус сектора')),
                ('area_sector_end_grad', models.FloatField(default=0, verbose_name='Внешний радиус сектора')),
                ('area_radius_m', models.FloatField(default=0, verbose_name='Радиус сектора (м)')),
                ('ip', models.CharField(default='', max_length=500, verbose_name='IP-адрес стрижа')),
                ('current_time', models.CharField(default='', max_length=500, verbose_name='Время засечки')),
                ('height', models.FloatField(default=0, verbose_name='Высота (м)')),
                ('strig_name', models.CharField(default='', max_length=500, verbose_name='Имя устройства')),
            ],
            options={
                'verbose_name': 'Дрон',
                'verbose_name_plural': 'Дроны',
            },
        ),
        migrations.CreateModel(
            name='DroneTrajectoryJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drone_id', models.CharField(default='0', max_length=500, verbose_name='Идентификатор дрона')),
                ('system_name', models.CharField(default='', max_length=500, verbose_name='Имя дрона')),
                ('center_freq', models.FloatField(default=0, verbose_name='Несущая частота')),
                ('brandwidth', models.FloatField(default=0, verbose_name='Пропускная способность')),
                ('detection_time', models.CharField(max_length=500, verbose_name='Время обнаружения')),
                ('comment_string', models.CharField(default='', max_length=500, verbose_name='Комментарии')),
                ('drone_lat', models.FloatField(default=0, max_length=10)),
                ('drone_lon', models.FloatField(default=0, max_length=10)),
                ('remote_lat', models.FloatField(default=0, verbose_name='Широта пульта')),
                ('remote_lon', models.FloatField(default=0, verbose_name='Долгота пульта')),
                ('azimuth', models.CharField(default='', max_length=500, verbose_name='Азимут')),
                ('area_sector_start_grad', models.FloatField(default=0, verbose_name='Внутренний радиус сектора')),
                ('area_sector_end_grad', models.FloatField(default=0, verbose_name='Внешний радиус сектора')),
                ('area_radius_m', models.FloatField(default=0, verbose_name='Радиус сектора (м)')),
                ('ip', models.CharField(default='', max_length=500, verbose_name='IP-адрес стрижа')),
                ('current_time', models.CharField(default='', max_length=500, verbose_name='Время засечки')),
                ('height', models.FloatField(default=0, verbose_name='Высота (м)')),
                ('strig_name', models.CharField(default='', max_length=500, verbose_name='Имя устройства')),
            ],
            options={
                'verbose_name': 'Дрон',
                'verbose_name_plural': 'Дроны',
            },
        ),
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_link', models.CharField(default='http://localhost:8000/static/spb_osm_new/{z}/{x}/{y}.png', error_messages={'required': ''}, max_length=500, verbose_name='Источник тайлов для карты (z/x/y)')),
                ('map_name', models.CharField(default='Спутниковая съемка', error_messages={'required': ''}, max_length=500, verbose_name='название карты')),
            ],
            options={
                'verbose_name': 'Карта',
                'verbose_name_plural': 'Карты',
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drone_id', models.CharField(default='', max_length=500, verbose_name='Идентификатор дрона')),
                ('system_name', models.CharField(max_length=500, verbose_name='Имя дрона')),
                ('center_freq', models.FloatField(verbose_name='Несущая частота')),
                ('brandwidth', models.FloatField(verbose_name='Пропускная способность')),
                ('detection_time', models.CharField(max_length=500, verbose_name='Время обнаружения')),
                ('comment_string', models.CharField(max_length=500, verbose_name='Комментарии')),
                ('drone_lat', models.FloatField(verbose_name='Широта')),
                ('drone_lon', models.FloatField(verbose_name='Долгота')),
                ('remote_lat', models.FloatField(default=0, verbose_name='Широта пульта')),
                ('remote_lon', models.FloatField(default=0, verbose_name='Долгота пульта')),
                ('azimuth', models.CharField(max_length=500, verbose_name='Азимут')),
                ('area_sector_start_grad', models.FloatField(verbose_name='Внутренний радиус сектора')),
                ('area_sector_end_grad', models.FloatField(verbose_name='Внешний радиус сектора')),
                ('area_radius_m', models.FloatField(default=None, verbose_name='Радиус сектора (м)')),
                ('ip', models.CharField(max_length=500, verbose_name='IP-адрес стрижа')),
                ('current_time', models.CharField(default='', max_length=500, verbose_name='Время засечки')),
                ('height', models.FloatField(default='', verbose_name='Высота (м)')),
                ('strig_name', models.CharField(default='', max_length=500, verbose_name='Имя стрижа')),
            ],
            options={
                'verbose_name': 'Дрон',
                'verbose_name_plural': 'Дроны',
            },
        ),
        migrations.CreateModel(
            name='SkyPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Скайпоинт 0 (по умолч.)', max_length=500, verbose_name='Имя устройства')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('lon', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
                ('ip', models.CharField(default='', max_length=500, verbose_name='IP')),
            ],
            options={
                'verbose_name': 'Скайпоинт',
                'verbose_name_plural': 'Скайпоинты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='StrigState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strig_name', models.CharField(max_length=500)),
                ('ip1_state', models.CharField(max_length=500)),
                ('ip2_state', models.CharField(max_length=500)),
                ('temperature', models.CharField(max_length=500)),
                ('temperature_state', models.CharField(max_length=500)),
                ('wetness', models.CharField(max_length=500)),
                ('wetness_state', models.CharField(max_length=500)),
                ('cooler', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Состояние стрижа',
                'verbose_name_plural': 'Состояния стрижей',
            },
        ),
        migrations.CreateModel(
            name='Strizh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='стриж 0 (по умолчанию)', max_length=500, verbose_name='Имя стрижа')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('lon', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
                ('ip1', models.CharField(default='', max_length=500, verbose_name='IP-адрес стрижа (хост 1)')),
                ('ip2', models.CharField(default='', max_length=500, verbose_name='IP-адрес стрижа (хост 2)')),
                ('uniping_ip', models.CharField(default='', max_length=500, verbose_name='IP-адрес Uniping')),
                ('radius', models.FloatField(blank=True, default=500, null=True, verbose_name='Радиус')),
                ('seconds_drone_show', models.IntegerField(default=10, verbose_name='Длительность отображения дрона')),
            ],
            options={
                'verbose_name': 'Стриж',
                'verbose_name_plural': 'Стрижи',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='StrizhJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filtered_strizhes', models.CharField(default='стриж 0 (по умолч.)', max_length=500, verbose_name='Нужные стрижи')),
                ('filtered_skypoints', models.CharField(default='skypoint 0 (по умолч.)', max_length=500, verbose_name='Нужные skypoints')),
                ('start_datetime', models.CharField(blank=True, max_length=50, null=True, verbose_name='Время начала')),
                ('end_datetime', models.CharField(blank=True, max_length=50, null=True, verbose_name='Время конца')),
            ],
            options={
                'verbose_name': 'Отфильтрованные стрижи',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='TimePick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_start', models.DateTimeField(blank=True, default='2000-01-01 00:00:01')),
                ('datetime_end', models.DateTimeField(blank=True, default='2100-01-01 00:00:01')),
            ],
            options={
                'verbose_name': 'Время',
                'verbose_name_plural': 'Время',
            },
        ),
    ]
