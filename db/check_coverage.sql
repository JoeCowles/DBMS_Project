-- Check coverage for a specific Policy, Procedure Type, and Date
-- Replace the values as needed:
-- PolicyID = 1
-- ProcedureTypeID = 1
-- Date = '2026-02-01'

SELECT Description, LinkToOriginal, StartDate, EndDate
FROM PolicyCoverage
WHERE PolicyID = 1
  AND ProcedureTypeID = 1
  AND '2026-02-01' BETWEEN StartDate AND EndDate

UNION ALL

SELECT 'No coverage found', NULL, NULL, NULL
WHERE NOT EXISTS (
    SELECT 1
    FROM PolicyCoverage
    WHERE PolicyID = 1
      AND ProcedureTypeID = 1
      AND '2026-02-01' BETWEEN StartDate AND EndDate
);

SELECT Description, LinkToOriginal, StartDate, EndDate
FROM PolicyCoverage
WHERE PolicyID = 1
  AND ProcedureTypeID = 1
  AND '2026-04-01' BETWEEN StartDate AND EndDate

UNION ALL

SELECT 'No coverage found', NULL, NULL, NULL
WHERE NOT EXISTS (
    SELECT 1
    FROM PolicyCoverage
    WHERE PolicyID = 1
      AND ProcedureTypeID = 1
      AND '2026-04-01' BETWEEN StartDate AND EndDate
);
