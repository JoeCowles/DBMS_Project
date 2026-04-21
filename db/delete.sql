DELETE FROM PolicyCode;
DELETE FROM PolicyCoverage;
DELETE FROM Procedure;
DELETE FROM Policy;
DELETE FROM ProcedureType;
DELETE FROM InsuranceProvider;
DELETE FROM PendingUsers;
DELETE FROM Users;

DELETE FROM sqlite_sequence WHERE name = 'PolicyCode';
DELETE FROM sqlite_sequence WHERE name = 'PolicyCoverage';
DELETE FROM sqlite_sequence WHERE name = 'Procedure';
DELETE FROM sqlite_sequence WHERE name = 'Policy';
DELETE FROM sqlite_sequence WHERE name = 'ProcedureType';
DELETE FROM sqlite_sequence WHERE name = 'InsuranceProvider';
DELETE FROM sqlite_sequence WHERE name = 'PendingUsers';