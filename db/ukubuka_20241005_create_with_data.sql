-- --------------------------------------------------------
-- Сервер:                       127.0.0.1
-- Версія сервера:               8.4.2 - MySQL Community Server - GPL
-- ОС сервера:                   Linux
-- HeidiSQL Версія:              12.8.0.6934
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

-- Dumping structure for таблиця ukubuka.category
CREATE TABLE IF NOT EXISTS `category` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `slug` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `parent_id` int unsigned DEFAULT NULL,
  `is_active` tinyint unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `alias` (`slug`) USING BTREE,
  KEY `FK_category_category` (`parent_id`) USING BTREE,
  CONSTRAINT `FK_category_category` FOREIGN KEY (`parent_id`) REFERENCES `category` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.category: ~2 rows (приблизно)
INSERT INTO `category` (`id`, `slug`, `parent_id`, `is_active`, `created_at`, `updated_at`, `deleted_at`) VALUES
	(2, 'test_category', NULL, 1, '2024-09-18 20:50:50', NULL, NULL),
	(3, 'test_subcategory', 2, 1, '2024-09-18 20:51:05', NULL, NULL);

-- Dumping structure for таблиця ukubuka.category_text
CREATE TABLE IF NOT EXISTS `category_text` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `category_id` int unsigned NOT NULL,
  `language_id` tinyint unsigned NOT NULL,
  `name` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `description` varchar(2048) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `Індекс 2` (`category_id`,`language_id`),
  KEY `FK_category_text_language` (`language_id`),
  CONSTRAINT `FK_category_text_category` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_category_text_language` FOREIGN KEY (`language_id`) REFERENCES `language` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.category_text: ~4 rows (приблизно)
INSERT INTO `category_text` (`id`, `category_id`, `language_id`, `name`, `description`, `created_at`, `updated_at`) VALUES
	(3, 2, 1, 'Test Category', 'Test category description', '2024-09-18 00:00:00', NULL),
	(4, 2, 2, 'Тестова Категорія', 'Опис тестової категорії', '2024-09-18 00:00:00', NULL),
	(5, 3, 1, 'Test Subcategory', 'Test subcategory description', '2024-09-18 00:00:00', NULL),
	(6, 3, 2, 'Тестова Підкатегорія', 'Опис тестової підкатегорії', '2024-09-18 00:00:00', NULL);

-- Dumping structure for таблиця ukubuka.characteristic_numeric
CREATE TABLE IF NOT EXISTS `characteristic_numeric` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `is_active` tinyint unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.characteristic_numeric: ~0 rows (приблизно)

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

-- Dumping data for table ukubuka.characteristic_numeric_text: ~0 rows (приблизно)

-- Dumping structure for таблиця ukubuka.characteristic_text
CREATE TABLE IF NOT EXISTS `characteristic_text` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `is_active` tinyint unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.characteristic_text: ~0 rows (приблизно)

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

-- Dumping data for table ukubuka.characteristic_text_text: ~0 rows (приблизно)

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

-- Dumping data for table ukubuka.complex_product_recipe: ~0 rows (приблизно)

-- Dumping structure for таблиця ukubuka.config
CREATE TABLE IF NOT EXISTS `config` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `value` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `config_code_ui` (`code`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.config: ~2 rows (приблизно)
INSERT INTO `config` (`id`, `code`, `value`, `created_at`, `updated_at`) VALUES
	(2, 'default_language_code', 'eng', '2023-12-02 00:35:14', NULL),
	(3, 'default_currency_code', 'UAH', '2024-10-05 15:54:06', NULL);

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

-- Dumping data for table ukubuka.currency: ~2 rows (приблизно)
INSERT INTO `currency` (`id`, `code`, `symbol`, `symbol_position`, `is_active`, `created_at`, `updated_at`) VALUES
	(1, 'UAH', '₴', 'after', 1, '2023-08-13 19:24:31', '2023-08-13 19:24:32'),
	(2, 'USD', '$', 'before', 0, '2023-08-13 19:28:12', '2023-08-13 19:28:13');

-- Dumping structure for таблиця ukubuka.language
CREATE TABLE IF NOT EXISTS `language` (
  `id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `code` char(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_active` tinyint unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `code_ui` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.language: ~3 rows (приблизно)
INSERT INTO `language` (`id`, `code`, `name`, `is_active`, `created_at`, `updated_at`, `deleted_at`) VALUES
	(1, 'eng', 'english', 1, '2023-08-13 19:56:19', NULL, NULL),
	(2, 'ukr', 'українська', 1, '2023-08-13 19:56:19', NULL, NULL),
	(13, 'tst', 'Test', 0, '2024-02-08 23:48:00', NULL, '2024-02-09 00:04:14');

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
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.page: ~17 rows (приблизно)
INSERT INTO `page` (`id`, `code`, `template`, `layout`, `is_active`, `created_at`, `updated_at`) VALUES
	(1, 'acp_languages', 'v1/acp/language/languages.html', 'v1/acp/layout/layout.html', 1, '2023-01-29 20:17:10', NULL),
	(2, 'acp_dashboard', 'v1/acp/dashboard/dashboard.html', 'v1/acp/layout/layout.html', 1, '2023-02-18 12:49:49', NULL),
	(3, 'acp_edit_language', 'v1/acp/language/edit_language.html', 'v1/acp/layout/layout.html', 1, '2023-06-04 21:59:51', '2023-10-26 23:03:35'),
	(4, 'product_page', 'v1/website/product/product_page.html', 'v1/layout/layout.html', 1, '2023-08-13 16:39:09', '2024-09-18 23:52:54'),
	(5, 'catalog', 'v1/catalog/catalog.html', 'v1/layout/layout.html', 1, '2023-09-27 22:43:43', NULL),
	(6, 'catalogs', 'v1/catalog/catalogs.html', 'v1/layout/layout.html', 1, '2023-09-27 22:47:26', NULL),
	(7, 'acp_add_language', 'v1/acp/language/add_language.html', 'v1/acp/layout/layout.html', 1, '2023-11-22 21:26:52', NULL),
	(9, 'acp_pages', 'v1/acp/page/pages.html', 'v1/acp/layout/layout.html', 1, '2023-12-01 23:07:45', NULL),
	(10, 'acp_edit_page', 'v1/acp/page/edit_page.html', 'v1/acp/layout/layout.html', 1, '2023-12-10 21:00:15', NULL),
	(11, 'acp_add_page', 'v1/acp/page/add_page.html', 'v1/acp/layout/layout.html', 1, '2023-12-10 21:02:23', NULL),
	(19, 'acp_add_page_translation', 'v1/acp/page/add_page_translation.html', 'v1/acp/layout/layout.html', 1, '2024-01-07 18:04:18', NULL),
	(20, 'acp_edit_page_translation', 'v1/acp/page/edit_page_translation.html', 'v1/acp/layout/layout.html', 1, '2024-01-07 18:04:39', NULL),
	(21, 'acp_page', 'v1/acp/page/page.html', 'v1/acp/layout/layout.html', 1, '2024-01-07 18:10:40', NULL),
	(25, 'acp_language', 'v1/acp/language/language.html', 'v1/acp/layout/layout.html', 1, '2024-02-08 00:46:47', NULL),
	(28, 'home_page', 'v1/website/home.html', 'v1/layout/layout.html', 1, '2024-08-25 14:42:22', NULL),
	(29, 'catalogs_page', 'v1/website/Catalog/catalogs_page.html', 'v1/layout/layout.html', 1, '2024-08-25 15:06:08', NULL),
	(30, 'catalog_page', 'v1/website/Catalog/catalog_page.html', 'v1/layout/layout.html', 1, '2024-08-25 15:40:43', NULL);

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
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.page_text: ~28 rows (приблизно)
INSERT INTO `page_text` (`id`, `page_id`, `language_id`, `title`, `created_at`, `updated_at`) VALUES
	(1, 1, 1, 'Languages', '2023-08-14 20:14:25', NULL),
	(2, 1, 2, 'Мови', '2023-08-14 20:14:25', NULL),
	(3, 2, 1, 'Dashboard', '2023-08-14 20:14:25', NULL),
	(4, 2, 2, 'Панель приладів', '2023-08-14 20:14:25', NULL),
	(5, 3, 1, 'Edit language', '2023-08-14 20:14:25', NULL),
	(6, 3, 2, 'Редагувати мову', '2023-08-14 20:14:25', NULL),
	(8, 4, 1, 'Product', '2023-08-14 23:15:29', NULL),
	(9, 4, 2, 'Товар', '2023-08-14 23:15:47', NULL),
	(10, 5, 1, 'Catalog', '2023-09-27 22:44:07', NULL),
	(11, 5, 2, 'Каталог', '2023-09-27 22:44:23', NULL),
	(12, 6, 1, 'Catalogs', '2023-09-27 22:47:49', NULL),
	(13, 6, 2, 'Каталоги', '2023-09-27 22:48:04', NULL),
	(14, 7, 1, 'Add language', '2023-11-22 21:28:07', NULL),
	(15, 7, 2, 'Додати мову', '2023-11-22 21:28:32', NULL),
	(18, 9, 1, 'Pages', '2023-12-01 23:08:26', NULL),
	(19, 9, 2, 'Сторінки', '2023-12-01 23:08:45', NULL),
	(20, 10, 1, 'Редагувати сторінку', '2023-12-10 21:00:57', NULL),
	(21, 10, 2, 'Edit page', '2023-12-10 21:01:12', NULL),
	(22, 11, 1, 'Додати сторінку', '2023-12-10 21:02:56', NULL),
	(23, 11, 2, 'Add page', '2023-12-10 21:03:10', NULL),
	(24, 19, 1, 'Add page translation', '2024-01-07 18:06:15', NULL),
	(25, 19, 2, 'Додати переклад сторінки', '2024-01-07 18:07:03', NULL),
	(26, 20, 1, 'Edit page translation', '2024-01-07 18:08:04', NULL),
	(27, 20, 2, 'Редагувати переклад сторінки', '2024-01-07 18:08:41', NULL),
	(28, 21, 1, 'Page', '2024-01-07 19:38:53', NULL),
	(29, 21, 2, 'Сторінка', '2024-01-07 19:39:07', NULL),
	(33, 25, 1, 'Language', '2024-02-08 00:47:08', NULL),
	(34, 25, 2, 'Мова', '2024-02-08 00:47:25', NULL);

-- Dumping structure for таблиця ukubuka.product
CREATE TABLE IF NOT EXISTS `product` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `slug` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_active` tinyint unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_slug_ui` (`slug`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.product: ~1 rows (приблизно)
INSERT INTO `product` (`id`, `slug`, `is_active`, `created_at`, `updated_at`, `deleted_at`) VALUES
	(1, 'test_product', 1, '2023-08-13 19:31:09', NULL, NULL);

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

-- Dumping data for table ukubuka.product_characteristic_numeric: ~0 rows (приблизно)

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

-- Dumping data for table ukubuka.product_characteristic_text: ~0 rows (приблизно)

-- Dumping structure for таблиця ukubuka.product_position
CREATE TABLE IF NOT EXISTS `product_position` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `sku` int unsigned NOT NULL,
  `slug` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `product_id` int unsigned NOT NULL,
  `is_active` tinyint unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_position_sku_ui` (`sku`) USING BTREE,
  UNIQUE KEY `product_position_slug_ui` (`slug`),
  KEY `product_position_product_id_fk` (`product_id`) USING BTREE,
  CONSTRAINT `product_position_product_id_fk` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.product_position: ~2 rows (приблизно)
INSERT INTO `product_position` (`id`, `sku`, `slug`, `product_id`, `is_active`, `created_at`, `updated_at`, `deleted_at`) VALUES
	(1, 11, 'test_product_position_1', 1, 1, '2024-10-04 13:01:54', NULL, NULL),
	(2, 12, 'test_product_position_2', 1, 1, '2024-10-04 13:02:21', NULL, NULL);

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

-- Dumping data for table ukubuka.product_position_price: ~0 rows (приблизно)

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.product_position_text: ~4 rows (приблизно)
INSERT INTO `product_position_text` (`id`, `product_position_id`, `language_id`, `name`, `description`, `created_at`, `updated_at`) VALUES
	(1, 1, 1, 'Position 1 of Test product Name', 'Position 1 of Test product Description', '2024-10-04 14:18:08', NULL),
	(2, 1, 2, 'Назва Позиції 1 Тестового товару', 'Опис Позиції 1 Тестового товару', '2024-10-04 14:18:18', NULL),
	(3, 2, 1, 'Position 2 of Test product Name', 'Position 2 of Test product Description', '2024-10-04 14:18:27', NULL),
	(4, 2, 2, 'Назва Позиції 2 Тестового товару', 'Опис Позиції 2 Тестового товару', '2024-10-04 14:18:34', NULL);

-- Dumping structure for таблиця ukubuka.product_price
CREATE TABLE IF NOT EXISTS `product_price` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `product_id` int unsigned NOT NULL,
  `currency_id` tinyint unsigned NOT NULL,
  `value` int unsigned NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_id_currency_id_ui` (`product_id`,`currency_id`) USING BTREE,
  KEY `currency_id_fk` (`currency_id`) USING BTREE,
  CONSTRAINT `currency_id_fk` FOREIGN KEY (`currency_id`) REFERENCES `currency` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `product_id_fk` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.product_price: ~1 rows (приблизно)
INSERT INTO `product_price` (`id`, `product_id`, `currency_id`, `value`, `created_at`, `updated_at`) VALUES
	(1, 1, 1, 13050, '2023-08-13 19:33:55', NULL);

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

-- Dumping data for table ukubuka.product_text: ~2 rows (приблизно)
INSERT INTO `product_text` (`id`, `product_id`, `language_id`, `name`, `description`, `created_at`, `updated_at`) VALUES
	(1, 1, 1, 'Test Product name', 'Test product description', '2023-08-13 20:46:26', NULL),
	(2, 1, 2, 'Назва тестового товару', 'Опис тестового товару', '2023-08-13 20:47:00', NULL);

-- Dumping structure for таблиця ukubuka.session
CREATE TABLE IF NOT EXISTS `session` (
  `id` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_datetime` datetime NOT NULL,
  `expired_datetime` datetime NOT NULL,
  `user_agent` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.session: ~13 rows (приблизно)
INSERT INTO `session` (`id`, `created_datetime`, `expired_datetime`, `user_agent`) VALUES
	('6ytkdodybed83m0g33ixbflueqvfjcpb', '2022-08-16 10:24:45', '2022-08-23 10:24:45', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'),
	('76w5ac55aq2dml2wq9ieztpd0yl9yd8f', '2021-11-16 22:32:04', '2021-11-23 22:32:04', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'),
	('8pem6y14nda0e7oce5hnq63wne8drl6n', '2021-11-09 20:27:25', '2021-11-16 20:27:25', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'),
	('b07wnoxpvgbbfq0rm71asp6g454dewfy', '2022-02-06 12:13:08', '2022-02-13 12:13:08', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'),
	('b5tgn1e71ezuw37qz1hvavzdbwcw93ml', '2021-12-11 16:42:57', '2021-12-18 16:42:57', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'),
	('c05ybbupo8ji4nk7hb924iz0mu8kzexf', '2021-12-26 20:06:55', '2022-01-02 20:06:55', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'),
	('dv8ygt8edy2crttwfei3t5cq3lnpstkj', '2022-08-08 17:53:14', '2022-08-15 17:53:14', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'),
	('fjz8m2itby578dubfn17ykmafxhnfo86', '2022-08-08 17:53:32', '2022-08-15 17:53:32', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'),
	('hp6yxp9kcaedqjf627b3qtf3qgtatq2n', '2022-02-14 22:50:01', '2022-02-21 22:50:01', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'),
	('huwttl6xlkcucsni9xp960s69zsyyynw', '2021-11-09 20:25:16', '2021-11-16 20:25:16', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'),
	('l7c5z8zw5p411m4dv2hy0kl4pcrcdz9h', '2021-12-18 20:32:53', '2021-12-25 20:32:53', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'),
	('m7j6galwdvoxr2l0qoojg1dj1oomgr01', '2021-11-09 20:24:43', '2021-11-16 20:24:43', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'),
	('x2zs6yz9i80dwibvb7rrvbwj7qzjh0xq', '2021-11-27 18:04:07', '2021-12-04 18:04:07', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36');

-- Dumping structure for таблиця ukubuka.session_data
CREATE TABLE IF NOT EXISTS `session_data` (
  `session_id` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `data` json NOT NULL,
  PRIMARY KEY (`session_id`),
  CONSTRAINT `FK_session_data_session` FOREIGN KEY (`session_id`) REFERENCES `session` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.session_data: ~0 rows (приблизно)

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

-- Dumping data for table ukubuka.session_user: ~5 rows (приблизно)
INSERT INTO `session_user` (`session_id`, `user_id`, `is_logged_in`) VALUES
	('6ytkdodybed83m0g33ixbflueqvfjcpb', 2, 1),
	('76w5ac55aq2dml2wq9ieztpd0yl9yd8f', 1, 1),
	('b5tgn1e71ezuw37qz1hvavzdbwcw93ml', 1, 0),
	('fjz8m2itby578dubfn17ykmafxhnfo86', 1, 1),
	('l7c5z8zw5p411m4dv2hy0kl4pcrcdz9h', 1, 1);

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

-- Dumping data for table ukubuka.sku: ~0 rows (приблизно)

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

-- Dumping data for table ukubuka.sku_price: ~0 rows (приблизно)

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

-- Dumping data for table ukubuka.sku_text: ~0 rows (приблизно)

-- Dumping structure for таблиця ukubuka.stock
CREATE TABLE IF NOT EXISTS `stock` (
  `sku` int unsigned NOT NULL,
  `number` int unsigned NOT NULL,
  PRIMARY KEY (`sku`),
  CONSTRAINT `FK_stock_sku` FOREIGN KEY (`sku`) REFERENCES `sku` (`sku`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.stock: ~0 rows (приблизно)

-- Dumping structure for таблиця ukubuka.text
CREATE TABLE IF NOT EXISTS `text` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `text` varchar(2048) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.text: ~94 rows (приблизно)
INSERT INTO `text` (`id`, `text`) VALUES
	(1, 'Translations'),
	(2, 'text'),
	(3, 'edit'),
	(4, 'delete'),
	(5, 'Home page'),
	(6, 'Categories'),
	(7, 'Products'),
	(8, 'Catalog'),
	(9, 'Dashboard'),
	(10, 'Ukubuka ACP Dashboard'),
	(11, 'Ukubuka home page'),
	(12, 'Account'),
	(13, 'Log in'),
	(14, 'Registration'),
	(15, 'Edit translations'),
	(16, 'ACP Dashboard'),
	(17, 'Session ID'),
	(18, 'User ID'),
	(19, 'First name'),
	(20, 'Last name'),
	(21, 'Registered on'),
	(22, 'Language'),
	(23, 'Log out'),
	(24, 'Edit translation'),
	(25, 'Wrong translation'),
	(26, 'Text'),
	(27, 'Users'),
	(28, 'Email'),
	(29, 'email'),
	(30, 'name'),
	(31, 'is confirmed'),
	(34, 'yes'),
	(35, 'no'),
	(36, 'registration date'),
	(37, 'block'),
	(38, 'Ukubuka'),
	(39, 'is blocked'),
	(40, 'unblock'),
	(42, 'ID'),
	(43, 'Is blocked'),
	(44, 'Password'),
	(48, 'password'),
	(49, 'first name'),
	(50, 'last name'),
	(51, 'alias'),
	(52, 'parent ID'),
	(53, 'date of creation'),
	(54, 'date of change'),
	(55, 'is active'),
	(56, ''),
	(57, ''),
	(58, ''),
	(59, ''),
	(60, ''),
	(61, ''),
	(62, ''),
	(63, ''),
	(64, ''),
	(65, ''),
	(66, ''),
	(67, ''),
	(68, ''),
	(69, ''),
	(70, ''),
	(71, ''),
	(72, ''),
	(73, ''),
	(74, ''),
	(75, ''),
	(76, ''),
	(77, ''),
	(78, ''),
	(79, ''),
	(80, ''),
	(81, ''),
	(82, ''),
	(83, ''),
	(84, ''),
	(85, ''),
	(86, ''),
	(87, ''),
	(88, ''),
	(89, ''),
	(90, ''),
	(91, ''),
	(92, ''),
	(93, ''),
	(94, ''),
	(95, ''),
	(96, ''),
	(97, ''),
	(98, ''),
	(99, ''),
	(100, '');

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

-- Dumping data for table ukubuka.translation: ~188 rows (приблизно)
INSERT INTO `translation` (`text_id`, `language`, `translation`) VALUES
	(1, 'eng', 'Translations'),
	(1, 'ukr', 'Переклади'),
	(2, 'eng', 'text'),
	(2, 'ukr', 'текст'),
	(3, 'eng', 'edit'),
	(3, 'ukr', 'редагувати'),
	(4, 'eng', 'delete'),
	(4, 'ukr', 'видалити'),
	(5, 'eng', 'Home page'),
	(5, 'ukr', 'Домашня сторінка'),
	(6, 'eng', 'Categories'),
	(6, 'ukr', 'Категорії'),
	(7, 'eng', 'Products'),
	(7, 'ukr', 'Товари'),
	(8, 'eng', 'Catalog'),
	(8, 'ukr', 'Каталог'),
	(9, 'eng', 'Dashboard'),
	(9, 'ukr', 'Dashboard'),
	(10, 'eng', 'Ukubuka ACP Dashboard'),
	(10, 'ukr', 'Ukubuka ACP Dashboard'),
	(11, 'eng', 'Ukubuka home page'),
	(11, 'ukr', 'Домашня сторінка Ukubuka'),
	(12, 'eng', 'Account'),
	(12, 'ukr', 'Аккаунт'),
	(13, 'eng', 'Log in'),
	(13, 'ukr', 'Увійти'),
	(14, 'eng', 'Registration'),
	(14, 'ukr', 'Реєстрація'),
	(15, 'eng', 'Edit translations'),
	(15, 'ukr', 'Редагувати переклади'),
	(16, 'eng', 'ACP Dashboard'),
	(16, 'ukr', 'ACP Dashboard'),
	(17, 'eng', 'Session ID'),
	(17, 'ukr', 'ID сесії'),
	(18, 'eng', 'User ID'),
	(18, 'ukr', 'ID користувача'),
	(19, 'eng', 'First name'),
	(19, 'ukr', 'Ім\'я'),
	(20, 'eng', 'Last name'),
	(20, 'ukr', 'Прізвище'),
	(21, 'eng', 'Registered on'),
	(21, 'ukr', 'Зареєструватися'),
	(22, 'eng', 'Language'),
	(22, 'ukr', 'Мова'),
	(23, 'eng', 'Log out'),
	(23, 'ukr', 'Вийти'),
	(24, 'eng', 'Edit translation'),
	(24, 'ukr', 'Редагувати переклад'),
	(25, 'eng', 'Wrong translation'),
	(25, 'ukr', 'Неправильний переклад'),
	(26, 'eng', 'Text'),
	(26, 'ukr', 'Текст'),
	(27, 'eng', 'Users'),
	(27, 'ukr', 'Користувачі'),
	(28, 'eng', 'Email'),
	(28, 'ukr', 'Емейл'),
	(29, 'eng', 'email'),
	(29, 'ukr', 'емейл'),
	(30, 'eng', 'name'),
	(30, 'ukr', 'ім\'я'),
	(31, 'eng', 'is confirmed'),
	(31, 'ukr', 'підтверджений'),
	(34, 'eng', 'yes'),
	(34, 'ukr', 'так'),
	(35, 'eng', 'no'),
	(35, 'ukr', 'ні'),
	(36, 'eng', 'registration date'),
	(36, 'ukr', 'дата реєстрації'),
	(37, 'eng', 'block'),
	(37, 'ukr', 'блокувати'),
	(38, 'eng', 'Ukubuka'),
	(38, 'ukr', 'Ukubuka'),
	(39, 'eng', 'is blocked'),
	(39, 'ukr', 'заблокований'),
	(40, 'eng', 'unblock'),
	(40, 'ukr', 'розблокувати'),
	(42, 'eng', 'ID'),
	(42, 'ukr', 'ID'),
	(43, 'eng', 'Is blocked'),
	(43, 'ukr', 'Заблокований'),
	(44, 'eng', 'Password'),
	(44, 'ukr', 'Пароль'),
	(48, 'eng', 'password'),
	(48, 'ukr', 'пароль'),
	(49, 'eng', 'first name'),
	(49, 'ukr', 'ім\'я'),
	(50, 'eng', 'last name'),
	(50, 'ukr', 'прізвище'),
	(51, 'eng', 'alias'),
	(51, 'ukr', 'псевдонім'),
	(52, 'eng', 'parent ID'),
	(52, 'ukr', 'батьківський ID'),
	(53, 'eng', ''),
	(53, 'ukr', ''),
	(54, 'eng', ''),
	(54, 'ukr', ''),
	(55, 'eng', ''),
	(55, 'ukr', ''),
	(56, 'eng', ''),
	(56, 'ukr', ''),
	(57, 'eng', ''),
	(57, 'ukr', ''),
	(58, 'eng', ''),
	(58, 'ukr', ''),
	(59, 'eng', ''),
	(59, 'ukr', ''),
	(60, 'eng', ''),
	(60, 'ukr', ''),
	(61, 'eng', ''),
	(61, 'ukr', ''),
	(62, 'eng', ''),
	(62, 'ukr', ''),
	(63, 'eng', ''),
	(63, 'ukr', ''),
	(64, 'eng', ''),
	(64, 'ukr', ''),
	(65, 'eng', ''),
	(65, 'ukr', ''),
	(66, 'eng', ''),
	(66, 'ukr', ''),
	(67, 'eng', ''),
	(67, 'ukr', ''),
	(68, 'eng', ''),
	(68, 'ukr', ''),
	(69, 'eng', ''),
	(69, 'ukr', ''),
	(70, 'eng', ''),
	(70, 'ukr', ''),
	(71, 'eng', ''),
	(71, 'ukr', ''),
	(72, 'eng', ''),
	(72, 'ukr', ''),
	(73, 'eng', ''),
	(73, 'ukr', ''),
	(74, 'eng', ''),
	(74, 'ukr', ''),
	(75, 'eng', ''),
	(75, 'ukr', ''),
	(76, 'eng', ''),
	(76, 'ukr', ''),
	(77, 'eng', ''),
	(77, 'ukr', ''),
	(78, 'eng', ''),
	(78, 'ukr', ''),
	(79, 'eng', ''),
	(79, 'ukr', ''),
	(80, 'eng', ''),
	(80, 'ukr', ''),
	(81, 'eng', ''),
	(81, 'ukr', ''),
	(82, 'eng', ''),
	(82, 'ukr', ''),
	(83, 'eng', ''),
	(83, 'ukr', ''),
	(84, 'eng', ''),
	(84, 'ukr', ''),
	(85, 'eng', ''),
	(85, 'ukr', ''),
	(86, 'eng', ''),
	(86, 'ukr', ''),
	(87, 'eng', ''),
	(87, 'ukr', ''),
	(88, 'eng', ''),
	(88, 'ukr', ''),
	(89, 'eng', ''),
	(89, 'ukr', ''),
	(90, 'eng', ''),
	(90, 'ukr', ''),
	(91, 'eng', ''),
	(91, 'ukr', ''),
	(92, 'eng', ''),
	(92, 'ukr', ''),
	(93, 'eng', ''),
	(93, 'ukr', ''),
	(94, 'eng', ''),
	(94, 'ukr', ''),
	(95, 'eng', ''),
	(95, 'ukr', ''),
	(96, 'eng', ''),
	(96, 'ukr', ''),
	(97, 'eng', ''),
	(97, 'ukr', ''),
	(98, 'eng', ''),
	(98, 'ukr', ''),
	(99, 'eng', ''),
	(99, 'ukr', ''),
	(100, 'eng', ''),
	(100, 'ukr', '');

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

-- Dumping data for table ukubuka.user: ~2 rows (приблизно)
INSERT INTO `user` (`id`, `email`, `first_name`, `last_name`, `is_blocked`, `registered_datetime`) VALUES
	(1, 'hutei@live.com', 'Вадим', 'Гутей', 0, '2021-11-19 17:19:54'),
	(2, 'hutei2@live.com', NULL, NULL, 1, '2022-08-17 15:29:55');

-- Dumping structure for таблиця ukubuka.user_password
CREATE TABLE IF NOT EXISTS `user_password` (
  `user_id` int unsigned NOT NULL,
  `password_hash` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `salt` varchar(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `FK_user_passwords_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table ukubuka.user_password: ~2 rows (приблизно)
INSERT INTO `user_password` (`user_id`, `password_hash`, `salt`) VALUES
	(1, 'f7fe84cf1842098524521f955fff817817afb7ea758bab950a3a82d3f25cbafb965cdde62ac8d308c614d6144ae01bd7434926643103fde9d31e6326746cbeed', 'nSRbsNDp2RZu'),
	(2, '1788d38766e84c3b120c6e66dd50ee25d5f416f27c979d773e79e109636c620d6618a67fb260f8eb3902f0dc67c8a6db95f763729f9c88bb42df9f8ff75cfbbe', 'aNotKyX8AZPw');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
