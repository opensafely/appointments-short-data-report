SELECT
    'BookedDate' AS column_name,
    MAX(BookedDate) AS max_date,
    MIN(BookedDate) AS min_date
UNION ALL
SELECT
    'StartDate' AS column_name,
    MAX(StartDate) AS max_date,
    MIN(StartDate) AS min_date
UNION ALL
SELECT
    'ArrivedDate' AS column_name,
    MAX(ArrivedDate) AS max_date,
    MIN(ArrivedDate) AS min_date
UNION ALL
SELECT
    'EndDate' AS column_name,
    MAX(EndDate) AS max_date,
    MIN(EndDate) AS min_date
UNION ALL
SELECT
    'FinishedDate' AS column_name,
    MAX(FinishedDate) AS max_date,
    MIN(FinishedDate) AS min_date
UNION ALL
SELECT
    'SeenDate' AS column_name,
    MAX(SeenDate) AS max_date,
    MIN(SeenDate) AS min_date
