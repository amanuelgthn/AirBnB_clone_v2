-- A script that prepares a MYSQL server for the project
-- A DATABASE hbnb_test_db
-- A new user hbnb_test (in localhost)
-- The password of hbnb_test is set to hbnb_test_pwd
-- hbnb_test has all PRIVILEGES on hte DATABASE hbnb_test_db
-- hbnb_test has SELECT PRIVILEGES on the DATABASE perfomance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO `hbnb_test`@'localhost';
GRANT SELECT ON `performance_schema`.* TO `hbnb_test`@'localhost';
FLUSH PRIVILEGES;