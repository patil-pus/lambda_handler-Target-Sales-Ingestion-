DEFAULT_KEYS={
    'customers.csv': 'customer_id',
    'geolocation.csv': 'geolocation_zip_code_prefix',
    'order_items.csv': 'order_item_id',
    'orders.csv': 'order_id',
    'payments.csv': 'payment_id',
    'products.csv': 'product_id',
    'sellers.csv': 'seller_id'
}

def infer_data_type(value):
    try:
        int(value)
        return 'N'
    except ValueError:
        try:
            float(value)
            return 'N'
        except ValueError:
            return 'S'
    
