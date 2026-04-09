from schema.policy_coverage import PolicyCoverageSchema


class PolicyCoverageDAO:

    def __init__(self, db_session):
        self.db_session = db_session

    def get_all_policy_coverages(self):
        return self.db_session.query(PolicyCoverageSchema).all()

    def get_policy_coverage_by_id(self, coverage_id):
        return self.db_session.query(PolicyCoverageSchema).filter(PolicyCoverageSchema.ID == coverage_id).first()

    def create_policy_coverage(self, coverage):
        self.db_session.add(coverage)
        self.db_session.commit()
        return coverage

    def update_policy_coverage(self, coverage):
        self.db_session.merge(coverage)
        self.db_session.commit()
        return coverage

    def delete_policy_coverage(self, coverage_id):
        coverage = self.get_policy_coverage_by_id(coverage_id)
        if coverage:
            self.db_session.delete(coverage)
            self.db_session.commit()
            return True
        return False
