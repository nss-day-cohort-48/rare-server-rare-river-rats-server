DROP TABLE "Rare_Users";
DROP TABLE "DemotionQueue";
DROP TABLE "Subscriptions";
DROP TABLE "Posts";
DROP TABLE "Comments";
DROP TABLE "Reactions";
DROP TABLE "PostReactions";
DROP TABLE "Tags";
DROP TABLE "PostTags";
DROP TABLE "Categories";
import datetime
from datetime CREATE TABLE "Rare_Users" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "bio" varchar,
        "profile_image_url" varchar,
        "created_on" DATE,
        --DEFAULT CURRENT_TIMESTAMP,
        "active" bit,
        "first_name" varchar,
        "last_name" varchar,
        "email" varchar,
        "username" varchar,
        "password" varchar,
        "is_admin" bit
    );
CREATE TABLE "DemotionQueue" (
    "action" varchar,
    "admin_id" INTEGER,
    "approver_one_id" INTEGER,
    FOREIGN KEY(`admin_id`) REFERENCES `Rare_Users`(`id`),
    FOREIGN KEY(`approver_one_id`) REFERENCES `Rare_Users`(`id`),
    PRIMARY KEY (action, admin_id, approver_one_id)
);
CREATE TABLE "Subscriptions" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "follower_id" INTEGER,
    "author_id" INTEGER,
    "created_on" date,
    FOREIGN KEY(`follower_id`) REFERENCES `Rare_Users`(`id`),
    FOREIGN KEY(`author_id`) REFERENCES `Rare_Users`(`id`)
);
CREATE TABLE "Posts" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "rare_user_id" INTEGER,
    "category_id" INTEGER,
    "title" varchar,
    "publication_date" date,
    "image_url" varchar,
    "content" varchar,
    "approved" boolean
);
CREATE TABLE "Comments" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "post_id" INTEGER,
    "author_id" INTEGER,
    "content" varchar,
    FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
    FOREIGN KEY(`author_id`) REFERENCES `Rare_Users`(`id`)
);
CREATE TABLE "Reactions" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "label" varchar,
    "image_url" varchar
);
CREATE TABLE "PostReactions" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "rare_user_id" INTEGER,
    "reaction_id" INTEGER,
    "post_id" INTEGER,
    FOREIGN KEY(`rare_user_id`) REFERENCES `Rare_Users`(`id`),
    FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
    FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);
CREATE TABLE "Tags" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "label" varchar
);
CREATE TABLE "PostTags" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "post_id" INTEGER,
    "tag_id" INTEGER,
    FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
    FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);
CREATE TABLE "Categories" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "label" varchar
);
INSERT INTO Categories ('label')
VALUES ('News');
INSERT INTO Tags ('label')
VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url')
VALUES ('happy', 'https://pngtree.com/so/happy');
INSERT INTO `Rare_Users`
VALUES (
        null,
        "New guy",
        "profile_image_url",
        "created_on",
        1,
        "Nick",
        "M",
        "nick@m.com",
        "Nick M",
        "password",
        1
    );
INSERT INTO `Rare_Users`
VALUES (
        null,
        "Cool guy",
        "profile_image_url",
        "created_on",
        1,
        "Ben",
        "K",
        "ben@k.com",
        "Ben K",
        "password",
        1
    );
INSERT INTO `Rare_Users`
VALUES (
        null,
        "Chill guy",
        "profile_image_url",
        "created_on",
        1,
        "Roger",
        "G",
        "roger@g.com",
        "Roger G",
        "password",
        1
    );
INSERT INTO `Rare_Users`
VALUES (
        null,
        "Young guy",
        "profile_image_url",
        "created_on",
        1,
        "Key",
        "N",
        "key@n.com",
        "Key N",
        "password",
        1
    );
INSERT INTO `Rare_Users`
VALUES (
        null,
        "New Wizard",
        "profile_image_url",
        "created_on",
        1,
        "Hannah",
        "Hall",
        "hanna@hall.com",
        "Hanna H",
        "password",
        1
    );
INSERT INTO `Posts`
VALUES (
        null,
        3,
        1,
        "Test Post",
        "publication_date",
        "profile_image_url",
        "Content Content Content",
        True
    )
INSERT INTO Posts (
        'rare_user_id',
        'category_id',
        'title',
        'publication_date',
        'image_url',
        'content',
        'approved'
    )
VALUES (
        '1',
        '1',
        'This is a test post - title field',
        date.today(),
        'https://pngtree.com/so/happy',
        'this is a test post - content field',
        1
    )
SELECT *
FROM Rare_Users;
SELECT *
FROM Posts
SELECT GetDate()