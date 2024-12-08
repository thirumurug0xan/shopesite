-- Create 'users' table
CREATE TABLE IF NOT EXISTS users (
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    user_name VARCHAR(50) NOT NULL UNIQUE,
    phone_no VARCHAR(10),
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50),
    PRIMARY KEY (user_name)
);

-- Create 'products' table
CREATE TABLE IF NOT EXISTS products (
    product_name VARCHAR(50) NOT NULL UNIQUE,
    price VARCHAR(5),
    quantity VARCHAR(50),
    image_name VARCHAR(50),
    PRIMARY KEY (product_name)
);

-- Create 'orders' table
CREATE TABLE IF NOT EXISTS orders (
    order_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ordered_user VARCHAR(50),
    order_size INT(5),
    FOREIGN KEY (ordered_user) REFERENCES users(user_name)
);
