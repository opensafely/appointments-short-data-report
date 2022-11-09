SELECT
    'BookedDate' AS column_name,
    CAST(MAX(BookedDate) AS DATE) AS max_date,
    CAST(MIN(BookedDate) AS DATE) AS min_date
FROM Appointment
UNION ALL
SELECT
    'StartDate' AS column_name,
    CAST(MAX(StartDate) AS DATE) AS max_date,
    CAST(MIN(StartDate) AS DATE) AS min_date
FROM Appointment
UNION ALL
SELECT
    'ArrivedDate' AS column_name,
    CAST(MAX(ArrivedDate) AS DATE) AS max_date,
    CAST(MIN(ArrivedDate) AS DATE) AS min_date
FROM Appointment
UNION ALL
SELECT
    'EndDate' AS column_name,
    CAST(MAX(EndDate) AS DATE) AS max_date,
    CAST(MIN(EndDate) AS DATE) AS min_date
FROM Appointment
UNION ALL
SELECT
    'FinishedDate' AS column_name,
    CAST(MAX(FinishedDate) AS DATE) AS max_date,
    CAST(MIN(FinishedDate) AS DATE) AS min_date
FROM Appointment
UNION ALL
SELECT
    'SeenDate' AS column_name,
    CAST(MAX(SeenDate) AS DATE) AS max_date,
    CAST(MIN(SeenDate) AS DATE) AS min_date
FROM Appointment
