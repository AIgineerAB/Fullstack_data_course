SELECT * FROM youtube;

-- there are nulls
DESC youtube;

-- 24 rows
SELECT distinct Category from youtube;

SELECT 
    count(*) - count("youtuber name") as null_youtuber,
    count(*) - count("channel name") as null_channel,
    count(*) - count("category") as null_category,
FROM youtube;