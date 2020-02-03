from django.apps import AppConfig
import os

default_app_config='test01.Test01Config'

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class Test01Config(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name="牛肉安全数据库"