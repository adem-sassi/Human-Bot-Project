


-- Fonction GET_NB_WORKERS
CREATE FUNCTION GET_NB_WORKERS(FACTORY_ID INTEGER) RETURNS INTEGER AS $$
BEGIN
    RETURN (SELECT COUNT(*)
    FROM employees
    WHERE factory_id = FACTORY_ID AND is_active = TRUE);
END;
$$ LANGUAGE plpgsql;

-- Fonction GET_NB_BIG_ROBOTS
CREATE FUNCTION GET_NB_BIG_ROBOTS() RETURNS INTEGER AS $$
BEGIN
    RETURN (SELECT COUNT(*)
    FROM robots
    WHERE parts_used > 3);
END;
$$ LANGUAGE plpgsql;

-- Fonction GET_BEST_SUPPLIER
CREATE FUNCTION GET_BEST_SUPPLIER() RETURNS VARCHAR(100) AS $$
BEGIN
    RETURN (SELECT supplier_name
    FROM BEST_SUPPLIERS LIMIT
    1);
END;
$$ LANGUAGE plpgsql;

-- Procédure SEED_DATA_WORKERS
CREATE PROCEDURE SEED_DATA_WORKERS(NB_WORKERS INTEGER, FACTORY_ID INTEGER) LANGUAGE plpgsql AS $$
DECLARE
    i INTEGER;
BEGIN
    FOR i IN 1..NB_WORKERS LOOP
    INSERT INTO employees
        (firstname, lastname, start_date, is_active, factory_id)
    VALUES
        ('worker_f_' || i, 'worker_l_' || i, (DATE
    '2065-01-01' +
    (random
    () *
    (DATE '2070-01-01' - DATE '2065-01-01'))::integer), TRUE, FACTORY_ID);
END
LOOP;
END;
$$;

-- Procédure ADD_NEW_ROBOT
CREATE PROCEDURE ADD_NEW_ROBOT(MODEL_NAME VARCHAR
(50)) LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO robots
        (robot_model, produced_quantity, parts_used, factory_id)
    VALUES
        (MODEL_NAME, 0, 0, (SELECT factory_id
            FROM factories LIMIT
    1));
END;
$$;
