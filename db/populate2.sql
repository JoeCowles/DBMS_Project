-- Add Aetna as Insurance Provider
INSERT INTO InsuranceProvider (ID, Name) VALUES (2, 'Aetna');

-- Add Aetna to Policy
INSERT INTO Policy (ID, InsuranceProviderID, Name, Deductible) VALUES (2, 2, 'Aetna - Standard Plan', '500');

-- ProcedureType for each PDF (corresponding to docs/aetna/*.pdf)
INSERT INTO ProcedureType (ID, Name, Description) VALUES (2,  'ADAMTS13 Assay for Thrombotic Thrombocytopenic Purpura (TTP) - Medical Clinical Policy Bulletins | Aetna', 'ADAMTS13 Assay for Thrombotic Thrombocytopenic Purpura (TTP) - Medical Clinical Policy Bulletins | Aetna');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (3,  'ADAMTS13, Recombinant-krhn (Adzynma)', 'ADAMTS13, Recombinant-krhn (Adzynma)');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (4,  'Abatacept (Orencia)', 'Abatacept (Orencia)');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (5,  'Abdominal Aortic Aneurysm Screening', 'Abdominal Aortic Aneurysm Screening');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (6,  'Abdominoplasty, Suction Lipectomy, and Ventral Hernia Repair', 'Abdominoplasty, Suction Lipectomy, and Ventral Hernia Repair');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (7,  'Acute Ischemic Stroke Treatments', 'Acute Ischemic Stroke Treatments');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (8,  'Adalimumab', 'Adalimumab');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (9,  'Afamelanotide (Scenesse)', 'Afamelanotide (Scenesse)');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (10, 'Automated Ambulatory Blood Pressure Monitoring', 'Automated Ambulatory Blood Pressure Monitoring');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (11, 'Automated Audiometry', 'Automated Audiometry');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (12, 'Back Pain - Invasive Procedures', 'Back Pain - Invasive Procedures');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (13, 'Back Pain - Non Invasive Treatments', 'Back Pain - Non Invasive Treatments');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (14, 'Brain Natriuretic Peptide Testing', 'Brain Natriuretic Peptide Testing');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (15, 'Cancer Vaccines', 'Cancer Vaccines');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (16, 'Chronic Vertigo', 'Chronic Vertigo');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (17, 'Dialysis', 'Dialysis');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (18, 'Dysphagia Therapy', 'Dysphagia Therapy');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (19, 'Gout', 'Gout');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (20, 'HIV Testing', 'HIV Testing');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (21, 'Hearing Aids', 'Hearing Aids');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (22, 'Influenza Rapid Diagnostic Tests', 'Influenza Rapid Diagnostic Tests');
INSERT INTO ProcedureType (ID, Name, Description) VALUES (23, 'Influenza Vaccines', 'Influenza Vaccines');

-- PolicyCoverage (corresponding to docs/aetna/*.pdf)
INSERT INTO PolicyCoverage (ID, PolicyID, ProcedureTypeID, Description, LinkToOriginal, StartDate, EndDate, DocumentURL, AddedDate) VALUES
(1,  2,  2,  'ADAMTS13 Assay for Thrombotic Thrombocytopenic Purpura (TTP) - Medical Clinical Policy Bulletins | Aetna', 'https://www.aetna.com/cpb/medical/data/1000_1099/1050.html', '2025-01-15', '2025-11-30', 'docs/aetna/ADAMTS13 Assay for Thrombotic Thrombocytopenic Purpura (TTP) - Medical Clinical Policy Bulletins _ Aetna.pdf', CURRENT_TIMESTAMP),
(2,  2,  3,  'ADAMTS13, Recombinant-krhn (Adzynma)','https://www.aetna.com/cpb/medical/data/700_799/0780.html',  '2025-03-01', '2026-02-28', 'docs/aetna/ADAMTS13, Recombinant-krhn (Adzynma).pdf',                                                                                CURRENT_TIMESTAMP),
(3,  2,  4,  'Abatacept (Orencia)','https://www.aetna.com/cpb/medical/data/700_799/0720.html',  '2025-06-01', '2026-05-31', 'docs/aetna/Abatacept (Orencia).pdf',                                                                                                         CURRENT_TIMESTAMP),
(4,  2,  5,  'Abdominal Aortic Aneurysm Screening','https://www.aetna.com/cpb/medical/data/700_799/0702.html',  '2025-02-14', '2025-12-31', 'docs/aetna/Abdominal Aortic Aneurysm Screening.pdf',                                                                                         CURRENT_TIMESTAMP),
(5,  2,  6,  'Abdominoplasty, Suction Lipectomy, and Ventral Hernia Repair','https://www.aetna.com/cpb/medical/data/200_299/0211.html',  '2025-07-10', '2026-07-09', 'docs/aetna/Abdominoplasty, Suction Lipectomy, and Ventral Hernia Repair.pdf',                                                               CURRENT_TIMESTAMP),
(6,  2,  7,  'Acute Ischemic Stroke Treatments','https://www.aetna.com/cpb/medical/data/700_799/0789.html',  '2025-04-20', '2026-04-19', 'docs/aetna/Acute Ischemic Stroke Treatments.pdf',                                                                                            CURRENT_TIMESTAMP),
(7,  2,  8,  'Adalimumab','https://www.aetna.com/cpb/medical/data/600_699/0655.html',  '2025-09-01', '2026-08-31', 'docs/aetna/Adalimumab.pdf',                                                                                                                   CURRENT_TIMESTAMP),
(8,  2,  9,  'Afamelanotide (Scenesse)','https://www.aetna.com/cpb/medical/data/900_999/0962.html',  '2025-05-15', '2025-12-14', 'docs/aetna/Afamelanotide (Scenesse).pdf',                                                                                                     CURRENT_TIMESTAMP),
(9,  2, 10,  'Automated Ambulatory Blood Pressure Monitoring','https://www.aetna.com/cpb/medical/data/1_99/0025.html',     '2025-01-01', '2025-06-30', 'docs/aetna/Automated Ambulatory Blood Pressure Monitoring.pdf',                                                                               CURRENT_TIMESTAMP),
(10, 2, 11,  'Automated Audiometry','https://www.aetna.com/cpb/medical/data/800_899/0870.html',  '2025-08-05', '2026-07-31', 'docs/aetna/Automated Audiometry.pdf',                                                                                                         CURRENT_TIMESTAMP),
(11, 2, 12,  'Back Pain - Invasive Procedures','https://www.aetna.com/cpb/medical/data/1_99/0016.html',     '2025-03-20', '2026-03-19', 'docs/aetna/Back Pain - Invasive Procedures.pdf',                                                                                              CURRENT_TIMESTAMP),
(12, 2, 13,  'Back Pain - Non Invasive Treatments','https://www.aetna.com/cpb/medical/data/200_299/0232.html',  '2025-10-01', '2026-09-30', 'docs/aetna/Back Pain - Non Invasive Treatments.pdf',                                                                                          CURRENT_TIMESTAMP),
(13, 2, 14,  'Brain Natriuretic Peptide Testing','https://www.aetna.com/cpb/medical/data/600_699/0618.html',  '2025-02-01', '2026-01-31', 'docs/aetna/Brain Natriuretic Peptide Testing.pdf',                                                                                            CURRENT_TIMESTAMP),
(14, 2, 15,  'Cancer Vaccines','https://www.aetna.com/cpb/medical/data/500_599/0557.html',  '2025-11-01', '2026-10-31', 'docs/aetna/Cancer Vaccines.pdf',                                                                                                               CURRENT_TIMESTAMP),
(15, 2, 16,  'Chronic Vertigo','https://www.aetna.com/cpb/medical/data/200_299/0238.html',  '2025-04-01', '2025-09-30', 'docs/aetna/Chronic Vertigo.pdf',                                                                                                               CURRENT_TIMESTAMP),
(16, 2, 17,  'Dialysis','https://www.aetna.com/cpb/medical/data/500_599/0541.html',  '2025-01-01', '2026-12-31', 'docs/aetna/Dialysis.pdf',                                                                                                                      CURRENT_TIMESTAMP),
(17, 2, 18,  'Dysphagia Therapy','https://www.aetna.com/cpb/medical/data/600_699/0625.html',  '2025-06-15', '2026-06-14', 'docs/aetna/Dysphagia Therapy.pdf',                                                                                                            CURRENT_TIMESTAMP),
(18, 2, 19,  'Gout','https://www.aetna.com/cpb/medical/data/800_899/0810.html',  '2025-07-20', '2026-07-19', 'docs/aetna/Gout.pdf',                                                                                                                          CURRENT_TIMESTAMP),
(19, 2, 20,  'HIV Testing','https://www.aetna.com/cpb/medical/data/500_599/0542.html',  '2025-12-01', '2026-11-30', 'docs/aetna/HIV Testing.pdf',                                                                                                                   CURRENT_TIMESTAMP),
(20, 2, 21,  'Hearing Aids','https://www.aetna.com/cpb/medical/data/600_699/0612.html',  '2025-05-01', '2026-04-30', 'docs/aetna/Hearing Aids.pdf',                                                                                                                  CURRENT_TIMESTAMP),
(21, 2, 22,  'Influenza Rapid Diagnostic Tests','https://www.aetna.com/cpb/medical/data/400_499/0476.html',  '2025-08-15', '2026-08-14', 'docs/aetna/Influenza Rapid Diagnostic Tests.pdf',                                                                                             CURRENT_TIMESTAMP),
(22, 2, 23,  'Influenza Vaccines','https://www.aetna.com/cpb/medical/data/1_99/0035.html',     '2025-09-01', '2026-08-31', 'docs/aetna/Influenza Vaccines.pdf',                                                                                                            CURRENT_TIMESTAMP);

-- PolicyCode for Influenza Vaccines
INSERT INTO PolicyCode (ID, PolicyCoverageID, Code, Description, CodeType, CoverageStatus) VALUES
(1,  22, '90612', 'Influenza virus vaccine, trivalent, and SARS-CoV-2 (COVID-19) vaccine, mRNA-LNP, 31.7 mcg/0.32 mL dosage, for intramuscular use', 'CPT', 'covered'),
(2,  22, '90613', 'Influenza virus vaccine, quadrivalent, and SARS-CoV-2 (COVID-19) vaccine, mRNA-LNP, 40 mcg/0.4 mL dosage, for intramuscular use', 'CPT', 'covered'),
(3,  22, '90630', 'Influenza virus vaccine, quadrivalent (IIV4), split virus, preservative free, for intradermal use', 'CPT', 'covered'),
(4,  22, '90637', 'Influenza virus vaccine, quadrivalent (qIRV), mRNA; 30 mcg/0.5 mL dosage, for intramuscular use', 'CPT', 'covered'),
(5,  22, '90638', 'Influenza virus vaccine, quadrivalent (qIRV), mRNA; 60 mcg/0.5 mL dosage, for intramuscular use', 'CPT', 'covered'),
(6,  22, '90653', 'Influenza vaccine, inactivated (IIV), subunit, adjuvanted, for intramuscular use', 'CPT', 'covered'),
(7,  22, '90654', 'Influenza virus vaccine, trivalent (IIV3), split virus, preservative-free, for intradermal use', 'CPT', 'covered'),
(8,  22, '90655', 'Influenza virus vaccine, trivalent (IIV3), split virus, preservative free, 0.25 mL dosage, for intramuscular use', 'CPT', 'covered'),
(9,  22, '90656', 'Influenza virus vaccine, trivalent (IIV3), split virus, preservative free, 0.5 mL dosage, for intramuscular use', 'CPT', 'covered'),
(10, 22, '90657', 'Influenza virus vaccine, trivalent (IIV3), split virus, 0.25 mL dosage, for intramuscular use', 'CPT', 'covered'),
(11, 22, '90658', 'Influenza virus vaccine, trivalent (IIV3), split virus, 0.5 mL dosage, for intramuscular use', 'CPT', 'covered'),
(12, 22, '90660', 'Influenza virus vaccine, trivalent, live (LAIV3), for intranasal use', 'CPT', 'covered'),
(13, 22, '90661', 'Influenza virus vaccine (ccIIV3), derived from cell cultures, subunit, preservative and antibiotic free, 0.5 mL dosage, for intramuscular use', 'CPT', 'covered'),
(14, 22, '90662', 'Influenza virus vaccine (IIV), split virus, preservative free, enhanced immunogenicity via increased antigen content, for intramuscular use', 'CPT', 'covered'),
(15, 22, '90672', 'Influenza virus vaccine, quadrivalent, live (LAIV4), for intranasal use', 'CPT', 'covered'),
(16, 22, '90673', 'Influenza virus vaccine, trivalent (RIV3), derived from recombinant DNA, hemagglutinin (HA) protein only, preservative and antibiotic free, for intramuscular use', 'CPT', 'covered'),
(17, 22, '90674', 'Influenza virus vaccine, quadrivalent (ccIIV4), derived from cell cultures, subunit, preservative and antibiotic free, 0.5 mL dosage, for intramuscular use', 'CPT', 'covered'),
(18, 22, '90682', 'Influenza virus vaccine, quadrivalent (RIV4), derived from recombinant DNA, hemagglutinin (HA) protein only, preservative and antibiotic free, for intramuscular use', 'CPT', 'covered'),
(19, 22, '90685', 'Influenza virus vaccine, quadrivalent (IIV4), split virus, preservative free, 0.25 mL dosage, for intramuscular use', 'CPT', 'covered'),
(20, 22, '90686', 'Influenza virus vaccine, quadrivalent (IIV4), split virus, preservative free, 0.5 mL dosage, for intramuscular use', 'CPT', 'covered'),
(21, 22, '90687', 'Influenza virus vaccine, quadrivalent (IIV4), split virus, 0.25 mL dosage, for intramuscular use', 'CPT', 'covered'),
(22, 22, '90688', 'Influenza virus vaccine, quadrivalent (IIV4), split virus, 0.5 mL dosage, for intramuscular use', 'CPT', 'covered'),
(23, 22, '90694', 'Influenza virus vaccine, quadrivalent (aIIV4), inactivated, adjuvanted, preservative free, 0.5 mL dosage, for intramuscular use [over age 65]', 'CPT', 'covered'),
(24, 22, '90695', 'Influenza virus vaccine, H5N8, derived from cell cultures, adjuvanted, for intramuscular use', 'CPT', 'covered'),
(25, 22, '90756', 'Influenza virus vaccine, quadrivalent (ccIIV4), derived from cell cultures, subunit, antibiotic free, 0.5mL dosage, for intramuscular use', 'CPT', 'covered'),
(26, 22, '90664', 'Influenza virus vaccine, live (LAIV), pandemic formulation, for intranasal use', 'CPT', 'not_covered'),
(27, 22, '87275', 'Infectious agent antigen detection by immunofluorescent technique; influenza B virus', 'CPT', 'related'),
(28, 22, '87276', 'Infectious agent antigen detection by immunofluorescent technique; influenza A virus', 'CPT', 'related'),
(29, 22, '87400', 'Infectious agent antigen detection by enzyme immunoassay technique; influenza A or B, each', 'CPT', 'related'),
(30, 22, '90460', 'Immunization administration through 18 years of age via any route of administration, with counseling; first or only component of each vaccine or toxoid administered', 'CPT', 'related'),
(31, 22, '90461', 'Immunization administration through 18 years of age; each additional vaccine or toxoid component administered', 'CPT', 'related'),
(32, 22, '90471', 'Immunization administration (includes percutaneous, intradermal, subcutaneous, intramuscular injections); one vaccine', 'CPT', 'related'),
(33, 22, '90472', 'Immunization administration; each additional vaccine (single or combination vaccine/toxoid)', 'CPT', 'related'),
(34, 22, '90473', 'Immunization administration by intranasal or oral route; one vaccine', 'CPT', 'related'),
(35, 22, '90474', 'Immunization administration by intranasal or oral route; each additional vaccine', 'CPT', 'related'),
(36, 22, '90482', 'Immunization counseling by physician when immunization is not administered on same date; 3 to 10 minutes', 'CPT', 'related'),
(37, 22, '90483', 'Immunization counseling by physician when immunization is not administered on same date; greater than 10 minutes up to 20 minutes', 'CPT', 'related'),
(38, 22, '90484', 'Immunization counseling by physician when immunization is not administered on same date; greater than 20 minutes', 'CPT', 'related'),
(39, 22, '90666', 'Influenza virus vaccine (IIV), pandemic formulation, split virus, preservative free, for intramuscular use', 'CPT', 'related'),
(40, 22, '90667', 'Influenza virus vaccine (IIV), pandemic formulation, split virus, adjuvanted, for intramuscular use', 'CPT', 'related'),
(41, 22, '90668', 'Influenza virus vaccine (IIV), pandemic formulation, split virus, for intramuscular use', 'CPT', 'related'),
(42, 22, 'G0008', 'Administration of influenza virus vaccine', 'HCPCS', 'covered'),
(43, 22, 'J3530', 'Nasal vaccine inhalation', 'HCPCS', 'covered'),
(44, 22, 'Q2034', 'Influenza virus vaccine, split virus, for intramuscular use (Agriflu)', 'HCPCS', 'covered'),
(45, 22, 'Q2035', 'Influenza virus vaccine, split virus, for intramuscular use (Afluria)', 'HCPCS', 'covered'),
(46, 22, 'Q2036', 'Influenza virus vaccine, split virus, for intramuscular use (Flulaval)', 'HCPCS', 'covered'),
(47, 22, 'Q2037', 'Influenza virus vaccine, split virus, for intramuscular use (Fluvirin)', 'HCPCS', 'covered'),
(48, 22, 'Q2038', 'Influenza virus vaccine, split virus, for intramuscular use (Fluzone)', 'HCPCS', 'covered'),
(49, 22, 'Q2039', 'Influenza virus vaccine, split virus, not otherwise specified', 'HCPCS', 'covered'),
(50, 22, 'G0310', 'Immunization counseling by physician when vaccine not administered on same date; 5 to 15 minutes (Medicaid)', 'HCPCS', 'related'),
(51, 22, 'G0311', 'Immunization counseling by physician when vaccine not administered on same date; 16 to 30 minutes (Medicaid)', 'HCPCS', 'related'),
(52, 22, 'G0312', 'Immunization counseling by physician when vaccine not administered on same date, under age 21; 5 to 15 minutes (Medicaid)', 'HCPCS', 'related'),
(53, 22, 'G0313', 'Immunization counseling by physician when vaccine not administered on same date, under age 21; 16 to 30 minutes (Medicaid)', 'HCPCS', 'related'),
(54, 22, 'Z23','Encounter for immunization','ICD-10', 'covered'),
(55, 22, 'D80.0-D89.839', 'Disorders involving the immune mechanism','ICD-10', 'not_covered'),
(56, 22, 'J45.20-J45.998','Asthma','ICD-10', 'not_covered'),
(57, 22, 'O00.101-O9A.519','Pregnancy, childbirth and the puerperium','ICD-10', 'not_covered');
