-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: mysql
-- ------------------------------------------------------
-- Server version	5.7.25-google-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `workout`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `workout` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `workout`;

--
-- Table structure for table `Action`
--

DROP TABLE IF EXISTS `Action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Action` (
  `id_action` int(11) NOT NULL AUTO_INCREMENT,
  `name_action` varchar(28) NOT NULL,
  `id_category` int(11) NOT NULL,
  PRIMARY KEY (`id_action`),
  KEY `id_category` (`id_category`),
  CONSTRAINT `Action_ibfk_1` FOREIGN KEY (`id_category`) REFERENCES `category` (`id_category`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Action`
--

LOCK TABLES `Action` WRITE;
/*!40000 ALTER TABLE `Action` DISABLE KEYS */;
INSERT INTO `Action` VALUES (3,'Bench Press',2),(4,'Pectoral Flys',2),(5,'Front Raises',3),(6,'Seated Row',4),(7,'Deadlift',4),(8,'Lat Pulldowns',4),(9,'Bicep Curls',5),(10,'Hammer Curls',5),(11,'Skull Crushers',5),(12,'Overhead Tricep Extensions',5),(15,'Leg Raises',6),(35,'Figure Eights',4),(36,'Face Pulls',4),(40,'1 Minute Plank',6),(41,'High Intense Super Sets',3);
/*!40000 ALTER TABLE `Action` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `id_category` int(11) NOT NULL AUTO_INCREMENT,
  `name_category` varchar(12) NOT NULL,
  PRIMARY KEY (`id_category`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Legs'),(2,'Chest'),(3,'Shoulders'),(4,'Back'),(5,'Arms'),(6,'Abs');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workout`
--

DROP TABLE IF EXISTS `workout`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workout` (
  `id_workout` int(11) NOT NULL AUTO_INCREMENT,
  `name_workout` varchar(28) NOT NULL,
  PRIMARY KEY (`id_workout`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workout`
--

LOCK TABLES `workout` WRITE;
/*!40000 ALTER TABLE `workout` DISABLE KEYS */;
INSERT INTO `workout` VALUES (9,'Leg Day'),(10,'Early Mondays'),(24,'Back at it'),(25,'Davids Chest Day'),(26,'Syed loves the gym'),(27,'Baileys Pre Ibiza Routine'),(28,'Home Workout');
/*!40000 ALTER TABLE `workout` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workout_action`
--

DROP TABLE IF EXISTS `workout_action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workout_action` (
  `id_workout_day` int(11) NOT NULL AUTO_INCREMENT,
  `id_workout` int(11) NOT NULL,
  `id_action` int(11) NOT NULL,
  PRIMARY KEY (`id_workout_day`),
  KEY `id_workout` (`id_workout`),
  KEY `id_action` (`id_action`),
  CONSTRAINT `workout_action_ibfk_1` FOREIGN KEY (`id_workout`) REFERENCES `workout` (`id_workout`),
  CONSTRAINT `workout_action_ibfk_2` FOREIGN KEY (`id_action`) REFERENCES `Action` (`id_action`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workout_action`
--

LOCK TABLES `workout_action` WRITE;
/*!40000 ALTER TABLE `workout_action` DISABLE KEYS */;
INSERT INTO `workout_action` VALUES (39,9,4),(42,9,40),(46,26,36),(47,26,35),(48,26,3),(49,27,10),(50,27,40),(52,27,12),(53,27,4),(54,9,7),(55,27,3),(56,25,4),(57,25,8),(59,28,3),(60,28,9),(61,28,4),(62,28,10),(63,28,35),(64,28,36),(65,28,40),(66,28,41);
/*!40000 ALTER TABLE `workout_action` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-22 11:26:35
