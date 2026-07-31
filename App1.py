from flask import Flask, render_template_string

app = Flask(__name__)


# =========================================================
# MAIN ADMIN DASHBOARD
# =========================================================

HOME_PAGE = """

<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>
        ShopSphere | Admin Dashboard
    </title>


    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }


        body {

            font-family:
                Arial,
                Helvetica,
                sans-serif;

            background:
                #f3f5f9;

            color:
                #20242b;

            min-height:
                100vh;

        }


        /* =====================================
           SIDEBAR
        ===================================== */

        .sidebar {

            width:
                255px;

            min-height:
                100vh;

            position:
                fixed;

            left:
                0;

            top:
                0;

            background:
                linear-gradient(
                    180deg,
                    #111827,
                    #1f2937
                );

            color:
                white;

            padding:
                25px 18px;

        }


        .brand {

            display:
                flex;

            align-items:
                center;

            gap:
                12px;

            padding:
                5px 12px 30px;

            border-bottom:
                1px solid
                rgba(
                    255,
                    255,
                    255,
                    0.1
                );

        }


        .logo {

            width:
                44px;

            height:
                44px;

            display:
                flex;

            align-items:
                center;

            justify-content:
                center;

            border-radius:
                12px;

            background:
                linear-gradient(
                    135deg,
                    #6366f1,
                    #8b5cf6
                );

            font-size:
                22px;

            font-weight:
                bold;

        }


        .brand-text h2 {

            font-size:
                20px;

        }


        .brand-text p {

            color:
                #9ca3af;

            font-size:
                12px;

            margin-top:
                3px;

        }


        .menu-title {

            color:
                #7f8795;

            font-size:
                11px;

            font-weight:
                bold;

            letter-spacing:
                1px;

            margin:
                30px 12px 12px;

        }


        .menu {

            list-style:
                none;

        }


        .menu li {

            margin:
                7px 0;

        }


        .menu a {

            text-decoration:
                none;

            color:
                #b7bfcb;

            padding:
                13px 15px;

            display:
                flex;

            align-items:
                center;

            gap:
                14px;

            border-radius:
                9px;

            transition:
                0.3s;

        }


        .menu a:hover {

            background:
                rgba(
                    255,
                    255,
                    255,
                    0.08
                );

            color:
                white;

        }


        .menu .active {

            color:
                white;

            background:
                linear-gradient(
                    90deg,
                    #4f46e5,
                    #6366f1
                );

            box-shadow:
                0 5px 15px
                rgba(
                    79,
                    70,
                    229,
                    0.3
                );

        }


        .menu-icon {

            width:
                22px;

            text-align:
                center;

            font-size:
                18px;

        }


        .sidebar-footer {

            position:
                absolute;

            bottom:
                25px;

            left:
                18px;

            right:
                18px;

            padding:
                16px;

            border-radius:
                12px;

            background:
                rgba(
                    255,
                    255,
                    255,
                    0.06
                );

        }


        .sidebar-footer p {

            color:
                #9ca3af;

            font-size:
                12px;

            margin-bottom:
                8px;

        }


        .upgrade-button {

            width:
                100%;

            border:
                none;

            padding:
                9px;

            color:
                white;

            background:
                #6366f1;

            border-radius:
                7px;

            cursor:
                pointer;

        }


        /* =====================================
           MAIN CONTENT
        ===================================== */

        .main {

            margin-left:
                255px;

            min-height:
                100vh;

        }


        /* =====================================
           TOP NAVIGATION
        ===================================== */

        .topbar {

            height:
                78px;

            display:
                flex;

            align-items:
                center;

            justify-content:
                space-between;

            padding:
                0 35px;

            background:
                white;

            border-bottom:
                1px solid
                #e8eaf0;

        }


        .search-box {

            width:
                390px;

            position:
                relative;

        }


        .search-box input {

            width:
                100%;

            padding:
                13px 18px 13px 45px;

            border:
                1px solid
                #e2e5eb;

            border-radius:
                10px;

            outline:
                none;

            background:
                #f8fafc;

            font-size:
                14px;

        }


        .search-icon {

            position:
                absolute;

            left:
                16px;

            top:
                12px;

            color:
                #7c8593;

            font-size:
                18px;

        }


        .top-actions {

            display:
                flex;

            align-items:
                center;

            gap:
                22px;

        }


        .notification {

            width:
                42px;

            height:
                42px;

            display:
                flex;

            align-items:
                center;

            justify-content:
                center;

            background:
                #f5f6fa;

            border-radius:
                50%;

            position:
                relative;

            font-size:
                19px;

        }


        .notification-dot {

            position:
                absolute;

            top:
                8px;

            right:
                9px;

            width:
                8px;

            height:
                8px;

            border-radius:
                50%;

            background:
                #ef4444;

            border:
                2px solid
                white;

        }


        .profile {

            display:
                flex;

            align-items:
                center;

            gap:
                11px;

        }


        .profile-image {

            width:
                43px;

            height:
                43px;

            display:
                flex;

            align-items:
                center;

            justify-content:
                center;

            border-radius:
                50%;

            background:
                linear-gradient(
                    135deg,
                    #f59e0b,
                    #ef4444
                );

            color:
                white;

            font-weight:
                bold;

            font-size:
                17px;

        }


        .profile-info h4 {

            font-size:
                14px;

        }


        .profile-info p {

            color:
                #8b93a1;

            font-size:
                12px;

            margin-top:
                3px;

        }


        /* =====================================
           DASHBOARD CONTENT
        ===================================== */

        .content {

            padding:
                32px 35px;

        }


        .page-header {

            display:
                flex;

            align-items:
                center;

            justify-content:
                space-between;

            margin-bottom:
                28px;

        }


        .page-header h1 {

            font-size:
                27px;

            margin-bottom:
                7px;

        }


        .page-header p {

            color:
                #7a8290;

            font-size:
                14px;

        }


        .add-product {

            padding:
                12px 20px;

            border:
                none;

            border-radius:
                9px;

            color:
                white;

            font-size:
                14px;

            cursor:
                pointer;

            background:
                linear-gradient(
                    90deg,
                    #4f46e5,
                    #6366f1
                );

            box-shadow:
                0 5px 13px
                rgba(
                    79,
                    70,
                    229,
                    0.25
                );

        }


        /* =====================================
           STATISTICS
        ===================================== */

        .statistics {

            display:
                grid;

            grid-template-columns:
                repeat(
                    4,
                    1fr
                );

            gap:
                20px;

            margin-bottom:
                28px;

        }


        .stat-card {

            background:
                white;

            padding:
                22px;

            border-radius:
                14px;

            box-shadow:
                0 3px 12px
                rgba(
                    0,
                    0,
                    0,
                    0.04
                );

            display:
                flex;

            justify-content:
                space-between;

            align-items:
                center;

        }


        .stat-card p {

            color:
                #7c8491;

            font-size:
                13px;

            margin-bottom:
                9px;

        }


        .stat-card h2 {

            font-size:
                25px;

        }


        .stat-icon {

            width:
                52px;

            height:
                52px;

            display:
                flex;

            align-items:
                center;

            justify-content:
                center;

            border-radius:
                13px;

            font-size:
                24px;

        }


        .purple {

            background:
                #ede9fe;

        }


        .blue {

            background:
                #dbeafe;

        }


        .green {

            background:
                #dcfce7;

        }


        .orange {

            background:
                #ffedd5;

        }


        /* =====================================
           PRODUCT TABLE
        ===================================== */

        .table-card {

            background:
                white;

            border-radius:
                15px;

            overflow:
                hidden;

            box-shadow:
                0 3px 15px
                rgba(
                    0,
                    0,
                    0,
                    0.04
                );

        }


        .table-header {

            padding:
                23px 25px;

            display:
                flex;

            align-items:
                center;

            justify-content:
                space-between;

            border-bottom:
                1px solid
                #edf0f4;

        }


        .table-header h2 {

            font-size:
                19px;

        }


        .table-header p {

            color:
                #7d8593;

            font-size:
                13px;

            margin-top:
                5px;

        }


        .filter-button {

            padding:
                10px 17px;

            border:
                1px solid
                #e1e5eb;

            background:
                white;

            border-radius:
                8px;

            cursor:
                pointer;

        }


        table {

            width:
                100%;

            border-collapse:
                collapse;

        }


        th {

            text-align:
                left;

            padding:
                15px 24px;

            color:
                #747d8a;

            background:
                #fafbfc;

            font-size:
                12px;

            letter-spacing:
                0.5px;

        }


        td {

            padding:
                18px 24px;

            border-top:
                1px solid
                #edf0f4;

            font-size:
                14px;

        }


        .product-info {

            display:
                flex;

            align-items:
                center;

            gap:
                14px;

        }


        .product-image {

            width:
                58px;

            height:
                58px;

            display:
                flex;

            align-items:
                center;

            justify-content:
                center;

            border-radius:
                11px;

            font-size:
                28px;

        }


        .mouse-image {

            background:
                linear-gradient(
                    135deg,
                    #e0e7ff,
                    #c7d2fe
                );

        }


        .keyboard-image {

            background:
                linear-gradient(
                    135deg,
                    #fce7f3,
                    #fbcfe8
                );

        }


        .headphone-image {

            background:
                linear-gradient(
                    135deg,
                    #dcfce7,
                    #bbf7d0
                );

        }


        .product-name {

            font-weight:
                bold;

            margin-bottom:
                6px;

        }


        .product-category {

            color:
                #8a929f;

            font-size:
                12px;

        }


        .price {

            font-weight:
                bold;

        }


        .stock {

            display:
                inline-block;

            padding:
                7px 11px;

            border-radius:
                20px;

            font-size:
                12px;

            font-weight:
                bold;

        }


        .in-stock {

            color:
                #15803d;

            background:
                #dcfce7;

        }


        .low-stock {

            color:
                #b45309;

            background:
                #fef3c7;

        }


        .out-stock {

            color:
                #b91c1c;

            background:
                #fee2e2;

        }


        .rating {

            color:
                #f59e0b;

            font-weight:
                bold;

        }


        .view-button {

            border:
                none;

            padding:
                10px 15px;

            border-radius:
                8px;

            color:
                #4f46e5;

            background:
                #eef2ff;

            font-weight:
                bold;

            cursor:
                pointer;

            transition:
                0.3s;

        }


        .view-button:hover {

            background:
                #4f46e5;

            color:
                white;

        }


        /* =====================================
           RESPONSIVE DESIGN
        ===================================== */

        @media (
            max-width:
            1000px
        ) {

            .statistics {

                grid-template-columns:
                    repeat(
                        2,
                        1fr
                    );

            }

        }


        @media (
            max-width:
            750px
        ) {

            .sidebar {

                width:
                    75px;

                padding:
                    20px 10px;

            }


            .brand-text,
            .menu-text,
            .menu-title,
            .sidebar-footer {

                display:
                    none;

            }


            .main {

                margin-left:
                    75px;

            }


            .statistics {

                grid-template-columns:
                    1fr;

            }


            .search-box {

                width:
                    220px;

            }


            table {

                min-width:
                    850px;

            }


            .table-card {

                overflow-x:
                    auto;

            }

        }

    </style>

</head>


<body>


<!-- =====================================
     SIDEBAR
===================================== -->

<aside class="sidebar">


    <div class="brand">

        <div class="logo">

            S

        </div>


        <div class="brand-text">

            <h2>

                ShopSphere

            </h2>


            <p>

                ADMIN PANEL

            </p>

        </div>

    </div>


    <p class="menu-title">

        MAIN MENU

    </p>


    <ul class="menu">


        <li>

            <a href="#">

                <span class="menu-icon">

                    ▦

                </span>

                <span class="menu-text">

                    Dashboard

                </span>

            </a>

        </li>


        <li>

            <a
                class="active"
                href="#"
            >

                <span class="menu-icon">

                    ▣

                </span>

                <span class="menu-text">

                    Products

                </span>

            </a>

        </li>


        <li>

            <a href="#">

                <span class="menu-icon">

                    ◉

                </span>

                <span class="menu-text">

                    Orders

                </span>

            </a>

        </li>


        <li>

            <a href="#">

                <span class="menu-icon">

                    ♙

                </span>

                <span class="menu-text">

                    Customers

                </span>

            </a>

        </li>


        <li>

            <a href="#">

                <span class="menu-icon">

                    ◈

                </span>

                <span class="menu-text">

                    Analytics

                </span>

            </a>

        </li>

    </ul>


    <p class="menu-title">

        SETTINGS

    </p>


    <ul class="menu">


        <li>

            <a href="#">

                <span class="menu-icon">

                    ⚙

                </span>

                <span class="menu-text">

                    Settings

                </span>

            </a>

        </li>


        <li>

            <a href="#">

                <span class="menu-icon">

                    ?

                </span>

                <span class="menu-text">

                    Help Center

                </span>

            </a>

        </li>

    </ul>


    <div class="sidebar-footer">

        <p>

            Upgrade your store

        </p>

        <button class="upgrade-button">

            Upgrade Plan

        </button>

    </div>


</aside>



<!-- =====================================
     MAIN AREA
===================================== -->

<main class="main">


    <!-- TOP BAR -->

    <header class="topbar">


        <div class="search-box">

            <span class="search-icon">

                ⌕

            </span>


            <input
                id="dashboard-search"
                type="text"
                placeholder="Search products, orders..."
            >

        </div>


        <div class="top-actions">


            <div class="notification">

                ♧

                <span class="notification-dot">

                </span>

            </div>


            <div class="profile">


                <div class="profile-image">

                    AP

                </div>


                <div class="profile-info">

                    <h4>

                        Alex Parker

                    </h4>


                    <p>

                        Store Administrator

                    </p>

                </div>

            </div>

        </div>


    </header>



    <!-- CONTENT -->

    <section class="content">


        <div class="page-header">


            <div>

                <h1>

                    Product Management

                </h1>


                <p>

                    Manage and monitor
                    all products in your store.

                </p>

            </div>


            <button class="add-product">

                + Add New Product

            </button>

        </div>



        <!-- STATISTICS -->

        <div class="statistics">


            <div class="stat-card">


                <div>

                    <p>

                        Total Products

                    </p>


                    <h2>

                        1,284

                    </h2>

                </div>


                <div class="stat-icon purple">

                    📦

                </div>

            </div>



            <div class="stat-card">


                <div>

                    <p>

                        In Stock

                    </p>


                    <h2>

                        1,126

                    </h2>

                </div>


                <div class="stat-icon green">

                    ✓

                </div>

            </div>



            <div class="stat-card">


                <div>

                    <p>

                        Low Stock

                    </p>


                    <h2>

                        86

                    </h2>

                </div>


                <div class="stat-icon orange">

                    !

                </div>

            </div>



            <div class="stat-card">


                <div>

                    <p>

                        Out of Stock

                    </p>


                    <h2>

                        72

                    </h2>

                </div>


                <div class="stat-icon blue">

                    ⊘

                </div>

            </div>


        </div>



        <!-- PRODUCT TABLE -->

        <div class="table-card">


            <div class="table-header">


                <div>

                    <h2>

                        All Products

                    </h2>


                    <p>

                        Showing 3 of 1,284 products

                    </p>

                </div>


                <button class="filter-button">

                    ⚲ Filter

                </button>

            </div>



            <table id="product-table">


                <thead>

                    <tr>

                        <th>

                            PRODUCT

                        </th>

                        <th>

                            PRICE

                        </th>

                        <th>

                            STOCK

                        </th>

                        <th>

                            RATING

                        </th>

                        <th>

                            ACTION

                        </th>

                    </tr>

                </thead>



                <tbody>


                    <!-- PRODUCT 1 -->

                    <tr class="product-row">


                        <td>


                            <div class="product-info">


                                <div
                                    class="
                                    product-image
                                    mouse-image
                                    "
                                >

                                    🖱️

                                </div>


                                <div>


                                    <div class="product-name">

                                        Wireless Mouse

                                    </div>


                                    <div class="product-category">

                                        Electronics

                                    </div>

                                </div>

                            </div>


                        </td>


                        <td class="price">

                            $29.99

                        </td>


                        <td>

                            <span
                                class="
                                stock
                                in-stock
                                "
                            >

                                In Stock

                            </span>

                        </td>


                        <td>

                            <span class="rating">

                                ★ 4.8

                            </span>

                        </td>


                        <td>


                            <button
                                id="view-details"
                                class="view-button"
                                onclick="
                                openProductDetails()
                                "
                            >

                                View Details

                            </button>


                        </td>


                    </tr>



                    <!-- PRODUCT 2 -->

                    <tr class="product-row">


                        <td>


                            <div class="product-info">


                                <div
                                    class="
                                    product-image
                                    keyboard-image
                                    "
                                >

                                    ⌨️

                                </div>


                                <div>


                                    <div class="product-name">

                                        Mechanical Keyboard

                                    </div>


                                    <div class="product-category">

                                        Electronics

                                    </div>

                                </div>

                            </div>


                        </td>


                        <td class="price">

                            $89.99

                        </td>


                        <td>

                            <span
                                class="
                                stock
                                low-stock
                                "
                            >

                                Low Stock

                            </span>

                        </td>


                        <td>

                            <span class="rating">

                                ★ 4.7

                            </span>

                        </td>


                        <td>


                            <button class="view-button">

                                View Details

                            </button>


                        </td>


                    </tr>



                    <!-- PRODUCT 3 -->

                    <tr class="product-row">


                        <td>


                            <div class="product-info">


                                <div
                                    class="
                                    product-image
                                    headphone-image
                                    "
                                >

                                    🎧

                                </div>


                                <div>


                                    <div class="product-name">

                                        Noise Cancelling Headphones

                                    </div>


                                    <div class="product-category">

                                        Audio

                                    </div>

                                </div>

                            </div>


                        </td>


                        <td class="price">

                            $149.99

                        </td>


                        <td>

                            <span
                                class="
                                stock
                                out-stock
                                "
                            >

                                Out of Stock

                            </span>

                        </td>


                        <td>

                            <span class="rating">

                                ★ 4.9

                            </span>

                        </td>


                        <td>


                            <button class="view-button">

                                View Details

                            </button>


                        </td>


                    </tr>


                </tbody>


            </table>


        </div>


    </section>


</main>



<script>


function openProductDetails() {


    window.open(

        "/product-details",

        "_blank"

    );


}


/* =====================================
   SEARCH PRODUCTS
===================================== */

document

.getElementById(

    "dashboard-search"

)

.addEventListener(

    "keyup",

    function() {


        let searchValue =

            this.value

            .toLowerCase();


        let rows =

            document

            .querySelectorAll(

                ".product-row"

            );


        rows.forEach(

            function(row) {


                let productName =

                    row

                    .querySelector(

                        ".product-name"

                    )

                    .innerText

                    .toLowerCase();


                if (

                    productName

                    .includes(

                        searchValue

                    )

                ) {


                    row.style.display = "";


                }

                else {


                    row.style.display = "none";


                }


            }

        );


    }

);


</script>


</body>

</html>

"""


