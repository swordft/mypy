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
  `name` varchar(20) NOT NULL COMMENT '机柜名',
  `idc_id` int(10) NOT NULL COMMENT '所在机房id',
  `u_num` varchar(20) NOT NULL COMMENT 'U位',
  `power` varchar(20) NOT NULL COMMENT '电量',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cabinet`
--

LOCK TABLES `cabinet` WRITE;
/*!40000 ALTER TABLE `cabinet` DISABLE KEYS */;
INSERT INTO `cabinet` VALUES (1,'A_1',2,'42U','5000W'),(2,'O_1',1,'42U','5000W'),(3,'TT_001',3,'42U','8000W');
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
  `name` varchar(20) NOT NULL COMMENT '机房英文简写',
  `name_cn` varchar(32) NOT NULL COMMENT '机房中文名',
  `address` varchar(64) NOT NULL COMMENT '地址',
  `admin` varchar(20) NOT NULL COMMENT '联系人',
  `phone` varchar(20) NOT NULL COMMENT '联系电话',
  `num` int(10) NOT NULL COMMENT '机柜数量',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `idc`
--

LOCK TABLES `idc` WRITE;
/*!40000 ALTER TABLE `idc` DISABLE KEYS */;
INSERT INTO `idc` VALUES (1,'DCITS-TF','腾飞数据中心','高新六路腾飞创新中心B座3层','郭为','15555555555',40),(2,'DCITS-NEW','神码智慧天地数据中心','神州数码科技园1栋3层','马云','16666666666',80),(3,'Tengxun-01','腾讯数据中心','灞桥区浐河东路','马化腾','17777777776',100);
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
  `hostname` varchar(32) NOT NULL COMMENT '主机名',
  `inter_ip` varchar(20) NOT NULL COMMENT '内部ip',
  `outer_ip` varchar(20) NOT NULL COMMENT '外部ip',
  `cabinet_id` varchar(20) NOT NULL COMMENT '机柜id',
  `op` varchar(20) NOT NULL COMMENT '负责人',
  `phone` varchar(20) NOT NULL COMMENT '联系电话',
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostname` (`hostname`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server`
--

LOCK TABLES `server` WRITE;
/*!40000 ALTER TABLE `server` DISABLE KEYS */;
INSERT INTO `server` VALUES (1,'dbserver1','10.50.107.21','218.30.19.40','2','fangtao','17719582670'),(2,'appserver1','10.50.17.41','218.30.19.41','2','luolong','12222222222'),(3,'aix-01','10.1.1.11','218.29.50.47','1','liuheling','13333333333'),(4,'netbank','172.20.19.50','212.50.30.74','3','haisheng','15222222222');
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
) ENGINE=MyISAM AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (22,'fangtao','方涛','504fcb88aa89aaefb305c37b311a0cd7','17719582670','swordft@163.com','admin',0),(28,'wjx','王娟侠','504fcb88aa89aaefb305c37b311a0cd7','17719582779','wjx@126.com','common_user',0),(29,'guojing','郭靖','504fcb88aa89aaefb305c37b311a0cd7','16666667777','guojing@163.com','common_user',0),(31,'linghuchong','令狐冲','111','111','lhc@126.com','common_user',0),(32,'qiaofeng','乔峰','xiaofang','111','qf@163.com','common_user',0),(34,'zhangwuji','张无忌','504fcb88aa89aaefb305c37b311a0cd7','13333333333','zwj@163.com','common_user',0),(45,'zhaozilong','赵子龙','03a8ecb67c476ea560e5dbb72008ab29','15214974138','11@163.com','common_user',0);
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

-- Dump completed on 2018-05-21  8:12:15
