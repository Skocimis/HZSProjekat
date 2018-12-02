class Team:

    def __init__(self, id, name, description, photo_url, team_uuid):
        self.id = id
        self.name = name
        self.description = description
        self.photo_url = photo_url
        self.team_uuid = team_uuid
        self.team_members = []

    def add_member(self, member):
        self.team_members.append(member)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'photo_url': self.photo_url,
            'team_uuid': self.team_uuid,
            'team_members': [member.to_dict() for member in self.team_members]
        }
