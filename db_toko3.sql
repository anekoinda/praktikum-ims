/*
SQLyog Ultimate v12.5.1 (64 bit)
MySQL - 8.0.23 : Database - db_toko3
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_toko3` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `db_toko3`;

/*Table structure for table `tb_history` */

DROP TABLE IF EXISTS `tb_history`;

CREATE TABLE `tb_history` (
  `id_history` int NOT NULL AUTO_INCREMENT,
  `id_transaksi` int DEFAULT NULL,
  `rekening` varchar(30) DEFAULT NULL,
  `tanggal` datetime DEFAULT NULL,
  `total` int DEFAULT NULL,
  `status` enum('not paid','paid') DEFAULT NULL,
  `action` enum('insert','update','delete') DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `sumber` enum('toko','bank') DEFAULT NULL,
  PRIMARY KEY (`id_history`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `tb_history` */

insert  into `tb_history`(`id_history`,`id_transaksi`,`rekening`,`tanggal`,`total`,`status`,`action`,`created_at`,`sumber`) values 
(1,1,'22222','2021-04-15 17:01:09',111,'not paid','insert','2021-04-15 09:13:49',NULL),
(2,2,'22222','2021-04-15 17:01:09',111,'not paid','insert','2021-04-15 09:14:24',NULL),
(3,3,'22222','2021-04-15 17:01:09',111,'not paid','insert','2021-04-15 09:14:57',NULL),
(4,4,'22222','2021-04-15 17:01:09',111,'not paid','insert','2021-04-15 09:15:48',NULL),
(5,3,'22222','2021-04-15 17:01:09',111,'not paid','delete','2021-04-15 09:15:56',NULL),
(6,1,'111','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 09:15:56',NULL),
(7,2,'111','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 09:15:57',NULL),
(8,4,'5555','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 09:16:31',NULL),
(9,4,'22222','2021-04-15 17:01:09',111,'paid','update','2021-04-15 09:16:32',NULL),
(10,4,'5555','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 09:16:46',NULL),
(11,4,'22222','2021-04-15 17:01:09',111,'paid','update','2021-04-15 09:16:50',NULL),
(12,4,'5555','2021-04-15 17:01:09',111,'paid','update','2021-04-15 09:16:58',NULL),
(13,4,'888888','2021-04-15 17:01:09',111,'paid','update','2021-04-15 09:22:57',NULL),
(14,4,'777777','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 09:23:34',NULL),
(15,4,'888888','2021-04-15 17:01:09',111,'paid','update','2021-04-15 09:23:40',NULL),
(16,4,'777777','2021-04-15 17:01:09',111,'paid','update','2021-04-15 09:23:46',NULL),
(17,5,'22222','2021-04-15 17:01:09',111,'not paid','insert','2021-04-15 09:31:31',NULL),
(18,4,'22222','2021-04-15 17:01:09',111,'not paid','delete','2021-04-15 09:32:31',NULL),
(19,6,'1111','2021-04-15 17:34:42',111,'not paid','insert','2021-04-15 09:34:59',NULL),
(20,7,'1111','2021-04-15 17:35:28',111,'not paid','insert','2021-04-15 09:35:38',NULL),
(21,8,'22222','2021-04-15 17:01:09',111,'not paid','insert','2021-04-15 09:35:51',NULL),
(22,9,'22222','2021-04-15 17:01:09',111,'not paid','insert','2021-04-15 09:36:04',NULL),
(23,10,'22222','2021-04-15 17:01:09',111,'not paid','insert','2021-04-15 09:36:58',NULL),
(24,8,'22222','2021-04-15 17:01:09',111,'not paid','delete','2021-04-15 09:37:13',NULL),
(25,6,'222','2021-04-15 17:34:42',111,'not paid','update','2021-04-15 09:37:14',NULL),
(26,7,'222','2021-04-15 17:35:28',111,'not paid','update','2021-04-15 09:37:14',NULL),
(31,11,'22222','2021-04-15 17:01:09',111,'not paid','insert','2021-04-15 09:43:50',NULL),
(32,1,'22222','2021-04-15 17:01:09',111,'not paid','delete','2021-04-15 09:43:50',NULL),
(33,2,'99999','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 09:43:52',NULL),
(34,5,'99999','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 09:43:53',NULL),
(35,12,'22222','2021-04-15 17:01:09',111,'not paid','insert','2021-04-15 09:45:33',NULL),
(36,2,'22222','2021-04-15 17:01:09',111,'not paid','delete','2021-04-15 09:45:34',NULL),
(37,5,'77777777','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 09:45:36',NULL),
(38,6,'77777777','2021-04-15 17:34:42',111,'not paid','update','2021-04-15 09:45:36',NULL),
(39,12,'1111111111','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 09:46:11',NULL),
(40,12,'22222','2021-04-15 17:01:09',111,'paid','update','2021-04-15 09:46:36',NULL),
(41,12,'1111111111','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 09:46:47',NULL),
(42,12,'1111111111','2021-04-15 17:01:09',111,'paid','update','2021-04-15 09:47:09',NULL),
(43,13,'7777777777','2021-04-15 17:51:03',22222,'not paid','insert','2021-04-15 09:51:25',NULL),
(44,5,'22222','2021-04-15 17:01:09',111,'not paid','delete','2021-04-15 09:51:26',NULL),
(45,7,'111','2021-04-15 17:35:28',111,'not paid','update','2021-04-15 09:51:28',NULL),
(46,9,'111','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 09:51:28',NULL),
(47,13,'7777777777','2021-04-15 17:51:03',22222,'paid','update','2021-04-15 09:57:36',NULL),
(48,13,'111','2021-04-15 17:51:03',22222,'not paid','update','2021-04-15 09:57:43',NULL),
(49,13,'7777777777','2021-04-15 17:51:03',22222,'paid','update','2021-04-15 09:58:09',NULL),
(50,13,'111','2021-04-15 17:51:03',22222,'paid','update','2021-04-15 09:58:18',NULL),
(51,14,'111','2021-04-15 18:01:49',111,'not paid','insert','2021-04-15 10:02:18','toko'),
(52,9,'111','2021-04-15 17:01:09',111,'paid','update','2021-04-15 10:03:24','bank'),
(53,14,'111','2021-04-15 18:01:49',111,'paid','update','2021-04-15 10:03:24','bank'),
(54,14,'111','2021-04-15 18:01:49',111,'not paid','update','2021-04-15 10:06:45','bank'),
(55,14,'222','2021-04-15 18:01:49',111,'paid','update','2021-04-15 10:06:48','toko'),
(56,14,'111','2021-04-15 18:01:49',111,'not paid','update','2021-04-15 10:07:17','bank'),
(57,14,'222','2021-04-15 18:01:49',111,'paid','update','2021-04-15 10:07:23','toko'),
(58,14,'222','2021-04-15 18:01:49',111,'not paid','update','2021-04-15 10:07:50','bank'),
(59,15,'22222','2021-04-15 17:01:09',111,'not paid','insert','2021-04-15 10:14:12','toko'),
(60,6,'1111','2021-04-15 17:34:42',111,'not paid','delete','2021-04-15 10:14:13','toko'),
(61,12,'8989898','2021-04-15 17:01:09',111,'paid','update','2021-04-15 10:14:16','toko'),
(62,13,'8989898','2021-04-15 17:51:03',22222,'paid','update','2021-04-15 10:14:51','toko'),
(63,10,'22222','2021-04-15 17:01:09',111,'paid','update','2021-04-15 10:15:51','bank'),
(64,10,'111111111111111','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 10:16:02','toko'),
(65,10,'22222','2021-04-15 17:01:09',111,'paid','update','2021-04-15 10:17:41','bank'),
(66,10,'111111111111111','2021-04-15 17:01:09',111,'paid','update','2021-04-15 10:17:51','toko'),
(67,14,'222','2021-04-15 18:01:49',111,'not paid','update','2021-04-15 10:26:33','bank'),
(68,14,'222','2021-04-15 18:01:49',111,'not paid','update','2021-04-15 10:28:12','bank'),
(69,14,'222','2021-04-15 18:01:49',111,'not paid','update','2021-04-15 10:28:45','bank'),
(70,14,'222','2021-04-15 18:01:49',111,'not paid','update','2021-04-15 10:29:18','bank'),
(71,14,'222','2021-04-15 18:01:49',111,'not paid','update','2021-04-15 10:29:51','bank'),
(72,14,'222','2021-04-15 18:01:49',111,'not paid','update','2021-04-15 10:30:03','bank'),
(73,14,'222','2021-04-15 18:01:49',111,'not paid','update','2021-04-15 10:30:36','bank'),
(74,14,'222','2021-04-15 18:01:49',111,'not paid','update','2021-04-15 10:31:09','bank'),
(75,14,'222','2021-04-15 18:01:49',111,'not paid','update','2021-04-15 10:31:42','bank'),
(76,14,'222','2021-04-15 18:01:49',111,'not paid','update','2021-04-15 10:32:15','bank'),
(77,16,'11111','2021-04-15 18:36:14',11111,'not paid','insert','2021-04-15 10:36:45','toko'),
(78,10,'111111111111111','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 10:36:47','bank'),
(79,10,'151515151','2021-04-15 17:01:09',111,'paid','update','2021-04-15 10:36:50','toko'),
(80,10,'111111111111111','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 10:37:21','bank'),
(81,10,'151515151','2021-04-15 17:01:09',111,'paid','update','2021-04-15 10:37:26','toko'),
(82,10,'151515151','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 10:37:54','bank'),
(83,16,'11111','2021-04-15 18:36:14',11111,'paid','update','2021-04-15 10:43:48','bank'),
(84,16,'122221','2021-04-15 18:36:14',11111,'not paid','update','2021-04-15 10:43:55','toko'),
(85,16,'11111','2021-04-15 18:36:14',11111,'paid','update','2021-04-15 10:44:22','bank'),
(86,16,'122221','2021-04-15 18:36:14',11111,'not paid','update','2021-04-15 10:44:33','toko'),
(87,16,'122221','2021-04-15 18:36:14',11111,'paid','update','2021-04-15 10:44:55','bank'),
(88,15,'90909090','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 10:50:53','toko'),
(89,15,'22222','2021-04-15 17:01:09',111,'paid','update','2021-04-15 10:50:59','bank'),
(90,15,'90909090','2021-04-15 17:01:09',111,'not paid','update','2021-04-15 10:51:31','toko'),
(91,15,'22222','2021-04-15 17:01:09',111,'paid','update','2021-04-15 10:51:32','bank'),
(92,15,'90909090','2021-04-15 17:01:09',111,'paid','update','2021-04-15 10:52:09','toko'),
(93,14,'808080808080808080800','2021-04-15 18:01:49',111,'not paid','update','2021-04-15 10:56:24','toko'),
(94,14,'222','2021-04-15 18:01:49',111,'paid','update','2021-04-15 10:56:46','bank'),
(95,14,'808080808080808080800','2021-04-15 18:01:49',111,'not paid','update','2021-04-15 10:57:02','toko'),
(96,14,'808080808080808080800','2021-04-15 18:01:49',111,'paid','update','2021-04-15 10:57:20','bank'),
(97,11,'22222','2021-04-15 17:01:09',111,'paid','update','2021-04-15 10:58:37','bank'),
(98,11,'111111111000000000','2021-04-15 17:01:09',111,'paid','update','2021-04-15 10:58:45','toko'),
(99,20,'22222','2021-04-15 17:01:09',111,'not paid','insert','2021-04-15 11:01:21','toko'),
(100,16,'11111','2021-04-15 18:36:14',11111,'not paid','delete','2021-04-15 11:01:26','toko'),
(101,7,'1111111111111222222222','2021-04-15 17:35:28',111,'not paid','update','2021-04-15 11:01:28','toko'),
(102,9,'1111111111111111222222','2021-04-15 17:01:09',111,'paid','update','2021-04-15 11:01:28','toko'),
(103,21,'2222','2021-04-15 19:04:28',1111,'not paid','insert','2021-04-15 11:04:56','toko'),
(104,20,'22222','2021-04-15 17:01:09',111,'not paid','delete','2021-04-15 11:05:02','toko'),
(105,14,'1111','2021-04-15 18:01:49',111,'paid','update','2021-04-15 11:05:03','toko'),
(106,15,'1111','2021-04-15 17:01:09',111,'paid','update','2021-04-15 11:05:04','toko'),
(107,7,'1111','2021-04-15 17:35:28',111,'not paid','delete','2021-04-15 11:13:40','toko'),
(108,14,'222221111','2021-04-15 18:01:49',111,'not paid','update','2021-04-15 11:13:46','toko'),
(109,15,'222221111','2021-04-15 17:01:09',111,'paid','update','2021-04-15 11:13:47','toko'),
(110,14,'222221111','2021-04-15 18:01:49',111,'paid','update','2021-04-15 11:14:13','bank'),
(111,25,'1111','2021-04-15 19:16:23',1111,'not paid','insert','2021-04-15 11:16:54','toko'),
(112,9,'22222','2021-04-15 17:01:09',111,'not paid','delete','2021-04-15 11:16:56','toko'),
(113,15,'33333','2021-04-15 17:01:09',111,'paid','update','2021-04-15 11:17:01','toko'),
(114,21,'33333','2021-04-15 19:04:28',1111,'not paid','update','2021-04-15 11:17:02','toko'),
(115,26,'22222','2021-04-15 17:01:09',111,'not paid','insert','2021-04-15 11:20:30','toko'),
(116,21,'2222','2021-04-15 19:04:28',1111,'not paid','delete','2021-04-15 11:20:37','toko'),
(117,15,'212121212','2021-04-15 17:01:09',111,'paid','update','2021-04-15 11:20:38','toko'),
(118,25,'212121212','2021-04-15 19:16:23',1111,'not paid','update','2021-04-15 11:20:39','toko'),
(119,27,'1111','2021-04-15 19:26:48',11111,'not paid','insert','2021-04-15 11:27:15','toko'),
(120,26,'22222','2021-04-15 17:01:09',111,'not paid','delete','2021-04-15 11:27:23','toko'),
(121,11,'2222222222333333333','2021-04-15 17:01:09',111,'paid','update','2021-04-15 11:27:23','toko'),
(122,12,'2222222222333333333','2021-04-15 17:01:09',111,'paid','update','2021-04-15 11:27:23','toko'),
(123,28,'22222','2021-04-15 17:01:09',111,'not paid','insert','2021-04-15 11:30:49','toko'),
(124,29,'111','2021-04-15 19:41:38',111,'not paid','insert','2021-04-15 11:42:00','toko'),
(125,28,'22222','2021-04-15 17:01:09',111,'not paid','delete','2021-04-15 11:42:09','toko'),
(126,25,'2222','2021-04-15 19:16:23',1111,'not paid','update','2021-04-15 11:42:09','toko'),
(127,27,'2222','2021-04-15 19:26:48',11111,'not paid','update','2021-04-15 11:42:10','toko');

/*Table structure for table `tb_transaksi` */

DROP TABLE IF EXISTS `tb_transaksi`;

CREATE TABLE `tb_transaksi` (
  `id_transaksi` int NOT NULL,
  `rekening` varchar(30) DEFAULT NULL,
  `tanggal` datetime DEFAULT NULL,
  `total` int DEFAULT NULL,
  `status` enum('not paid','paid') DEFAULT NULL,
  PRIMARY KEY (`id_transaksi`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `tb_transaksi` */

insert  into `tb_transaksi`(`id_transaksi`,`rekening`,`tanggal`,`total`,`status`) values 
(10,'151515151','2021-04-15 17:01:09',111,'not paid'),
(11,'2222222222333333333','2021-04-15 17:01:09',111,'paid'),
(12,'2222222222333333333','2021-04-15 17:01:09',111,'paid'),
(13,'8989898','2021-04-15 17:51:03',22222,'paid'),
(14,'222221111','2021-04-15 18:01:49',111,'not paid'),
(15,'212121212','2021-04-15 17:01:09',111,'paid'),
(25,'2222','2021-04-15 19:16:23',1111,'not paid'),
(27,'2222','2021-04-15 19:26:48',11111,'not paid'),
(29,'111','2021-04-15 19:41:38',111,'not paid');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
