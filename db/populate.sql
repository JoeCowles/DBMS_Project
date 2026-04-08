INSERT INTO Users (Username, Email, Password) VALUES ('User 1', 'user1@mail.com', 'pass1');

INSERT INTO ProcedureType (Name, Description) VALUES ('Procedure Type 1', 'Procedure Description 1');

INSERT INTO Procedure (ProcedureTypeID, UserID, DateOfService) VALUES (1, 'User 1', '2026-02-01');
INSERT INTO Procedure (ProcedureTypeID, UserID, DateOfService) VALUES (1, 'User 1', '2026-04-01');

INSERT INTO InsuranceProvider (Name) VALUES ('Insurance 1');

INSERT INTO Policy (InsuranceProviderID, Name, Deductible) VALUES (1, 'Insurance 1 - Policy 1', '100');

INSERT INTO PolicyCoverage (PolicyID, ProcedureTypeID, Description, LinkToOriginal, StartDate, EndDate) VALUES (1, 1, '80% coverage', 'https://www.test.com', '2026-01-01', '2026-03-01');
