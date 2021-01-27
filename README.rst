===========================
Django admin - No more blue
===========================
Django admin - no more blue is a Django app that let you choose a skin for your django admin. You can let your users to set their favorite theme on the session or you can choose to statically set the theme for the entire application.
With a variations of fruity themes you can now set a unique skin for your Django.

Color your environments! It's easier not to break something into production now.

Show me how to use it
---------------------
After you follow the guide bellow on getting started with django-admin-no-more-blue it should work like this:

If STATIC_THEME is False

The theme will be selected by every user and will be saved on the session

.. image:: https://github.com/CoLuiza/django-admin-no-more-blue/blob/master/docs/images/SCR1.PNG?raw=true

You can spot the CHANGE THEME button, don't be shy! Click it!

.. image:: https://github.com/CoLuiza/django-admin-no-more-blue/blob/master/docs/images/SCR2.PNG?raw=true

Let's say we change the theme to PLUM.

.. image:: https://github.com/CoLuiza/django-admin-no-more-blue/blob/master/docs/images/SCR3.PNG?raw=true

That's it, your theme is now purple and fine!

If STATIC_THEME is True

The select theme option will not be visible anymore and all the users will see the theme configured in settings.

.. image:: https://github.com/CoLuiza/django-admin-no-more-blue/blob/master/docs/images/SCR4.PNG?raw=true

As you can see, in the settings, the THEME is set to "apple".

Quick Start
-----------
* Add "no_more_blue" to your INSTALLED_APPS settings like this::

    INSTALLED_APPS = [
        'no_more_blue',
        ...
    ]

! The order is important

* In settings.py, make sure you have 'django.template.context_processors.request' added in the context_processors.
* In settings.py, at TEMPLATES section, inside 'OPTIONS', at the same level with context_processors, add::

    'libraries': {
                'themes': 'no_more_blue.templatetags.themes',
      }

TEMPLATES should look like this::

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request',
                     ...
                ],
                'libraries': {
                    'themes': 'no_more_blue.templatetags.themes',

                }
            },
        },
    ]

* Include URLconf into your project urls.py like this::

    from no_more_blue.urls import themes_urlpatterns
    ...

    urlpatterns = [
        path('themes/', include(themes_urlpatterns)),
        ...
    ]


* And as a final step add STATIC_THEME and THEME variables in your settings.

    STATIC_THEME - True/False depending on whether you want the theme to be static and all the users will have the same theme.
    THEME - if the theme is static (STATIC_THEME = True) you can set which theme you want to be rendered. Here you should set the AKA for the theme.

List of themes:
   =========  ===================  ========
    AKA         TITLE               COLOR
   =========  ===================  ========
   base         Base Theme          Light blue
   blueberry    Blueberry Theme     Blue
   apple        Green Apple Theme   Green
   melon        Melon Theme         Dark Green
   peach        Peach Theme         Orange
   plum         Plum Theme          Light Purple
   grapes       Grapes Theme        Purple
   =========  ===================  ========
