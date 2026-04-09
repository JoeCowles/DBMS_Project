from schema.procedure_type import ProcedureTypeSchema


class ProcedureTypeDAO:

    def __init__(self, db_session):
        self.db_session = db_session

    def get_all_procedure_types(self):
        return self.db_session.query(ProcedureTypeSchema).all()

    def get_procedure_type_by_id(self, procedure_type_id):
        return self.db_session.query(ProcedureTypeSchema).filter(ProcedureTypeSchema.ID == procedure_type_id).first()

    def create_procedure_type(self, procedure_type):
        self.db_session.add(procedure_type)
        self.db_session.commit()
        return procedure_type

    def update_procedure_type(self, procedure_type):
        self.db_session.merge(procedure_type)
        self.db_session.commit()
        return procedure_type

    def delete_procedure_type(self, procedure_type_id):
        procedure_type = self.get_procedure_type_by_id(procedure_type_id)
        if procedure_type:
            self.db_session.delete(procedure_type)
            self.db_session.commit()
            return True
        return False
