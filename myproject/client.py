import requests

BASE_URL = 'http://127.0.0.1:5000/products'

def add_product(name, description, price):
    """Add a new product to the API."""
    product_data = {
        'name': name,
        'description': description,
        'price': price
    }

    response = requests.post(BASE_URL, json=product_data)

    if response.status_code == 201:
        print(f"Product added: {response.json()}")
    else:
        print(f"Failed to add product: {response.json()}")

def get_products():
    """Retrieve and print the list of all products."""
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        products = response.json()
        print("List of Products:")
        for product in products:
            print(f"Name: {product['name']}, Description: {product['description']}, Price: {product['price']}")
    else:
        print("Failed to retrieve products")

if __name__ == '__main__':
    # Example usage:
    add_product("Product 1", "Description of Product 1", 19.99)
    add_product("Product 2", "Description of Product 2", 29.99)
    
    # Retrieve and print all products
    get_products()