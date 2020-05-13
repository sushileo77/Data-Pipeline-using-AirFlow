class SqlQueries:
	create_table_artist = ("""
        CREATE TABLE IF NOT EXISTS public.artists (
                artistid varchar(256) NOT NULL,
                name varchar(256),
                location varchar(256),
                lattitude numeric(18,0),
                longitude numeric(18,0)
         );
    """)
    
   create_table_songplays = ("""
        CREATE TABLE IF NOT EXISTS public.songplays        
            playid varchar PRIMARY KEY,
            start_time timestamp NOT NULL,
            userid int NOT NULL,
            "level" varchar,
            songid varchar,
            artistid varchar,
            sessionid int,
            location varchar,
            user_agent varchar,
            
        );
    """)
    
   create_table_songs = ("""
        CREATE TABLE IF NOT EXISTS public.songs (
            songid varchar PRIMARY KEY,
            title varchar(256),
            artistid varchar(256),
            "year" int4,
            duration numeric(18,0),
            
        );
    """)
    
   create_table_staging_events = ("""
        CREATE TABLE IF NOT EXISTS public.staging_events (
            artist varchar,
            auth varchar,
            firstname varchar,
            gender varchar,
            iteminsession int,
            lastname varchar,
            length numeric,
            "level" varchar,
            location varchar,
            "method" varchar,
            page varchar,
            registration numeric,
            sessionid int,
            song varchar,
            status int,
            ts int,
            useragent varchar,
            userid 
        );
    """)
    
   create_table_staging_songs = ("""
        CREATE TABLE IF NOT EXISTS public.staging_songs (
                num_songs int,
                artist_id varchar,
                artist_name varchar,
                artist_latitude numeric,
                artist_longitude numeric,
                artist_location varchar,
                song_id varchar,
                title varchar,
                duration numeric,
                "year" int
            );
    """)
    
   create_table_time = ("""
        CREATE TABLE IF NOT EXISTS public."time" (
            start_time timestamp PRIMARY KEY,
            "hour" int,
            "day" int,
            week int,
            "month" varchar,
            "year" int,
            weekday varchar,
            
        );
    """)
    
   create_table_users = ("""
        CREATE TABLE IF NOT EXISTS public.users (
            userid int PRIMARY KEY,
            first_name varchar,
            last_name varchar,
            gender varchar,
            "level" varchar,
        
        );
    """)
    
   songplay_table_insert = ("""
        SELECT
                md5(events.sessionid || events.start_time) songplay_id,
                events.start_time, 
                events.userid, 
                events.level, 
                songs.song_id, 
                songs.artist_id, 
                events.sessionid, 
                events.location, 
                events.useragent
                FROM (SELECT TIMESTAMP 'epoch' + ts/1000 * interval '1 second' AS start_time, *
            FROM staging_events
            WHERE page='NextSong') events
            LEFT JOIN staging_songs songs
            ON events.song = songs.title
                AND events.artist = songs.artist_name
                AND events.length = songs.duration
    """)

   user_table_insert = ("""
        SELECT distinct userid, firstname, lastname, gender, level
        FROM staging_events
        WHERE page='NextSong'
    """)

   song_table_insert = ("""
        SELECT distinct song_id, title, artist_id, year, duration
        FROM staging_songs
    """)

   artist_table_insert = ("""
        SELECT distinct artist_id, artist_name, artist_location, artist_latitude, artist_longitude
        FROM staging_songs
    """)

   time_table_insert = ("""
        SELECT start_time, extract(hour from start_time), extract(day from start_time), extract(week from start_time), 
               extract(month from start_time), extract(year from start_time), extract(dayofweek from start_time)
        FROM songplays
    """)