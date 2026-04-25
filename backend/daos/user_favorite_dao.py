from sqlalchemy import text
from schema.user_favorite import UserFavoriteSchema

class UserFavoriteDAO:
    def __init__(self, db_session):
        self.db_session = db_session

    def list_for_user(self, user_id):
        sql = """
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
                COUNT(pcode.ID)   AS code_count,
                uf.AddedAt        AS favorited_at
            FROM UserFavorite uf
            JOIN PolicyCoverage     pc    ON uf.PolicyCoverageID   = pc.ID
            JOIN ProcedureType      pt    ON pc.ProcedureTypeID    = pt.ID
            JOIN Policy             p     ON pc.PolicyID           = p.ID
            JOIN InsuranceProvider  ip    ON p.InsuranceProviderID = ip.ID
            LEFT JOIN PolicyCode    pcode ON pc.ID                 = pcode.PolicyCoverageID
            WHERE uf.UserID = :user_id
            GROUP BY pc.ID, uf.AddedAt
            ORDER BY uf.AddedAt DESC
        """
        return self.db_session.execute(text(sql), {"user_id": user_id}).mappings().all()

    def ids_for_user(self, user_id):
        rows = self.db_session.query(UserFavoriteSchema.PolicyCoverageID).filter(
            UserFavoriteSchema.UserID == user_id
        ).all()
        return [r[0] for r in rows]

    def exists(self, user_id, policy_coverage_id):
        return self.db_session.query(UserFavoriteSchema).filter(
            UserFavoriteSchema.UserID == user_id,
            UserFavoriteSchema.PolicyCoverageID == policy_coverage_id,
        ).first() is not None

    def add(self, user_id, policy_coverage_id):
        if self.exists(user_id, policy_coverage_id):
            return None
        fav = UserFavoriteSchema(UserID=user_id, PolicyCoverageID=policy_coverage_id)
        self.db_session.add(fav)
        self.db_session.commit()
        return fav

    def remove(self, user_id, policy_coverage_id):
        fav = self.db_session.query(UserFavoriteSchema).filter(
            UserFavoriteSchema.UserID == user_id,
            UserFavoriteSchema.PolicyCoverageID == policy_coverage_id,
        ).first()
        if not fav:
            return False
        self.db_session.delete(fav)
        self.db_session.commit()
        return True
