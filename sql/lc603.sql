-- Consective avaliable seat, 83%

# Write your MySQL query statement below
SELECT DISTINCT t1.seat_id
FROM cinema t1, cinema t2
WHERE abs(t1.seat_id - t2.seat_id) = 1 and t1.free = 1 and t2.free = 1
ORDER BY t1.seat_id
