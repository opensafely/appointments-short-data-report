SELECT
    'BookedDate' AS column_name,
    CAST(MIN(BookedDate) AS DATE) AS min_date,
    CAST(MAX(BookedDate) AS DATE) AS max_date
FROM Appointment
UNION ALL
SELECT
    'StartDate' AS column_name,
    CAST(MIN(StartDate) AS DATE) AS min_date,
    CAST(MAX(StartDate) AS DATE) AS max_date
FROM Appointment
UNION ALL
SELECT
    'ArrivedDate' AS column_name,
    CAST(MIN(ArrivedDate) AS DATE) AS min_date,
    CAST(MAX(ArrivedDate) AS DATE) AS max_date
FROM Appointment
UNION ALL
SELECT
    'EndDate' AS column_name,
    CAST(MIN(EndDate) AS DATE) AS min_date,
    CAST(MAX(EndDate) AS DATE) AS max_date
FROM Appointment
UNION ALL
SELECT
    'FinishedDate' AS column_name,
    CAST(MIN(FinishedDate) AS DATE) AS min_date,
    CAST(MAX(FinishedDate) AS DATE) AS max_date
FROM Appointment
UNION ALL
SELECT
    'SeenDate' AS column_name,
    CAST(MIN(SeenDate) AS DATE) AS min_date,
    CAST(MAX(SeenDate) AS DATE) AS max_date
FROM Appointment
