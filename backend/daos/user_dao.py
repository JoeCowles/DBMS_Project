from schema.user import UserSchema


class UserDAO:

    def __init__(self, db_session):
        self.db_session = db_session

    def get_all_users(self):
        return self.db_session.query(UserSchema).all()

    def get_user_by_username(self, username):
        return self.db_session.query(UserSchema).filter(UserSchema.Username == username).first()

    def create_user(self, user):
        self.db_session.add(user)
        self.db_session.commit()
        return user

    def update_user(self, user):
        self.db_session.merge(user)
        self.db_session.commit()
        return user

    def authenticate_user(self, identifier, password):
        # identifier can be username or email
        user = self.db_session.query(UserSchema).filter(
            (UserSchema.Username == identifier) | (UserSchema.Email == identifier)
        ).first()
        if user and user.Password == password:
            return user
        return None
