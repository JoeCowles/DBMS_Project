from schema.insurance_provider import InsuranceProviderSchema


class InsuranceProviderDAO:

    def __init__(self, db_session):
        self.db_session = db_session

    def get_all_insurance_providers(self):
        return self.db_session.query(InsuranceProviderSchema).all()

    def get_insurance_provider_by_id(self, provider_id):
        return self.db_session.query(InsuranceProviderSchema).filter(InsuranceProviderSchema.ID == provider_id).first()

    def create_insurance_provider(self, provider):
        self.db_session.add(provider)
        self.db_session.commit()
        return provider

    def update_insurance_provider(self, provider):
        self.db_session.merge(provider)
        self.db_session.commit()
        return provider

    def delete_insurance_provider(self, provider_id):
        provider = self.get_insurance_provider_by_id(provider_id)
        if provider:
            self.db_session.delete(provider)
            self.db_session.commit()
            return True
        return False
