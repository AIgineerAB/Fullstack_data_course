desc;

SELECT * FROM youtube;

-- science and tech
SELECT  
	*
FROM
	youtube
WHERE
	category = 'Science & Technology';


-- audience country
SELECT  
	DISTINCT "audience country"
FROM
	youtube;


-- Japan - will I find anime channels there?
SELECT
	*
FROM
	youtube
WHERE
	"audience country" = 'Japan'
;

-- which audience countries are most represented in the dataset?
SELECT
	"audience country",
	count(*) as number_youtubers
FROM
	youtube
GROUP BY
	"audience country"
ORDER BY
	number_youtubers DESC
LIMIT 10
;


-- category by popularity
SELECT
	category,
	count(*) AS number
FROM
	youtube
GROUP BY
	category
ORDER BY
	number DESC; 
	

-- check comments
SELECT
	DISTINCT "avg comments"
FROM
	youtube;

-- COUNT COUNTRIES

SELECT
	"youtuber name",
	CASE 
		WHEN "avg comments" = 'N/A' THEN 0
		WHEN "avg comments" LIKE '%K' THEN CAST(REPLACE("avg comments",
		'K',
		'') AS INTEGER)* 1000
		ELSE CAST("avg comments" AS INTEGER)
	END AS avg_comments
FROM
	youtube
ORDER BY
	avg_comments DESC;







