from flask import Blueprint, request, jsonify

from controller.main_controller import get_all_teams, create_team, get_team, update_team, delete_team, _connect, team_id_of_member, napravi_clana, obrisi_clana, team_uuid_of_member

DB_PATH = 'D:/Aki/Hakaton/Projekti/backend-master/db/hzs.db'
teams = Blueprint('teams', __name__, url_prefix='/teams')



@teams.route('/hello', methods=['GET'])
def hello_world1():
    return 'Hello, World!'

@teams.route('/', methods=['GET', 'POST'])
def teams_view():
    if request.method == 'GET':  # get all teams
        all_teams = get_all_teams()

        response_body = [t.to_dict() for t in all_teams]
        return jsonify(response_body), 200

    if request.method == 'POST':  # create a new team
        # mention validation issues
        body = request.json
        created = create_team(body)
        if created is 1:
            return "Tim mora da ima 3 ili 4 clana!", 406

        return jsonify(created), 201


@teams.route('/<string:team_uuid>', methods=['GET', 'PUT', 'DELETE'])
def single_team_view(team_uuid):
    if request.method == 'GET':  # get the team
        team = get_team(team_uuid)
        if team is None:
            return jsonify({'error': 'team with unique id {} not found'.format(team_uuid)}), 404

        response_body = team.to_dict()
        return jsonify(response_body), 200

    if request.method == 'PUT':  # update the team
        body = request.json
        updated = update_team(body)
        if updated is None:
            return jsonify({'error': 'team with unique id {} not found'.format(team_uuid)}), 404
        if updated is 1:
            return "Tim mora da ima 3 ili 4 clana!", 406
        return jsonify(updated), 200

    if request.method == 'DELETE':  # remove the team
        success = delete_team(team_uuid)

        if not success:
            return jsonify({'error': 'team with unique id {} not found'.format(team_uuid)}), 404

        return jsonify({}), 204

@teams.route('/<string:team_uuid>/', methods=['POST'])#novi clan u timu
def func(team_uuid):
    return napravi_clana(team_uuid, request.json, 0)

'''
@teams.route('/dovuci/<string:member_id>/<string:team_uuid>', methods = ['PUT'])#Dovlacenje clana sa idjem member_id u tim sa uuidjem uuid
def dovuci(member_id, team_uuid):
    a = 0
    team = get_team(team_uuid)
    if(team is None):
        return "Tim sa UUIDjem ne postoji"
    for m in team.team_members:
        a = a+1
    if a is 4:
        return "Tim u koji clan treba da se dovuce je pun!"
    g = team_uuid_of_member(member_id)
    if g is None:
        return "Uneli ste los ID clana!"
    team = get_team(team_uuid_of_member(member_id))
    a = 0
    for m2 in team.team_members:
        a = a+1
    if a is 3:
        return "Tim iz kog je clan vec ima minimalni moguci broj clanova"
        
    team = get_team(team_uuid)
    upit1 = "UPDATE team_member SET team_id=? WHERE id=? "
    conn = _connect()
    c = conn.cursor()
    c.execute(upit1, (team.id, member_id, ))
    conn.commit()
    c.close()
    conn.close()
    return "Uspesno!"
'''
@teams.route('/<string:team_uuid>/<string:member_id>', methods=['DELETE', 'PUT'])#Brisanje clana tima, mora da se zna i uuid tima
def funkk2(team_uuid, member_id):
    if request.method == 'DELETE':
        return obrisi_clana(team_uuid, member_id, 0)
        
    if request.method=='PUT': # izmena clana
        obr = obrisi_clana(team_uuid, member_id, 1)
        if obr is "Ne mozemo da nadjemo clana sa IDjem ID!":
            return "Ne mozemo da nadjemo clana sa IDjem ID!"
        nap = napravi_clana(team_uuid, request.json, 1)
        return "Uspesno!"



        
