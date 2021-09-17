-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 16, 2021 at 10:16 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mazama`
--

-- --------------------------------------------------------

--
-- Table structure for table `manager`
--

CREATE TABLE `manager` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(40) NOT NULL,
  `pwd` varchar(40) NOT NULL,
  `created_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `manager`
--

INSERT INTO `manager` (`id`, `username`, `email`, `pwd`, `created_date`) VALUES
(2, '', 'normanburtonfree@gmail.com', '45eed7f4b1f7cac74e0515a744ce5919', '2021-09-17'),
(3, 'mark', '', '45eed7f4b1f7cac74e0515a744ce5919', '2021-09-17');

-- --------------------------------------------------------

--
-- Table structure for table `userlist`
--

CREATE TABLE `userlist` (
  `id` int(11) NOT NULL,
  `email` char(50) DEFAULT NULL,
  `First_name` char(30) NOT NULL,
  `Middle_name` char(30) DEFAULT NULL,
  `Last_Name` char(30) DEFAULT NULL,
  `Second_Name` char(30) DEFAULT NULL,
  `Suffix` char(10) NOT NULL,
  `DateOfBirth` char(30) NOT NULL,
  `SocialSecurityNumber` char(4) NOT NULL,
  `ResidenceAddresss` char(30) NOT NULL,
  `Apartment` char(30) NOT NULL,
  `Permanent` tinyint(1) DEFAULT NULL,
  `Unit_address` char(30) NOT NULL,
  `Unit_Apartment` char(30) NOT NULL,
  `Unit_zipcode` char(5) NOT NULL,
  `ResidenceZipcode` char(5) NOT NULL,
  `ResidenceCity` char(30) NOT NULL,
  `ResidenceState` char(30) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userlist`
--

INSERT INTO `userlist` (`id`, `email`, `First_name`, `Middle_name`, `Last_Name`, `Second_Name`, `Suffix`, `DateOfBirth`, `SocialSecurityNumber`, `ResidenceAddresss`, `Apartment`, `Permanent`, `Unit_address`, `Unit_Apartment`, `Unit_zipcode`, `ResidenceZipcode`, `ResidenceCity`, `ResidenceState`, `created_at`) VALUES
(1, 'normanburtonfree@gmail.com', 'Mark', 'Norman', 'Burton', 'Leopz', 'I', '10-02-1998', '1002', 'address', 'apartment10', 0, '', '', '', '30134', 'City', 'GA', '2021-09-13 14:55:25'),
(2, 'normanburtonfree@gmail.com', 'First', 'Middle', 'Last', 'Second', 'II', '09-03-1997', '9033', 'address', 'apartment10', 0, '', '', '', '30134', 'City', 'GA', '2021-09-13 14:56:33'),
(3, 'normanburtonfree@gmail.com', 'Alex', 'makarenco', 'vladi', 'nick', 'V', '08-26-1995', '8263', 'address', 'apartment11', 1, 'address1', 'apartment1', '30135', '30134', 'City', 'GA', '2021-09-13 14:58:07'),
(4, 'denea1288@gmail.com', 'Marks', 'Norman', 'Burtons', 'Leopz', 'I', '10-02-1993', '1002', 'address', 'apartment10', 0, '', '', '', '30134', 'City', 'GA', '2021-09-13 14:55:25'),
(6, 'denea1288@gmail.com', 'Alexs', 'makarenco', 'vladi', 'nick', 'V', '08-26-1995', '8264', 'address', 'apartment11', 1, 'address1', 'apartment1', '30135', '30134', 'City', 'GA', '2021-09-13 14:58:07'),
(7, 'normanburtonfree@gmail.com', 'Marka', 'Norman', 'Burton', 'Leopz', 'I', '10-02-1998', '1002', 'address', 'apartment10', 0, '', '', '', '30134', 'City', 'GA', '2021-09-13 14:55:25'),
(8, 'normanburtonfree@gmail.com', 'Firsta', 'Middle', 'Last', 'Second', 'II', '09-03-1997', '9033', 'address', 'apartment10', 0, '', '', '', '30134', 'City', 'GA', '2021-09-13 14:56:33'),
(9, 'normanburtonfree@gmail.com', 'Alexa', 'makarenco', 'vladi', 'nick', 'V', '08-26-1995', '8263', 'address', 'apartment11', 1, 'address1', 'apartment1', '30135', '30134', 'City', 'GA', '2021-09-13 14:58:07'),
(10, 'denea1288@gmail.com', 'Marksa', 'Norman', 'Burtons', 'Leopz', 'I', '10-02-1993', '1002', 'address', 'apartment10', 0, '', '', '', '30134', 'City', 'GA', '2021-09-13 14:55:25'),
(11, 'denea1288@gmail.com', 'Alexsa', 'makarenco', 'vladi', 'nick', 'V', '08-26-1995', '8264', 'address', 'apartment11', 1, 'address1', 'apartment1', '30135', '30134', 'City', 'GA', '2021-09-13 14:58:07'),
(12, 'normanburtonfree@gmail.com', 'Markb', 'Norman', 'Burton', 'Leopz', 'I', '10-02-1998', '1002', 'address', 'apartment10', 0, '', '', '', '30134', 'City', 'GA', '2021-09-13 14:55:25'),
(13, 'normanburtonfree@gmail.com', 'Firstb', 'Middle', 'Last', 'Second', 'II', '09-03-1997', '9033', 'address', 'apartment10', 0, '', '', '', '30134', 'City', 'GA', '2021-09-13 14:56:33'),
(14, 'normanburtonfree@gmail.com', 'Alexb', 'makarenco', 'vladi', 'nick', 'V', '08-26-1995', '8263', 'address', 'apartment11', 1, 'address1', 'apartment1', '30135', '30134', 'City', 'GA', '2021-09-13 14:58:07'),
(15, 'denea1288@gmail.com', 'Marksb', 'Norman', 'Burtons', 'Leopz', 'I', '10-02-1993', '1002', 'address', 'apartment10', 0, '', '', '', '30134', 'City', 'GA', '2021-09-13 14:55:25'),
(16, 'denea1288@gmail.com', 'Alexsb', 'makarenco', 'vladi', 'nick', 'V', '08-26-1995', '8264', 'address', 'apartment11', 1, 'address1', 'apartment1', '30135', '30134', 'City', 'GA', '2021-09-13 14:58:07'),
(17, 'normanburtonfree@gmail.com', 'Markab', 'Norman', 'Burton', 'Leopz', 'I', '10-02-1998', '1002', 'address', 'apartment10', 0, '', '', '', '30134', 'City', 'GA', '2021-09-13 14:55:25'),
(18, 'normanburtonfree@gmail.com', 'Firstab', 'Middle', 'Last', 'Second', 'II', '09-03-1997', '9033', 'address', 'apartment10', 0, '', '', '', '30134', 'City', 'GA', '2021-09-13 14:56:33'),
(19, 'normanburtonfree@gmail.com', 'Alexab', 'makarenco', 'vladi', 'nick', 'V', '08-26-1995', '8263', 'address', 'apartment11', 1, 'address1', 'apartment1', '30135', '30134', 'City', 'GA', '2021-09-13 14:58:07'),
(20, 'denea1288@gmail.com', 'Marksab', 'Norman', 'Burtons', 'Leopz', 'I', '10-02-1993', '1002', 'address', 'apartment10', 0, '', '', '', '30134', 'City', 'GA', '2021-09-13 14:55:25'),
(21, 'denea1288@gmail.com', 'Alexsab', 'makarenco', 'vladi', 'nick', 'V', '08-26-1995', '8264', 'address', 'apartment11', 1, 'address1', 'apartment1', '30135', '30134', 'City', 'GA', '2021-09-13 14:58:07');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `manager`
--
ALTER TABLE `manager`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userlist`
--
ALTER TABLE `userlist`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `manager`
--
ALTER TABLE `manager`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `userlist`
--
ALTER TABLE `userlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
