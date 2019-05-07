-- count(*) will be faster than count(specific_column)
SELECT t2.requester_id AS id, t2.num
FROM
(SELECT t.requester_id, COUNT(*) AS num
FROM
(SELECT requester_id FROM request_accepted
UNION ALL
SELECT accepter_id FROM request_accepted) AS t
GROUP BY requester_id) AS t2
ORDER BY t2.num DESC
LIMIT 1
