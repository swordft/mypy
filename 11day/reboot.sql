-- MySQL dump 10.13  Distrib 5.7.20, for linux-glibc2.12 (x86_64)
--
-- Host: localhost    Database: reboot
-- ------------------------------------------------------
-- Server version	5.7.20-log

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

--SET @@GLOBAL.GTID_PURGED='27826377-17a5-11e8-be67-000c29dd8ec6:1-872';

--
-- Current Database: `reboot`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `reboot` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `reboot`;

--
-- Table structure for table `cabinet`
--

DROP TABLE IF EXISTS `cabinet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cabinet` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `cicode` varchar(20) DEFAULT NULL,
  `capacity` varchar(20) NOT NULL COMMENT '机柜容量',
  `location` varchar(20) NOT NULL COMMENT '位置',
  `idc` varchar(100) NOT NULL COMMENT '所在机房',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cabinet`
--

LOCK TABLES `cabinet` WRITE;
/*!40000 ALTER TABLE `cabinet` DISABLE KEYS */;
INSERT INTO `cabinet` VALUES (1,'A_2','42U','A排2号','神州信息金融数据中心');
/*!40000 ALTER TABLE `cabinet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `idc`
--

DROP TABLE IF EXISTS `idc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `idc` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `cicode` varchar(20) DEFAULT NULL,
  `name` varchar(20) NOT NULL COMMENT '机房名称',
  `city` varchar(20) NOT NULL COMMENT '城市',
  `address` varchar(100) NOT NULL COMMENT '地址',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `idc`
--

LOCK TABLES `idc` WRITE;
/*!40000 ALTER TABLE `idc` DISABLE KEYS */;
INSERT INTO `idc` VALUES (2,'IDC_001','神州信息金融数据中心','西安','丈八四路20号神州数码科技园1栋3层');
/*!40000 ALTER TABLE `idc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `server`
--

DROP TABLE IF EXISTS `server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `cicode` varchar(20) DEFAULT NULL,
  `sn` varchar(20) NOT NULL COMMENT '机柜容量',
  `model` varchar(20) NOT NULL COMMENT '机柜容量',
  `architecture` varchar(20) NOT NULL COMMENT '位置',
  `cpu` varchar(20) NOT NULL COMMENT '所在机房',
  `memory` varchar(20) NOT NULL COMMENT '位置',
  `disk` varchar(20) NOT NULL COMMENT '所在机房',
  `cabinet` varchar(20) NOT NULL COMMENT '所在机房',
  `ip` varchar(20) DEFAULT NULL,
  `hostname` varchar(20) DEFAULT NULL,
  `os` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server`
--

LOCK TABLES `server` WRITE;
/*!40000 ALTER TABLE `server` DISABLE KEYS */;
INSERT INTO `server` VALUES (1,'netbank_product_001','6CU6127450','HP DL580 Gen8','x86','Xeon 3.6GHz * 32','128G','5T','A_2','10.120.253.12','dbserver','Linux');
/*!40000 ALTER TABLE `server` ENABLE KEYS */;
UNLOCK TABLES;

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
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (22,'fangtao','方涛','xiaofang','17719582670','swordft@163.com','admin',0),(28,'wjx','王娟侠','xiaofang','17719582779','wjx@163.com','common_user',0),(29,'guojing','郭靖','xiaofang','16666666666','guojing@163.com','common_user',0),(30,'huangrong','黄蓉','xiaofang','13333333333','hr@163.com','common_user',0),(31,'linghuchong','令狐冲','xiaofang','18888888888','lhc@126.com','common_user',0),(32,'qiaofeng','乔峰','xiaofang','14444444444','qf@163.com','common_user',0),(33,'huangyaoshi','黄药师','xiaofang','13333333333','hys@126.com','common_user',0),(34,'zhangwuji','张无忌','xiaofang','13333333333','zwj@163.com','common_user',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-06 17:38:54
