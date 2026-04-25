INSERT INTO Users (ID, Username, Email, Password) VALUES (1, 'user1', 'user1@mail.com', 'pass1');
INSERT INTO Users (ID, Username, Email, Password) VALUES (2, 'michelng', 'michelng', 'michelng');

INSERT INTO ProcedureType (ID, Name, Description) VALUES (1, 'Procedure Type 1', 'Procedure Description 1');

INSERT INTO Procedure (ID, ProcedureTypeID, UserID, DateOfService) VALUES (1, 1, 1, '2026-02-01');
INSERT INTO Procedure (ID, ProcedureTypeID, UserID, DateOfService) VALUES (2, 1, 2, '2026-04-01');

INSERT INTO InsuranceProvider (ID, Name) VALUES (1, 'Insurance 1');

INSERT INTO Policy (ID, InsuranceProviderID, Name, Deductible) VALUES (1, 1, 'Insurance 1 - Policy 1', '100');