-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: python13_bolotov_tenirberdi
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `actions`
--

DROP TABLE IF EXISTS `actions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_storage` int NOT NULL,
  `operation` varchar(60) NOT NULL,
  `id_counterparties` int NOT NULL,
  `action_date` datetime NOT NULL,
  `id_product` int NOT NULL,
  `amount` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `actions_fk0` (`id_storage`),
  KEY `actions_fk1` (`id_counterparties`),
  KEY `actions_fk2` (`id_product`),
  CONSTRAINT `actions_fk0` FOREIGN KEY (`id_storage`) REFERENCES `storage` (`id`),
  CONSTRAINT `actions_fk1` FOREIGN KEY (`id_counterparties`) REFERENCES `counterparties` (`id`),
  CONSTRAINT `actions_fk2` FOREIGN KEY (`id_product`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actions`
--

LOCK TABLES `actions` WRITE;
/*!40000 ALTER TABLE `actions` DISABLE KEYS */;
INSERT INTO `actions` VALUES (1,1,'coming',1,'2020-01-01 00:00:00',1,10),(2,1,'coming',3,'2019-08-01 00:00:00',2,45),(3,2,'coming',4,'2019-08-01 00:00:00',3,30),(4,1,'coming',1,'2020-01-11 00:00:00',4,10),(5,3,'leaving',1,'2020-09-01 00:00:00',5,-20),(6,1,'coming',4,'2020-01-01 00:00:00',6,50),(7,1,'coming',1,'2019-01-01 00:00:00',1,10),(8,2,'leaving',1,'2020-01-12 00:00:00',2,-15),(9,3,'coming',2,'2019-12-01 00:00:00',5,30),(10,1,'coming',4,'2020-01-01 00:00:00',4,30),(11,2,'coming',1,'2020-11-01 00:00:00',5,10),(12,1,'coming',1,'2019-01-01 00:00:00',6,12),(13,2,'leaving',4,'2020-07-01 00:00:00',1,-16),(14,2,'coming',1,'2020-10-01 00:00:00',2,5),(15,1,'coming',5,'2020-01-04 00:00:00',3,10),(16,3,'coming',1,'2019-01-02 00:00:00',4,10),(17,1,'coming',2,'2020-01-01 00:00:00',5,15),(18,3,'coming',1,'2019-09-01 00:00:00',6,9),(19,1,'coming',2,'2020-01-03 00:00:00',7,10),(20,1,'leaving',2,'2020-01-01 00:00:00',2,-20),(21,1,'leaving',2,'2021-11-21 00:00:00',4,-5),(22,3,'leaving',2,'2020-01-01 00:00:00',2,-20),(26,4,'transfer',20,'2020-01-01 00:00:00',3,10),(27,4,'transfer',21,'2020-01-01 00:00:00',2,15),(28,4,'transfer',20,'2020-01-01 00:00:00',1,20),(29,4,'transfer',20,'2020-01-01 00:00:00',3,10),(30,4,'transfer',19,'2020-01-01 00:00:00',2,10),(31,4,'transfer',20,'2020-01-01 00:00:00',3,30),(32,4,'transfer',20,'2020-01-01 00:00:00',3,10);
/*!40000 ALTER TABLE `actions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brand`
--

DROP TABLE IF EXISTS `brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brand` (
  `id` int NOT NULL AUTO_INCREMENT,
  `brand` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand`
--

LOCK TABLES `brand` WRITE;
/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
INSERT INTO `brand` VALUES (1,'brand1'),(2,'brand2'),(3,'brand3'),(4,'brand4'),(5,'brand5'),(6,'brand1'),(7,'brand2'),(8,'brand3'),(9,'brand4'),(10,'brand5'),(11,'brand1'),(12,'brand2'),(13,'brand3'),(14,'brand4'),(15,'brand5');
/*!40000 ALTER TABLE `brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'category'),(2,'category2'),(3,'category3'),(4,'category4'),(5,'category5'),(6,'category'),(7,'category2'),(8,'category3'),(9,'category4'),(10,'category5'),(11,'category'),(12,'category2'),(13,'category3'),(14,'category4'),(15,'category5');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `counterparties`
--

DROP TABLE IF EXISTS `counterparties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `counterparties` (
  `id` int NOT NULL AUTO_INCREMENT,
  `contractor` varchar(40) NOT NULL,
  `id_storage` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `counterparties_fk0` (`id_storage`),
  CONSTRAINT `counterparties_fk0` FOREIGN KEY (`id_storage`) REFERENCES `storage` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `counterparties`
--

LOCK TABLES `counterparties` WRITE;
/*!40000 ALTER TABLE `counterparties` DISABLE KEYS */;
INSERT INTO `counterparties` VALUES (1,'contractor1',NULL),(2,'contractor2',NULL),(3,'contractor3',NULL),(4,'contractor4',NULL),(5,'contractor5',NULL),(6,'contractor6',NULL),(19,'storage1',1),(20,'storage2',2),(21,'storage3',3);
/*!40000 ALTER TABLE `counterparties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product` varchar(60) NOT NULL,
  `id_category` int NOT NULL,
  `id_brand` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `products_fk0` (`id_category`),
  KEY `products_fk1` (`id_brand`),
  CONSTRAINT `products_fk0` FOREIGN KEY (`id_category`) REFERENCES `category` (`id`),
  CONSTRAINT `products_fk1` FOREIGN KEY (`id_brand`) REFERENCES `brand` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'product1',3,2),(2,'product2',1,4),(3,'product3',1,3),(4,'product4',5,1),(5,'product5',5,2),(6,'product6',3,2),(7,'product7',2,3),(8,'product8',2,5),(9,'product1',3,2),(10,'product2',1,4),(11,'product3',1,3),(12,'product4',5,1),(13,'product5',5,2),(14,'product6',3,2),(15,'product7',2,3),(16,'product8',2,5),(17,'product1',3,2),(18,'product2',1,4),(19,'product3',1,3),(20,'product4',5,1),(21,'product5',5,2),(22,'product6',3,2),(23,'product7',2,3),(24,'product8',2,5);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storage`
--

DROP TABLE IF EXISTS `storage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storage` (
  `id` int NOT NULL AUTO_INCREMENT,
  `address` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storage`
--

LOCK TABLES `storage` WRITE;
/*!40000 ALTER TABLE `storage` DISABLE KEYS */;
INSERT INTO `storage` VALUES (1,'address1'),(2,'address2'),(3,'address3'),(4,'address4'),(5,'address5'),(6,'address6'),(7,'address1'),(8,'address2'),(9,'address3'),(10,'address4'),(11,'address5'),(12,'address6'),(13,'address1'),(14,'address2'),(15,'address3'),(16,'address4'),(17,'address5'),(18,'address6');
/*!40000 ALTER TABLE `storage` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-17 17:00:53
