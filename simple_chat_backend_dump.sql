PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO django_migrations VALUES(1,'contenttypes','0001_initial','2024-06-13 19:08:20.172396');
INSERT INTO django_migrations VALUES(2,'contenttypes','0002_remove_content_type_name','2024-06-13 19:08:20.180261');
INSERT INTO django_migrations VALUES(3,'auth','0001_initial','2024-06-13 19:08:20.193853');
INSERT INTO django_migrations VALUES(4,'auth','0002_alter_permission_name_max_length','2024-06-13 19:08:20.201155');
INSERT INTO django_migrations VALUES(5,'auth','0003_alter_user_email_max_length','2024-06-13 19:08:20.207812');
INSERT INTO django_migrations VALUES(6,'auth','0004_alter_user_username_opts','2024-06-13 19:08:20.214189');
INSERT INTO django_migrations VALUES(7,'auth','0005_alter_user_last_login_null','2024-06-13 19:08:20.219549');
INSERT INTO django_migrations VALUES(8,'auth','0006_require_contenttypes_0002','2024-06-13 19:08:20.222769');
INSERT INTO django_migrations VALUES(9,'auth','0007_alter_validators_add_error_messages','2024-06-13 19:08:20.229329');
INSERT INTO django_migrations VALUES(10,'auth','0008_alter_user_username_max_length','2024-06-13 19:08:20.235342');
INSERT INTO django_migrations VALUES(11,'auth','0009_alter_user_last_name_max_length','2024-06-13 19:08:20.241017');
INSERT INTO django_migrations VALUES(12,'auth','0010_alter_group_name_max_length','2024-06-13 19:08:20.248451');
INSERT INTO django_migrations VALUES(13,'auth','0011_update_proxy_permissions','2024-06-13 19:08:20.254234');
INSERT INTO django_migrations VALUES(14,'auth','0012_alter_user_first_name_max_length','2024-06-13 19:08:20.260154');
INSERT INTO django_migrations VALUES(15,'users','0001_initial','2024-06-13 19:08:20.271312');
INSERT INTO django_migrations VALUES(16,'admin','0001_initial','2024-06-13 19:08:20.281212');
INSERT INTO django_migrations VALUES(17,'admin','0002_logentry_remove_auto_add','2024-06-13 19:08:20.293040');
INSERT INTO django_migrations VALUES(18,'admin','0003_logentry_add_action_flag_choices','2024-06-13 19:08:20.303514');
INSERT INTO django_migrations VALUES(19,'chat','0001_initial','2024-06-13 19:08:20.325626');
INSERT INTO django_migrations VALUES(20,'chat','0002_rename_tread_message_thread','2024-06-13 19:08:20.339873');
INSERT INTO django_migrations VALUES(21,'chat','0003_alter_message_options_alter_thread_options','2024-06-13 19:08:20.355974');
INSERT INTO django_migrations VALUES(22,'sessions','0001_initial','2024-06-13 19:08:20.360591');
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO django_content_type VALUES(1,'admin','logentry');
INSERT INTO django_content_type VALUES(2,'auth','permission');
INSERT INTO django_content_type VALUES(3,'auth','group');
INSERT INTO django_content_type VALUES(4,'contenttypes','contenttype');
INSERT INTO django_content_type VALUES(5,'sessions','session');
INSERT INTO django_content_type VALUES(6,'users','user');
INSERT INTO django_content_type VALUES(7,'chat','thread');
INSERT INTO django_content_type VALUES(8,'chat','message');
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO auth_permission VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO auth_permission VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO auth_permission VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO auth_permission VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO auth_permission VALUES(5,2,'add_permission','Can add permission');
INSERT INTO auth_permission VALUES(6,2,'change_permission','Can change permission');
INSERT INTO auth_permission VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO auth_permission VALUES(8,2,'view_permission','Can view permission');
INSERT INTO auth_permission VALUES(9,3,'add_group','Can add group');
INSERT INTO auth_permission VALUES(10,3,'change_group','Can change group');
INSERT INTO auth_permission VALUES(11,3,'delete_group','Can delete group');
INSERT INTO auth_permission VALUES(12,3,'view_group','Can view group');
INSERT INTO auth_permission VALUES(13,4,'add_contenttype','Can add content type');
INSERT INTO auth_permission VALUES(14,4,'change_contenttype','Can change content type');
INSERT INTO auth_permission VALUES(15,4,'delete_contenttype','Can delete content type');
INSERT INTO auth_permission VALUES(16,4,'view_contenttype','Can view content type');
INSERT INTO auth_permission VALUES(17,5,'add_session','Can add session');
INSERT INTO auth_permission VALUES(18,5,'change_session','Can change session');
INSERT INTO auth_permission VALUES(19,5,'delete_session','Can delete session');
INSERT INTO auth_permission VALUES(20,5,'view_session','Can view session');
INSERT INTO auth_permission VALUES(21,6,'add_user','Can add user');
INSERT INTO auth_permission VALUES(22,6,'change_user','Can change user');
INSERT INTO auth_permission VALUES(23,6,'delete_user','Can delete user');
INSERT INTO auth_permission VALUES(24,6,'view_user','Can view user');
INSERT INTO auth_permission VALUES(25,7,'add_thread','Can add thread');
INSERT INTO auth_permission VALUES(26,7,'change_thread','Can change thread');
INSERT INTO auth_permission VALUES(27,7,'delete_thread','Can delete thread');
INSERT INTO auth_permission VALUES(28,7,'view_thread','Can view thread');
INSERT INTO auth_permission VALUES(29,8,'add_message','Can add message');
INSERT INTO auth_permission VALUES(30,8,'change_message','Can change message');
INSERT INTO auth_permission VALUES(31,8,'delete_message','Can delete message');
INSERT INTO auth_permission VALUES(32,8,'view_message','Can view message');
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "users_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL);
INSERT INTO users_user VALUES(1,'pbkdf2_sha256$600000$gTGju6Q8KC1zoGjSFk57Vh$rWrVZqIIZQ+tzXyTJKPdZuEQvRzBGJDPDt3Qo/5GiD4=','2024-06-13 19:13:07.234160',1,'admin','','','',1,1,'2024-06-13 19:11:45.755978');
INSERT INTO users_user VALUES(2,'pbkdf2_sha256$600000$3VOj3iGMvFCsDrIRe55TCn$MtabTLcnmv1khASbMRv4pM1+qUnXOdrDWJya5XVodfg=','2024-06-13 19:13:43.092578',1,'second_admin','','','',1,1,'2024-06-13 19:12:14.408430');
CREATE TABLE IF NOT EXISTS "users_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" bigint NOT NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "users_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" bigint NOT NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);
INSERT INTO django_admin_log VALUES(1,'1','Thread object (1)',1,'[{"added": {}}]',7,1,'2024-06-13 19:13:20.958478');
INSERT INTO django_admin_log VALUES(2,'1','Message object (1)',1,'[{"added": {}}]',8,1,'2024-06-13 19:13:29.205743');
CREATE TABLE IF NOT EXISTS "chat_thread" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" datetime NOT NULL, "updated_on" datetime NOT NULL, "created_by_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "updated_by_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO chat_thread VALUES(1,'2024-06-13 19:13:20.955320','2024-06-13 19:13:20.955362',1,1);
CREATE TABLE IF NOT EXISTS "chat_thread_participants" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "thread_id" bigint NOT NULL REFERENCES "chat_thread" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO chat_thread_participants VALUES(1,1,1);
INSERT INTO chat_thread_participants VALUES(2,1,2);
CREATE TABLE IF NOT EXISTS "chat_message" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_on" datetime NOT NULL, "updated_on" datetime NOT NULL, "text" text NOT NULL, "is_read" bool NOT NULL, "created_by_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "updated_by_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "thread_id" bigint NULL REFERENCES "chat_thread" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO chat_message VALUES(1,'2024-06-13 19:13:29.204739','2024-06-13 19:13:29.204783','TEST',0,1,1,1);
CREATE TABLE IF NOT EXISTS "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO django_session VALUES('64ox5c0f2wxfywynm7x88md0v1qs6obg','.eJxVjDsOwjAQBe_iGln-JbEp6TmDtd5d4wCypTipEHeHSCmgfTPzXiLCtpa4dV7iTOIsjDj9bgnwwXUHdId6axJbXZc5yV2RB-3y2oifl8P9OyjQy7ceMSlkzcanyZDPYDJONnDw1thMNjsCG7L2qAYkRUrD4KxLCXH0Hli8PwMWOL0:1sHptH:OUgaTqAQ0IJFQL5wzH11txGVXWT93kLY5p2qxGmHjJs','2024-06-27 19:13:43.094239');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('django_migrations',22);
INSERT INTO sqlite_sequence VALUES('django_content_type',8);
INSERT INTO sqlite_sequence VALUES('auth_permission',32);
INSERT INTO sqlite_sequence VALUES('auth_group',0);
INSERT INTO sqlite_sequence VALUES('django_admin_log',2);
INSERT INTO sqlite_sequence VALUES('chat_message',1);
INSERT INTO sqlite_sequence VALUES('users_user',2);
INSERT INTO sqlite_sequence VALUES('chat_thread',1);
INSERT INTO sqlite_sequence VALUES('chat_thread_participants',2);
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE UNIQUE INDEX "users_user_groups_user_id_group_id_b88eab82_uniq" ON "users_user_groups" ("user_id", "group_id");
CREATE INDEX "users_user_groups_user_id_5f6f5a90" ON "users_user_groups" ("user_id");
CREATE INDEX "users_user_groups_group_id_9afc8d0e" ON "users_user_groups" ("group_id");
CREATE UNIQUE INDEX "users_user_user_permissions_user_id_permission_id_43338c45_uniq" ON "users_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "users_user_user_permissions_user_id_20aca447" ON "users_user_user_permissions" ("user_id");
CREATE INDEX "users_user_user_permissions_permission_id_0b93982e" ON "users_user_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE INDEX "chat_thread_created_by_id_6684e5d8" ON "chat_thread" ("created_by_id");
CREATE INDEX "chat_thread_updated_by_id_7900bcbf" ON "chat_thread" ("updated_by_id");
CREATE UNIQUE INDEX "chat_thread_participants_thread_id_user_id_5b426d72_uniq" ON "chat_thread_participants" ("thread_id", "user_id");
CREATE INDEX "chat_thread_participants_thread_id_5167d8b7" ON "chat_thread_participants" ("thread_id");
CREATE INDEX "chat_thread_participants_user_id_83d3d42d" ON "chat_thread_participants" ("user_id");
CREATE INDEX "chat_message_created_by_id_a189218f" ON "chat_message" ("created_by_id");
CREATE INDEX "chat_message_updated_by_id_bfb7aa4a" ON "chat_message" ("updated_by_id");
CREATE INDEX "chat_message_thread_id_6a43dfba" ON "chat_message" ("thread_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
COMMIT;
