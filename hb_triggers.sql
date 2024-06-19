
-- Trigger pour intercepter les insertions dans ALL_WORKERS_ELAPSED
CREATE TRIGGER prevent_insert_on_all_workers_elapsed
INSTEAD OF INSERT ON ALL_WORKERS_ELAPSED
FOR EACH ROW EXECUTE FUNCTION raise_exception();

CREATE OR REPLACE FUNCTION raise_exception() RETURNS trigger AS $$
BEGIN
    RAISE EXCEPTION 'Insertion not allowed on view ALL_WORKERS_ELAPSED';
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- Trigger pour enregistrer la date d'ajout d'un nouveau robot
CREATE TRIGGER log_new_robot
AFTER INSERT ON robots
FOR EACH ROW EXECUTE FUNCTION log_robot_addition();

CREATE OR REPLACE FUNCTION log_robot_addition() RETURNS trigger AS $$
BEGIN
    INSERT INTO audit_robot (robot_id, creation_date) VALUES (NEW.robot_id, CURRENT_DATE);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger pour vérifier la cohérence entre la table FACTORIES et les tables WORKERS_FACTORY_<N>
CREATE TRIGGER check_factory_table_consistency
BEFORE INSERT OR UPDATE OR DELETE ON ROBOTS_FACTORIES
FOR EACH STATEMENT EXECUTE FUNCTION check_consistency();

CREATE OR REPLACE FUNCTION check_consistency() RETURNS trigger AS $$
DECLARE
    factory_count INTEGER;
    worker_table_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO factory_count FROM factories;
    SELECT COUNT(*) INTO worker_table_count FROM pg_tables WHERE tablename LIKE 'workers_factory_%';

    IF factory_count != worker_table_count THEN
        RAISE EXCEPTION 'Factory count does not match worker table count';
    END IF;

    RETURN NULL;
END;
$$ LANGUAGE plpgsql;
