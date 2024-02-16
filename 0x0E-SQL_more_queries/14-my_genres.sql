--script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT g.'name'
	FROM 'tv_genres' As g
	inner join 'tv_show_genres' AS s
	on g.'id' = s.'genre_id'

	inner join 'tv_shows' As t
	on t.'id' = s.'shows_id'
	where t.'title' = "Dexter"
	order by g.'name';
