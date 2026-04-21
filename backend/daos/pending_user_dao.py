from schema.pending_user import PendingUserSchema


class PendingUserDAO:

    def __init__(self, db_session):
        self.db_session = db_session

    def get_all_pending_users(self):
        return self.db_session.query(PendingUserSchema).all()

    def get_pending_user_by_id(self, pending_id):
        return (
            self.db_session.query(PendingUserSchema)
            .filter(PendingUserSchema.Id == pending_id)
            .first()
        )

    def get_pending_user_by_email(self, email):
        return (
            self.db_session.query(PendingUserSchema)
            .filter(PendingUserSchema.Email == email)
            .first()
        )

    def create_pending_user(self, pending_user):
        self.db_session.add(pending_user)
        self.db_session.commit()
        self.db_session.refresh(pending_user)
        return pending_user

    def update_pending_user(self, pending_user):
        self.db_session.merge(pending_user)
        self.db_session.commit()
        return pending_user

    def delete_pending_user(self, pending_id):
        pending_user = self.get_pending_user_by_id(pending_id)
        if not pending_user:
            return False
        self.db_session.delete(pending_user)
        self.db_session.commit()
        return True
