--script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT 'name' , sum('rate') AS 'rating'
	FROM 'tv_genres' As g
	inner join 'tv_show_genres' As s
	on s.'genre_id' = g.'id'

	inner join 'tv_show_ratings' As r
	on r.'show_id' = s.'show_id'
	group by 'name'
	order by 'rating' DESC;
