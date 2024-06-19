

-- Trigger Function: Handle Insertions into ALL_WORKERS_ELAPSED
CREATE OR REPLACE FUNCTION handle_insert_all_workers_elapsed()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO employees (firstname, lastname, age, start_date, is_active, factory_id)
        VALUES (NEW.firstname, NEW.lastname, NEW.age, NEW.start_date, TRUE, (SELECT factory_id FROM factories LIMIT 1));
        RETURN NEW;
    ELSIF TG_OP = 'UPDATE' THEN
        RAISE EXCEPTION 'UPDATING the view ALL_WORKERS_ELAPSED is not allowed';
    ELSIF TG_OP = 'DELETE' THEN
        RAISE EXCEPTION 'DELETING from the view ALL_WORKERS_ELAPSED is not allowed';
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_all_workers_elapsed
INSTEAD OF INSERT OR UPDATE OR DELETE ON ALL_WORKERS_ELAPSED
FOR EACH ROW EXECUTE FUNCTION handle_insert_all_workers_elapsed();

CREATE OR REPLACE FUNCTION record_robot_addition()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_robot (robot_id, creation_date) 
    VALUES (NEW.robot_id, CURRENT_DATE);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_robot_addition
AFTER INSERT ON robots
FOR EACH ROW EXECUTE FUNCTION record_robot_addition();

CREATE OR REPLACE FUNCTION validate_factory_and_tables()
RETURNS TRIGGER AS $$
DECLARE
    factory_count INTEGER;
    table_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO factory_count FROM factories;

    SELECT COUNT(*) INTO table_count
    FROM pg_tables
    WHERE schemaname = 'public' AND tablename LIKE 'workers_factory_%';

    IF factory_count <> table_count THEN
        RAISE EXCEPTION 'Modification is not allowed as the number of factories (%) does not match the number of tables (WORKERS_FACTORY_<N>) (%).', factory_count, table_count;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_robots_factories
INSTEAD OF INSERT OR UPDATE OR DELETE ON ROBOTS_FACTORIES
FOR EACH ROW EXECUTE FUNCTION validate_factory_and_tables();
