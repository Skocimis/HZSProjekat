import sqlite3
import uuid

from flask import jsonify
from model.team import Team
from model.team_member import TeamMember

DB_PATH = 'D:/Aki/Hakaton/Projekti/backend-master/db/hzs.db'  # Relativna putanja ne radi.


def _connect():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    conn.commit()
    return conn


def get_all_teams():
    conn = _connect()  # todo use connection as context manager
    c = conn.cursor()
    query = """SELECT id, name, description, photo_url, team_uuid FROM team"""
    c.execute(query)
    result_set = c.fetchall()

    teams = []

    for t in result_set:
        created_team = Team(id=t[0], name=t[1], description=t[2], photo_url=t[3], team_uuid=t[4])

        member_query = """SELECT id, first_name, last_name, email, phone_number, school, city FROM 
        team_member WHERE team_id=?"""
        c.execute(member_query, (created_team.id,))
        members = c.fetchall()

        for m in members:
            created_member = TeamMember(id=m[0], first_name=m[1], last_name=m[2], email=m[3], phone_number=m[4],
                                        school=m[5], city=m[6], team=created_team)
            created_team.add_member(created_member)

        teams.append(created_team)

    conn.commit()
    c.close()
    conn.close()

    return teams

def team_uuid_of_member(member_id):
    conn = _connect()
    c = conn.cursor()
    query = "SELECT team_uuid FROM team_member WHERE id=?"
    c.execute(query, (member_id,))
    t = c.fetchone()
    if t is None:
        return None
    return t[0]

def team_id_of_member(member_id):
    conn = _connect()
    c = conn.cursor()
    query = "SELECT team_id FROM team_member WHERE id=?"
    c.execute(query, (member_id,))
    t = c.fetchone()
    if t is None:
        return None
    return t[0]

def get_team(team_uuid):
    conn = _connect()  # todo use connection as context manager
    c = conn.cursor()
    query = """SELECT id, name, description, photo_url, team_uuid FROM team WHERE team_uuid=?"""
    c.execute(query, (team_uuid,))
    t = c.fetchone()

    if t is None:
        return None

    created_team = Team(id=t[0], name=t[1], description=t[2], photo_url=t[3], team_uuid=t[4])

    member_query = """SELECT id, first_name, last_name, email, phone_number, school, city FROM 
    team_member WHERE team_id=?"""
    c.execute(member_query, (created_team.id,))
    members = c.fetchall()

    for m in members:
        created_member = TeamMember(id=m[0], first_name=m[1], last_name=m[2], email=m[3], phone_number=m[4],
                                    school=m[5], city=m[6], team=created_team)
        created_team.add_member(created_member)

    conn.commit()
    c.close()
    conn.close()

    return created_team


def create_team(data):
    conn = _connect()  # todo use connection as context manager
    c = conn.cursor()

    team_query = """INSERT INTO team (name, description, photo_url, team_uuid) VALUES (?,?,?,?)"""
    team_uuid = uuid.uuid4()
    c.execute(team_query, (data['name'], data['description'], data['photo_url'], str(team_uuid)))
    team_id = c.lastrowid
    data['id'] = team_id
    data['team_uuid'] = team_uuid
    i = 0
    for m in data['team_members']:
        member_query = """INSERT INTO team_member (first_name, last_name, email, phone_number, school, city, team_id) 
        VALUES (?,?,?,?,?,?,?)"""
        c.execute(member_query,
                  (m['first_name'], m['last_name'], m['email'], m['phone_number'], m['school'], m['city'], team_id))
        m['id'] = c.lastrowid
        i = i + 1
    if i is not 3 and i is not 4:
        return 1
    conn.commit()
    c.close()
    conn.close()
    return data


def update_team(data):
    conn = _connect()  # todo use connection as context manager
    c = conn.cursor()

    delete_all_team_members(data['id'])

    team_query = """UPDATE team SET name=?, description=?, photo_url=? WHERE team_uuid=?"""

    c.execute(team_query, (data['name'], data['description'], data['photo_url'], data['team_uuid']))
    i = 0
    for m in data['team_members']:
        member_query = """INSERT INTO team_member (first_name, last_name, email, phone_number, school, city, team_id) 
        VALUES (?,?,?,?,?,?,?)"""
        c.execute(member_query,
                  (m['first_name'], m['last_name'], m['email'], m['phone_number'], m['school'], m['city'], data['id']))
        m['id'] = c.lastrowid
        i = i + 1

    if i is not 3 and i is not 4:
        return 1
    conn.commit()
    c.close()
    conn.close()
    return data


def delete_team(team_uuid):
    conn = _connect()

    with conn:
        team_query = """DELETE FROM team WHERE team_uuid=?"""
        status = conn.execute(team_query, (team_uuid,))
        success = False
        if status.rowcount == 1:
            success = True

    return success


def delete_all_team_members(team_id):
    conn = _connect()
    try:
        with conn:
            team_query = """DELETE FROM team_member WHERE team_id=?"""
            status = conn.execute(team_query, (team_id,))
            success = False
            if status.rowcount > 0:
                success = True

            return success
    except sqlite3.Error:
        return False

def napravi_clana(team_uuid, body, bol):
    a = 0
    team = get_team(team_uuid)
    for m in team.team_members:
        a = a+1
    if a is 4 and bol is 0:
        return "Tim vec ima 4 clana i ne moze da mu se doda novi!", 406
    conn = _connect()
    c = conn.cursor()

    member_query = """INSERT INTO team_member (first_name, last_name, email, phone_number, school, city, team_id) 
        VALUES (?,?,?,?,?,?,?)"""
    c.execute(member_query, (body['first_name'], body['last_name'], body['email'], body['phone_number'], body['school'], body['city'], team.id,))
    conn.commit()
    c.close()
    conn.close()
    return jsonify(get_team(team_uuid).team_members[a].to_dict())

def obrisi_clana(team_uuid, member_id, bol):
    conn = _connect()
    c = conn.cursor()
    t = team_id_of_member(member_id)
    if t is None:
        return "Ne mozemo da nadjemo clana sa IDjem ID!"
        c.close()
        conn.close()
    delete_query = "DELETE FROM team_member WHERE id=? AND (SELECT team_uuid FROM team WHERE id=?)=? "

    ii = 0
    for aa in get_team(team_uuid).team_members:
        ii = ii + 1
    if ii is 3 and bol is 0:
        return "Tim vec ima 3 clana i vise ne moze da se brise!"
        c.close()
        conn.close()
    c.execute(delete_query, (member_id,t,team_uuid,))
    conn.commit()
    c.close()
    conn.close()
    return "Uspesno brisanje clana!"
