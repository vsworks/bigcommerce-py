from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="BC",
    settings_files=[
        'settings.toml',
        'constants.toml',  # load project constants (e.g. BC API base URLs)
        '.secrets.toml',
    ],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
