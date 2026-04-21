import sqlite3

with sqlite3.connect('database.db') as db:
    # Enable FK constraint checking
    db.execute("PRAGMA foreign_keys = ON;")

    # User table
    db.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            Username TEXT PRIMARY KEY,
            Email TEXT NOT NULL,
            Password TEXT NOT NULL
        );
    """)

    # Procedure Type table
    db.execute("""
        CREATE TABLE IF NOT EXISTS ProcedureType (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Description TEXT NOT NULL
        );
    """)

    # Procedure table
    db.execute("""
        CREATE TABLE IF NOT EXISTS Procedure (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ProcedureTypeID INTEGER NOT NULL REFERENCES ProcedureType (ID) ON DELETE CASCADE,
            UserID TEXT NOT NULL REFERENCES Users(Username) ON DELETE CASCADE,
            DateOfService DATE NOT NULL
        )
    """)

    # Insurance Provider table
    db.execute("""
        CREATE TABLE IF NOT EXISTS InsuranceProvider (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL
        );
    """)

    # Policy table
    db.execute("""
        CREATE TABLE IF NOT EXISTS Policy (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            InsuranceProviderID INTEGER NOT NULL REFERENCES InsuranceProvider(ID) ON DELETE CASCADE,
            Name TEXT NOT NULL,
            Deductible TEXT NOT NULL
        );
    """)

    # Policy Coverage table
    db.execute("""
        CREATE TABLE IF NOT EXISTS PolicyCoverage (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            PolicyID INTEGER NOT NULL REFERENCES Policy(ID) ON DELETE CASCADE,
            ProcedureTypeID INTEGER NOT NULL REFERENCES ProcedureType(ID) ON DELETE CASCADE,
            Description TEXT NOT NULL,
            LinkToOriginal TEXT NOT NULL,
            StartDate DATE NOT NULL,
            EndDate DATE NOT NULL,
            DocumentURL TEXT,
            AddedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)



