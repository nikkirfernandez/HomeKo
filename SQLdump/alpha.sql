-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: homeko
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

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
-- Table structure for table `additionalinfo`
--

DROP TABLE IF EXISTS `additionalinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `additionalinfo` (
  `additionalInfoID` int(11) NOT NULL AUTO_INCREMENT,
  `additionalInfoName` varchar(70) NOT NULL,
  `additionalInfoType` int(11) NOT NULL,
  PRIMARY KEY (`additionalInfoID`),
  KEY `infoType` (`additionalInfoType`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `additionalinfo`
--

LOCK TABLES `additionalinfo` WRITE;
/*!40000 ALTER TABLE `additionalinfo` DISABLE KEYS */;
INSERT INTO `additionalinfo` VALUES (13,'Telephone',1),(14,'Gym',2),(15,'Laundry Area',2),(16,'Curfew',3),(17,'Balcony',2);
/*!40000 ALTER TABLE `additionalinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `area`
--

DROP TABLE IF EXISTS `area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `area` (
  `areaID` int(11) NOT NULL AUTO_INCREMENT,
  `areaName` varchar(30) NOT NULL,
  PRIMARY KEY (`areaID`),
  KEY `areaName` (`areaName`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area`
--

LOCK TABLES `area` WRITE;
/*!40000 ALTER TABLE `area` DISABLE KEYS */;
INSERT INTO `area` VALUES (10,'Area 1'),(11,'Area 2');
/*!40000 ALTER TABLE `area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (2,'pbkdf2_sha256$120000$DYwlrCPxD4Oa$tPE190UMrVdyWLsy5zxQQ3g/AZN3B6GWbmaVmEadzdk=','2019-04-21 14:48:25.506793',1,'crkasilag','','','crkasilag@up.edu.ph',1,1,'2019-03-21 08:00:00.585561'),(3,'pbkdf2_sha256$120000$USt8LYIxNdMy$QCJNVxXZ0ymWNq30vQVR57Ekhg6Aoij5hjs37GJnPXs=','2019-04-21 14:45:46.313893',0,'edgarfelizmenio','Edgar','Felizmenio','123@123.com',0,1,'2019-04-21 14:44:34.064880');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact`
--

DROP TABLE IF EXISTS `contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contact` (
  `contactID` int(11) NOT NULL AUTO_INCREMENT,
  `contactNo` varchar(11) NOT NULL,
  `ownerID` int(11) NOT NULL,
  PRIMARY KEY (`contactID`),
  KEY `ownerID_idx` (`ownerID`),
  CONSTRAINT `ownerID` FOREIGN KEY (`ownerID`) REFERENCES `owner` (`ownerID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact`
--

LOCK TABLES `contact` WRITE;
/*!40000 ALTER TABLE `contact` DISABLE KEYS */;
INSERT INTO `contact` VALUES (5,'09669388244',4),(6,'09123456755',5),(7,'09000000000',6),(8,'099999999',7);
/*!40000 ALTER TABLE `contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('eh442tn2873vzr08degz9yvgfrcnhkp7','ODE2Y2U5NWMxMzE2YWE5ZmRiNGFjMGYwYTgyNTdiOTVjMTllN2I5Nzp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4NWI0NzRkOWI5YjE4MjZkZjkxNzg1MjAyYzEzOWNjODgyMDdlZGRhIn0=','2019-04-04 08:02:11.368480'),('qqhdytak6qj6xh8128nb0q8k8r4gihf9','NjA4ZjgxMDAzMWJlODViMTEzOWE5NDE4MTA1MTRjNzhlYjM5ZDM3OTp7InNlYXJjaFJlc3VsdCI6WzExLDEyXSwiX2F1dGhfdXNlcl9pZCI6IjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6Ijg1YjQ3NGQ5YjliMTgyNmRmOTE3ODUyMDJjMTM5Y2M4ODIwN2VkZGEifQ==','2019-05-05 14:49:11.891957');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback` (
  `feedbackID` int(11) NOT NULL AUTO_INCREMENT,
  `housingID` int(11) NOT NULL,
  `comment` varchar(500) NOT NULL,
  `status` int(11) NOT NULL,
  `datePosted` date NOT NULL,
  PRIMARY KEY (`feedbackID`),
  KEY `status` (`status`),
  KEY `housingID_idx` (`housingID`),
  CONSTRAINT `housingID` FOREIGN KEY (`housingID`) REFERENCES `housing` (`housingID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (9,11,'Gym too few equipments',2,'2019-04-21'),(10,11,'Room # 3 is pretty decent for its price, very large.',2,'2019-04-21'),(11,11,'Very Accomodating Seller, item shipped quickly',3,'2019-04-21'),(12,12,'Awkward yung name ng rooms.',1,'2019-04-21'),(13,12,'di totoo na may gym, forever under construction',2,'2019-04-21');
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `houseType`
--

DROP TABLE IF EXISTS `houseType`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `houseType` (
  `houseTypeID` int(11) NOT NULL AUTO_INCREMENT,
  `houseTypeName` varchar(20) NOT NULL,
  PRIMARY KEY (`houseTypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `houseType`
--

LOCK TABLES `houseType` WRITE;
/*!40000 ALTER TABLE `houseType` DISABLE KEYS */;
INSERT INTO `houseType` VALUES (1,'Apartment'),(2,'Shared Room'),(3,'Entire House');
/*!40000 ALTER TABLE `houseType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `housetype`
--

DROP TABLE IF EXISTS `housetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `housetype` (
  `houseTypeID` int(11) NOT NULL AUTO_INCREMENT,
  `houseTypeName` varchar(20) NOT NULL,
  PRIMARY KEY (`houseTypeID`),
  KEY `typeName` (`houseTypeName`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `housetype`
--

LOCK TABLES `housetype` WRITE;
/*!40000 ALTER TABLE `housetype` DISABLE KEYS */;
INSERT INTO `housetype` VALUES (4,'DummyHouseType1'),(5,'DummyHouseType2');
/*!40000 ALTER TABLE `housetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `housing`
--

DROP TABLE IF EXISTS `housing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `housing` (
  `housingID` int(11) NOT NULL AUTO_INCREMENT,
  `housingName` varchar(50) NOT NULL,
  `area` int(11) NOT NULL,
  `address` varchar(80) NOT NULL,
  `propertyType` int(11) NOT NULL,
  `houseType` int(11) NOT NULL,
  `mapHTML` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`housingID`),
  KEY `propertyType_idx` (`propertyType`),
  KEY `houseType_idx` (`houseType`),
  KEY `area_idx` (`area`),
  KEY `housingName` (`housingName`),
  CONSTRAINT `area` FOREIGN KEY (`area`) REFERENCES `area` (`areaID`),
  CONSTRAINT `houseType` FOREIGN KEY (`houseType`) REFERENCES `housetype` (`houseTypeID`),
  CONSTRAINT `propertyType` FOREIGN KEY (`propertyType`) REFERENCES `propertytype` (`propertyTypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `housing`
--

LOCK TABLES `housing` WRITE;
/*!40000 ALTER TABLE `housing` DISABLE KEYS */;
INSERT INTO `housing` VALUES (11,'DummyHouse1',10,'Street #5',3,4,''),(12,'DummyHouse2',11,'Street # 10',4,5,'');
/*!40000 ALTER TABLE `housing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `housingadditionalinfo`
--

DROP TABLE IF EXISTS `housingadditionalinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `housingadditionalinfo` (
  `housingAdditionalInfoID` int(11) NOT NULL AUTO_INCREMENT,
  `additionalInfoID` int(11) NOT NULL,
  `description` varchar(300) DEFAULT NULL,
  `housingID` int(11) NOT NULL,
  PRIMARY KEY (`housingAdditionalInfoID`),
  KEY `additionalInfoID_idx` (`additionalInfoID`),
  KEY `housingID_idx` (`housingID`),
  CONSTRAINT `additionalinfoid2` FOREIGN KEY (`additionalInfoID`) REFERENCES `additionalinfo` (`additionalInfoID`),
  CONSTRAINT `housingid2` FOREIGN KEY (`housingID`) REFERENCES `housing` (`housingID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `housingadditionalinfo`
--

LOCK TABLES `housingadditionalinfo` WRITE;
/*!40000 ALTER TABLE `housingadditionalinfo` DISABLE KEYS */;
INSERT INTO `housingadditionalinfo` VALUES (10,14,'Open 10AM-9PM',11),(11,16,'11PM',11),(12,16,'10PM',12),(13,13,'10 pesos per minute',11),(14,17,'8 sqm',11),(15,14,'Under Construction',12),(16,15,'Washing Machines Available for rent',12);
/*!40000 ALTER TABLE `housingadditionalinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `housingowner`
--

DROP TABLE IF EXISTS `housingowner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `housingowner` (
  `housingOwnerID` int(11) NOT NULL AUTO_INCREMENT,
  `housingID` int(11) NOT NULL,
  `ownerID` int(11) NOT NULL,
  PRIMARY KEY (`housingOwnerID`),
  KEY `housingID_idx` (`housingID`),
  KEY `ownerID_idx` (`ownerID`),
  CONSTRAINT `housingid3` FOREIGN KEY (`housingID`) REFERENCES `housing` (`housingID`),
  CONSTRAINT `ownerid2` FOREIGN KEY (`ownerID`) REFERENCES `owner` (`ownerID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `housingowner`
--

LOCK TABLES `housingowner` WRITE;
/*!40000 ALTER TABLE `housingowner` DISABLE KEYS */;
INSERT INTO `housingowner` VALUES (3,11,4),(4,12,5);
/*!40000 ALTER TABLE `housingowner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `housingrequest`
--

DROP TABLE IF EXISTS `housingrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `housingrequest` (
  `housingRequestID` int(11) NOT NULL AUTO_INCREMENT,
  `requestID` int(11) NOT NULL,
  `housingID` int(11) NOT NULL,
  PRIMARY KEY (`housingRequestID`),
  KEY `requestID_idx` (`requestID`),
  KEY `housingID_idx` (`housingID`),
  CONSTRAINT `housingid4` FOREIGN KEY (`housingID`) REFERENCES `housing` (`housingID`),
  CONSTRAINT `requestid` FOREIGN KEY (`requestID`) REFERENCES `request` (`requestID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `housingrequest`
--

LOCK TABLES `housingrequest` WRITE;
/*!40000 ALTER TABLE `housingrequest` DISABLE KEYS */;
INSERT INTO `housingrequest` VALUES (1,3,11),(2,2,12);
/*!40000 ALTER TABLE `housingrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `owner`
--

DROP TABLE IF EXISTS `owner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `owner` (
  `ownerID` int(11) NOT NULL AUTO_INCREMENT,
  `ownerName` varchar(70) NOT NULL,
  `firstName` varchar(40) NOT NULL,
  `lastName` varchar(40) NOT NULL,
  `email` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`ownerID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `owner`
--

LOCK TABLES `owner` WRITE;
/*!40000 ALTER TABLE `owner` DISABLE KEYS */;
INSERT INTO `owner` VALUES (4,'pczuniga','Phillip Christian','Zuniga','someemail@somesite.com'),(5,'razuniga','Rose Anne','Zuniga','emailnimamz@homeko.com'),(6,'wmtan','Wilson','Tan','emailnisirwilson@site.com'),(7,'edgarfelizmenio','Edgar','Felizmenio','123@123.com');
/*!40000 ALTER TABLE `owner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `picture`
--

DROP TABLE IF EXISTS `picture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `picture` (
  `pictureID` int(11) NOT NULL AUTO_INCREMENT,
  `fileName` varchar(30) NOT NULL,
  `housingID` int(11) NOT NULL,
  PRIMARY KEY (`pictureID`),
  KEY `housingID_idx` (`housingID`),
  CONSTRAINT `housingid5` FOREIGN KEY (`housingID`) REFERENCES `housing` (`housingID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picture`
--

LOCK TABLES `picture` WRITE;
/*!40000 ALTER TABLE `picture` DISABLE KEYS */;
INSERT INTO `picture` VALUES (1,'something.png',11);
/*!40000 ALTER TABLE `picture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `propertyType`
--

DROP TABLE IF EXISTS `propertyType`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `propertyType` (
  `propertyTypeID` int(11) NOT NULL AUTO_INCREMENT,
  `propertyTypeName` varchar(20) NOT NULL,
  PRIMARY KEY (`propertyTypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `propertyType`
--

LOCK TABLES `propertyType` WRITE;
/*!40000 ALTER TABLE `propertyType` DISABLE KEYS */;
INSERT INTO `propertyType` VALUES (1,'tentative'),(2,'House');
/*!40000 ALTER TABLE `propertyType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `propertytype`
--

DROP TABLE IF EXISTS `propertytype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `propertytype` (
  `propertyTypeID` int(11) NOT NULL AUTO_INCREMENT,
  `propertyTypeName` varchar(20) NOT NULL,
  PRIMARY KEY (`propertyTypeID`),
  KEY `typeName` (`propertyTypeName`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `propertytype`
--

LOCK TABLES `propertytype` WRITE;
/*!40000 ALTER TABLE `propertytype` DISABLE KEYS */;
INSERT INTO `propertytype` VALUES (3,'DummyPropertyType1'),(4,'DummyPropertyType2');
/*!40000 ALTER TABLE `propertytype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request`
--

DROP TABLE IF EXISTS `request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `request` (
  `requestID` int(11) NOT NULL AUTO_INCREMENT,
  `type` int(11) NOT NULL,
  `message` varchar(500) NOT NULL,
  `status` int(11) NOT NULL,
  `dateSent` date NOT NULL,
  `sender` varchar(50) NOT NULL,
  PRIMARY KEY (`requestID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request`
--

LOCK TABLES `request` WRITE;
/*!40000 ALTER TABLE `request` DISABLE KEYS */;
INSERT INTO `request` VALUES (1,1,'Malingap St.\r\n\r\nContact No: 09xxxxxxxxxx',2,'2019-04-21','someuser@somesite.com'),(2,2,'Superman Room DummyHouse2 price adjusted to 8000',2,'2019-04-21','something@something.com'),(3,3,'Room # 3 DummyHouse1 is temporarily unavailable',2,'2019-04-21','something@something.com');
/*!40000 ALTER TABLE `request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roomcost`
--

DROP TABLE IF EXISTS `roomcost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roomcost` (
  `roomID` int(11) NOT NULL AUTO_INCREMENT,
  `roomName` varchar(100) NOT NULL,
  `cost` float NOT NULL,
  `housingID` int(11) NOT NULL,
  PRIMARY KEY (`roomID`),
  KEY `housingid6_idx` (`housingID`),
  CONSTRAINT `housingid6` FOREIGN KEY (`housingID`) REFERENCES `housing` (`housingID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roomcost`
--

LOCK TABLES `roomcost` WRITE;
/*!40000 ALTER TABLE `roomcost` DISABLE KEYS */;
INSERT INTO `roomcost` VALUES (6,'Room # 1',3000,11),(7,'Room # 2',3000,11),(8,'Room # 3',4500,11),(9,'Flash',2500,12),(10,'Superman',6000,12),(11,'Batman',4000,12),(12,'Wonder Woman',6500,12);
/*!40000 ALTER TABLE `roomcost` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-22  4:49:23
