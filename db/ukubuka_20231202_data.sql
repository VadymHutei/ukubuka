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

-- Dumping data for table ukubuka.catalog: ~2 rows (приблизно)
INSERT INTO `catalog` (`id`, `code`, `is_active`, `created_at`, `updated_at`, `deleted_at`) VALUES
	(1, 'test_catalog', 1, '2023-09-24 18:46:49', NULL, NULL),
	(2, 'test_catalog_2', 1, '2023-09-27 22:48:29', NULL, NULL);

-- Dumping data for table ukubuka.catalog_category: ~0 rows (приблизно)

-- Dumping data for table ukubuka.catalog_product: ~0 rows (приблизно)

-- Dumping data for table ukubuka.catalog_text: ~4 rows (приблизно)
INSERT INTO `catalog_text` (`id`, `catalog_id`, `language_id`, `name`, `description`, `created_at`, `updated_at`) VALUES
	(1, 1, 1, 'Catalog name', 'Catalog description', '2023-09-24 22:50:31', NULL),
	(2, 1, 2, 'Назва каталогу', 'Опис каталогу', '2023-09-24 22:50:50', NULL),
	(3, 2, 1, 'Catalog 2 name', 'Catalog 2 description', '2023-09-27 22:49:14', NULL),
	(4, 2, 2, 'Назва каталогу 2', 'Опис каталогу 2', '2023-09-27 22:49:38', NULL);

-- Dumping data for table ukubuka.category: ~1 rows (приблизно)
INSERT INTO `category` (`id`, `alias`, `parent_id`, `created_datetime`, `changed_datetime`, `is_active`) VALUES
	(1, 'test', NULL, '2022-02-14 22:55:42', '2022-02-14 22:55:44', 1);

-- Dumping data for table ukubuka.category_text: ~2 rows (приблизно)
INSERT INTO `category_text` (`category_id`, `language`, `name`) VALUES
	(1, 'eng', 'Test'),
	(1, 'ukr', 'Тест');

-- Dumping data for table ukubuka.characteristic_numeric: ~0 rows (приблизно)

-- Dumping data for table ukubuka.characteristic_numeric_text: ~0 rows (приблизно)

-- Dumping data for table ukubuka.characteristic_text: ~0 rows (приблизно)

-- Dumping data for table ukubuka.characteristic_text_text: ~0 rows (приблизно)

-- Dumping data for table ukubuka.complex_product_recipe: ~0 rows (приблизно)

-- Dumping data for table ukubuka.config: ~2 rows (приблизно)
INSERT INTO `config` (`id`, `code`, `value`, `created_at`, `updated_at`) VALUES
	(1, 'default_language_id', '1', '2023-08-20 13:27:22', NULL),
	(2, 'default_language_code', 'eng', '2023-12-02 00:35:14', NULL);

-- Dumping data for table ukubuka.currency: ~2 rows (приблизно)
INSERT INTO `currency` (`id`, `code`, `symbol`, `symbol_position`, `is_active`, `created_at`, `updated_at`) VALUES
	(1, 'UAH', '₴', 'after', 1, '2023-08-13 19:24:31', '2023-08-13 19:24:32'),
	(2, 'USD', '$', 'before', 0, '2023-08-13 19:28:12', '2023-08-13 19:28:13');

-- Dumping data for table ukubuka.language: ~2 rows (приблизно)
INSERT INTO `language` (`id`, `code`, `name`, `is_active`, `created_at`, `updated_at`) VALUES
	(1, 'eng', 'english', 1, '2023-08-13 19:56:19', NULL),
	(2, 'ukr', 'українська', 1, '2023-08-13 19:56:19', NULL);

-- Dumping data for table ukubuka.page: ~8 rows (приблизно)
INSERT INTO `page` (`id`, `code`, `template`, `layout`, `is_active`, `created_at`, `updated_at`) VALUES
	(1, 'acp_languages', 'v1/acp/language/languages.html', 'v1/acp/layout/layout.html', 1, '2023-01-29 20:17:10', NULL),
	(2, 'acp_dashboard', 'v1/acp/dashboard/dashboard.html', 'v1/acp/layout/layout.html', 1, '2023-02-18 12:49:49', NULL),
	(3, 'acp_edit_language', 'v1/acp/language/edit_language.html', 'v1/acp/layout/layout.html', 1, '2023-06-04 21:59:51', '2023-10-26 23:03:35'),
	(4, 'product', 'v1/product/product.html', 'v1/layout/layout.html', 1, '2023-08-13 16:39:09', NULL),
	(5, 'catalog', 'v1/catalog/catalog.html', 'v1/layout/layout.html', 1, '2023-09-27 22:43:43', NULL),
	(6, 'catalogs', 'v1/catalog/catalogs.html', 'v1/layout/layout.html', 1, '2023-09-27 22:47:26', NULL),
	(7, 'acp_add_language', 'v1/acp/language/add_language.html', 'v1/acp/layout/layout.html', 1, '2023-11-22 21:26:52', NULL),
	(9, 'acp_pages', 'v1/acp/page/pages.html', 'v1/acp/layout/layout.html', 1, '2023-12-01 23:07:45', NULL);

