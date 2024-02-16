--script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT g.'name' As 'genre' ,
	COUNT(*) AS 'number_of_shows'
	from 'tv_genres' As g
	inner join 'tv_show_genres' As t
	on g.'id' = t.'genre_id'
	group by g.'name'
	order by 'number_of_shows' DESC;
