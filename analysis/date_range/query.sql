SELECT 'BookedDate' AS column_name
SELECT MAX(BookedDate) AS max_date
SELECT MIN(BookedDate) AS min_date
UNION ALL
SELECT 'StartDate' AS column_name
SELECT MAX(StartDate) AS max_date
SELECT MIN(StartDate) AS min_date
UNION ALL
SELECT 'ArrivedDate' AS column_name
SELECT MAX(ArrivedDate) AS max_date
SELECT MIN(ArrivedDate) AS min_date
UNION ALL
SELECT 'EndDate' AS column_name
SELECT MAX(EndDate) AS max_date
SELECT MIN(EndDate) AS min_date
UNION ALL
SELECT 'FinishedDate' AS column_name
SELECT MAX(FinishedDate) AS max_date
SELECT MIN(FinishedDate) AS min_date
UNION ALL
SELECT 'SeenDate' AS column_name
SELECT MAX(SeenDate) AS max_date
SELECT MIN(SeenDate) AS min_date
