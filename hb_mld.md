# Modèle Logique de Données

## Table: factories
- factory_id: SERIAL PRIMARY KEY
- factory_name: VARCHAR(100) NOT NULL

## Table: employees
- employee_id: SERIAL PRIMARY KEY
- firstname: VARCHAR(50) NOT NULL
- lastname: VARCHAR(50) NOT NULL
- age: INTEGER
- start_date: DATE NOT NULL
- end_date: DATE
- is_active: BOOLEAN NOT NULL DEFAULT TRUE
- factory_id: INTEGER REFERENCES factories(factory_id)

## Table: suppliers
- supplier_id: SERIAL PRIMARY KEY
- supplier_name: VARCHAR(100) NOT NULL

## Table: deliveries
- delivery_id: SERIAL PRIMARY KEY
- supplier_id: INTEGER REFERENCES suppliers(supplier_id)
- delivery_date: DATE NOT NULL
- quantity: INTEGER NOT NULL
- received_by: INTEGER REFERENCES employees(employee_id)
- factory_id: INTEGER REFERENCES factories(factory_id)

## Table: robots
- robot_id: SERIAL PRIMARY KEY
- robot_model: VARCHAR(50) NOT NULL
- produced_quantity: INTEGER NOT NULL
- parts_used: INTEGER NOT NULL
- factory_id: INTEGER REFERENCES factories(factory_id)

## Table: audit_robot
- audit_id: SERIAL PRIMARY KEY
- robot_id: INTEGER REFERENCES robots(robot_id)
- creation_date: DATE NOT NULL DEFAULT CURRENT_DATE
