INSERT INTO Users (Username, Email, Password) VALUES ('User 1', 'user1@mail.com', 'pass1');
INSERT INTO Users (Username, Email, Password) VALUES ('User 2', 'michelng', 'michelng');

INSERT INTO ProcedureType (ID, Name, Description) VALUES (1, 'Procedure Type 1', 'Procedure Description 1');

INSERT INTO Procedure (ID, ProcedureTypeID, UserID, DateOfService) VALUES (1, 1, 'User 1', '2026-02-01');
INSERT INTO Procedure (ID, ProcedureTypeID, UserID, DateOfService) VALUES (2, 1, 'User 1', '2026-04-01');

INSERT INTO InsuranceProvider (ID, Name) VALUES (1, 'Insurance 1');

INSERT INTO Policy (ID, InsuranceProviderID, Name, Deductible) VALUES (1, 1, 'Insurance 1 - Policy 1', '100');