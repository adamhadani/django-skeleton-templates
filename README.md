# django-skeleton-templates

Reusable Django skeleton project / app  templates

Starting with Django 1.4, you can now define templates for creating new projects / apps when running 'startproject' and 'startapp'.

## Usage

To use a project template, invoke startproject thus:

```bash
django-admin.py startproject --template /path/to/this-repository/project-template-01/ --extension py,md <yourprojectname>
```

For using with an app, as you'd expect:

```bash
django-admin.py startapp --template /path/to/this-repository/app-template-01/ --extension py,md <yourprojectname>/apps/<yourappname>
```

NOTE: I highly recommend you create your projects in separated virtualenv's.


## Credits

I've based some of this on the following project template which I recommend as a good starting point as well:

* https://github.com/amccloud/django-project-skel
* http://amccloud.com/post/14689947527/django-1-4-custom-project-template

