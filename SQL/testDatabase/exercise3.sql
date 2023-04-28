-- ##### Restart ##### --
DROP TABLE fans CASCADE ;
DROP TABLE players CASCADE ;
DROP TABLE teams CASCADE ; 

-- ##### Create tables ##### --
CREATE TABLE teams (
  	name VARCHAR(40),
	captain varchar(40) UNIQUE,
  	color VARCHAR(40) UNIQUE,
	PRIMARY KEY (name)
);

CREATE TABLE players(
	name VARCHAR(40),
	playsFor VARCHAR(40),
	PRIMARY KEY (name)
);

CREATE TABLE fans(
	name VARCHAR(40),
	fTeam VARCHAR(40),
	fPlayer VARCHAR(40),
	fColor VARCHAR(40),
	PRIMARY KEY (name)
);

ALTER TABLE players
ADD FOREIGN KEY(playsFor)
REFERENCES teams(name);

ALTER TABLE teams
ADD FOREIGN KEY(captain)
REFERENCES players(name);

ALTER TABLE fans ADD FOREIGN KEY (fPlayer) REFERENCES players(name);
ALTER TABLE fans ADD FOREIGN KEY (fTeam) REFERENCES teams(name);
ALTER TABLE fans ADD FOREIGN KEY (fColor) REFERENCES teams(color);

-- ##### Insert Data ##### --
INSERT INTO teams(name, color) VALUES('DIKU', 'Red');
INSERT INTO teams(name, color) VALUES('FosMat', 'Blue');

INSERT INTO players VALUES('August', 'DIKU');
INSERT INTO players VALUES('Mr. Sky', 'DIKU');
INSERT INTO players VALUES('Toby Flenderson', 'FosMat');
INSERT INTO players VALUES('Jens', 'FosMat');

UPDATE teams SET captain = 'August' WHERE name = 'DIKU';
UPDATE teams SET captain = 'Toby Flenderson' WHERE name = 'FosMat';

INSERT INTO fans(name, fPlayer) VALUES('Jørgen', 'Mr. Sky');
INSERT INTO fans(name, fPlayer) VALUES('Tim', 'Jens');
UPDATE fans SET fTeam = (
SELECT playsFor FROM players
WHERE name = fPlayer );
UPDATE fans SET fColor = (
SELECT color FROM teams
WHERE name = fTeam );
