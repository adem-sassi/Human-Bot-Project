-- Vue affichant les employés dont l'âge est renseigné
CREATE OR REPLACE VIEW employees_with_age
AS
SELECT *
FROM employees
WHERE age IS NOT NULL;

-- Vue ALL_WORKERS
CREATE OR REPLACE VIEW ALL_WORKERS
AS
SELECT lastname, firstname, age, start_date
FROM employees
WHERE end_date IS NULL
ORDER BY start_date DESC;

-- Vue ALL_WORKERS_ELAPSED
CREATE OR REPLACE VIEW ALL_WORKERS_ELAPSED
AS
SELECT lastname, firstname, age, start_date, CURRENT_DATE - start_date AS days_elapsed
FROM ALL_WORKERS;

-- Vue BEST_SUPPLIERS
CREATE OR REPLACE VIEW BEST_SUPPLIERS
AS
SELECT supplier_name, SUM(quantity) AS total_quantity
FROM deliveries
    JOIN suppliers ON deliveries.supplier_id = suppliers.supplier_id
GROUP BY supplier_name
HAVING SUM(quantity) > 1000
ORDER BY total_quantity DESC;

-- Vue ROBOTS_FACTORIES
CREATE OR REPLACE VIEW ROBOTS_FACTORIES
AS
SELECT robot_id, robot_model, factory_name
FROM robots
    JOIN factories ON robots.factory_id = factories.factory_id;
