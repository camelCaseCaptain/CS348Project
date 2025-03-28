
-- Drop if it exists
DROP FUNCTION IF EXISTS search_food_trucks(TEXT, TEXT);

-- Create it again
CREATE OR REPLACE FUNCTION search_food_trucks(search_term TEXT, sort_by TEXT)
RETURNS TABLE (
    name TEXT,
    location TEXT,
    latitude NUMERIC,
    longitude NUMERIC,
    openTime NUMERIC,
    closeTime NUMERIC
) AS $$
BEGIN
    RETURN QUERY EXECUTE format(
        'SELECT name, location, latitude, longitude, openTime, closeTime
         FROM yourapp_foodtruck
         WHERE name ILIKE %%L OR location ILIKE %%L
         ORDER BY %I',
        '%' || search_term || '%',
        '%' || search_term || '%',
        sort_by
    );
END;
$$ LANGUAGE plpgsql;