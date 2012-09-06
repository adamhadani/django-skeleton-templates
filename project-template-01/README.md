# {{ project_name|title }} Django Project #
## Prerequisites ##

- python >= 2.5
- pip
- virtualenv/wrapper (optional)
- django-boss (CLI helpers for django, removes need for per-project manage.py)

## Installation ##
### Creating the environment ###
Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv --no-site-packages {{ project_name }}-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages {{ project_name }}-env
cd {{ project_name }}-env
source bin/activate
```

### Clone the code ###
Obtain the url to your git repository.

```bash
git clone <URL_TO_GIT_RESPOSITORY> {{ project_name }}
```

### Install requirements ###
```bash
cd {{ project_name }}
pip install -r requirements.txt
```

### Configure project ###
In your virtual environment postactivate hook (when using virtualenvwrapper),
Add the directive to point to relevant DJANGO_SETTINGS_MODULE, e.g for development settings:
```bash
export DJANGO_SETTINGS_MODULE={{ project_name }}.configs.development.settings
```

### Sync database ###
```bash
djboss manage syncdb
```

## Running ##
```bash
djboss manage runserver
```

Open browser to http://127.0.0.1:8000

