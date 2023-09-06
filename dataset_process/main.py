import sqlite3
import pandas as pd

COLUMNS = ["player_id","player_url","fifa_version","fifa_update","fifa_update_date","short_name","long_name","player_positions","overall","potential","value_eur","wage_eur","age","dob","height_cm","weight_kg","league_id","league_name","league_level","club_team_id","club_name","club_position","club_jersey_number","club_loaned_from","club_joined_date","club_contract_valid_until_year","nationality_id","nationality_name","nation_team_id","nation_position","nation_jersey_number","preferred_foot","weak_foot","skill_moves","international_reputation","work_rate","body_type","real_face","release_clause_eur","player_tags","player_traits","pace","shooting","passing","dribbling","defending","physic","attacking_crossing","attacking_finishing","attacking_heading_accuracy","attacking_short_passing","attacking_volleys","skill_dribbling","skill_curve","skill_fk_accuracy","skill_long_passing","skill_ball_control","movement_acceleration","movement_sprint_speed","movement_agility","movement_reactions","movement_balance","power_shot_power","power_jumping","power_stamina","power_strength","power_long_shots","mentality_aggression","mentality_interceptions","mentality_positioning","mentality_vision","mentality_penalties","mentality_composure","defending_marking_awareness","defending_standing_tackle","defending_sliding_tackle","goalkeeping_diving","goalkeeping_handling","goalkeeping_kicking","goalkeeping_positioning","goalkeeping_reflexes","goalkeeping_speed","ls","st","rs","lw","lf","cf","rf","rw","lam","cam","ram","lm","lcm","cm","rcm","rm","lwb","ldm","cdm","rdm","rwb","lb","lcb","cb","rcb","rb","gk"]
LAST_COLUMN = "player_face_url"
conn = sqlite3.connect('fifa.db')
cursor = conn.cursor()

def create_db():
    cursor.execute(create_table_query)


def test_read():
    conn = sqlite3.connect('fifa.db')
    cursor = conn.cursor()
    result = cursor.execute("select * from fifa order by player_id desc limit 10");
    conn.commit()
    print(result.fetchall())

def read_csv():
    chunk_size = 1000
    limit = 0
    chunks = pd.read_csv('male_players.csv', chunksize=chunk_size)
    
    for chunk in chunks:
        for index, row in chunk.iterrows():
            arr = []
            for cell in row:
                # print(cell)
                arr.append(str(cell))
            arr[0] = int(arr[0])
            try:
                if (str(arr[2]) != '23'):
                    continue
                cursor.execute(insert_query, tuple(arr))
            except sqlite3.Error as err:
                print(err)
                continue
        conn.commit()
            # return


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
    overall TEXT,
    potential TEXT,
    value_eur TEXT,
    wage_eur TEXT,
    age TEXT,
    dob TEXT,
    height_cm TEXT,
    weight_kg TEXT,
    league_id TEXT,
    league_name TEXT,
    league_level TEXT,
    club_team_id TEXT,
    club_name TEXT,
    club_position TEXT,
    club_jersey_number TEXT,
    club_loaned_from TEXT,
    club_joined_date TEXT,
    club_contract_valid_until_year TEXT,
    nationality_id TEXT,
    nationality_name TEXT,
    nation_team_id TEXT,
    nation_position TEXT,
    nation_jersey_number TEXT,
    preferred_foot TEXT,
    weak_foot TEXT,
    skill_moves TEXT,
    international_reputation TEXT,
    work_rate TEXT,
    body_type TEXT,
    real_face TEXT,
    release_clause_eur TEXT,
    player_tags TEXT,
    player_traits TEXT,
    pace TEXT,
    shooting TEXT,
    passing TEXT,
    dribbling TEXT,
    defending TEXT,
    physic TEXT,
    attacking_crossing TEXT,
    attacking_finishing TEXT,
    attacking_heading_accuracy TEXT,
    attacking_short_passing TEXT,
    attacking_volleys TEXT,
    skill_dribbling TEXT,
    skill_curve TEXT,
    skill_fk_accuracy TEXT,
    skill_long_passing TEXT,
    skill_ball_control TEXT,
    movement_acceleration TEXT,
    movement_sprint_speed TEXT,
    movement_agility TEXT,
    movement_reactions TEXT,
    movement_balance TEXT,
    power_shot_power TEXT,
    power_jumping TEXT,
    power_stamina TEXT,
    power_strength TEXT,
    power_long_shots TEXT,
    mentality_aggression TEXT,
    mentality_interceptions TEXT,
    mentality_positioning TEXT,
    mentality_vision TEXT,
    mentality_penalties TEXT,
    mentality_composure TEXT,
    defending_marking_awareness TEXT,
    defending_standing_tackle TEXT,
    defending_sliding_tackle TEXT,
    goalkeeping_diving TEXT,
    goalkeeping_handling TEXT,
    goalkeeping_kicking TEXT,
    goalkeeping_positioning TEXT,
    goalkeeping_reflexes TEXT,
    goalkeeping_speed TEXT,
    ls TEXT,
    st TEXT,
    rs TEXT,
    lw TEXT,
    lf TEXT,
    cf TEXT,
    rf TEXT,
    rw TEXT,
    lam TEXT,
    cam TEXT,
    ram TEXT,
    lm TEXT,
    lcm TEXT,
    cm TEXT,
    rcm TEXT,
    rm TEXT,
    lwb TEXT,
    ldm TEXT,
    cdm TEXT,
    rdm TEXT,
    rwb TEXT,
    lb TEXT,
    lcb TEXT,
    cb TEXT,
    rcb TEXT,
    rb TEXT,
    gk TEXT,
    player_face_url TEXT
);
'''

long_string = ",".join(['?' for i in range(0,110)])

insert_query = f'''
INSERT INTO FIFA (
    player_id,
    player_url,fifa_version,fifa_update,fifa_update_date,short_name,long_name,player_positions,overall,potential,value_eur,wage_eur,age,dob,height_cm,weight_kg,league_id,league_name,
    league_level,club_team_id,club_name,club_position,club_jersey_number,club_loaned_from,club_joined_date,club_contract_valid_until_year,nationality_id,nationality_name,nation_team_id,nation_position,nation_jersey_number,preferred_foot,weak_foot,skill_moves,international_reputation,work_rate,body_type,real_face,release_clause_eur,player_tags,player_traits,pace,
    shooting,passing,dribbling,defending,physic,attacking_crossing,attacking_finishing,attacking_heading_accuracy,attacking_short_passing,attacking_volleys,skill_dribbling,skill_curve,skill_fk_accuracy,skill_long_passing,skill_ball_control,movement_acceleration,movement_sprint_speed,movement_agility,movement_reactions,movement_balance,power_shot_power,power_jumping,power_stamina,power_strength,power_long_shots,mentality_aggression,mentality_interceptions,mentality_positioning,mentality_vision,mentality_penalties,mentality_composure,defending_marking_awareness,defending_standing_tackle,defending_sliding_tackle,goalkeeping_diving,goalkeeping_handling,goalkeeping_kicking,goalkeeping_positioning,goalkeeping_reflexes,goalkeeping_speed,ls,st,rs,lw,lf,cf,rf,rw,lam,cam,ram,lm,lcm,cm,rcm,rm,lwb,ldm,
    cdm,rdm,rwb,lb,lcb,cb,
    rcb, rb, gk, player_face_url )
     values ({long_string})
'''
print(long_string)

if __name__ == '__main__':
    read_csv()
    # create_db()
    # test_write()
    # test_read()