-- Dumping data for table ukubuka.page_text: ~16 rows (приблизно)
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
	(19, 9, 2, 'Сторінки', '2023-12-01 23:08:45', NULL);

-- Dumping data for table ukubuka.product: ~1 rows (приблизно)
INSERT INTO `product` (`id`, `code`, `is_active`, `created_at`, `updated_at`, `deleted_at`) VALUES
	(1, 'test', 1, '2023-08-13 19:31:09', NULL, NULL);

-- Dumping data for table ukubuka.product_characteristic_numeric: ~0 rows (приблизно)

-- Dumping data for table ukubuka.product_characteristic_text: ~0 rows (приблизно)

-- Dumping data for table ukubuka.product_position: ~0 rows (приблизно)

-- Dumping data for table ukubuka.product_position_price: ~0 rows (приблизно)

-- Dumping data for table ukubuka.product_position_text: ~0 rows (приблизно)

-- Dumping data for table ukubuka.product_price: ~1 rows (приблизно)
INSERT INTO `product_price` (`id`, `product_id`, `currency_id`, `value`, `created_at`, `updated_at`) VALUES
	(1, 1, 1, 13050, '2023-08-13 19:33:55', NULL);

-- Dumping data for table ukubuka.product_text: ~2 rows (приблизно)
INSERT INTO `product_text` (`id`, `product_id`, `language_id`, `name`, `description`, `created_at`, `updated_at`) VALUES
	(1, 1, 1, 'Test Product name', 'Test product description', '2023-08-13 20:46:26', NULL),
	(2, 1, 2, 'Назва тестового товару', 'Опис тестового товару', '2023-08-13 20:47:00', NULL);

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

-- Dumping data for table ukubuka.session_data: ~0 rows (приблизно)

-- Dumping data for table ukubuka.session_user: ~5 rows (приблизно)
INSERT INTO `session_user` (`session_id`, `user_id`, `is_logged_in`) VALUES
	('6ytkdodybed83m0g33ixbflueqvfjcpb', 2, 1),
	('76w5ac55aq2dml2wq9ieztpd0yl9yd8f', 1, 1),
	('b5tgn1e71ezuw37qz1hvavzdbwcw93ml', 1, 0),
	('fjz8m2itby578dubfn17ykmafxhnfo86', 1, 1),
	('l7c5z8zw5p411m4dv2hy0kl4pcrcdz9h', 1, 1);

-- Dumping data for table ukubuka.sku: ~0 rows (приблизно)

-- Dumping data for table ukubuka.sku_price: ~0 rows (приблизно)

-- Dumping data for table ukubuka.sku_text: ~0 rows (приблизно)

-- Dumping data for table ukubuka.stock: ~0 rows (приблизно)

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

-- Dumping data for table ukubuka.user: ~2 rows (приблизно)
INSERT INTO `user` (`id`, `email`, `first_name`, `last_name`, `is_blocked`, `registered_datetime`) VALUES
	(1, 'hutei@live.com', 'Вадим', 'Гутей', 0, '2021-11-19 17:19:54'),
	(2, 'hutei2@live.com', NULL, NULL, 1, '2022-08-17 15:29:55');

-- Dumping data for table ukubuka.user_password: ~2 rows (приблизно)
INSERT INTO `user_password` (`user_id`, `password_hash`, `salt`) VALUES
	(1, 'f7fe84cf1842098524521f955fff817817afb7ea758bab950a3a82d3f25cbafb965cdde62ac8d308c614d6144ae01bd7434926643103fde9d31e6326746cbeed', 'nSRbsNDp2RZu'),
	(2, '1788d38766e84c3b120c6e66dd50ee25d5f416f27c979d773e79e109636c620d6618a67fb260f8eb3902f0dc67c8a6db95f763729f9c88bb42df9f8ff75cfbbe', 'aNotKyX8AZPw');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
