from schema.user_preference import UserPreferenceSchema

class UserPreferenceDAO:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_for_user(self, user_id):
        return self.db_session.query(UserPreferenceSchema).filter(
            UserPreferenceSchema.UserID == user_id
        ).first()

    def set_for_user(self, user_id, preference):
        existing = self.get_for_user(user_id)
        if existing:
            existing.Preference = preference
            self.db_session.commit()
            return existing
        new_pref = UserPreferenceSchema(UserID=user_id, Preference=preference)
        self.db_session.add(new_pref)
        self.db_session.commit()
        return new_pref
