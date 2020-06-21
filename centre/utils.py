import imp


def get_default_django_settings_module():
    try:
        file_ = imp.find_module('local', ['centre/settings'])[0]
    except ImportError:
        default_django_settings_module = "centre.settings.base"
    else:
        default_django_settings_module = "centre.settings.local"
        file_.close()
    print(default_django_settings_module)
    return default_django_settings_module
