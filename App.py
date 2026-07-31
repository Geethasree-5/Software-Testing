from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Wireless Mouse",
        "price": 24.99,
        "stock": "In Stock"
    },
    {
        "id": 2,
        "name": "Mechanical Keyboard",
        "price": 59.99,
        "stock": "In Stock"
    },
    {
        "id": 3,
        "name": "USB-C Cable",
        "price": 9.99,
        "stock": "Out of Stock"
    }
]

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>E-Commerce Admin Dashboard</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f6f8;
            margin: 0;
            padding: 30px;
        }

        .container {
            background-color: white;
            max-width: 900px;
            margin: auto;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
        }

        h1 {
            text-align: center;
        }

        #product-search {
            width: 97%;
            padding: 12px;
            margin-bottom: 20px;
            font-size: 16px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            padding: 14px;
            border: 1px solid #cccccc;
            text-align: left;
        }

        th {
            background-color: #333333;
            color: white;
        }

        button {
            padding: 8px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            background-color: #1976d2;
            color: white;
        }

        button:hover {
            background-color: #0d47a1;
        }

        #edit-form {
            display: none;
            margin-top: 25px;
            padding: 20px;
            border: 1px solid #cccccc;
            background-color: #f9f9f9;
        }

        #product-price {
            padding: 10px;
            width: 200px;
            margin: 10px;
        }

        .success-message {
            display: none;
            margin-top: 20px;
            padding: 12px;
            background-color: #d4edda;
            color: #155724;
            border-radius: 5px;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>E-Commerce Admin Dashboard</h1>

    <input
        type="text"
        id="product-search"
        placeholder="Search product..."
        onkeyup="searchProduct()"
    >

    <table id="product-table">

        <thead>
            <tr>
                <th>Product Name</th>
                <th>Price</th>
                <th>Stock Status</th>
                <th>Action</th>
            </tr>
        </thead>

        <tbody>

        {% for product in products %}

            <tr data-product-id="{{ product.id }}">

                <td class="product-name">
                    {{ product.name }}
                </td>

                <td class="product-price">
                    ${{ "%.2f"|format(product.price) }}
                </td>

                <td class="stock">
                    {{ product.stock }}
                </td>

                <td>
                    <button
                        class="edit-button"
                        onclick="openEditForm(
                            {{ product.id }},
                            '{{ product.name }}',
                            {{ product.price }}
                        )"
                    >
                        Edit
                    </button>
                </td>

            </tr>

        {% endfor %}

        </tbody>

    </table>


    <div id="edit-form">

        <h2>Edit Product</h2>

        <p>
            Product:
            <strong id="edit-product-name"></strong>
        </p>

        <input
            type="hidden"
            id="product-id"
        >

        <label>Price:</label>

        <input
            type="number"
            id="product-price"
            step="0.01"
        >

        <button
            id="save-product"
            onclick="saveProduct()"
        >
            Save Changes
        </button>

    </div>


    <div class="success-message">
        Product updated successfully!
    </div>

</div>


<script>

function searchProduct() {

    let searchValue =
        document
        .getElementById("product-search")
        .value
        .toLowerCase();

    let rows =
        document
        .querySelectorAll("#product-table tbody tr");

    rows.forEach(function(row) {

        let productName =
            row
            .querySelector(".product-name")
            .innerText
            .toLowerCase();

        if (productName.includes(searchValue)) {

            row.style.display = "";

        } else {

            row.style.display = "none";

        }

    });

}


function openEditForm(id, name, price) {

    document
    .getElementById("product-id")
    .value = id;

    document
    .getElementById("edit-product-name")
    .innerText = name;

    document
    .getElementById("product-price")
    .value = price;

    document
    .getElementById("edit-form")
    .style.display = "block";

}


function saveProduct() {

    let productId =
        document
        .getElementById("product-id")
        .value;

    let newPrice =
        document
        .getElementById("product-price")
        .value;


    fetch("/update-product", {

        method: "POST",

        headers: {
            "Content-Type":
            "application/json"
        },

        body: JSON.stringify({

            id: productId,

            price: newPrice

        })

    })

    .then(response =>
        response.json()
    )

    .then(data => {

        if (data.success) {

            let row =
                document
                .querySelector(
                    'tr[data-product-id="' +
                    productId +
                    '"]'
                );

            row
            .querySelector(".product-price")
            .innerText =
            "$" +
            Number(newPrice).toFixed(2);


            document
            .querySelector(".success-message")
            .style.display =
            "block";

        }

    });

}

</script>

</body>
</html>
"""


@app.route("/")
def home():

    return render_template_string(
        HTML_PAGE,
        products=products
    )


@app.route(
    "/update-product",
    methods=["POST"]
)
def update_product():

    data = request.get_json()

    product_id = int(
        data["id"]
    )

    new_price = float(
        data["price"]
    )

    for product in products:

        if product["id"] == product_id:

            product["price"] = new_price

            break

    return jsonify({
        "success": True
    })


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )