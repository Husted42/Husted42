-- Restart --
DROP TABLE teams CASCADE;
DROP TABLE players CASCADE;
DROP TABLE fans CASCADE;

-- ##### Create tables ##### --
CREATE TABLE teams (
	id serial NOT NULL,
  	name VARCHAR(40) UNIQUE,
	captain_id int,
  	color VARCHAR(40) UNIQUE,
	PRIMARY KEY (id)
);

CREATE TABLE players(
	id serial NOT NULL,
	name VARCHAR(40),
	playsFor int,
	PRIMARY KEY (id)
);

CREATE TABLE fans(
	id serial NOT NULL,
	name VARCHAR(40),
	fTeam int,
	fPlayer int,
	fColor int,
	PRIMARY KEY (id)
);

ALTER TABLE players
ADD FOREIGN KEY(playsFor)
REFERENCES teams(id);

ALTER TABLE teams
ADD FOREIGN KEY(captain_id)
REFERENCES players(id);

ALTER TABLE fans ADD FOREIGN KEY (fPlayer) REFERENCES players(id);
ALTER TABLE fans ADD FOREIGN KEY (fTeam) REFERENCES teams(id);
ALTER TABLE fans ADD FOREIGN KEY (fColor) REFERENCES teams(id);

INSERT INTO teams(name, color) VALUES('DIKU', 'Red');
INSERT INTO teams(name, color) VALUES('FosMat', 'Blue');

INSERT INTO players(name, playsFor) VALUES('August', 1);
INSERT INTO players(name, playsFor) VALUES('Mr. Sky', 1);
INSERT INTO players(name, playsFor) VALUES('Toby Flenderson', 2);
INSERT INTO players(name, playsFor) VALUES('Jens', 2);

UPDATE teams SET captain =  WHERE name = 'DIKU';
UPDATE teams SET captain = 'Toby Flenderson' WHERE name = 'FosMat';