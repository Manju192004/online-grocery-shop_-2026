CREATE DATABASE  IF NOT EXISTS `homedb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `homedb`;
-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: homedb
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` text DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (10,'Breakfast Cereals','Breakfast Cereals','breakfast_cereals.jpg'),(11,'Instant Food','Instant Food','a8cbf851-33ee-4fb6-b1c8-7e49088488e8-InstantFoods.jpg'),(12,'Bread','Bread','245e6bbf-a296-4c1a-8c00-64bb9ccfaa26-BreadJam.jpg'),(13,'Edible oil','Edible oil','download.jfif'),(14,'Flour','Flour','images.jfif'),(15,'Cereals','Cereals','download.jfif'),(16,'Masalas ','Masalas ','f87319bc-4808-4d35-9dd2-226033122411-masalaSpices.jpg'),(17,'Rice Products','Rice Products','a98919e2-a014-47ca-b434-437ff4acfd77-riceproducts.jpg'),(18,'Diary Products','Diary Products','219873a9-52a9-44e6-9ce1-3665ab8c75f5-DairyProducts.jpg'),(19,'Fryums','Fryums','download_1.jpg'),(20,'Stationery','Stationery','download.jfif');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `content`
--

DROP TABLE IF EXISTS `content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Phone` varchar(20) DEFAULT NULL,
  `Role` varchar(50) DEFAULT 'User',
  PRIMARY KEY (`id`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content`
--

LOCK TABLES `content` WRITE;
/*!40000 ALTER TABLE `content` DISABLE KEYS */;
INSERT INTO `content` VALUES (1,'Admin User','admin@gmail.com','admin123',NULL,'Admin'),(3,'Manju seenivasan','manjuseenivasan07@gmail.com','admin123','9780654321','User'),(13,'Manju seenivasan','manjuseenivasan09@gmail.com','mmmmm','9780654321','User'),(15,'Manju seenivasan','manjuseenivasan08@gmail.com','mmmmm','9780654321','User'),(16,'Manju seenivasan','manjuseenivasan10@gmail.com','mmmmm','9780654321','User'),(17,'Akshaya Mayakannan','manju@gmail.com','123','9876543210','User'),(19,'thara shree','thara@gmail.com','123','9876543210','User'),(22,'shanmathy shanmathy','shan@gmail.com','12345','9087987654','User'),(23,'aru mugan','aru@gmail.com','123456','9942203285','User'),(25,'New Admin','newadmin@gmail.com','admin','1111111111','User'),(26,'Test User','testuser@gmail.com','Password123!','1234567890','User'),(28,'Test User','test@gmail.com','test','1112223333','User'),(29,'Test User','test@example.com','Password123','1234567890','User'),(31,'Admin User','admin2@gmail.com','root','9876543210','User');
/*!40000 ALTER TABLE `content` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contents`
--

DROP TABLE IF EXISTS `contents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contents` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Phone` varchar(20) DEFAULT NULL,
  `Role` varchar(50) DEFAULT 'User',
  PRIMARY KEY (`id`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contents`
--

LOCK TABLES `contents` WRITE;
/*!40000 ALTER TABLE `contents` DISABLE KEYS */;
INSERT INTO `contents` VALUES (1,'Admin User','admin@gmail.com','admin123',NULL,'Admin');
/*!40000 ALTER TABLE `contents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `database`
--

DROP TABLE IF EXISTS `database`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `database` (
  `iddatabase` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `database`
--

LOCK TABLES `database` WRITE;
/*!40000 ALTER TABLE `database` DISABLE KEYS */;
/*!40000 ALTER TABLE `database` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `rating` varchar(50) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `submitted_at` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `feedback_ibfk_2` (`product_id`),
  CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `content` (`id`),
  CONSTRAINT `feedback_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (1,NULL,NULL,'1-Terrible','          nottt good  ','2026-02-04 07:24:14'),(2,NULL,NULL,'5-Excellent','              good','2026-02-04 07:32:11'),(15,16,NULL,'5','good','2026-02-04 10:48:00'),(16,16,NULL,'5','good','2026-02-04 10:48:11'),(17,16,NULL,'5','good','2026-02-04 10:59:09'),(18,16,NULL,'3','not good','2026-02-04 10:59:58'),(26,19,NULL,'5','good','2026-02-09 06:48:55'),(27,19,NULL,'3','bad','2026-02-09 07:02:26'),(28,19,NULL,'5','good','2026-02-09 07:39:54'),(29,19,NULL,'4','Customer Happy.......','2026-02-09 07:42:10'),(30,19,NULL,'5','wow','2026-02-09 07:45:39'),(31,19,NULL,'4','not bad','2026-02-09 08:30:33'),(41,17,51,'4','good','2026-03-30 08:37:48');
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` varchar(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `item_name` varchar(255) NOT NULL,
  `qty` float DEFAULT 1,
  `total_price` decimal(10,2) NOT NULL,
  `order_date` timestamp NULL DEFAULT current_timestamp(),
  `status` varchar(50) DEFAULT 'Pending',
  `customer_name` varchar(255) DEFAULT NULL,
  `customer_email` varchar(255) DEFAULT NULL,
  `customer_phone` varchar(20) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `payment_method` varchar(50) DEFAULT NULL,
  `order_trace` varchar(100) DEFAULT 'Order Placed',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'#INV-6116',19,'chilli',1,15.00,'2026-02-09 08:33:29','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(2,'#INV-8621',19,'biscuits',1,10.00,'2026-02-09 08:34:36','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(3,'#INV-8622',19,'Chips',1,10.00,'2026-02-09 08:44:00','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(4,'#INV-6710',23,'Tomato',1,20.00,'2026-02-09 09:36:11','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(5,'#INV-1759',17,'Potato',1,10.00,'2026-02-10 17:19:37','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(6,'#INV-8941',17,'Brinjal',1,20.00,'2026-02-14 09:27:33','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(7,'#INV-8941',17,'Brinjal',1,20.00,'2026-02-14 09:27:33','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(8,'#INV-8941',17,'Capsicum',2,30.00,'2026-02-14 09:27:33','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(9,'#INV-8353',17,'Brinjal',1,20.00,'2026-02-14 09:40:02','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(10,'#INV-8353',17,'chilli',1,15.00,'2026-02-14 09:40:02','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(11,'#INV-8353',17,'chilli',1,15.00,'2026-02-14 09:42:37','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(12,'#INV-8353',17,'Brinjal',1,20.00,'2026-02-14 09:42:37','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(13,'#INV-7726',17,'Brinjal',1,20.00,'2026-02-20 10:19:03','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(14,'#INV-7726',17,'Drumstick',1,10.00,'2026-02-20 10:19:03','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(15,'#INV-1488',17,'Cocount',1,10.00,'2026-02-21 05:30:05','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(16,'#INV-1488',17,'Drumstick',1,10.00,'2026-02-21 05:30:05','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(17,'#INV-3060',17,'Drumstick',1,10.00,'2026-02-21 05:41:51','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(18,'#INV-3060',17,'chilli',1,15.00,'2026-02-21 05:41:51','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(19,'#INV-4066',17,'Tomato',1,20.00,'2026-02-21 05:52:12','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(20,'#INV-4066',17,'chilli',1,15.00,'2026-02-21 05:52:12','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(21,'#INV-4066',17,'Brinjal',1,20.00,'2026-02-21 05:52:12','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(22,'#INV-5411',17,'Tomato',1,20.00,'2026-02-21 05:53:03','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(23,'#INV-2433',17,'Onion',1,10.00,'2026-02-21 05:53:39','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(24,'#INV-8310',17,'Tomato',1,20.00,'2026-03-15 16:09:04','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(25,'#INV-8310',17,'Potato',2,20.00,'2026-03-15 16:09:04','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(26,'#INV-8310',17,'Brinjal',1,20.00,'2026-03-15 16:09:04','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(27,'#INV-8310',17,'Tomato',1,20.00,'2026-03-15 16:09:05','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(28,'#INV-8310',17,'Brinjal',1,20.00,'2026-03-15 16:09:05','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(29,'#INV-8310',17,'Tomato',1,20.00,'2026-03-15 16:09:05','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(30,'#INV-9900',17,'Brinjal',1,20.00,'2026-03-16 08:00:13','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(31,'#INV-1167',17,'Potato',1,10.00,'2026-03-16 08:08:17','Pending',NULL,NULL,NULL,NULL,NULL,'Order Placed'),(32,'#INV-6427',1,'Brinjal',1,20.00,'2026-03-16 09:50:05','Pending','Manju','ajay@gmail.com','+919942203285','murukan kuruchi 1/201','UPI','Order Placed'),(33,'#INV-6427',1,'Drumstick',1,10.00,'2026-03-16 09:50:05','Pending','Manju','ajay@gmail.com','+919942203285','murukan kuruchi 1/201','UPI','Order Placed'),(34,'#INV-6427',1,'Brinjal',1,20.00,'2026-03-16 09:50:05','Pending','Manju','ajay@gmail.com','+919942203285','murukan kuruchi 1/201','UPI','Order Placed'),(35,'#INV-6427',1,'Cocount',1,10.00,'2026-03-16 09:50:06','Pending','Manju','ajay@gmail.com','+919942203285','murukan kuruchi 1/201','UPI','Order Placed'),(36,'#INV-7055',17,'Brinjal',1,20.00,'2026-03-16 09:58:05','Pending','Manju192004','manjuseenivasan2004@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(37,'#INV-3500',17,'Potato',1,10.00,'2026-03-16 11:04:09','Pending','Manju','manjuseenivasan2004@gmail.com','9487184056','madurai','COD','Order Placed'),(38,'#INV-9829',17,'Brinjal',1,20.00,'2026-03-16 11:21:13','Pending','Manju','manjuseenivasan2004@gmail.com','9487184056','chennai','COD','Order Placed'),(39,'#INV-3980',17,'Tomato',1,20.00,'2026-03-18 05:56:23','Pending','Manju','manjuseenivasan07@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(40,'#INV-9647',17,'Potato',1,10.00,'2026-03-18 07:10:54','Pending','Manju192004','manjuseenivasan2004@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(41,'#INV-9943',17,'Brinjal',1,20.00,'2026-03-18 07:15:07','Pending','Manju192004','manjuseenivasan2004@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(42,'#INV-5983',17,'Brinjal',1,20.00,'2026-03-18 07:42:01','Pending','Manju','manjuseenivasan07@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(43,'#INV-7520',17,'Brinjal',1,20.00,'2026-03-18 07:55:54','Delivered','Manju','manjuseenivasan07@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(44,'#INV-7122',17,'chilli',1,15.00,'2026-03-18 08:00:17','Pending','Manju','manjuseenivasan07@gmail.com','9487184056','murukan kuruchi 1/201','COD','Order Placed'),(45,'#INV-7122',17,'Tomato',1,20.00,'2026-03-18 08:00:17','Pending','Manju','manjuseenivasan07@gmail.com','9487184056','murukan kuruchi 1/201','COD','Order Placed'),(46,'#INV-7122',17,'Brinjal',1,20.00,'2026-03-18 08:00:17','Pending','Manju','manjuseenivasan07@gmail.com','9487184056','murukan kuruchi 1/201','COD','Order Placed'),(47,'#INV-7630',17,'chilli',1,15.00,'2026-03-18 08:00:53','Pending','Manju','manjuseenivasan07@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(48,'#INV-7630',17,'Tomato',1,20.00,'2026-03-18 08:00:54','Pending','Manju','manjuseenivasan07@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(49,'#INV-7630',17,'Brinjal',1,20.00,'2026-03-18 08:00:54','Pending','Manju','manjuseenivasan07@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(50,'#INV-6240',17,'Potato',1,10.00,'2026-03-18 09:00:29','Shipped','Manju192004','manjuseenivasan2004@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(51,'#INV-5712',17,'Brinjal',1,20.00,'2026-03-20 09:12:03','Delivered','Manikandaaa','manjuseenivasan07@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(52,'#INV-1478',17,'Brinjal',1,20.00,'2026-03-23 07:06:25','Delivered','Manju192004','manjuseenivasan2004@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(53,'#INV-5801',17,'chocolate',1,10.00,'2026-03-23 07:48:21','Delivered','Manju192004','manjuseenivasan2004@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(54,'#INV-7937',17,'Tomato',1,20.00,'2026-03-23 08:27:19','Delivered','Manju192004','manjuseenivasan2004@gmail.com','6379716355','murukan kuruchi 1/201','UPI','Order Placed'),(55,'#INV-5134',17,'Brinjal',1,20.00,'2026-03-23 08:28:25','Delivered','Manju192004','manjuseenivasan2004@gmail.com','6379754716','murukan kuruchi 1/201','UPI','Order Placed'),(56,'#INV-2654',29,'chilli',1,15.00,'2026-03-23 10:09:37','Delivered','Test User','test@example.com','1234567890','123 Test Street, Test City, 123456','COD','Order Placed'),(57,'#FM-1672',17,'chilli',1,15.00,'2026-03-23 17:14:23','Delivered','Manju192004','manjuseenivasan2004@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(58,'#FM-4069',1,'Cocount',1,10.00,'2026-03-24 13:38:06','Delivered','Manju192004','manjuseenivasan2004@gmail.com','9487184056','murukan kuruchi 1/201','COD','Order Placed'),(59,'#INV-2840',17,'Brinjal',1,20.00,'2026-03-26 05:01:07','Ordered','ajay','ajay@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(60,'#INV-2840',17,'Onion',4,40.00,'2026-03-26 05:01:07','Ordered','ajay','ajay@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(61,'#INV-2840',17,'Note',1,20.00,'2026-03-26 05:01:07','Ordered','ajay','ajay@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed'),(62,'#INV-2840',17,'chocolate',1,10.00,'2026-03-26 05:01:07','Shipped','ajay','ajay@gmail.com','9487184056','murukan kuruchi 1/201','UPI','Order Placed');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  `quantity` float DEFAULT 0,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `image` varchar(255) DEFAULT NULL,
  `restock_level` int(11) DEFAULT 10,
  `unit` varchar(10) DEFAULT 'pcs',
  `original_price` decimal(10,2) DEFAULT NULL,
  `description` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (38,'Kelloggs Chocos','Breakfast Cereals',19,100,'2026-03-30 07:07:12','choco_crunchs.jpg',10,'1 Kg',20.00,'Kelloggs Chocos offers a great range of breakfast items which offer perfect health and taste. Kelloggs Chocos is ideal for children who tend to skip their breakfast due to monotony.'),(39,'Kelloggs Corn Flakes Original ₹53.35 ₹','Breakfast Cereals',53,50,'2026-03-30 07:08:44','kellogs_corn_flakes.jpg',10,'1 Kg',55.00,'Corn flakes is one of the healthiest breakfast, as it is rich with the essential ingredients and a high nutritional value.Kellogg\'s Corn Flakes Original & The Best Breakfast Cereals, is enriched with Iron, Vitamin B and C. It doesn\'t contain any cholesterol or preservatives.'),(40,'Lion Australian Oats Refill','Breakfast Cereals',49,80,'2026-03-30 07:10:18','lion_oats.jpg',10,'200gram ',50.00,'Lion Australian Oats Refill this vegetarian australian oats weighing 1.25 kilograms in total. The shelf life of this product is 9 months.'),(41,'Nestle Munch','Breakfast Cereals',75,80,'2026-03-30 07:12:14','munch.jpeg',10,'200 gram',80.00,'nestle munch offers a great range of breakfast items which offer perfect health and taste. nestle munch  is ideal for children who tend to skip their breakfast due to monotony.'),(42,'Aachi Hyderabadi Biriyani Paste','Instant Food',75,100,'2026-03-30 07:16:23','3b3afd61-ec22-4dd4-885c-85a5a513c5ac-AachiHyderabadiBiryaniMasalaPaste177gm.jpg',50,'100 gram',80.00,'\r\nAachi hyderabadi biryani paste description\r\n\r\n\r\nAI Mode\r\nAll\r\nImages\r\nVideos\r\nForums\r\nShort videos\r\nWeb\r\nMore\r\nTools\r\nAI Overview\r\nAachi Hyderabadi Biryani Masala Paste is a ready-to-use, aromatic spice blend designed to replicate authentic Hyderabadi-style biryani at home. It combines traditional spices like coriander, cardamom, cinnamon, and cloves with chili for a savory, aromatic profile. It offers a convenient, \"sweat-free\" cooking experience for both vegetarian and non-vegetarian dishes.'),(43,'Asal Half Cooked Chapathi ','Instant Food',38,200,'2026-03-30 07:18:02','0cee7fdc-879c-47ef-a966-893601b92ea2-4870.jpg',80,'10 piece',47.00,'These chapatis are indian breads very similar to tortillas. They are a must with any indian meal. Complete a chicken, fish, or vegetarian dish with fresh chapati or eat it by itself. From the moment you open these freshly made chapatis, your mouth will water.\r\n'),(44,'Harima Choco Chips  ','Instant Food',107,100,'2026-03-30 07:22:13','Harima_Choco_Chips_100gm_1588.jpg',60,'100 gm',120.00,'Harima Choco Chips can be used to make choco chip cookies, cakes, and ice creams. They are often available in a round, flat-bottomed and teardrop shape. Choco chips should be stored in a cool and dry place in an air-tight container. '),(45,'Haiku Sweet Bread','Bread',48,100,'2026-03-30 07:23:57','a9c31b08-d259-4cc9-b17f-11ab198e8b42-22.jpg',70,'350 gm',50.00,'Haiku Sweet Breadis one of life\'s greatest pleasures. Our breads are made using the finest ingredients. We make this bread extra special, so we hope you will enjoy eating it as much as we enjoyed baking it.  Its enriched with vitamins required for healthy living. Perfect for any homemade preparation.'),(46,'Kissan Peanut Butter ','Bread',44,100,'2026-03-30 07:25:56','90f60882-13e3-474d-ab64-67bedce7fff1-14879.jpg',70,'100 gm',45.00,'A Fruity Jam For A Scrumptious Breakfast. If you\'re looking out for a delicious and fruity jam to spread across your toast every morning,.'),(47,'Haiku Milk Bread ','Bread',44,150,'2026-03-30 07:27:33','f14f183e-a93a-4909-9423-f57921540808-21.jpg',80,'350 gm',50.00,'Haiku Milk Breadis baked twice to give it crispiness. It is a popular companion with your Tea/coffee. Finest ingredients are used to make it extra crispy, tasty and healthy.'),(48,'Fortune Sunlite Refined Sunflower Oil Pouch ','Edible oil',187,500,'2026-03-30 07:31:14','Fortune_Sunlite_Refined_Sunflower_Oil_1ltr_3183.jpg',300,'1 litre',190.00,'Fortune Sunlite Refined Sunflower Oil is made from the finest of the seeds. Sunflower oil has a strong aroma and flavour which helps to stimulate your appetite. This sunflower oil is used in every household from decades. Fortune Sunlite Refined Sunflower Oil delivers the best taste and come in very handy packages so you can store them in your kitchen in a dry and cool place. They add great taste to pickles and preserve them for a very long time. Cooking oil is light, healthy and easy to use. It can be used for cooking as well as seasoning.'),(49,'777 Gingelly Oil ₹','Edible oil',159,400,'2026-03-30 07:32:30','855f26e7-fcc3-4aac-b534-fa28feb07ac0-250.jpg',250,'500 ml',189.00,'777 Gingelly Oil is a type of oil that is extracted from sesame seed. It is uses include cooking, applying on the body and hair for nourishment as well as for performing puja ceremonies in many Indian households.'),(50,'Roobini Refined Palmolein Oil  ','Edible oil',145,500,'2026-03-30 07:34:48','roobini_refined_palmolein_oil_1ltr.jpg',200,'1 litr',170.00,'Roobini refined palmolein oil presents its finest quality of palm oil through the refined palmolein oil. Cholesterol free, trans fat free, healthy palmolein oil and cost effective, with excellent oxidative properties. An important feature of this oil is that it is neutral in taste and flavour and stable at high temperature. It is good for shallow as well as deep frying as it has moderate linoleic acid content and high level of natural antioxidants which gives it a high smoke point. Its natural property enables reuse without affecting the quality of the food.'),(51,'Anil Rice Flour','Flour',38,100,'2026-03-30 07:38:00','a44cf0bd-64c4-4eb8-8204-d064bd77caeb-anil_rice_flour_500gm.jpg',80,'500 gm',39.00,'Rice has been the staple food of India since historical times. A variant form of this rice is the ground form of it which can be stored for long durations and used to make instant recipes. Rice is first roasted or dried to remove any moisture in it and then ground into a fine powder as the rice flour. This flour can be used to make many recipes like kozhukattai, puttu, idiyappam etc.'),(52,'Aachi Puttu Powder ₹46.1 ₹48','Flour',46,100,'2026-03-30 07:39:23','aachi_puttu_powder_500gm.jpg',60,'500gm',48.00,'Aachi puttu podi is prepared from selected white rice. The steamed puttu is processed under hygienic condition with gmp standards. Very soft texture. Only needs 3-5 minutes for steaming.'),(53,'Aashirvaad Atta','Flour',72,500,'2026-03-30 07:40:47','aashirvaad_select_whole_wheat_atta_5kg.jpg',100,'1 Kg',74.00,'Aashirvaad select whole wheat atta is made from 100 percent naturally growned wheat. Here the golden fields are sun kissed to perfection and showered by the right amount of rain. This is why each grain has a golden sheen and is heavier in feel. Aashirvaad select whole wheat atta is prepared to give you the finest, softest and fluffiest rotis you have ever tasted. The best of nature with every bite.'),(54,'Krishna Kozhakkate Idiyappam Flour','Flour',69,200,'2026-03-30 07:41:56','krishna_kozhakkate_idiyappam_flour_500gm.jpg',80,'1 Kg',72.00,'Idiyappam is made with red rice powder. They can be steamed with the help of a puttu maker or a pressure cooker and can be made into thick rice tubes which can be used in any south indian delicacy.'),(55,'Krishna Ragi Puttu Podi','Flour',75,500,'2026-03-30 07:43:16','krishna_ragi_puttu_podi_500gm.jpg',200,'500g',78.00,'Ragi puttu podi is prepared from carefully graded de- stoned ragi which is a superior supply of fiber. Ragi has low glycemic index which makes it digest especially slowly thus keeping the blood sugar levels steady. Ragi is wealthy in numerous minerals such as thiamine, iron and calcium and has sufficient amino acids.'),(56,'Sakthi Chicken Masala ₹₹31','Masalas ',29,800,'2026-03-30 07:45:39','5c2e535d-9bd8-43e8-9937-7221cf046265-SakthiChickenMasala.jpg',500,'100g',31.00,'Sakthi Chicken Masala is a unique combination of pure and fresh spices. It is rich in taste and aroma. You can also use this masala to marinate chicken. Sakthi, founded in 1975, manufactures varieties of spice and masala powders, pickles, flour varieties, appalams, ghee and sunflower oil.'),(57,'Aachi Garam Masala ','Masalas ',34,500,'2026-03-30 07:46:57','aachi_garam_masala_50gm_1760.jpg',200,'50 gm',36.00,'Garam Masala is a perfect blend of fine quality spices which adds the requisite taste and flavour to your veg and nonveg dishes. Top ingredients include cumin, black cardamom, clove, coriander, black pepper, turmeric, garlic, fenugreek etc.'),(58,'  Aachi Chilli Powder','masalas',22,200,'2026-03-30 07:48:44','aachi_chilli_powder_50gm_2040.jpg',150,'50 gm',24.00,'The best quality Red Chilli is choose from the field, cleaned, powdered and packed hygienically. The packing is tamper proof that helps to increase the shelf life and keep the aroma for long time.'),(59,'Aachi Kulambu Chilly Masala','Masalas',21,500,'2026-03-30 07:49:51','aachi_kulambu_chilly_masala_100gm_2022.jpg',200,'50 gm',22.00,'Aachi Chilli Powder Kuzhambu is a ready to add masala powder that can spice up your vegetarian or non vegetarian dishes. Prepared from choicest of spices, Aachi Chilli Powder Kuzhambu brings delight to the chef and the entire family.'),(60,'Heritage Basmathi  Rice','Rice Products',79,500,'2026-03-30 07:54:08','475a0843-ed08-4082-bdc2-97996ce120e8-farmers-harvest-_-gold-basmati-rice-1-kg-pack-of-5-product-images-orvsctzgsxn-p602936403-0-202307051040_11zon-remove.png',200,'1 kg',80.00,'HeritageBasmati Rice is long slender grain has unique fragrance and flavor. It is naturally protein enriched product.'),(61,'India Gate Feast Rozzana Basmathi Rice ','Rice Products',95,800,'2026-03-30 07:55:12','india_gate_feast_rozzana_basmathi_rice_1kg.jpg',500,'1 Kg',122.00,'India gate basmathi rice brings to you natures priceless gift, original basmati rice in an affordable price. It is half of the full basmati grain and belongs to the ever popular super/pusa grains. Its delightful taste and captivating aroma will make your every meal a delicacy.'),(62,'Farmers Harvest Rice','Rice Products',75,300,'2026-03-30 07:56:34','a6f688ce-167e-44e9-bcb9-244c5d76cc54-basmati.jpg',100,'1 Kg',80.00,'India gate basmathi rice brings to you natures priceless gift, original basmati rice in an affordable price. It is half of the full basmati grain and belongs to the ever popular super/pusa grains. Its delightful taste and captivating aroma will make your every meal a delicacy.'),(63,'  Amul Butter Unsalted ','Diary Products',60,500,'2026-03-30 08:04:28','4148c0ae-04e3-4270-94f6-0af21e0e0fc1-AmulButterUnsalted.jpg',150,'100gm',61.00,'Butter is a delicious fatspread common in nearly every Indian household. Its an essential ingredient and a known taste enhancer for nearly all your cooking and baking recipes. And when its Amul Butter, none can match to its smooth, creamy, rich, irresistible taste & nutritive value.'),(64,'Milkymist Table Butter ','Diary Products',87,300,'2026-03-30 08:05:53','af8fac77-6e6f-42b4-912b-03ea224d07a1-cover_539HZ6MaIA_11zon.jpeg',100,'100 gm',90.00,'Milkymist Table Butter'),(65,'Milky Mist Butter Milk','Diary Products',19,500,'2026-03-30 08:06:57','milky_mist_butter_milk_200ml.jpg',200,'100gm',20.00,'This sour, creamy beverage is drunk in many parts of the world and is derived when cream is churned to produce butter, the milk that remains after the butter is churned is known as buttermilk. It contains no butter and is low in fat and calories making it good health. It contains many vitamins and minerals and has many health benefits. Nutrition of butter milk buttermilk is low on fats and calories.'),(66,'Mily Mist Paneer','Diary Products',90,400,'2026-03-30 08:09:18','milky_mist_paneer_200gm_4672.jpg',200,'100gm',120.00,'Milk Mist paneer.'),(67,'Cumin & Jeera Pappad','Fryums',16,100,'2026-03-30 08:13:44','29b2cce5-88cb-4aa2-91b0-4ece8ddfb085-CuminJeeraPappad.jpg',70,'100gm',20.00,'Cumin & Jeera Pappad are a crisp savory accompaniment to the traditional Indian meal. They make delicious party snacks, enliven tea times, and can be had with yoghurt as a dip or as masala papads after garnishing with coriander leaves, chopped onion, lime and chillies.'),(68,'Sago Cumin Papad ','Fryums',23,100,'2026-03-30 08:14:42','53c144ce-5a6a-4481-a2d4-afd585300ba5-SagoCuminPapad.jpg',70,'100 gm',35.00,'Sago Cumin Papad is a crisp savory accompaniment to the traditional Indian meal. They make delicious party snacks, enliven tea times'),(69,'  Bindu Dinner Special Appalam ','Fryums',99,100,'2026-03-30 08:15:38','bindu_dinner_special_appalam_200gm.jpg',80,'100 gm',150.00,'Our sema tasty bindu appalams are very delicious & tasty in nature. Papad appalam are hygienically prepared from dal, rice, potato and additional flours. We suggest striking assortment of crunchy and delicious appala'),(70,'Bat Pappad ','Fryums',13,100,'2026-03-30 08:16:30','ce35011f-f469-4926-a586-0df9e5fe5aab-BatPappad.jpg',50,'100gm',15.00,'Bat Pappad is ready to fry papad snack ideal to have with your daily meals and snacks.'),(71,'Cello My Gel Pen Blue Ink','Breakfast Cereals',31,100,'2026-03-30 08:20:33','db569bab-40aa-4f63-b8da-0e8c4a892753-40107097_4-cello-my-gel-pen-blue_11zon.jpeg',10,'1 pack',35.00,'Cello My Gel Pen Mostly Preferred By School Or College Students. These Pens Gives Smooth Hand Clear Writing Experience. Gel Pen in a wide variety of rich colour inks and invokes the artistic streak in you.');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock_in`
--

DROP TABLE IF EXISTS `stock_in`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stock_in` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `supplier_name` varchar(100) NOT NULL,
  `supplier_address` text DEFAULT NULL,
  `quantity` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `entry_date` timestamp NULL DEFAULT current_timestamp(),
  `date_added` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `stock_in_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock_in`
--

LOCK TABLES `stock_in` WRITE;
/*!40000 ALTER TABLE `stock_in` DISABLE KEYS */;
/*!40000 ALTER TABLE `stock_in` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `role` varchar(20) DEFAULT 'user',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-30 19:46:49
