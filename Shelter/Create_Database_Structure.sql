USE Shelter
GO

CREATE TABLE dbo.CatType
(
	CatTypeId INT NOT NULL PRIMARY KEY
	,CatTypeValue VARCHAR(256)
)

CREATE TABLE dbo.Cat 
(
	CatId INT NOT NULL PRIMARY KEY
	,CatTypeId INT NOT NULL FOREIGN KEY REFERENCES CatType(CatTypeId)
	,CatName VARCHAR(256)
)

CREATE TABLE dbo.Gender 
(
	GenderId INT NOT NULL PRIMARY KEY
	,GenderValue VARCHAR(32)
)

CREATE TABLE dbo.CatBiometric 
(
	CatBiometricId INT NOT NULL PRIMARY KEY
	,CatId INT NOT NULL FOREIGN KEY REFERENCES Cat(CatId)
	,GenderId INT NOT NULL FOREIGN KEY REFERENCES Gender(GenderId)
	,DateOfBirth DATETIME
)

CREATE TABLE dbo.CatShelterReasonType
(
	CatShelterReasonTypeId INT NOT NULL PRIMARY KEY
	,CatShelterReasonTypeValue VARCHAR(256)
)

CREATE TABLE dbo.CatShelterReason
(
	CatShelterReasonId INT NOT NULL PRIMARY KEY
	,CatId INT NOT NULL FOREIGN KEY REFERENCES Cat(CatId)
	,CatShelterReasonTypeId INT NOT NULL FOREIGN KEY REFERENCES CatShelterReasonType(CatShelterReasonTypeId)
)

CREATE TABLE dbo.CatAdoption 
(
	CatAdoptionId INT NOT NULL PRIMARY KEY
	,CatId INT NOT NULL FOREIGN KEY REFERENCES Cat(CatId)
	,CatAdoptionDate DATETIME
	,AmountPaid DECIMAL
)