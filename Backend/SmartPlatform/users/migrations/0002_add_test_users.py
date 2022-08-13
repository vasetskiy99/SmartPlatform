from django.contrib.auth.models import User
from django.db import migrations
from django.contrib.auth.hashers import make_password


def load_admin(apps, schema_editor):
    admin = User.objects.create(
        email='admin@admin.admin',
        username='admin',
        password=make_password('1'),
        first_name='Андрей',
        last_name='Васецкий',
        is_superuser=True,
        is_staff=True
    )
    profile_type = apps.get_model("users", "Profile")
    super_user = profile_type.objects.create(user_id=admin.id)
    super_user.save()


def load_test_user_with_device(apps, schema_editor):

    user = User.objects.create(
        email='test_user@test.test',
        username='test_user',
        password=make_password('test'),
        first_name='Test',
        last_name='User',
    )
    profile_type = apps.get_model("users", "Profile")
    profile_type_test = profile_type.objects.create(user_id=user.id)
    profile_type_test.save()

    device_type = apps.get_model("users", "Device")
    device_type_test = device_type.objects.create(owner_id=user.id, name="Тестовое устройство")
    device_type_test.save()


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_admin),
        migrations.RunPython(load_test_user_with_device),
    ]
