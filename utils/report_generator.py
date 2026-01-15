from datetime import datetime

def generate_sales_report(
    output_file,
    valid_count,
    invalid_count,
    total_sales,
    sales_by_region,
    top_products,
    customer_summary,
    daily_sales,
    peak_day,
    low_products
):
    """
    Generates a formatted sales report and saves it to sales_report.txt
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("SALES ANALYTICS REPORT\n")
        file.write("=" * 60 + "\n")
        file.write(f"Generated on: {datetime.now()}\n")
        file.write(f"Valid Transactions: {valid_count}\n")
        file.write(f"Invalid Transactions: {invalid_count}\n\n")

        file.write("OVERALL SALES SUMMARY\n")
        file.write("-" * 60 + "\n")
        file.write(f"Total Sales Revenue: ₹{total_sales:,.2f}\n\n")

        file.write("SALES BY REGION\n")
        file.write("-" * 60 + "\n")
        for region, amount in sales_by_region.items():
            file.write(f"{region:<10} : ₹{amount:,.2f}\n")
        file.write("\n")

        file.write("TOP PRODUCTS BY REVENUE\n")
        file.write("-" * 60 + "\n")
        for product, revenue in top_products:
            file.write(f"{product:<30} ₹{revenue:,.2f}\n")
        file.write("\n")

        file.write("CUSTOMER SUMMARY (Sample)\n")
        file.write("-" * 60 + "\n")
        for cid, info in list(customer_summary.items())[:5]:
            file.write(
                f"{cid} | Total: ₹{info['total_spent']:,.2f} | "
                f"Orders: {info['purchase_count']} | "
                f"Avg Order: ₹{info['avg_order_value']:,.2f} | "
                f"Unique Products: {info['unique_products']}\n"
            )
        file.write("\n")

        file.write("DAILY SALES TREND (Sample)\n")
        file.write("-" * 60 + "\n")
        for date, amount in list(daily_sales.items())[:5]:
            file.write(f"{date} : ₹{amount:,.2f}\n")

        file.write("\n")
        file.write(
            f"PEAK SALES DAY: {peak_day[0]} "
            f"(₹{peak_day[1]:,.2f})\n\n"
        )

        file.write("LOW PERFORMANCE PRODUCTS\n")
        file.write("-" * 60 + "\n")
        for product, revenue in low_products:
            file.write(f"{product:<30} ₹{revenue:,.2f}\n")

    print(f"Sales report generated successfully: {output_file}")
