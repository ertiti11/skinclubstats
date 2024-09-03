CREATE TABLE IF NOT EXISTS "skins" (
	"skin_id" INTEGER NOT NULL UNIQUE,
	"name" TEXT,
	-- 'Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'
	"rarity" TEXT,
	"price" REAL,
	"image_url" TEXT,
	"state" TEXT,
	"created_at" TIMESTAMP,
	PRIMARY KEY("skin_id")
);

CREATE TABLE IF NOT EXISTS "cases" (
	"case_id" INTEGER NOT NULL UNIQUE,
	"case_name" TEXT,
	"price" REAL,
	"profit_chance" REAL,
	"image_url" TEXT,
	"profit_chanceX1dot5" REAL,
	"profit_chanceX2" REAL,
	"profit_chanceX3" REAL,
	"profit_chanceX10" REAL,
	"real_price" REAL,
	"ev" REAL,
	"irb" REAL,
	"created_at" TIMESTAMP,
	PRIMARY KEY("case_id")
);

CREATE TABLE IF NOT EXISTS "case_skins" (
	"case_id" INTEGER NOT NULL UNIQUE,
	"skin_id" INTEGER,
	"probability" REAL,
	PRIMARY KEY("case_id"),
	FOREIGN KEY ("case_id") REFERENCES "cases"("case_id")
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY ("skin_id") REFERENCES "skins"("skin_id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);