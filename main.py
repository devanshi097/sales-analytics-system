from utils.file_handler import read_sales_data
from utils.data_processor import (
    parse_transactions,
    validate_and_filter,
    calculate_total_sales,
    sales_by_region,
    top_products_by_revenue,
    customer_analysis,
    daily_sales_trend,
    peak_sales_day,
    low_performance_products
)
from utils.api_handler import (
    fetch_products,
    create_product_mapping,
    enrich_sales_data
)
from utils.report_generator import generate_sales_report


def main():
    print("Starting Sales Analytics System...")

    raw = read_sales_data("data/sales_data.txt")
    parsed = parse_transactions(raw)

    valid, invalid_count, _ = validate_and_filter(parsed)

    total_sales = calculate_total_sales(valid)
    region_sales = sales_by_region(valid)
    top_products = top_products_by_revenue(valid, 5)
    customers = customer_analysis(valid)
    daily_sales = daily_sales_trend(valid)
    peak_date, peak_amount = peak_sales_day(valid)
    low_products = low_performance_products(valid, 5)

    products = fetch_products()
    product_map = create_product_mapping(products)

    enrich_sales_data(
        valid,
        product_map,
        "data/enriched_sales_data.txt"
    )

    generate_sales_report(
        output_file="output/sales_report.txt",
        valid_count=len(valid),
        invalid_count=invalid_count,
        total_sales=total_sales,
        sales_by_region=region_sales,
        top_products=top_products,
        customer_summary=customers,
        daily_sales=daily_sales,
        peak_day=(peak_date, peak_amount),
        low_products=low_products
    )

    print("Sales Analytics System completed successfully.")


if __name__ == "__main__":
    main()
