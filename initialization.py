import os
from db.DB import DB
from models.user import User


def create_folder():
    static_folder = 'static'
    images_folder = '/images/'
    full_path = static_folder + images_folder

    if not os.path.exists(full_path):
        return os.makedirs(static_folder + images_folder)


def init_db():
    DB.create_table("""CREATE TABLE IF NOT EXISTS `user` (
                        `id` int NOT NULL AUTO_INCREMENT,
                        `username` varchar(255) NOT NULL,
                        `password` varchar(255) NOT NULL,
                        PRIMARY KEY (`id`),
                        UNIQUE KEY `username_UNIQUE` (`username`)
                    ) ENGINE=InnoDB""")

    #username and password for login
    username = "admin"
    password = User.hash_password("VkT}9;N3$kdAp]Nc")

    DB.insert_into_query(
        "INSERT IGNORE INTO user (username, password) VALUES (%s, %s)", (username, password))

    DB.create_table("""CREATE TABLE IF NOT EXISTS `employee` (
                        `id` int NOT NULL AUTO_INCREMENT,
                        `first_name` varchar(255) NOT NULL,
                        `last_name` varchar(255) NOT NULL,
                        `order` int NOT NULL,
                        `linked_in` varchar(255) DEFAULT NULL,
                        `xing` varchar(255) DEFAULT NULL,
                        `role` varchar(255) NOT NULL,
                        `email` varchar(255) NOT NULL,
                        `photo_url` varchar(255) NOT NULL,
                        PRIMARY KEY (`id`)
                    ) ENGINE=InnoDB""")


def init():
    # create_folder()
    init_db()
