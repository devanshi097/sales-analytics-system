def parse_transactions(raw_lines):
    """
    Parses raw lines into clean list of dictionaries
    """
    transactions = []

    for line in raw_lines:
        parts = line.split('|')

        if len(parts) != 8:
            continue

        transaction_id = parts[0]
        date = parts[1]
        product_id = parts[2]
        product_name = parts[3].replace(',', '')
        quantity = parts[4]
        unit_price = parts[5]
        customer_id = parts[6]
        region = parts[7]

        try:
            quantity = int(quantity.replace(',', ''))
            unit_price = float(unit_price.replace(',', ''))
        except ValueError:
            continue

        transaction = {
            'TransactionID': transaction_id,
            'Date': date,
            'ProductID': product_id,
            'ProductName': product_name,
            'Quantity': quantity,
            'UnitPrice': unit_price,
            'CustomerID': customer_id,
            'Region': region
        }

        transactions.append(transaction)

    return transactions

def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    """
    Validates transactions and applies optional filters
    """
    valid_transactions = []
    invalid_count = 0

    for tx in transactions:
        if not tx['TransactionID'].startswith('T'):
            invalid_count += 1
            continue

        if not tx['ProductID'].startswith('P'):
            invalid_count += 1
            continue

        if tx['Quantity'] <= 0 or tx['UnitPrice'] <= 0:
            invalid_count += 1
            continue

        if not tx['CustomerID'] or not tx['Region']:
            invalid_count += 1
            continue

        amount = tx['Quantity'] * tx['UnitPrice']

        if region and tx['Region'] != region:
            continue

        if min_amount and amount < min_amount:
            continue

        if max_amount and amount > max_amount:
            continue

        valid_transactions.append(tx)

    filter_summary = {
        'region': region,
        'min_amount': min_amount,
        'max_amount': max_amount,
        'total_valid': len(valid_transactions),
        'total_invalid': invalid_count
    }

    return valid_transactions, invalid_count, filter_summary

def calculate_total_sales(transactions):
    """
    Calculates total revenue from all transactions
    """
    total_sales = 0

    for tx in transactions:
        total_sales += tx['Quantity'] * tx['UnitPrice']

    return total_sales


def sales_by_region(transactions):
    """
    Calculates total sales per region
    """
    region_sales = {}

    for tx in transactions:
        region = tx['Region']
        amount = tx['Quantity'] * tx['UnitPrice']

        if region not in region_sales:
            region_sales[region] = 0

        region_sales[region] += amount

    return region_sales


def top_products_by_revenue(transactions, n=5):
    """
    Returns top N products by total revenue
    """
    product_sales = {}

    for tx in transactions:
        product = tx['ProductName']
        amount = tx['Quantity'] * tx['UnitPrice']

        if product not in product_sales:
            product_sales[product] = 0

        product_sales[product] += amount

    sorted_products = sorted(
        product_sales.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_products[:n]


def customer_analysis(transactions):
    """
    Performs customer-wise sales analysis
    """
    customers = {}

    for tx in transactions:
        customer_id = tx['CustomerID']
        product = tx['ProductName']
        amount = tx['Quantity'] * tx['UnitPrice']

        if customer_id not in customers:
            customers[customer_id] = {
                'total_spent': 0,
                'purchase_count': 0,
                'products': set()
            }

        customers[customer_id]['total_spent'] += amount
        customers[customer_id]['purchase_count'] += 1
        customers[customer_id]['products'].add(product)

    for customer_id in customers:
        customers[customer_id]['avg_order_value'] = (
            customers[customer_id]['total_spent'] /
            customers[customer_id]['purchase_count']
        )
        customers[customer_id]['unique_products'] = len(
            customers[customer_id]['products']
        )
        del customers[customer_id]['products']

    return customers

def daily_sales_trend(transactions):
    """
    Calculates total sales per day
    """
    daily_sales = {}

    for tx in transactions:
        date = tx['Date']
        amount = tx['Quantity'] * tx['UnitPrice']

        if date not in daily_sales:
            daily_sales[date] = 0

        daily_sales[date] += amount

    return daily_sales


def peak_sales_day(transactions):
    """
    Finds the date with highest total sales
    """
    daily_sales = daily_sales_trend(transactions)

    peak_date = max(daily_sales, key=daily_sales.get)
    peak_amount = daily_sales[peak_date]

    return peak_date, peak_amount


def low_performance_products(transactions, n=5):
    """
    Returns bottom N products by total revenue
    """
    product_sales = {}

    for tx in transactions:
        product = tx['ProductName']
        amount = tx['Quantity'] * tx['UnitPrice']

        if product not in product_sales:
            product_sales[product] = 0

        product_sales[product] += amount

    sorted_products = sorted(
        product_sales.items(),
        key=lambda x: x[1]
    )

    return sorted_products[:n]
