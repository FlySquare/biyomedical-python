-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 20, 2020 at 08:01 PM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `biyomedic`
--

-- --------------------------------------------------------

--
-- Table structure for table `musterilistesi`
--

DROP TABLE IF EXISTS `musterilistesi`;
CREATE TABLE IF NOT EXISTS `musterilistesi` (
  `musterilistesi_id` int(11) NOT NULL AUTO_INCREMENT,
  `musterilistesi_hastanead` varchar(250) COLLATE utf8mb4_turkish_ci NOT NULL,
  `musterilistesi_yetkiliad` varchar(250) COLLATE utf8mb4_turkish_ci NOT NULL,
  `musterilistesi_telno` varchar(250) COLLATE utf8mb4_turkish_ci NOT NULL,
  `musterilistesi_mail` varchar(250) COLLATE utf8mb4_turkish_ci NOT NULL,
  `musterilistesi_adres` varchar(250) COLLATE utf8mb4_turkish_ci NOT NULL,
  PRIMARY KEY (`musterilistesi_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `personel`
--

DROP TABLE IF EXISTS `personel`;
CREATE TABLE IF NOT EXISTS `personel` (
  `personel_id` int(11) NOT NULL AUTO_INCREMENT,
  `personel_username` varchar(250) COLLATE utf8mb4_turkish_ci NOT NULL,
  `personel_sifre` varchar(250) COLLATE utf8mb4_turkish_ci NOT NULL,
  PRIMARY KEY (`personel_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

--
-- Dumping data for table `personel`
--

INSERT INTO `personel` (`personel_id`, `personel_username`, `personel_sifre`) VALUES
(1, 'biyoser20', 'bct2020');

-- --------------------------------------------------------

--
-- Table structure for table `servistalepleri`
--

DROP TABLE IF EXISTS `servistalepleri`;
CREATE TABLE IF NOT EXISTS `servistalepleri` (
  `servistalepleri_id` int(11) NOT NULL AUTO_INCREMENT,
  `servistalepleri_not` varchar(250) COLLATE utf8mb4_turkish_ci NOT NULL,
  `servistalepleri_talep` varchar(250) COLLATE utf8mb4_turkish_ci NOT NULL,
  PRIMARY KEY (`servistalepleri_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `servistalepleribiten`
--

DROP TABLE IF EXISTS `servistalepleribiten`;
CREATE TABLE IF NOT EXISTS `servistalepleribiten` (
  `servistalepleribiten_id` int(11) NOT NULL AUTO_INCREMENT,
  `servistalepleribiten_not` varchar(250) COLLATE utf8mb4_turkish_ci NOT NULL,
  `servistalepleribiten_talep` varchar(250) COLLATE utf8mb4_turkish_ci NOT NULL,
  PRIMARY KEY (`servistalepleribiten_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `servistalepleridevam`
--

DROP TABLE IF EXISTS `servistalepleridevam`;
CREATE TABLE IF NOT EXISTS `servistalepleridevam` (
  `servistalepleridevam_id` int(11) NOT NULL AUTO_INCREMENT,
  `servistalepleridevam_not` varchar(250) COLLATE utf8mb4_turkish_ci NOT NULL,
  `servistalepleridevam_talep` varchar(250) COLLATE utf8mb4_turkish_ci NOT NULL,
  PRIMARY KEY (`servistalepleridevam_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
