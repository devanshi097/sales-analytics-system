import requests

def fetch_products():
    """
    Fetches product data from DummyJSON API
    Returns: list of product dictionaries
    """
    url = "https://dummyjson.com/products?limit=100"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Error fetching products:", e)
        return []

    data = response.json()
    products = data.get("products", [])

    print(f"Fetched {len(products)} products from API")
    return products


def create_product_mapping(products):
    """
    Creates a mapping from product ID to product details
    """
    product_map = {}

    for product in products:
        product_id = product.get('id')

        product_map[product_id] = {
            'title': product.get('title'),
            'brand': product.get('brand'),
            'category': product.get('category'),
            'rating': product.get('rating')
        }

    return product_map


def enrich_sales_data(transactions, product_map, output_file):
    """
    Enriches sales data with API product info and saves to file
    """
    enriched_transactions = []

    for tx in transactions:
        product_id_str = tx['ProductID']
        product_id_num = int(product_id_str[1:])

        api_data = product_map.get(product_id_num)

        enriched_tx = tx.copy()

        if api_data:
            enriched_tx['API_Category'] = api_data['category']
            enriched_tx['API_Brand'] = api_data['brand']
            enriched_tx['API_Rating'] = api_data['rating']
            enriched_tx['API_Match'] = True
        else:
            enriched_tx['API_Category'] = None
            enriched_tx['API_Brand'] = None
            enriched_tx['API_Rating'] = None
            enriched_tx['API_Match'] = False

        enriched_transactions.append(enriched_tx)

    with open(output_file, 'w', encoding='utf-8') as file:
        headers = enriched_transactions[0].keys()
        file.write('|'.join(headers) + '\n')

        for tx in enriched_transactions:
            row = [str(tx[h]) for h in headers]
            file.write('|'.join(row) + '\n')

    print(f"Enriched data saved to {output_file}")
    return enriched_transactions
