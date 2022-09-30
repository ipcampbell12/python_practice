"""  #LOAD QUERY RESULTS
        query = '''
        SELECT p.fname || ' ' || p.lname AS name, COUNT(m.winner) AS games_won FROM players p 
        JOIN match_player mp
        ON p.id = mp.player_id 
        JOIN matches m
        ON mp.matches_id = m.id
        WHERE p.id = m.winner
        GROUP BY p.fname,p.lname;
        ''' """
