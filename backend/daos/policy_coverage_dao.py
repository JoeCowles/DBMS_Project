from sqlalchemy import text
from schema.policy_coverage import PolicyCoverageSchema


class PolicyCoverageDAO:

    def __init__(self, db_session):
        self.db_session = db_session

    def search(self, name=None, cpt_code=None, provider=None):
        base = """
            SELECT
                pc.ID             AS id,
                pc.Description    AS description,
                pt.Name           AS procedure_name,
                p.Name            AS policy_name,
                ip.Name           AS provider_name,
                pc.StartDate      AS start_date,
                pc.EndDate        AS end_date,
                pc.DocumentURL    AS document_url,
                pc.LinkToOriginal AS link_to_original,
                COUNT(pcode.ID)   AS code_count
            FROM PolicyCoverage pc
            JOIN ProcedureType     pt    ON pc.ProcedureTypeID    = pt.ID
            JOIN Policy             p    ON pc.PolicyID           = p.ID
            JOIN InsuranceProvider  ip   ON p.InsuranceProviderID = ip.ID
            LEFT JOIN PolicyCode    pcode ON pc.ID                = pcode.PolicyCoverageID
        """
        conditions, params = [], {}

        if cpt_code:
            conditions.append("pcode.Code LIKE :cpt_code")
            params["cpt_code"] = f"%{cpt_code}%"

        if name:
            conditions.append("pt.Name LIKE :name")
            params["name"] = f"%{name}%"

        if provider:
            conditions.append("ip.Name LIKE :provider")
            params["provider"] = f"%{provider}%"

        if conditions:
            base += " WHERE " + " AND ".join(conditions)
        base += " GROUP BY pc.ID"

        return self.db_session.execute(text(base), params).mappings().all()

    def get_coverage_details(self, coverage_id):
        meta = self.db_session.execute(text("""
            SELECT
                pc.ID             AS id,
                pc.Description    AS description,
                pt.Name           AS procedure_name,
                p.Name            AS policy_name,
                ip.Name           AS provider_name,
                pc.StartDate      AS start_date,
                pc.EndDate        AS end_date,
                pc.DocumentURL    AS document_url,
                pc.LinkToOriginal AS link_to_original
            FROM PolicyCoverage pc
            JOIN ProcedureType     pt  ON pc.ProcedureTypeID    = pt.ID
            JOIN Policy             p  ON pc.PolicyID           = p.ID
            JOIN InsuranceProvider  ip ON p.InsuranceProviderID = ip.ID
            WHERE pc.ID = :id
        """), {"id": coverage_id}).mappings().first()

        if not meta:
            return None

        codes = self.db_session.execute(text("""
            SELECT
                Code            AS code,
                Description     AS description,
                CodeType        AS code_type,
                CoverageStatus  AS coverage_status
            FROM PolicyCode
            WHERE PolicyCoverageID = :id
            ORDER BY CodeType, CoverageStatus
        """), {"id": coverage_id}).mappings().all()

        return {**dict(meta), "codes": [dict(c) for c in codes]}

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
