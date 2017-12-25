-- MySQL dump 10.14  Distrib 5.5.56-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: reboot
-- ------------------------------------------------------
-- Server version	5.5.56-MariaDB

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
-- Current Database: `reboot`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `reboot` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `reboot`;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL COMMENT '用户名',
  `name_cn` varchar(32) NOT NULL COMMENT '中文名',
  `password` varchar(64) NOT NULL COMMENT '密码',
  `mobile` varchar(20) NOT NULL COMMENT '手机号码',
  `email` varchar(20) NOT NULL COMMENT '电子邮件',
  `role` varchar(16) NOT NULL COMMENT '角色',
  `status` int(10) NOT NULL COMMENT '帐号状态',
  `create_time` varchar(16) NOT NULL COMMENT '创建时间',
  `last_time` varchar(16) DEFAULT NULL COMMENT '最后登录时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (22,'fangtao','方涛','xiaofang','17719582670','swordft@163.com','OPS',0,'20170101-00:00','20171220-10:00'),(23,'wjx','王娟侠','wjx','17719582779','wjx@163.com','ICU',0,'20170102-12:00','20171222-18:00'),(24,'Linghuchong','令狐冲','linghuchong','13001011001','lhc@163.com','Huashan',0,'20160202-18:00','20171220-18:00'),(25,'Qiaofeng','乔峰','qiaofeng','18681867501','qiaofeng@126.com','Gaibang',0,'20160302-15:00','20161120-12:00'),(26,'Guojing','郭靖','guojing','15389265411','guojing@126.com','Gaibang',0,'20160512-13:00','20170320-12:00');
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

-- Dump completed on 2017-12-25 15:05:35
