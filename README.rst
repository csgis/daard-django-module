=====
DAARD
=====

Daard is a Django app to build a Bone - Disease database.
The Modul will update a geoserver map which acts as an entrypoint.
A decoupled frontend will add user capabilities.

Quick start
-----------

1. Add "daard_database" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        # daard
        'categories',
        'categories.editor',
        'easy_select2',
        'daard_database',
        'geoposition',
        'import_export',
    ]

2. Include the polls URLconf in your project urls.py like this::

    from daard_database import urls as daard_urls
    ...
    urlpatterns += daard_urls.urlpatterns

3. Run ``python manage.py migrate`` to create the daard_database models.

4. Start the development server and visit http://127.0.0.1:8000/admin/

5. Visit http://127.0.0.1:8000/api/daard/ to visit the api

# load initial data

```
./manage.py loaddata /usr/src/daard-database/fixtures/Bone.json 
```

