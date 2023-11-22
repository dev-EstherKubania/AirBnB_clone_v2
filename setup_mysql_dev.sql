-- Create db hbnb_dev_db if not exists
-- Create user hbnb_dev with pwd hbnb_dev_pwd
-- Grant hbnb_dev_db on performance_schema
-- Grant all previleges on hbnb_dev_db

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