# =========================================================
# PRODUCT DETAILS PAGE
# =========================================================

DETAILS_PAGE = """

<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>
        Wireless Mouse | ShopSphere
    </title>


    <style>


        * {

            margin:
                0;

            padding:
                0;

            box-sizing:
                border-box;

        }


        body {

            font-family:
                Arial,
                Helvetica,
                sans-serif;

            background:
                #f4f6fa;

            color:
                #20242b;

        }


        /* =====================================
           LOADING SCREEN
        ===================================== */

        #loading-screen {

            position:
                fixed;

            inset:
                0;

            display:
                flex;

            flex-direction:
                column;

            align-items:
                center;

            justify-content:
                center;

            background:
                white;

            z-index:
                100;

        }


        #loading-spinner {

            width:
                70px;

            height:
                70px;

            border:
                7px solid
                #e5e7eb;

            border-top:
                7px solid
                #4f46e5;

            border-radius:
                50%;

            animation:
                spin
                0.9s
                linear
                infinite;

        }


        .loading-title {

            margin-top:
                25px;

            font-size:
                20px;

            font-weight:
                bold;

        }


        .loading-text {

            color:
                #858d9a;

            margin-top:
                8px;

            font-size:
                14px;

        }


        @keyframes spin {


            0% {

                transform:
                    rotate(
                        0deg
                    );

            }


            100% {

                transform:
                    rotate(
                        360deg
                    );

            }


        }


        /* =====================================
           PRODUCT CONTENT
        ===================================== */

        #product-content {

            display:
                none;

        }


        .details-topbar {

            height:
                72px;

            background:
                white;

            display:
                flex;

            align-items:
                center;

            justify-content:
                space-between;

            padding:
                0 8%;

            border-bottom:
                1px solid
                #e6e9ef;

        }


        .details-brand {

            display:
                flex;

            align-items:
                center;

            gap:
                11px;

            font-weight:
                bold;

            font-size:
                20px;

        }


        .details-logo {

            width:
                40px;

            height:
                40px;

            display:
                flex;

            align-items:
                center;

            justify-content:
                center;

            color:
                white;

            background:
                linear-gradient(
                    135deg,
                    #4f46e5,
                    #8b5cf6
                );

            border-radius:
                11px;

        }


        .back-button {

            padding:
                10px 17px;

            border:
                1px solid
                #e0e4ea;

            border-radius:
                8px;

            background:
                white;

            cursor:
                pointer;

        }


        .details-container {

            max-width:
                1100px;

            margin:
                45px auto;

            padding:
                0 25px;

        }


        .breadcrumb {

            color:
                #777f8c;

            font-size:
                13px;

            margin-bottom:
                25px;

        }


        .details-card {

            background:
                white;

            border-radius:
                18px;

            padding:
                45px;

            display:
                grid;

            grid-template-columns:
                1fr 1fr;

            gap:
                60px;

            box-shadow:
                0 5px 25px
                rgba(
                    0,
                    0,
                    0,
                    0.06
                );

        }


        .main-product-image {

            min-height:
                390px;

            display:
                flex;

            align-items:
                center;

            justify-content:
                center;

            border-radius:
                18px;

            background:
                linear-gradient(
                    145deg,
                    #e0e7ff,
                    #c7d2fe
                );

            font-size:
                190px;

        }


        .category {

            color:
                #4f46e5;

            font-size:
                13px;

            font-weight:
                bold;

            letter-spacing:
                1px;

            margin-bottom:
                15px;

        }


        #product-name {

            font-size:
                37px;

            line-height:
                1.2;

            margin-bottom:
                17px;

        }


        .product-rating {

            display:
                flex;

            align-items:
                center;

            gap:
                10px;

            margin-bottom:
                22px;

        }


        .stars {

            color:
                #f59e0b;

            font-size:
                20px;

        }


        #product-rating {

            font-weight:
                bold;

        }


        .review-count {

            color:
                #808896;

            font-size:
                14px;

        }


        .product-price {

            font-size:
                33px;

            font-weight:
                bold;

            color:
                #4f46e5;

            margin:
                22px 0;

        }


        .description {

            color:
                #6e7683;

            line-height:
                1.8;

            font-size:
                15px;

            margin-bottom:
                25px;

        }


        .stock-box {

            display:
                flex;

            align-items:
                center;

            gap:
                10px;

            padding:
                15px;

            border-radius:
                10px;

            color:
                #166534;

            background:
                #dcfce7;

            margin-bottom:
                25px;

            font-weight:
                bold;

        }


        .stock-dot {

            width:
                10px;

            height:
                10px;

            border-radius:
                50%;

            background:
                #22c55e;

        }


        .information-grid {

            display:
                grid;

            grid-template-columns:
                1fr 1fr;

            gap:
                14px;

            margin-top:
                20px;

        }


        .information-item {

            padding:
                15px;

            background:
                #f8fafc;

            border-radius:
                10px;

        }


        .information-item p {

            color:
                #8a929f;

            font-size:
                12px;

            margin-bottom:
                6px;

        }


        .information-item h4 {

            font-size:
                14px;

        }


        @media (

            max-width:
            800px

        ) {


            .details-card {

                grid-template-columns:
                    1fr;

                padding:
                    25px;

            }


            .main-product-image {

                min-height:
                    270px;

                font-size:
                    130px;

            }


        }


    </style>

</head>


<body>


<!-- =====================================
     LOADING PAGE
===================================== -->

<div id="loading-screen">


    <div id="loading-spinner">

    </div>


    <div class="loading-title">

        Loading Product Details

    </div>


    <div class="loading-text">

        Please wait while we
        retrieve product information...

    </div>


</div>



<!-- =====================================
     PRODUCT DETAILS
===================================== -->

<div id="product-content">


    <header class="details-topbar">


        <div class="details-brand">


            <div class="details-logo">

                S

            </div>


            ShopSphere


        </div>


        <button
            class="back-button"
            onclick="window.close()"
        >

            ← Close Details

        </button>


    </header>



    <main class="details-container">


        <div class="breadcrumb">

            Dashboard
            /
            Products
            /
            Wireless Mouse

        </div>



        <div class="details-card">


            <!-- PRODUCT IMAGE -->

            <div class="main-product-image">

                🖱️

            </div>



            <!-- PRODUCT INFORMATION -->

            <div>


                <p class="category">

                    ELECTRONICS

                </p>


                <h1 id="product-name">

                    Wireless Mouse

                </h1>


                <div class="product-rating">


                    <span class="stars">

                        ★★★★★

                    </span>


                    <span id="product-rating">

                        4.8

                    </span>


                    <span class="review-count">

                        1,248 customer reviews

                    </span>


                </div>


                <div class="product-price">

                    $29.99

                </div>


                <p class="description">

                    Experience smooth and
                    accurate navigation with
                    this premium wireless mouse.
                    It features an ergonomic
                    design, silent clicking,
                    high-precision tracking,
                    and a long-lasting battery.

                </p>


                <div class="stock-box">


                    <span class="stock-dot">

                    </span>


                    In Stock

                    <span>

                        — 248 units available

                    </span>


                </div>


                <div class="information-grid">


                    <div class="information-item">

                        <p>

                            CATEGORY

                        </p>


                        <h4>

                            Computer Accessories

                        </h4>

                    </div>


                    <div class="information-item">

                        <p>

                            PRODUCT ID

                        </p>


                        <h4>

                            WM-2026-001

                        </h4>

                    </div>


                    <div class="information-item">

                        <p>

                            SHIPPING

                        </p>


                        <h4>

                            Free Delivery

                        </h4>

                    </div>


                    <div class="information-item">

                        <p>

                            WARRANTY

                        </p>


                        <h4>

                            1 Year Warranty

                        </h4>

                    </div>


                </div>


            </div>


        </div>


    </main>


</div>



<script>


/* =====================================
   SIMULATE ASYNCHRONOUS DATA LOADING
===================================== */

setTimeout(

    function() {


        document

        .getElementById(

            "loading-screen"

        )

        .style

        .display =

        "none";


        document

        .getElementById(

            "product-content"

        )

        .style

        .display =

        "block";


    },

    3500

);


</script>


</body>

</html>

"""


# =========================================================
# FLASK ROUTES
# =========================================================

@app.route("/")
def home():

    return render_template_string(
        HOME_PAGE
    )


@app.route("/product-details")
def product_details():

    return render_template_string(
        DETAILS_PAGE
    )


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(

        host="127.0.0.1",

        port=5000,

        debug=False

    )