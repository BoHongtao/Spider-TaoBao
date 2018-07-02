/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : spider

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2018-07-02 16:00:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tmall
-- ----------------------------
DROP TABLE IF EXISTS `tmall`;
CREATE TABLE `tmall` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image_url` varchar(256) DEFAULT NULL,
  `price` varchar(64) DEFAULT NULL,
  `deal` varchar(64) DEFAULT NULL,
  `title` varchar(128) DEFAULT NULL,
  `shop` varchar(64) DEFAULT NULL,
  `location` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1283 DEFAULT CHARSET=utf8;
