class TeamMember:

    def __init__(self, id, first_name, last_name, email, phone_number, school, city, team):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.school = school
        self.city = city
        self.team = team

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'school': self.school,
            'city': self.city,
            'team_id': self.team.id
        }
