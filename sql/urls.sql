CREATE DATABASE  IF NOT EXISTS `urls` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `urls`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: urls
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `links`
--

DROP TABLE IF EXISTS `links`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `links` (
  `idlinks` int NOT NULL AUTO_INCREMENT,
  `name_link` varchar(100) DEFAULT NULL,
  `linkcorto` varchar(45) DEFAULT NULL,
  `iduser` int DEFAULT NULL,
  PRIMARY KEY (`idlinks`),
  KEY `fk_link_usuario_idx` (`iduser`),
  CONSTRAINT `fk_link_usuario` FOREIGN KEY (`iduser`) REFERENCES `usuario` (`idusuario`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `links`
--

LOCK TABLES `links` WRITE;
/*!40000 ALTER TABLE `links` DISABLE KEYS */;
INSERT INTO `links` VALUES (2,'http://127.0.0.1:5000/enlaces/create',NULL,NULL),(3,'https://www.youtube.com/watch?v=rVABbWlRuz8',NULL,NULL),(4,'https://www.youtube.com/watch?v=rVABbWlRuz8',NULL,NULL),(5,'https://www.youtube.com/watch?v=rVABbWlRuz8',NULL,NULL),(6,'https://www.youtube.com/watch?v=rVABbWlRuz8',NULL,NULL),(7,'https://www.youtube.com/watch?v=TgCqbq8p4eA','WWW.myencalecorto/yxLa',NULL),(8,'https://www.youtube.com/watch?v=g7Usra5trqk','WWW.myencalecorto/wMNt',NULL),(9,'https://www.youtube.com/watch?v=g7Usra5trqk','WWW.myencalecorto/VcfZ',NULL),(10,'https://www.youtube.com/watch?v=g7Usra5trqk','WWW.myencalecorto/siua',NULL),(11,'https://www.youtube.com/watch?v=g7Usra5trqk','WWW.myencalecorto/sHhI',NULL),(12,'https://www.youtube.com/watch?v=g7Usra5trqk','WWW.myencalecorto/THTp',NULL),(13,'https://www.youtube.com/watch?v=g7Usra5trqk','WWW.myencalecorto/mbbf',NULL),(14,'https://www.youtube.com/watch?v=g7Usra5trqk','WWW.myencalecorto/HWaF',NULL),(15,'https://www.youtube.com/watch?v=g7Usra5trqk','WWW.myencalecorto/GdGG',NULL),(16,'https://www.youtube.com/watch?v=g7Usra5trqk','WWW.myencalecorto/HIBw',NULL),(17,'https://www.youtube.com/watch?v=g7Usra5trqk','WWW.myencalecorto/kaZj',NULL),(18,'https://www.youtube.com/watch?v=g7Usra5trqk','WWW.myencalecorto/kWBN',NULL),(19,'https://www.youtube.com/watch?v=g7Usra5trqk','WWW.myencalecorto/ewrh',NULL),(20,'https://www.youtube.com/watch?v=g7Usra5trqk','WWW.myencalecorto/vOQL',NULL),(21,'https://www.youtube.com/watch?v=g7Usra5trqk','WWW.myencalecorto/mIjy',NULL),(22,'https://www.youtube.com/watch?v=g7Usra5trqk','www.myencalecorto/OcWL',NULL),(23,'https://getbootstrap.com/docs/5.0/customize/color/','www.myencalecorto/kPQO',4),(24,'https://www.youtube.com/watch?v=g7Usra5trqk','127.0.0.1:5000/MVgOp',2),(32,'https://getbootstrap.com/docs/5.0/components/buttons/','127.0.0.1:5000/Seba',6),(42,'https://es.vecteezy.com/vectores-gratis/bien','127.0.0.1:5000/unJw',5),(43,'https://es.vecteezy.com/vectores-gratis/bien','127.0.0.1:5000/bXHT',5),(44,'https://es.vecteezy.com/vectores-gratis/bien','127.0.0.1:5000/HEmj',5),(45,'https://es.vecteezy.com/vectores-gratis/bien','127.0.0.1:5000/UIoO',5);
/*!40000 ALTER TABLE `links` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `idusuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `correo` varchar(45) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idusuario`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'ddfd','josment123jf@gmail.com','fdf'),(2,'prueba','josment123jf@gmail.com','202cb962ac59075b964b07152d234b70'),(3,'josment12','josment123jf@gmail.com','c8ffe9a587b126f152ed3d89a146b445'),(4,'pruebav3','josmen@gmail.com','pbkdf2:sha256:150000$ezf0vHmr$c59b9da739cd5d29df16a21bc6e32f66d7d8686e7aa9a744d42dcede53ad5a2d'),(5,'prueba','prueba@prueba.com','pbkdf2:sha256:150000$0x6iFVZI$efbc4ba7322555f85d1969b65c0b894253acbc5e2a5ba9a1d1d3575fe699fb06'),(6,'edinson menseses','edinson@gmail.com','pbkdf2:sha256:150000$rDDTc4J0$06262182298194fa52a7c537c5c0f97899aabaccb50e6c11d1c1612f4dcf6954');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-21 13:31:47
