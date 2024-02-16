--script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT t.'title' , g.'name'
	FROM 'tv_shows' As t
	left join 'tv_show_genres' As s
	on t.'id' = s.'show_id'

	left join 'tv_genres' As g
	on s.'genre_id' = g.'id'
	order by t.'title' , g.'name';
