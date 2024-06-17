-- Table EMPLOYEES
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    age INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE
);

-- Table SUPPLIERS
CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL
);

-- Table DELIVERIES
CREATE TABLE deliveries (
    delivery_id SERIAL PRIMARY KEY,
    delivery_date DATE NOT NULL,
    delivered_quantity INTEGER NOT NULL,
    receiver_id INTEGER REFERENCES employees(employee_id),
    supplier_id INTEGER REFERENCES suppliers(supplier_id)
);

-- Table FACTORIES
CREATE TABLE factories (
    factory_id SERIAL PRIMARY KEY,
    factory_name VARCHAR(100) NOT NULL
);

-- Table ROBOTS
CREATE TABLE robots (
    robot_id SERIAL PRIMARY KEY,
    robot_model VARCHAR(50) NOT NULL,
    produced_quantity INTEGER NOT NULL,
    parts_used INTEGER NOT NULL,
    factory_id INTEGER REFERENCES factories(factory_id)
);
