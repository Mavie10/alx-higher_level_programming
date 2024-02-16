--script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT 'title' , SUM('rate') As 'rating'
from 'tv_shows' As t
inner join 'tv_show_ratings' AS r
on t.'id' = r.'show_id'
group by 'title'
order by 'rating' DESC;
