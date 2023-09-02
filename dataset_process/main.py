import sqlite3
import pandas as pd

COLUMNS = ["player_id","player_url","fifa_version","fifa_update","fifa_update_date","short_name","long_name","player_positions","overall","potential","value_eur","wage_eur","age","dob","height_cm","weight_kg","league_id","league_name","league_level","club_team_id","club_name","club_position","club_jersey_number","club_loaned_from","club_joined_date","club_contract_valid_until_year","nationality_id","nationality_name","nation_team_id","nation_position","nation_jersey_number","preferred_foot","weak_foot","skill_moves","international_reputation","work_rate","body_type","real_face","release_clause_eur","player_tags","player_traits","pace","shooting","passing","dribbling","defending","physic","attacking_crossing","attacking_finishing","attacking_heading_accuracy","attacking_short_passing","attacking_volleys","skill_dribbling","skill_curve","skill_fk_accuracy","skill_long_passing","skill_ball_control","movement_acceleration","movement_sprint_speed","movement_agility","movement_reactions","movement_balance","power_shot_power","power_jumping","power_stamina","power_strength","power_long_shots","mentality_aggression","mentality_interceptions","mentality_positioning","mentality_vision","mentality_penalties","mentality_composure","defending_marking_awareness","defending_standing_tackle","defending_sliding_tackle","goalkeeping_diving","goalkeeping_handling","goalkeeping_kicking","goalkeeping_positioning","goalkeeping_reflexes","goalkeeping_speed","ls","st","rs","lw","lf","cf","rf","rw","lam","cam","ram","lm","lcm","cm","rcm","rm","lwb","ldm","cdm","rdm","rwb","lb","lcb","cb","rcb","rb","gk"]
LAST_COLUMN = "player_face_url"

def create_db():
    conn = sqlite3.connect('fifa.db')
    cursor = conn.cursor()

    # cols_string = ''

    # for column in COLUMNS:
    #     cols_string += column + ','
    # cols_string += LAST_COLUMN

    # table_create_query = f'''
    #     CREATE TABLE IF NOT EXISTS FIFA (
    #         {cols_string}
    #     );  
    # '''
    # print(table_create_query)
    cursor.execute(create_table_query)


def test_read():
    conn = sqlite3.connect('fifa.db')
    cursor = conn.cursor()
    result = cursor.execute("PRAGMA table_info('fifa')")
    print(result.fetchmany())



def read_csv():
    # df = pd.read_csv('male_players.csv', )
    print('hello')
    chunk_size = 100
    limit = 0
    chunks = pd.read_csv('male_players.csv', chunksize=chunk_size)
    
    for chunk in chunks:
        for index, row in chunk.iterrows():
            print(type(row))
        
        # chunk.        
        # print('-----------')
        # # print(chunk['ls'])
        # for item in chunk['short_name']:
        #     print(item)
        # print('-----------')
       
create_table_query = '''
CREATE TABLE IF NOT EXISTS FIFA (
    player_id INTEGER PRIMARY KEY,
    player_url TEXT,
    fifa_version TEXT,
    fifa_update TEXT,
    fifa_update_date TEXT,
    short_name TEXT,
    long_name TEXT,
    player_positions TEXT,
    overall INTEGER,
    potential INTEGER,
    value_eur INTEGER,
    wage_eur INTEGER,
    age INTEGER,
    dob TEXT,
    height_cm INTEGER,
    weight_kg INTEGER,
    league_id INTEGER,
    league_name TEXT,
    league_level INTEGER,
    club_team_id INTEGER,
    club_name TEXT,
    club_position TEXT,
    club_jersey_number INTEGER,
    club_loaned_from TEXT,
    club_joined_date TEXT,
    club_contract_valid_until_year INTEGER,
    nationality_id INTEGER,
    nationality_name TEXT,
    nation_team_id INTEGER,
    nation_position TEXT,
    nation_jersey_number INTEGER,
    preferred_foot TEXT,
    weak_foot INTEGER,
    skill_moves INTEGER,
    international_reputation INTEGER,
    work_rate TEXT,
    body_type TEXT,
    real_face TEXT,
    release_clause_eur INTEGER,
    player_tags TEXT,
    player_traits TEXT,
    pace INTEGER,
    shooting INTEGER,
    passing INTEGER,
    dribbling INTEGER,
    defending INTEGER,
    physic INTEGER,
    attacking_crossing INTEGER,
    attacking_finishing INTEGER,
    attacking_heading_accuracy INTEGER,
    attacking_short_passing INTEGER,
    attacking_volleys INTEGER,
    skill_dribbling INTEGER,
    skill_curve INTEGER,
    skill_fk_accuracy INTEGER,
    skill_long_passing INTEGER,
    skill_ball_control INTEGER,
    movement_acceleration INTEGER,
    movement_sprint_speed INTEGER,
    movement_agility INTEGER,
    movement_reactions INTEGER,
    movement_balance INTEGER,
    power_shot_power INTEGER,
    power_jumping INTEGER,
    power_stamina INTEGER,
    power_strength INTEGER,
    power_long_shots INTEGER,
    mentality_aggression INTEGER,
    mentality_interceptions INTEGER,
    mentality_positioning INTEGER,
    mentality_vision INTEGER,
    mentality_penalties INTEGER,
    mentality_composure INTEGER,
    defending_marking_awareness INTEGER,
    defending_standing_tackle INTEGER,
    defending_sliding_tackle INTEGER,
    goalkeeping_diving INTEGER,
    goalkeeping_handling INTEGER,
    goalkeeping_kicking INTEGER,
    goalkeeping_positioning INTEGER,
    goalkeeping_reflexes INTEGER,
    goalkeeping_speed INTEGER,
    ls INTEGER,
    st INTEGER,
    rs INTEGER,
    lw INTEGER,
    lf INTEGER,
    cf INTEGER,
    rf INTEGER,
    rw INTEGER,
    lam INTEGER,
    cam INTEGER,
    ram INTEGER,
    lm INTEGER,
    lcm INTEGER,
    cm INTEGER,
    rcm INTEGER,
    rm INTEGER,
    lwb INTEGER,
    ldm INTEGER,
    cdm INTEGER,
    rdm INTEGER,
    rwb INTEGER,
    lb INTEGER,
    lcb INTEGER,
    cb INTEGER,
    rcb INTEGER,
    rb INTEGER,
    gk INTEGER,
    player_face_url TEXT
);
'''


if __name__ == '__main__':
    # read_csv()
    # create_db()
    test_read()



