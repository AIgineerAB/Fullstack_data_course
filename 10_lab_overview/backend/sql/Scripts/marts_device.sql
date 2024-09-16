CREATE TABLE IF NOT EXISTS marts.device_views_date AS (
SELECT
	STRFTIME('%Y-%m-%d',
	datum) AS Datum,
	Enhetstyp,
	sum(Visningar) AS Visningar
FROM
	enhetstyp.diagramdata d
GROUP BY
	(datum,
	Enhetstyp )
ORDER BY 
	Datum ASC );

CREATE TABLE IF NOT EXISTS marts.device_summary AS (
SELECT
	Enhetstyp,
	Visningar,
	"Visningstid (timmar)" AS Visningstid_timmar,
	"Genomsnittlig visningslängd" AS Visningslängd_genomsnitt
FROM
	enhetstyp.tabelldata );



-- checks
SELECT * FROM marts.device_views_date;
SELECT * FROM marts.device_summary;