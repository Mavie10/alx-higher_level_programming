-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT t.'title'
	FROM 'tv_shows' AS t
	inner join 'tv_shows_genres' As s
	on t.'id' = s.'show_id'

	inner join 'tv_genres' AS g
	on g.'id' = s.'genre_id'
	where g.'name' = "Comedy"
	order by t.'title';
