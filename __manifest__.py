{
    'name': "Estate Model",
    'version': "1.0",
    'summary': """Estate model dev.""",
    'author': "Emanoel Cardoso",
    'depends': ["crm"],
    'license': 'LGPL-3',
    'data': [
        #SECURITY
        "security/res_groups.xml",
        "security/ir.model.access.csv",

        #VIEWS
        "views/estate_property_views.xml",

        #MENU
        "views/estate_menus.xml",
    ],
    'demo': [
        "demo/demo.xml",
    ],
}