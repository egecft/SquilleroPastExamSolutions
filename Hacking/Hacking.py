INPUT_FILE_PRODUCTS = "products.txt"
INPUT_FILE_PURCHASES = "purchases.txt"


def read_products():
    products_dict = dict()
    try:
        with open(INPUT_FILE_PRODUCTS, "r") as products_file:
            for line in products_file:
                clean_line = line.strip()
                clean_line_list = clean_line.split()

                product_id = clean_line_list[0]
                seller_id = clean_line_list[1]
                products_dict[product_id] = [seller_id]
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return products_dict


def read_purchases():
    purchases_dict = dict()
    try:
        with open(INPUT_FILE_PURCHASES, "r") as purchases_file:
            for line in purchases_file:
                clean_line = line.strip()
                clean_line_list = clean_line.split()

                product_id = clean_line_list[0]
                seller_id = clean_line_list[1]

                if product_id in purchases_dict.keys():
                    purchases_dict[product_id].append(seller_id)
                else:
                    purchases_dict[product_id] = [seller_id]
    except OSError as problem:
        exit(f"We have a problem: {problem}")
    return purchases_dict


def create_output():
    products_dict = read_products()
    purchases_dict = read_purchases()

    print("\nSuspicious transactions list:\n")
    for key, value in purchases_dict.items():
        for code in value:
            if code not in products_dict[key]:
                print(f"Product code: {key}")
                print(f"Official dealer: {products_dict[key][0]}")
                print(f"Dealer list: {' '.join(purchases_dict[key])}\n")


def main():
    read_products()
    read_purchases()
    create_output()


if __name__ == "__main__":
    main()
