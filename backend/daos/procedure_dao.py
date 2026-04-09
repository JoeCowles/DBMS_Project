from schema.procedure import ProcedureSchema


class ProcedureDAO:

    def __init__(self, db_session):
        self.db_session = db_session

    def get_all_procedures(self):
        return self.db_session.query(ProcedureSchema).all()

    def get_procedure_by_id(self, procedure_id):
        return self.db_session.query(ProcedureSchema).filter(ProcedureSchema.ID == procedure_id).first()

    def create_procedure(self, procedure):
        self.db_session.add(procedure)
        self.db_session.commit()
        return procedure

    def update_procedure(self, procedure):
        self.db_session.merge(procedure)
        self.db_session.commit()
        return procedure

    def delete_procedure(self, procedure_id):
        procedure = self.get_procedure_by_id(procedure_id)
        if procedure:
            self.db_session.delete(procedure)
            self.db_session.commit()
            return True
        return False
