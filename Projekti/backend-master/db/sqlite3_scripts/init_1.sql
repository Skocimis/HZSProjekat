BEGIN TRANSACTION;

CREATE TABLE "team_member" (
  `id`           INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `first_name`   TEXT    NOT NULL,
  `last_name`    TEXT    NOT NULL,
  `email`        TEXT    NOT NULL,
  `phone_number` TEXT,
  `school`       TEXT,
  `city`         TEXT,
  `team_id`      INTEGER NOT NULL,
  FOREIGN KEY (`team_id`) REFERENCES team (`id`)
    ON DELETE CASCADE
);

CREATE TABLE `team` (
  `id`          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name`        TEXT    NOT NULL,
  `description` TEXT,
  `photo_url`   TEXT,
  `team_uuid`   TEXT
);
COMMIT;
