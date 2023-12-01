-- --------------------------------------------------------
-- Сервер:                       127.0.0.1
-- Версія сервера:               8.1.0 - MySQL Community Server - GPL
-- ОС сервера:                   Linux
-- HeidiSQL Версія:              12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for ukubuka
CREATE DATABASE IF NOT EXISTS `ukubuka` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ukubuka`;

-- Dumping structure for таблиця ukubuka.catalog
CREATE TABLE IF NOT EXISTS `catalog` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_active` tinyint unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `catalog_code_ui` (`code`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.catalog_category
CREATE TABLE IF NOT EXISTS `catalog_category` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `catalog_id` int unsigned NOT NULL,
  `category_id` int unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `catalog_category_catalog_id_category_id_ui` (`catalog_id`,`category_id`),
  KEY `catalog_category_category_id_fk` (`category_id`),
  CONSTRAINT `catalog_category_catalog_id_fk` FOREIGN KEY (`catalog_id`) REFERENCES `catalog` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `catalog_category_category_id_fk` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.catalog_product
CREATE TABLE IF NOT EXISTS `catalog_product` (
  `catalog_id` int unsigned NOT NULL,
  `product_id` int unsigned NOT NULL,
  PRIMARY KEY (`catalog_id`,`product_id`),
  KEY `FK__product` (`product_id`),
  CONSTRAINT `FK__catalog` FOREIGN KEY (`catalog_id`) REFERENCES `catalog` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK__product` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.catalog_text
CREATE TABLE IF NOT EXISTS `catalog_text` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `catalog_id` int unsigned NOT NULL,
  `language_id` tinyint unsigned NOT NULL,
  `name` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `description` varchar(1024) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `catalog_text_catalog_id_language_id_ui` (`catalog_id`,`language_id`),
  KEY `catalog_text_language_id_fk` (`language_id`),
  CONSTRAINT `catalog_text_catalog_id_fk` FOREIGN KEY (`catalog_id`) REFERENCES `catalog` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `catalog_text_language_id_fk` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.category
CREATE TABLE IF NOT EXISTS `category` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `alias` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `parent_id` int unsigned DEFAULT NULL,
  `created_datetime` datetime NOT NULL,
  `changed_datetime` datetime NOT NULL,
  `is_active` tinyint unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `alias` (`alias`) USING BTREE,
  KEY `FK_category_category` (`parent_id`) USING BTREE,
  CONSTRAINT `FK_category_category` FOREIGN KEY (`parent_id`) REFERENCES `category` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.category_text
CREATE TABLE IF NOT EXISTS `category_text` (
  `category_id` int unsigned NOT NULL,
  `language` char(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`category_id`,`language`) USING BTREE,
  KEY `FK_category_text_languages` (`language`) USING BTREE,
  CONSTRAINT `FK_category_text_category` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_category_text_languages` FOREIGN KEY (`language`) REFERENCES `language` (`code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.characteristic_numeric
CREATE TABLE IF NOT EXISTS `characteristic_numeric` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `is_active` tinyint unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.characteristic_numeric_text
CREATE TABLE IF NOT EXISTS `characteristic_numeric_text` (
  `characteristic_id` int unsigned NOT NULL,
  `language` char(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `unit` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`characteristic_id`,`language`) USING BTREE,
  KEY `FK_characteristic_numeric_text_language` (`language`),
  CONSTRAINT `FK_characteristic_numeric_text_characteristic_numeric` FOREIGN KEY (`characteristic_id`) REFERENCES `characteristic_numeric` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_characteristic_numeric_text_language` FOREIGN KEY (`language`) REFERENCES `language` (`code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.characteristic_text
CREATE TABLE IF NOT EXISTS `characteristic_text` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `is_active` tinyint unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.characteristic_text_text
CREATE TABLE IF NOT EXISTS `characteristic_text_text` (
  `characteristic_id` int unsigned NOT NULL,
  `language` char(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `unit` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`characteristic_id`,`language`),
  KEY `FK_characteristic_text_text_language` (`language`),
  CONSTRAINT `FK_characteristic_text_text_characteristic_text` FOREIGN KEY (`characteristic_id`) REFERENCES `characteristic_text` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_characteristic_text_text_language` FOREIGN KEY (`language`) REFERENCES `language` (`code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.complex_product_recipe
CREATE TABLE IF NOT EXISTS `complex_product_recipe` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `product_id` int unsigned NOT NULL,
  `position_id` int unsigned NOT NULL,
  `number` mediumint unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `complex_product_recipe_product_id_position_id_ui` (`product_id`,`position_id`),
  KEY `complex_product_recipe_position_id_fk` (`position_id`),
  CONSTRAINT `complex_product_recipe_position_id_fk` FOREIGN KEY (`position_id`) REFERENCES `product_position` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `complex_product_recipe_product_id_fk` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.config
CREATE TABLE IF NOT EXISTS `config` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `value` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `config_code_ui` (`code`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.currency
CREATE TABLE IF NOT EXISTS `currency` (
  `id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `symbol` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `symbol_position` enum('before','after') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_active` int unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.language
CREATE TABLE IF NOT EXISTS `language` (
  `id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `code` char(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_active` tinyint unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `code_ui` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.page
CREATE TABLE IF NOT EXISTS `page` (
  `id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `template` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `layout` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `is_active` tinyint unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `page_code_ui` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.page_text
CREATE TABLE IF NOT EXISTS `page_text` (
  `id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `page_id` smallint unsigned NOT NULL,
  `language_id` tinyint unsigned NOT NULL,
  `title` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `page_text_page_id_language_id_ui` (`page_id`,`language_id`),
  KEY `page_text_language_id_fk` (`language_id`),
  CONSTRAINT `page_text_language_id_fk` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `page_text_page_id_fk` FOREIGN KEY (`page_id`) REFERENCES `page` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.product
CREATE TABLE IF NOT EXISTS `product` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_active` tinyint unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_code_ui` (`code`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.product_characteristic_numeric
CREATE TABLE IF NOT EXISTS `product_characteristic_numeric` (
  `product_id` int unsigned NOT NULL,
  `characteristic_id` int unsigned NOT NULL,
  `value` int NOT NULL,
  PRIMARY KEY (`product_id`,`characteristic_id`),
  KEY `FK_product_characteristic_numeric_characteristic_numeric` (`characteristic_id`),
  CONSTRAINT `FK_product_characteristic_numeric_characteristic_numeric` FOREIGN KEY (`characteristic_id`) REFERENCES `characteristic_numeric` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_product_characteristic_numeric_product` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.product_characteristic_text
CREATE TABLE IF NOT EXISTS `product_characteristic_text` (
  `product_id` int unsigned NOT NULL,
  `characteristic_id` int unsigned NOT NULL,
  `language` char(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `value` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`product_id`,`characteristic_id`,`language`) USING BTREE,
  KEY `FK_product_characteristic_text_characteristic_text` (`characteristic_id`),
  KEY `FK_product_characteristic_text_language` (`language`),
  CONSTRAINT `FK_product_characteristic_text_characteristic_text` FOREIGN KEY (`characteristic_id`) REFERENCES `characteristic_text` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_product_characteristic_text_language` FOREIGN KEY (`language`) REFERENCES `language` (`code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_product_characteristic_text_product` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.product_position
CREATE TABLE IF NOT EXISTS `product_position` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `sku` int unsigned NOT NULL,
  `product_id` int unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_position_sku_ui` (`sku`) USING BTREE,
  KEY `product_position_product_id_fk` (`product_id`) USING BTREE,
  CONSTRAINT `product_position_product_id_fk` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.product_position_price
CREATE TABLE IF NOT EXISTS `product_position_price` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `product_position_id` int unsigned NOT NULL,
  `currency_id` tinyint unsigned NOT NULL,
  `value` int unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_position_price_product_position_id_currency_id_ui` (`product_position_id`,`currency_id`),
  KEY `product_position_price_currency_id_fk` (`currency_id`),
  CONSTRAINT `product_position_price_currency_id_fk` FOREIGN KEY (`currency_id`) REFERENCES `currency` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `product_position_price_product_position_id_fk` FOREIGN KEY (`product_position_id`) REFERENCES `product_position` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.product_position_text
CREATE TABLE IF NOT EXISTS `product_position_text` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `product_position_id` int unsigned NOT NULL,
  `language_id` tinyint unsigned NOT NULL,
  `name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `description` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_position_text_product_position_id_language_id_ui` (`product_position_id`,`language_id`),
  KEY `product_position_text_language_id_fk` (`language_id`) USING BTREE,
  KEY `product_position_text_product_position_id_fk` (`product_position_id`) USING BTREE,
  CONSTRAINT `product_position_text_language_id_fk` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `product_position_text_product_position_id_fk` FOREIGN KEY (`product_position_id`) REFERENCES `product_position` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.product_price
CREATE TABLE IF NOT EXISTS `product_price` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `product_id` int unsigned NOT NULL,
  `currency_id` tinyint unsigned NOT NULL,
  `value` int unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_currency_ui` (`product_id`,`currency_id`) USING BTREE,
  KEY `currency_fk` (`currency_id`),
  CONSTRAINT `currency_fk` FOREIGN KEY (`currency_id`) REFERENCES `currency` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `product_fk` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.product_text
CREATE TABLE IF NOT EXISTS `product_text` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `product_id` int unsigned NOT NULL,
  `language_id` tinyint unsigned NOT NULL,
  `name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `description` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_text_product_id_language_id_ui` (`product_id`,`language_id`),
  KEY `product_text_language_id_fk` (`language_id`),
  CONSTRAINT `product_text_language_id_fk` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `product_text_product_id_fk` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.session
CREATE TABLE IF NOT EXISTS `session` (
  `id` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_datetime` datetime NOT NULL,
  `expired_datetime` datetime NOT NULL,
  `user_agent` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.session_data
CREATE TABLE IF NOT EXISTS `session_data` (
  `session_id` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `data` json NOT NULL,
  PRIMARY KEY (`session_id`),
  CONSTRAINT `FK_session_data_session` FOREIGN KEY (`session_id`) REFERENCES `session` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.session_user
CREATE TABLE IF NOT EXISTS `session_user` (
  `session_id` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `user_id` int unsigned NOT NULL,
  `is_logged_in` tinyint unsigned NOT NULL,
  PRIMARY KEY (`session_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `FK_session_user_session` FOREIGN KEY (`session_id`) REFERENCES `session` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_session_user_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.sku
CREATE TABLE IF NOT EXISTS `sku` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `sku` int unsigned NOT NULL,
  `product_id` int unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sku_sku_ui` (`sku`) USING BTREE,
  KEY `sku_product_id_fk` (`product_id`) USING BTREE,
  CONSTRAINT `sku_product_id_fk` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.sku_price
CREATE TABLE IF NOT EXISTS `sku_price` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `sku_id` int unsigned NOT NULL,
  `currency_id` tinyint unsigned NOT NULL,
  `value` int unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sku_price_sku_id_currency_id_ui` (`sku_id`,`currency_id`),
  KEY `sku_price_currency_id_fk` (`currency_id`),
  CONSTRAINT `sku_price_currency_id_fk` FOREIGN KEY (`currency_id`) REFERENCES `currency` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `sku_price_sku_id_fk` FOREIGN KEY (`sku_id`) REFERENCES `sku` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.sku_text
CREATE TABLE IF NOT EXISTS `sku_text` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `sku_id` int unsigned NOT NULL,
  `language_id` tinyint unsigned NOT NULL,
  `name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `description` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sku_text_sku_id_language_id_ui` (`sku_id`,`language_id`),
  KEY `sku_text_language_id_fk` (`language_id`) USING BTREE,
  KEY `sku_text_sku_id_fk` (`sku_id`) USING BTREE,
  CONSTRAINT `sku_text_language_id_fk` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `sku_text_sku_id_fk` FOREIGN KEY (`sku_id`) REFERENCES `sku` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.stock
CREATE TABLE IF NOT EXISTS `stock` (
  `sku` int unsigned NOT NULL,
  `number` int unsigned NOT NULL,
  PRIMARY KEY (`sku`),
  CONSTRAINT `FK_stock_sku` FOREIGN KEY (`sku`) REFERENCES `sku` (`sku`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.text
CREATE TABLE IF NOT EXISTS `text` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `text` varchar(2048) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.translation
CREATE TABLE IF NOT EXISTS `translation` (
  `text_id` int unsigned NOT NULL,
  `language` char(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `translation` varchar(2048) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`text_id`,`language`),
  KEY `FK_translation_language` (`language`),
  CONSTRAINT `FK_translation_language` FOREIGN KEY (`language`) REFERENCES `language` (`code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_translation_text` FOREIGN KEY (`text_id`) REFERENCES `text` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.user
CREATE TABLE IF NOT EXISTS `user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `first_name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `last_name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `is_blocked` tinyint unsigned NOT NULL,
  `registered_datetime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

-- Dumping structure for таблиця ukubuka.user_password
CREATE TABLE IF NOT EXISTS `user_password` (
  `user_id` int unsigned NOT NULL,
  `password_hash` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `salt` varchar(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `FK_user_passwords_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Дані для експорту не вибрані

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
