-- MySQL dump 10.13  Distrib 8.0.19, for osx10.14 (x86_64)
--
-- Host: localhost    Database: blogapp
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blogpost`
--

DROP TABLE IF EXISTS `blogpost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blogpost` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `author` varchar(50) DEFAULT NULL,
  `body` text,
  `blog_img` varchar(50) NOT NULL,
  `pub_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogpost`
--

LOCK TABLES `blogpost` WRITE;
/*!40000 ALTER TABLE `blogpost` DISABLE KEYS */;
INSERT INTO `blogpost` VALUES (1,'Blog','svthapa','<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Cursus risus at ultrices mi tempus. Enim nunc faucibus a pellentesque sit amet porttitor eget dolor. Donec pretium vulputate sapien nec. Nisi est sit amet facilisis magna etiam tempor. Lobortis feugiat vivamus at augue eget arcu. Bibendum enim facilisis gravida neque convallis a cras semper. Ac felis donec et odio pellentesque diam volutpat. Ultrices sagittis orci a scelerisque purus semper eget duis. Sed lectus vestibulum mattis ullamcorper velit sed ullamcorper morbi tincidunt. Quis commodo odio aenean sed adipiscing diam donec adipiscing tristique. Sollicitudin tempor id eu nisl nunc mi ipsum faucibus. Blandit volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque.123</p>\r\n\r\n<p>&nbsp;</p>\r\n','IMG_2443.JPG','2020-04-13 01:18:49'),(2,'Vietnam My Love!','sneupane','<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.hello1234</p>\r\n','vietnam.jpg','2020-04-13 04:52:29');
/*!40000 ALTER TABLE `blogpost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` mediumint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(25) DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `register_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Saurav Neupane','saurav@gmail.com','sneupane','$5$rounds=535000$PXuaT.YvebBlPcF1$zcJFWEjea0Gvld3OFUEiYMwwCSx7iu8slj.eYbacJ71','2020-04-10 04:27:23'),(2,'Samrajya Thapa','samrajya@gmail.com','svthapa','$5$rounds=535000$3lEDB.VU4B4DwRac$uBoKSkHIs.fQqy2kPOtpt6caOqDMYwt7ypqE4Ox8NW1','2020-04-11 01:27:20'),(3,'Aayush Dhakal','ayush@gmail.com','adhakal','$5$rounds=535000$lGRiXRBYwEvLd/33$Ma3LKYLUXXs9QPqr4oPAqov6OpZAN21swoWgF23BA24','2020-04-13 03:22:08');
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

-- Dump completed on 2020-04-13 19:20:58
