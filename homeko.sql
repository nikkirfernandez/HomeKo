-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: homeko
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
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
 SET character_set_client = utf8 ;
CREATE TABLE `additionalinfo` (
  `additionalInfoID` int(11) NOT NULL AUTO_INCREMENT,
  `additionalInfoName` varchar(70) NOT NULL,
  `additionalInfoType` int(11) NOT NULL,
  PRIMARY KEY (`additionalInfoID`),
  KEY `infoType` (`additionalInfoType`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `additionalinfo`
--

LOCK TABLES `additionalinfo` WRITE;
/*!40000 ALTER TABLE `additionalinfo` DISABLE KEYS */;
INSERT INTO `additionalinfo` VALUES (2,'Air conditioning',1),(3,'Washer',1),(4,'Dryer',1),(5,'Wifi',1),(6,'Iron',1),(7,'TV',1),(8,'Parking',2),(9,'Pets allowed',3),(10,'Smoking allowed',3),(11,'No curfew',3),(12,'Kitchen',1);
/*!40000 ALTER TABLE `additionalinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `area`
--

DROP TABLE IF EXISTS `area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `area` (
  `areaID` int(11) NOT NULL AUTO_INCREMENT,
  `areaName` varchar(30) NOT NULL,
  PRIMARY KEY (`areaID`),
  KEY `areaName` (`areaName`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area`
--

LOCK TABLES `area` WRITE;
/*!40000 ALTER TABLE `area` DISABLE KEYS */;
INSERT INTO `area` VALUES (1,'Area 1'),(2,'Area 2'),(3,'Hardin ng Doña Aurora'),(4,'Kapitbalay ng Kalinaw'),(5,'Pook Dagohoy'),(6,'Pook Palaris'),(7,'Pook Ricarte'),(8,'Village A'),(9,'Village B');
/*!40000 ALTER TABLE `area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
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
 SET character_set_client = utf8 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
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
 SET character_set_client = utf8 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add additionalinfo',1,'add_additionalinfo'),(2,'Can change additionalinfo',1,'change_additionalinfo'),(3,'Can delete additionalinfo',1,'delete_additionalinfo'),(4,'Can view additionalinfo',1,'view_additionalinfo'),(5,'Can add area',2,'add_area'),(6,'Can change area',2,'change_area'),(7,'Can delete area',2,'delete_area'),(8,'Can view area',2,'view_area'),(9,'Can add auth group',3,'add_authgroup'),(10,'Can change auth group',3,'change_authgroup'),(11,'Can delete auth group',3,'delete_authgroup'),(12,'Can view auth group',3,'view_authgroup'),(13,'Can add auth group permissions',4,'add_authgrouppermissions'),(14,'Can change auth group permissions',4,'change_authgrouppermissions'),(15,'Can delete auth group permissions',4,'delete_authgrouppermissions'),(16,'Can view auth group permissions',4,'view_authgrouppermissions'),(17,'Can add auth permission',5,'add_authpermission'),(18,'Can change auth permission',5,'change_authpermission'),(19,'Can delete auth permission',5,'delete_authpermission'),(20,'Can view auth permission',5,'view_authpermission'),(21,'Can add auth user',6,'add_authuser'),(22,'Can change auth user',6,'change_authuser'),(23,'Can delete auth user',6,'delete_authuser'),(24,'Can view auth user',6,'view_authuser'),(25,'Can add auth user groups',7,'add_authusergroups'),(26,'Can change auth user groups',7,'change_authusergroups'),(27,'Can delete auth user groups',7,'delete_authusergroups'),(28,'Can view auth user groups',7,'view_authusergroups'),(29,'Can add auth user user permissions',8,'add_authuseruserpermissions'),(30,'Can change auth user user permissions',8,'change_authuseruserpermissions'),(31,'Can delete auth user user permissions',8,'delete_authuseruserpermissions'),(32,'Can view auth user user permissions',8,'view_authuseruserpermissions'),(33,'Can add contact',9,'add_contact'),(34,'Can change contact',9,'change_contact'),(35,'Can delete contact',9,'delete_contact'),(36,'Can view contact',9,'view_contact'),(37,'Can add django admin log',10,'add_djangoadminlog'),(38,'Can change django admin log',10,'change_djangoadminlog'),(39,'Can delete django admin log',10,'delete_djangoadminlog'),(40,'Can view django admin log',10,'view_djangoadminlog'),(41,'Can add django content type',11,'add_djangocontenttype'),(42,'Can change django content type',11,'change_djangocontenttype'),(43,'Can delete django content type',11,'delete_djangocontenttype'),(44,'Can view django content type',11,'view_djangocontenttype'),(45,'Can add django migrations',12,'add_djangomigrations'),(46,'Can change django migrations',12,'change_djangomigrations'),(47,'Can delete django migrations',12,'delete_djangomigrations'),(48,'Can view django migrations',12,'view_djangomigrations'),(49,'Can add django session',13,'add_djangosession'),(50,'Can change django session',13,'change_djangosession'),(51,'Can delete django session',13,'delete_djangosession'),(52,'Can view django session',13,'view_djangosession'),(53,'Can add feedback',14,'add_feedback'),(54,'Can change feedback',14,'change_feedback'),(55,'Can delete feedback',14,'delete_feedback'),(56,'Can view feedback',14,'view_feedback'),(57,'Can add housetype',15,'add_housetype'),(58,'Can change housetype',15,'change_housetype'),(59,'Can delete housetype',15,'delete_housetype'),(60,'Can view housetype',15,'view_housetype'),(61,'Can add housing',16,'add_housing'),(62,'Can change housing',16,'change_housing'),(63,'Can delete housing',16,'delete_housing'),(64,'Can view housing',16,'view_housing'),(65,'Can add owner',17,'add_owner'),(66,'Can change owner',17,'change_owner'),(67,'Can delete owner',17,'delete_owner'),(68,'Can view owner',17,'view_owner'),(69,'Can add propertytype',18,'add_propertytype'),(70,'Can change propertytype',18,'change_propertytype'),(71,'Can delete propertytype',18,'delete_propertytype'),(72,'Can view propertytype',18,'view_propertytype'),(73,'Can add request',19,'add_request'),(74,'Can change request',19,'change_request'),(75,'Can delete request',19,'delete_request'),(76,'Can view request',19,'view_request'),(77,'Can add log entry',20,'add_logentry'),(78,'Can change log entry',20,'change_logentry'),(79,'Can delete log entry',20,'delete_logentry'),(80,'Can view log entry',20,'view_logentry'),(81,'Can add permission',21,'add_permission'),(82,'Can change permission',21,'change_permission'),(83,'Can delete permission',21,'delete_permission'),(84,'Can view permission',21,'view_permission'),(85,'Can add group',22,'add_group'),(86,'Can change group',22,'change_group'),(87,'Can delete group',22,'delete_group'),(88,'Can view group',22,'view_group'),(89,'Can add user',23,'add_user'),(90,'Can change user',23,'change_user'),(91,'Can delete user',23,'delete_user'),(92,'Can view user',23,'view_user'),(93,'Can add content type',24,'add_contenttype'),(94,'Can change content type',24,'change_contenttype'),(95,'Can delete content type',24,'delete_contenttype'),(96,'Can view content type',24,'view_contenttype'),(97,'Can add session',25,'add_session'),(98,'Can change session',25,'change_session'),(99,'Can delete session',25,'delete_session'),(100,'Can view session',25,'view_session'),(101,'Can add housing additional info',26,'add_housingadditionalinfo'),(102,'Can change housing additional info',26,'change_housingadditionalinfo'),(103,'Can delete housing additional info',26,'delete_housingadditionalinfo'),(104,'Can view housing additional info',26,'view_housingadditionalinfo'),(105,'Can add housing owner',27,'add_housingowner'),(106,'Can change housing owner',27,'change_housingowner'),(107,'Can delete housing owner',27,'delete_housingowner'),(108,'Can view housing owner',27,'view_housingowner'),(109,'Can add housing request',28,'add_housingrequest'),(110,'Can change housing request',28,'change_housingrequest'),(111,'Can delete housing request',28,'delete_housingrequest'),(112,'Can view housing request',28,'view_housingrequest'),(113,'Can add picture',29,'add_picture'),(114,'Can change picture',29,'change_picture'),(115,'Can delete picture',29,'delete_picture'),(116,'Can view picture',29,'view_picture'),(117,'Can add room cost',30,'add_roomcost'),(118,'Can change room cost',30,'change_roomcost'),(119,'Can delete room cost',30,'delete_roomcost'),(120,'Can view room cost',30,'view_roomcost');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$n6ICjGtEw66O$HrUqWwz4OuIE8Fr6Wuo1TggZVQF5r40YdqzSI6wsuCo=','2019-02-09 02:56:06.543046',1,'nvsontillano','','','nvsontillano@up.edu.ph',1,1,'2019-02-05 08:46:39.075385');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
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
 SET character_set_client = utf8 ;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
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
 SET character_set_client = utf8 ;
CREATE TABLE `contact` (
  `contactID` int(11) NOT NULL AUTO_INCREMENT,
  `contactNo` varchar(11) NOT NULL,
  `ownerID` int(11) NOT NULL,
  PRIMARY KEY (`contactID`),
  KEY `ownerID_idx` (`ownerID`),
  CONSTRAINT `ownerID` FOREIGN KEY (`ownerID`) REFERENCES `owner` (`ownerID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact`
--

LOCK TABLES `contact` WRITE;
/*!40000 ALTER TABLE `contact` DISABLE KEYS */;
INSERT INTO `contact` VALUES (1,'09123456789',1),(2,'09821141133',1),(3,'09887124412',2),(4,'09554221444',3);
/*!40000 ALTER TABLE `contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
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
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-02-05 09:11:58.688573','1','Area object (1)',1,'[{\"added\": {}}]',2,1),(2,'2019-02-05 09:12:07.954334','2','Area object (2)',1,'[{\"added\": {}}]',2,1),(3,'2019-02-05 09:16:15.727255','3','Area object (3)',1,'[{\"added\": {}}]',2,1),(4,'2019-02-05 09:16:44.477045','4','Area object (4)',1,'[{\"added\": {}}]',2,1),(5,'2019-02-05 09:16:54.461578','5','Area object (5)',1,'[{\"added\": {}}]',2,1),(6,'2019-02-05 09:16:59.742191','6','Area object (6)',1,'[{\"added\": {}}]',2,1),(7,'2019-02-05 09:17:09.648568','7','Area object (7)',1,'[{\"added\": {}}]',2,1),(8,'2019-02-05 09:17:15.023646','8','Area object (8)',1,'[{\"added\": {}}]',2,1),(9,'2019-02-05 09:17:20.929979','9','Area object (9)',1,'[{\"added\": {}}]',2,1),(10,'2019-02-05 09:17:46.335454','1','Propertytype object (1)',1,'[{\"added\": {}}]',18,1),(11,'2019-02-05 09:17:53.444944','2','Propertytype object (2)',1,'[{\"added\": {}}]',18,1),(12,'2019-02-05 09:18:04.943793','1','Propertytype object (1)',2,'[]',18,1),(13,'2019-02-05 09:18:35.458828','1','Housetype object (1)',1,'[{\"added\": {}}]',15,1),(14,'2019-02-05 09:18:51.021550','2','Housetype object (2)',1,'[{\"added\": {}}]',15,1),(15,'2019-02-05 09:19:16.817238','3','Housetype object (3)',1,'[{\"added\": {}}]',15,1),(16,'2019-02-05 09:19:21.489195','3','Housetype object (3)',2,'[]',15,1),(17,'2019-02-05 10:45:41.758238','1','Owner object (1)',1,'[{\"added\": {}}]',17,2),(18,'2019-02-05 10:45:45.752651','1','Contact object (1)',1,'[{\"added\": {}}]',9,2),(19,'2019-02-05 10:50:06.858439','2','jcarlos - 09821141133',1,'[{\"added\": {}}]',9,2),(20,'2019-02-05 10:50:39.455565','2','nikkis',1,'[{\"added\": {}}]',17,2),(21,'2019-02-05 10:50:41.689609','3','nikkis - 09887124412',1,'[{\"added\": {}}]',9,2),(22,'2019-02-05 10:51:16.000734','3','nikkif',1,'[{\"added\": {}}]',17,2),(23,'2019-02-05 10:51:18.051311','4','nikkif - 09554221444',1,'[{\"added\": {}}]',9,2),(24,'2019-02-05 10:53:02.539156','1','Housetype object (1)',1,'[{\"added\": {}}]',15,2),(25,'2019-02-05 10:53:36.502805','1','Propertytype object (1)',1,'[{\"added\": {}}]',18,2),(26,'2019-02-05 10:53:56.526183','1','Housing object (1)',1,'[{\"added\": {}}]',16,2),(27,'2019-02-05 10:59:53.655157','2','Shared Room',1,'[{\"added\": {}}]',15,2),(28,'2019-02-05 11:00:02.668036','3','Entire House',1,'[{\"added\": {}}]',15,2),(29,'2019-02-05 11:00:43.038138','2','House',1,'[{\"added\": {}}]',18,2),(30,'2019-02-05 11:00:58.808312','2','Bahay ni Chancy',1,'[{\"added\": {}}]',16,2),(31,'2019-02-05 15:24:21.283075','1','HousingOwner object (1)',1,'[{\"added\": {}}]',27,1),(32,'2019-02-05 15:24:34.055626','2','HousingOwner object (2)',1,'[{\"added\": {}}]',27,1),(33,'2019-02-05 15:26:46.582315','1','Feedback object (1)',1,'[{\"added\": {}}]',14,1),(34,'2019-02-05 15:27:13.276063','2','Feedback object (2)',1,'[{\"added\": {}}]',14,1),(35,'2019-02-05 15:28:10.833724','3','Feedback object (3)',1,'[{\"added\": {}}]',14,1),(36,'2019-02-05 15:29:09.586689','1','Kitchen - 1',1,'[{\"added\": {}}]',1,1),(37,'2019-02-05 15:29:52.175242','2','Air conditioning - 1',1,'[{\"added\": {}}]',1,1),(38,'2019-02-05 15:29:59.987842','3','Washer - 1',1,'[{\"added\": {}}]',1,1),(39,'2019-02-05 15:30:06.661534','4','Dryer - 1',1,'[{\"added\": {}}]',1,1),(40,'2019-02-05 15:30:19.005463','5','Wifi - 1',1,'[{\"added\": {}}]',1,1),(41,'2019-02-05 15:30:32.630656','6','Iron - 1',1,'[{\"added\": {}}]',1,1),(42,'2019-02-05 15:30:39.699537','7','TV - 1',1,'[{\"added\": {}}]',1,1),(43,'2019-02-05 15:32:06.768447','8','Parking - 2',1,'[{\"added\": {}}]',1,1),(44,'2019-02-05 15:32:18.893628','9','Pets allowed - 3',1,'[{\"added\": {}}]',1,1),(45,'2019-02-05 15:32:41.815822','10','Smoking allowed - 3',1,'[{\"added\": {}}]',1,1),(46,'2019-02-05 15:32:54.956634','11','No curfew - 3',1,'[{\"added\": {}}]',1,1),(47,'2019-02-05 15:35:50.355661','1','Kitchen - 1',3,'',1,1),(49,'2019-02-05 15:38:39.770866','12','Kitchen - 1',1,'[{\"added\": {}}]',1,1),(50,'2019-02-05 15:39:06.424659','1','HousingAdditionalInfo object (1)',1,'[{\"added\": {}}]',26,1),(51,'2019-02-05 15:39:26.201536','2','HousingAdditionalInfo object (2)',1,'[{\"added\": {}}]',26,1),(52,'2019-02-05 15:40:13.916215','3','HousingAdditionalInfo object (3)',1,'[{\"added\": {}}]',26,1),(53,'2019-02-05 15:40:28.161411','4','HousingAdditionalInfo object (4)',1,'[{\"added\": {}}]',26,1),(54,'2019-02-05 15:40:55.458671','5','HousingAdditionalInfo object (5)',1,'[{\"added\": {}}]',26,1),(55,'2019-02-05 15:41:13.318499','6','HousingAdditionalInfo object (6)',1,'[{\"added\": {}}]',26,1),(56,'2019-02-05 15:41:29.035840','7','HousingAdditionalInfo object (7)',1,'[{\"added\": {}}]',26,1),(57,'2019-02-05 15:41:56.583106','8','HousingAdditionalInfo object (8)',1,'[{\"added\": {}}]',26,1),(58,'2019-02-05 15:42:18.033319','9','HousingAdditionalInfo object (9)',1,'[{\"added\": {}}]',26,1),(59,'2019-02-05 15:44:29.936720','1','RoomCost object (1)',1,'[{\"added\": {}}]',30,1),(60,'2019-02-05 15:45:05.491738','2','RoomCost object (2)',1,'[{\"added\": {}}]',30,1),(61,'2019-02-05 15:45:42.816778','3','RoomCost object (3)',1,'[{\"added\": {}}]',30,1),(62,'2019-02-05 15:46:03.160817','4','RoomCost object (4)',1,'[{\"added\": {}}]',30,1),(63,'2019-02-05 15:46:24.239385','5','RoomCost object (5)',1,'[{\"added\": {}}]',30,1),(64,'2019-02-06 20:28:59.467318','1','Bahay ni Nikki F',2,'[{\"changed\": {\"fields\": [\"maphtml\"]}}]',16,1),(65,'2019-02-06 20:32:50.555072','2','Bahay ni Chancy',2,'[]',16,1),(66,'2019-02-07 21:56:29.700923','2','Bahay ni Chancy',2,'[]',16,1),(67,'2019-02-07 21:59:37.839823','3','Yellow House',1,'[{\"added\": {}}]',16,1),(68,'2019-02-07 22:13:03.789293','3','Yellow House',3,'',16,1),(69,'2019-02-08 00:08:59.694206','4','Yellow House',1,'[{\"added\": {}}]',16,1),(70,'2019-02-08 00:09:15.210050','4','Yellow House',2,'[]',16,1),(71,'2019-02-08 00:11:21.384287','5','Orange House',1,'[{\"added\": {}}]',16,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (20,'admin','logentry'),(22,'auth','group'),(21,'auth','permission'),(23,'auth','user'),(24,'contenttypes','contenttype'),(1,'mainpage','additionalinfo'),(2,'mainpage','area'),(3,'mainpage','authgroup'),(4,'mainpage','authgrouppermissions'),(5,'mainpage','authpermission'),(6,'mainpage','authuser'),(7,'mainpage','authusergroups'),(8,'mainpage','authuseruserpermissions'),(9,'mainpage','contact'),(10,'mainpage','djangoadminlog'),(11,'mainpage','djangocontenttype'),(12,'mainpage','djangomigrations'),(13,'mainpage','djangosession'),(14,'mainpage','feedback'),(15,'mainpage','housetype'),(16,'mainpage','housing'),(26,'mainpage','housingadditionalinfo'),(27,'mainpage','housingowner'),(28,'mainpage','housingrequest'),(17,'mainpage','owner'),(29,'mainpage','picture'),(18,'mainpage','propertytype'),(19,'mainpage','request'),(30,'mainpage','roomcost'),(25,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-02-05 08:43:25.949107'),(2,'auth','0001_initial','2019-02-05 08:43:26.605349'),(3,'admin','0001_initial','2019-02-05 08:43:26.792854'),(4,'admin','0002_logentry_remove_auto_add','2019-02-05 08:43:26.808494'),(5,'admin','0003_logentry_add_action_flag_choices','2019-02-05 08:43:26.824120'),(6,'contenttypes','0002_remove_content_type_name','2019-02-05 08:43:26.917870'),(7,'auth','0002_alter_permission_name_max_length','2019-02-05 08:43:26.980360'),(8,'auth','0003_alter_user_email_max_length','2019-02-05 08:43:27.027247'),(9,'auth','0004_alter_user_username_opts','2019-02-05 08:43:27.042856'),(10,'auth','0005_alter_user_last_login_null','2019-02-05 08:43:27.089750'),(11,'auth','0006_require_contenttypes_0002','2019-02-05 08:43:27.105356'),(12,'auth','0007_alter_validators_add_error_messages','2019-02-05 08:43:27.120985'),(13,'auth','0008_alter_user_username_max_length','2019-02-05 08:43:27.183483'),(14,'auth','0009_alter_user_last_name_max_length','2019-02-05 08:43:27.245985'),(15,'mainpage','0001_initial','2019-02-05 08:43:27.277237'),(16,'sessions','0001_initial','2019-02-05 08:43:27.339736'),(17,'mainpage','0002_auto_20190205_2312','2019-02-05 15:12:12.570928');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('nynj8ce2hnbkz2a63433tpv9ymgrw3ey','MDZkZGY1ZWM0OWIzNzZjYTA1ZWI4MzBmMmJjNTdiMDIxZTA4NzkyMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNTIyYWI3MWQ4ZGUxNDVlYTg2MzhmZGFlNDA1MGE4NjU2OWEzYzYxIn0=','2019-02-19 08:47:16.294578'),('rifn8b243t5dpvze9or8gvsl9s82cscc','MWY2MDUzOGZjOTMxYTNkNzg1M2IzOGMwMjM5YmY2ZjAwMzdlNDU5ZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNTIyYWI3MWQ4ZGUxNDVlYTg2MzhmZGFlNDA1MGE4NjU2OWEzYzYxIiwic2VhcmNoUmVzdWx0IjpbMSwyLDQsNSw2LDcsOSwxMF19','2019-03-20 16:30:28.494398');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (1,1,'mabait yung landlady',2,'2019-02-05'),(2,2,'ganda dito',2,'2019-02-05'),(3,1,'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin auctor quis risus sit amet blandit. Suspendisse id dui at ligula feugiat laoreet. Donec mi turpis, malesuada quis fermentum dignissim, mollis non sapien. Phasellus sit amet ligula ac elit pharetra mollis vel nec ante. Duis vitae scelerisque metus, id commodo velit.',2,'2019-02-05'),(4,6,'hello',1,'2019-03-03'),(5,6,'hello',1,'2019-03-03'),(6,6,'hello',1,'2019-03-03'),(7,6,'help',1,'2019-03-03'),(8,6,'kajsndkhjeb',1,'2019-03-03');
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `housetype`
--

DROP TABLE IF EXISTS `housetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `housetype` (
  `houseTypeID` int(11) NOT NULL AUTO_INCREMENT,
  `houseTypeName` varchar(20) NOT NULL,
  PRIMARY KEY (`houseTypeID`),
  KEY `typeName` (`houseTypeName`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `housetype`
--

LOCK TABLES `housetype` WRITE;
/*!40000 ALTER TABLE `housetype` DISABLE KEYS */;
INSERT INTO `housetype` VALUES (1,'Entire place'),(2,'Private room'),(3,'Shared room');
/*!40000 ALTER TABLE `housetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `housing`
--

DROP TABLE IF EXISTS `housing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `housing`
--

LOCK TABLES `housing` WRITE;
/*!40000 ALTER TABLE `housing` DISABLE KEYS */;
INSERT INTO `housing` VALUES (1,'Bahay ni Nikki F',6,'2nd St.',1,2,'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3859.9385911281083!2d121.07119751435769!3d14.659426389765029!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3397b75dfef56eb3%3A0x83cbae2de31e220a!2sIlang+Ilang+Residence+Hall!5e0!3m2!1sen!2sph!4v1549024344251'),(2,'Bahay ni Chancy',7,'Unang kanto',2,3,NULL),(4,'Yellow House',1,'3 asdfl street',2,2,NULL),(5,'Orange House',1,'werty',2,1,NULL),(6,'new house',5,'1st street',1,3,NULL),(7,'new house 2',4,'2nd street',2,2,''),(9,'new house 3',2,'3rd street',1,2,''),(10,'sharpie yeyyyy',3,'445th corner',1,2,'');
/*!40000 ALTER TABLE `housing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `housingadditionalinfo`
--

DROP TABLE IF EXISTS `housingadditionalinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `housingadditionalinfo`
--

LOCK TABLES `housingadditionalinfo` WRITE;
/*!40000 ALTER TABLE `housingadditionalinfo` DISABLE KEYS */;
INSERT INTO `housingadditionalinfo` VALUES (1,12,'di kumpleto ang gamit',1),(2,7,'agawan kayo sa TV',1),(3,5,'medyo mabilis ang wifi',1),(4,11,NULL,1),(5,3,'unlimited use',2),(6,6,'unlimited use',2),(7,5,NULL,2),(8,8,NULL,2),(9,9,'max of 2 pets per person',2);
/*!40000 ALTER TABLE `housingadditionalinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `housingowner`
--

DROP TABLE IF EXISTS `housingowner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `housingowner` (
  `housingOwnerID` int(11) NOT NULL AUTO_INCREMENT,
  `housingID` int(11) NOT NULL,
  `ownerID` int(11) NOT NULL,
  PRIMARY KEY (`housingOwnerID`),
  KEY `housingID_idx` (`housingID`),
  KEY `ownerID_idx` (`ownerID`),
  CONSTRAINT `housingid3` FOREIGN KEY (`housingID`) REFERENCES `housing` (`housingID`),
  CONSTRAINT `ownerid2` FOREIGN KEY (`ownerID`) REFERENCES `owner` (`ownerID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `housingowner`
--

LOCK TABLES `housingowner` WRITE;
/*!40000 ALTER TABLE `housingowner` DISABLE KEYS */;
INSERT INTO `housingowner` VALUES (1,1,3),(2,2,1);
/*!40000 ALTER TABLE `housingowner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `housingrequest`
--

DROP TABLE IF EXISTS `housingrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `housingrequest` (
  `housingRequestID` int(11) NOT NULL AUTO_INCREMENT,
  `requestID` int(11) NOT NULL,
  `housingID` int(11) NOT NULL,
  PRIMARY KEY (`housingRequestID`),
  KEY `requestID_idx` (`requestID`),
  KEY `housingID_idx` (`housingID`),
  CONSTRAINT `housingid4` FOREIGN KEY (`housingID`) REFERENCES `housing` (`housingID`),
  CONSTRAINT `requestid` FOREIGN KEY (`requestID`) REFERENCES `request` (`requestID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `housingrequest`
--

LOCK TABLES `housingrequest` WRITE;
/*!40000 ALTER TABLE `housingrequest` DISABLE KEYS */;
/*!40000 ALTER TABLE `housingrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `owner`
--

DROP TABLE IF EXISTS `owner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `owner` (
  `ownerID` int(11) NOT NULL AUTO_INCREMENT,
  `ownerName` varchar(70) NOT NULL,
  `firstName` varchar(40) NOT NULL,
  `lastName` varchar(40) NOT NULL,
  `email` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`ownerID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `owner`
--

LOCK TABLES `owner` WRITE;
/*!40000 ALTER TABLE `owner` DISABLE KEYS */;
INSERT INTO `owner` VALUES (1,'jcarlos','Jose','Carlos','josecarlos@websitenijose.com'),(2,'nikkis','Nicole','Sontillano','nicoles@coolwebsite.ph'),(3,'nikkif','Nikki','Fernandez','nikkif@somepetgroomingsite.com');
/*!40000 ALTER TABLE `owner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `picture`
--

DROP TABLE IF EXISTS `picture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `picture` (
  `pictureID` int(11) NOT NULL AUTO_INCREMENT,
  `fileName` varchar(30) NOT NULL,
  `housingID` int(11) NOT NULL,
  PRIMARY KEY (`pictureID`),
  KEY `housingID_idx` (`housingID`),
  CONSTRAINT `housingid5` FOREIGN KEY (`housingID`) REFERENCES `housing` (`housingID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `picture`
--

LOCK TABLES `picture` WRITE;
/*!40000 ALTER TABLE `picture` DISABLE KEYS */;
/*!40000 ALTER TABLE `picture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `propertytype`
--

DROP TABLE IF EXISTS `propertytype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `propertytype` (
  `propertyTypeID` int(11) NOT NULL AUTO_INCREMENT,
  `propertyTypeName` varchar(20) NOT NULL,
  PRIMARY KEY (`propertyTypeID`),
  KEY `typeName` (`propertyTypeName`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `propertytype`
--

LOCK TABLES `propertytype` WRITE;
/*!40000 ALTER TABLE `propertytype` DISABLE KEYS */;
INSERT INTO `propertytype` VALUES (2,'Apartment'),(1,'House');
/*!40000 ALTER TABLE `propertytype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request`
--

DROP TABLE IF EXISTS `request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `request` (
  `requestID` int(11) NOT NULL AUTO_INCREMENT,
  `type` int(11) NOT NULL,
  `message` varchar(500) NOT NULL,
  `status` int(11) NOT NULL,
  `dateSent` date NOT NULL,
  `sender` varchar(50) NOT NULL,
  PRIMARY KEY (`requestID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request`
--

LOCK TABLES `request` WRITE;
/*!40000 ALTER TABLE `request` DISABLE KEYS */;
/*!40000 ALTER TABLE `request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roomcost`
--

DROP TABLE IF EXISTS `roomcost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8 ;
CREATE TABLE `roomcost` (
  `roomID` int(11) NOT NULL AUTO_INCREMENT,
  `roomName` varchar(100) NOT NULL,
  `cost` float NOT NULL,
  `housingID` int(11) NOT NULL,
  PRIMARY KEY (`roomID`),
  KEY `housingid6_idx` (`housingID`),
  CONSTRAINT `housingid6` FOREIGN KEY (`housingID`) REFERENCES `housing` (`housingID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roomcost`
--

LOCK TABLES `roomcost` WRITE;
/*!40000 ALTER TABLE `roomcost` DISABLE KEYS */;
INSERT INTO `roomcost` VALUES (1,'Room 1',8000,1),(2,'Rooms 2-5',5000,1),(3,'Rooms A and B',13000,2),(4,'Rooms C and D',12000,2),(5,'Rooms E and F',10000,2);
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

-- Dump completed on 2019-03-07  1:23:42
