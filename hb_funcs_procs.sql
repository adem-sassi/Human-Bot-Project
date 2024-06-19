-- Functions

-- 1. GET_NB_WORKERS
CREATE OR REPLACE FUNCTION GET_NB_WORKERS
(FACTORY_ID INTEGER)
RETURNS INTEGER AS $$
DECLARE
    NUM_WORKERS INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO NUM_WORKERS
    FROM employees
    WHERE employees.factory_id = GET_NB_WORKERS.FACTORY_ID AND employees.is_active = TRUE;

    RETURN NUM_WORKERS;
END;
$$ LANGUAGE plpgsql;



-- 2. GET_NB_BIG_ROBOTS
CREATE OR REPLACE FUNCTION GET_NB_BIG_ROBOTS
()
RETURNS INTEGER AS $$
DECLARE
    NUM_BIG_ROBOTS INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO NUM_BIG_ROBOTS
    FROM robots
    WHERE robots.parts_used > 3;

    RETURN NUM_BIG_ROBOTS;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION GET_BEST_SUPPLIER
()
RETURNS VARCHAR
(100) AS $$
DECLARE
    BEST_SUPPLIER_NAME VARCHAR
(100);
BEGIN
    SELECT supplier_name
    INTO BEST_SUPPLIER_NAME
    FROM BEST_SUPPLIERS
    ORDER BY supplier_name -- Example: Order by supplier_name for simplicity
    LIMIT 1;

    RETURN BEST_SUPPLIER_NAME;
END;
$$ LANGUAGE plpgsql;


-- Procedures

-- 1. SEED_DATA_WORKERS
CREATE OR REPLACE PROCEDURE SEED_DATA_WORKERS
(NB_WORKERS INTEGER, FACTORY_ID INTEGER)
LANGUAGE plpgsql AS $$
DECLARE
    i INTEGER;
BEGIN
    FOR i IN 1..NB_WORKERS LOOP
    INSERT INTO employees
        (firstname, lastname, start_date, is_active, factory_id)
    VALUES
        ('worker_f_' || i, 'worker_l_' || i,
            (DATE
    '2065-01-01' +
    (random
    () *
    (DATE '2070-01-01' - DATE '2065-01-01'))::integer),
                TRUE, FACTORY_ID);
END
LOOP;
END;
$$;


-- 2. ADD_NEW_ROBOT
CREATE OR REPLACE PROCEDURE ADD_NEW_ROBOT
(MODEL_NAME VARCHAR
(50))
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO robots
        (robot_model, produced_quantity, parts_used, factory_id)
    VALUES
        (MODEL_NAME, 0, 0, (SELECT factory_id
            FROM factories LIMIT
    1));
END;
$$;
