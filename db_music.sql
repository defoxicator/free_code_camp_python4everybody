BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Artist" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Album" (
	"id"	INTEGER NOT NULL UNIQUE,
	"artist_id"	INTEGER,
	"title"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Genre" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Track" (
	"id"	INTEGER NOT NULL UNIQUE,
	"album_id"	INTEGER,
	"genre_id"	INTEGER,
	"len"	INTEGER,
	"rating"	INTEGER,
	"title"	TEXT,
	"count"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "Artist" VALUES (1,'Led Zepplin');
INSERT INTO "Artist" VALUES (2,'AC/DC');
INSERT INTO "Album" VALUES (1,2,'Who Made Who');
INSERT INTO "Album" VALUES (2,1,'IV');
INSERT INTO "Genre" VALUES (1,'Rock');
INSERT INTO "Genre" VALUES (2,'Metal');
INSERT INTO "Track" VALUES (1,2,1,297,5,'Black Dog',0);
INSERT INTO "Track" VALUES (2,2,1,482,5,'Stairway',0);
INSERT INTO "Track" VALUES (3,1,2,313,5,'About to Rock',0);
INSERT INTO "Track" VALUES (4,1,2,207,5,'Who Made Who',0);
COMMIT;
