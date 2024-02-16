--script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

--Each record should display: tv_shows.title - tv_show_genres.genre_id
--Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
--You can use only one SELECT statement
--The database name will be passed as an argument of the mysql command
SELECT s.'title' , g.'genre_id'
	FROM 'tv_Shows' As s
	left join 'tv_show_genres' As g
	on s.'id' = g.'show_id'
	where g.genre_id'  IS NULL
	order by s.'title', g.'genre_id';
