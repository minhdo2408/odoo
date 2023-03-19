{
    'name': 'Apartment_service',
    'version': '1.0',
    'summary': 'Quản lý dịch vụ chung cư',
    'description': 'Hỗ trợ quản lý hóa đơn dịch vụ của cư dân',
    'category': 'Category',
    'author': 'Minh Do',
    'depends': [],
    'data': [
        'views/service_view.xml',
        'views/customer_view.xml',
        'views/bill_view.xml',
        'views/vehicle_view.xml',
        'views/price_view.xml',
        'views/apartment_view.xml',
        'security/apartment_service_security.xml',
        'security/ir.model.access.csv',
        'wizard/date_to_leave_view.xml',
        'wizard/date_to_paid_view.xml'
    ],
    'application': True,
    'installable': True,
    'auto_install': False
}
