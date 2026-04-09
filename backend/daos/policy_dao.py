from schema.policy import PolicySchema


class PolicyDAO:

    def __init__(self, db_session):
        self.db_session = db_session

    def get_all_policies(self):
        return self.db_session.query(PolicySchema).all()

    def get_policy_by_id(self, policy_id):
        return self.db_session.query(PolicySchema).filter(PolicySchema.ID == policy_id).first()

    def create_policy(self, policy):
        self.db_session.add(policy)
        self.db_session.commit()
        return policy

    def update_policy(self, policy):
        self.db_session.merge(policy)
        self.db_session.commit()
        return policy

    def delete_policy(self, policy_id):
        policy = self.get_policy_by_id(policy_id)
        if policy:
            self.db_session.delete(policy)
            self.db_session.commit()
            return True
        return False
