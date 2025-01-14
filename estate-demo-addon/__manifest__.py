{
    "name": "Real Estate",
    "depends": [
        "base",
    ],
    "version": "18.0.0.1",
    "application": "True",
    "category": "Sales",
    "description": "Manage real estate offerings",
    "license": "LGPL-3",
    "data": [
        "security/ir.model.access.csv",

        "views/estate_property_views.xml",
        "views/estate_menus.xml",
    ],
    'assets': {
        'web.assets_frontend': [
            '/estate-demo-addon/static/src/img/moduleOdoo.JPG',
        ],
    },
    'icon': '/estate-demo-addon/static/src/img/moduleOdoo.JPG',
}
