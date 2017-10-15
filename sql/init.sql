-- 001 table
CREATE TABLE level1 (
    id SERIAL PRIMARY KEY NOT NULL,
    idiom TEXT UNIQUE NOT NULL,
    title TEXT,
    name TEXT,
    learnt_date DATE NOT NULL,
    learnt_count SMALLINT DEFAULT 0 NOT NULL,
    last_updated TIMESTAMP NOT NULL,
    created TIMESTAMP DEFAULT NOW() NOT NULL

);


-- 002 indexes
