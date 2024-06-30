USE Shelter
GO

INSERT INTO dbo.CatType (CatTypeId, CatTypeValue)
VALUES 
(1, 'Siamese'),
(2, 'British Shorthair'),
(3, 'Main Coon'),
(4, 'Persain'),
(5, 'Ragdoll'),
(6 ,'Sphynx'),
(7, 'Abyssinian'),
(8, 'American Shorthair'),
(9, 'Burmese'),
(10, 'Bombay')

INSERT INTO dbo.Gender (GenderId, GenderValue)
VALUES
(1, 'Female'),
(2, 'Male')

INSERT INTO dbo.CatShelterReasonType (CatShelterReasonTypeId, CatShelterReasonTypeValue)
VALUES
(1, 'Stray'),
(2, 'Rescued'),
(3, 'Born in Captivity'),
(4, 'Ownwer Surrender'),
(5, 'Other')
