-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 15, 2021 at 06:33 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nithcoin`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add site settings', 7, 'add_sitesettings'),
(26, 'Can change site settings', 7, 'change_sitesettings'),
(27, 'Can delete site settings', 7, 'delete_sitesettings'),
(28, 'Can view site settings', 7, 'view_sitesettings'),
(29, 'Can add userlogs', 8, 'add_userlogs'),
(30, 'Can change userlogs', 8, 'change_userlogs'),
(31, 'Can delete userlogs', 8, 'delete_userlogs'),
(32, 'Can view userlogs', 8, 'view_userlogs'),
(33, 'Can add transactions', 9, 'add_transactions'),
(34, 'Can change transactions', 9, 'change_transactions'),
(35, 'Can delete transactions', 9, 'delete_transactions'),
(36, 'Can view transactions', 9, 'view_transactions'),
(37, 'Can add proofs', 10, 'add_proofs'),
(38, 'Can change proofs', 10, 'change_proofs'),
(39, 'Can delete proofs', 10, 'delete_proofs'),
(40, 'Can view proofs', 10, 'view_proofs'),
(41, 'Can add wallets', 11, 'add_wallets'),
(42, 'Can change wallets', 11, 'change_wallets'),
(43, 'Can delete wallets', 11, 'delete_wallets'),
(44, 'Can view wallets', 11, 'view_wallets'),
(45, 'Can add vendors', 12, 'add_vendors'),
(46, 'Can change vendors', 12, 'change_vendors'),
(47, 'Can delete vendors', 12, 'delete_vendors'),
(48, 'Can view vendors', 12, 'view_vendors'),
(49, 'Can add payment methods', 13, 'add_paymentmethods'),
(50, 'Can change payment methods', 13, 'change_paymentmethods'),
(51, 'Can delete payment methods', 13, 'delete_paymentmethods'),
(52, 'Can view payment methods', 13, 'view_paymentmethods'),
(53, 'Can add current price', 14, 'add_currentprice'),
(54, 'Can change current price', 14, 'change_currentprice'),
(55, 'Can delete current price', 14, 'delete_currentprice'),
(56, 'Can view current price', 14, 'view_currentprice'),
(57, 'Can add account nums', 15, 'add_accountnums'),
(58, 'Can change account nums', 15, 'change_accountnums'),
(59, 'Can delete account nums', 15, 'delete_accountnums'),
(60, 'Can view account nums', 15, 'view_accountnums'),
(61, 'Can add vendors', 16, 'add_vendors'),
(62, 'Can change vendors', 16, 'change_vendors'),
(63, 'Can delete vendors', 16, 'delete_vendors'),
(64, 'Can view vendors', 16, 'view_vendors'),
(65, 'Can add users', 16, 'add_users'),
(66, 'Can change users', 16, 'change_users'),
(67, 'Can delete users', 16, 'delete_users'),
(68, 'Can view users', 16, 'view_users'),
(69, 'Can add messages', 17, 'add_messages'),
(70, 'Can change messages', 17, 'change_messages'),
(71, 'Can delete messages', 17, 'delete_messages'),
(72, 'Can view messages', 17, 'view_messages'),
(73, 'Can add referrals', 18, 'add_referrals'),
(74, 'Can change referrals', 18, 'change_referrals'),
(75, 'Can delete referrals', 18, 'delete_referrals'),
(76, 'Can view referrals', 18, 'view_referrals'),
(77, 'Can add cards', 19, 'add_cards'),
(78, 'Can change cards', 19, 'change_cards'),
(79, 'Can delete cards', 19, 'delete_cards'),
(80, 'Can view cards', 19, 'view_cards'),
(81, 'Can add reset password', 20, 'add_resetpassword'),
(82, 'Can change reset password', 20, 'change_resetpassword'),
(83, 'Can delete reset password', 20, 'delete_resetpassword'),
(84, 'Can view reset password', 20, 'view_resetpassword');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_verified` int(11) NOT NULL DEFAULT 0,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_verified`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(2, 'pbkdf2_sha256$216000$QWh1EP87OUT6$WAjjieSHom+/r0+J7ZSHGYcz5LpczMQFVnE7RiJ1cXc=', '2021-01-21 20:54:17.726148', 0, 0, '2222455555', '', '', 'dfdddggW@gdggdd.vvv', 0, 1, '2021-01-10 09:36:25.595233'),
(3, 'pbkdf2_sha256$216000$oz6H2ASyfRaG$IzO7V+bNjWrEU+113mNQ9YDq4JwG6k1mFzfRh2yiy4c=', '2021-02-04 19:59:50.241994', 0, 0, '9c46b710cc6f5c36ce402e40fb160d2c', '', '', 'dfdddggW@gdggdds.vvv', 0, 1, '2021-01-10 09:42:51.602429'),
(4, 'pbkdf2_sha256$216000$ngCTJjyj2OrY$9V9V6z+8kONw9ZzFlBhb/47C4SpGOA9zbU8qll692Zk=', '2021-02-04 17:28:08.218389', 0, 0, '9293219798', '', '', 'ffggg@gggg.vvv', 0, 1, '2021-01-10 12:49:16.336962'),
(5, 'pbkdf2_sha256$216000$SPWw1tl2WV92$Kv8nnR8vDjG23BTa7aQdkDW1g5t8sk8boa7IVkj3IxE=', '2021-01-13 09:53:29.116077', 0, 0, '8397363127', '', '', 'jhhgjhggj@jhhj.gg', 0, 1, '2021-01-10 20:28:12.150106'),
(6, 'pbkdf2_sha256$216000$iLq8FRHMTxoa$lu98sXDJzrox0AzMYCHaTr7/8esLtwPrJeYZZrrttpc=', '2021-02-05 20:08:17.213892', 0, 0, '8199651128', '', '', 'vendor1@vendor.com', 0, 1, '2021-01-12 13:04:37.561111'),
(7, 'pbkdf2_sha256$216000$SHduwIkrhNd3$bTMuTTUR60NY0GezIGP9Ee8heOZTUvwRmSUDd1M/bko=', '2021-02-06 06:09:49.569548', 0, 0, '8701194694', '', '', 'userano@email.com', 0, 1, '2021-02-06 06:08:14.619444'),
(17, 'pbkdf2_sha256$216000$oiXwhfJIAGIv$g0aQ6KvVGfBmoJBOa8oibFOHuiTl1HYyx1MBdr5OtOM=', NULL, 0, 0, '8832476820', '', '', 'vjjjhyj@gdgdg.vvv', 0, 1, '2021-02-06 06:40:47.378437'),
(18, 'pbkdf2_sha256$216000$7N4LtO5fBOyj$XcJ5JxbQrtI7mFpv+yc4v8vLk9LcfKcucn0/Au3OZ2k=', NULL, 0, 0, '2365084576', '', '', 'fsdssd@fddsd.vvv', 0, 1, '2021-02-06 07:07:46.559246'),
(19, 'pbkdf2_sha256$216000$YydLycxGUllf$jQ5LGJXwnGaTIdsqd1xGaQa2LoDoUdsghtJJB88/u6g=', NULL, 0, 0, '5329410403', '', '', 'dafgxxf@fgddh.bbb', 0, 1, '2021-02-06 07:08:37.343859'),
(20, 'pbkdf2_sha256$216000$qtgTiAcxTTB4$zw5PL45Y4l40WYTZjFjLvzJ8QlHo8FaVyWNutlNcuk4=', NULL, 0, 0, '3483593609', '', '', 'dgdgdgdg@fdfdfd.vvv', 0, 1, '2021-02-06 07:10:25.502123'),
(21, 'pbkdf2_sha256$216000$mo65sGrCH0Ni$VVp1GSIOEZAz49U6QnyeT9R6ndH5Lf4Uq4nPqSqj/jg=', NULL, 0, 0, '3696440955', '', '', 'ggsgsgsg@fwfsff.bbb', 0, 1, '2021-02-06 07:11:54.772747'),
(22, 'pbkdf2_sha256$216000$8k4rAVEP5lI5$aKaQnAlugl8hMGUKiIh+sY0n3o+1Zs/2woCQImD8+HU=', NULL, 0, 0, '5383054111', '', '', 'hchdhgdh@grfujkguk.nnn', 0, 1, '2021-02-15 11:37:52.108475'),
(23, 'pbkdf2_sha256$216000$5LOW7gKYcSk7$maJMg6xYkPS65L/AfefsPxefvbWb8EgfKcszVeD7WaA=', NULL, 0, 0, '9452527250', '', '', 'hchdhgdh@grfujkguk.nnn', 0, 1, '2021-02-15 12:08:54.273776'),
(24, 'pbkdf2_sha256$216000$320TYVtJB5rp$WPenXBqtLGu9MKtTOyWxTAgdLy98PBs5LC4C1Qbxpek=', NULL, 0, 0, '1934288898', '', '', 'r3rfdfh@grfujkguk.nnn', 0, 1, '2021-02-15 12:26:29.564256'),
(25, 'pbkdf2_sha256$216000$tMm4gBZ6UIkU$DUC3cbuEA8UzgcgjirDbaKHJkg/Zhq2uHekLWSCIiGc=', '2021-02-15 12:47:02.208689', 0, 0, '2986947545', '', '', 'adamsondamilola@gmail.com', 0, 1, '2021-02-15 12:45:31.363717'),
(26, 'pbkdf2_sha256$216000$sWQMsaJ1mE1q$1CpWl2uRUNurtjrVmMwUVUX9R4mFCT3la0kie5TvAvQ=', '2021-02-15 15:57:23.135263', 0, 0, '6243858417', '', '', 'adamshdhdd@dgg.bbb', 0, 1, '2021-02-15 13:14:41.621839');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_resetpassword`
--

CREATE TABLE `auth_user_resetpassword` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `temp_password` varchar(255) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL,
  `unique` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user_resetpassword`
--

INSERT INTO `auth_user_resetpassword` (`id`, `user_id`, `status`, `temp_password`, `code`, `date_added`, `unique`, `email`) VALUES
(48, 26, 0, '', '26eb47f41baadb0b1b7304b746b9f99e', '2021-02-15 23:14:01.416657', '4aa03540b0df8be83aeba37e64afd53c', 'adamshdhdd@dgg.bbb'),
(49, 26, 0, '', '094a3e43ff5b75e4cf809d2a6275a0ed', '2021-02-15 23:14:25.608705', 'c8f9de9ea19245610ba699b87f0fe1c2', 'adamshdhdd@dgg.bbb'),
(50, 26, 0, '', '3e083cda7f47cac42f8e91c955bd0c96', '2021-02-15 23:14:32.855540', 'a8fe81419b3a553bf68ed76037ee0cc0', 'adamshdhdd@dgg.bbb'),
(51, 26, 0, '', 'c63e25455fb4bedf5572a74725754d4e', '2021-02-15 23:14:46.666704', '141c9f7ea476228ce97f16a3650d0e7e', 'adamshdhdd@dgg.bbb'),
(52, 26, 0, '', '922e051293f2a9d5efe599a2bd4de9e0', '2021-02-15 23:14:50.464684', '10991cead51e75be49b94355ccf94357', 'adamshdhdd@dgg.bbb'),
(53, 26, 0, '', '1435b50660d6300cddd0517dceb17b6f', '2021-02-15 23:15:27.917593', 'f8d16b51323aebb65d7ac59ba3b8eff8', 'adamshdhdd@dgg.bbb'),
(54, 26, 0, '', '892caab93c8b546aced201216c207478', '2021-02-15 23:16:50.658131', '364d674b1b2e07ede2a2a57fed5e4ce0', 'adamshdhdd@dgg.bbb'),
(55, 26, 0, '', 'd4983e0bddb98a2bfd9c0eed28805830', '2021-02-15 23:16:52.959750', '26dfcc03adfcb991eb0420da94611960', 'adamshdhdd@dgg.bbb'),
(56, 26, 0, '', 'e29160bfda60317f64d5f03fa0f7987e', '2021-02-15 23:17:37.655055', '1707cd25a567155fd29a54494a7d419b', 'adamshdhdd@dgg.bbb'),
(57, 26, 0, '', '7e5a3011668424d81dd52b843bc8d613', '2021-02-15 23:17:56.979313', 'f9cfb1fe8f699a8270d783d2810319fa', 'adamshdhdd@dgg.bbb'),
(58, 26, 0, '', '91cc3639fb20f52f010685721d8470ac', '2021-02-15 23:18:26.675775', 'fe4f924f619944d1783096005fc9323e', 'adamshdhdd@dgg.bbb'),
(59, 26, 0, '', '5fd28f085ab935907480a69f231d7f89', '2021-02-15 23:20:08.381478', '003f660925cba2c4c51bad5808d49edc', 'adamshdhdd@dgg.bbb'),
(60, 26, 0, '', 'aabeb7b1995a23f3cee04da1e58cdb54', '2021-02-15 23:20:58.897661', 'c5321c765c07b3e6e79735923deac5e6', 'adamshdhdd@dgg.bbb'),
(61, 26, 0, '', '65a905bcb6c908d06e9f11ca6376ebe6', '2021-02-15 23:21:57.863628', 'ccc01f555234fccec7f2c0fc33082732', 'adamshdhdd@dgg.bbb'),
(62, 26, 0, '', '35c725999b83ad42e3f4e89b5d5b42d5', '2021-02-15 23:23:08.497998', 'e9dc6e20f3b5a83611238a414696e2bd', 'adamshdhdd@dgg.bbb'),
(63, 26, 0, '', 'c36ae4dc78413eeb1e75f1c312991552', '2021-02-15 23:24:56.738478', '63e164f69872764c1f42b361f3202b72', 'adamshdhdd@dgg.bbb'),
(64, 26, 0, '', '67e3806806c2fa0366d625efefcd75ec', '2021-02-15 23:27:38.865565', '6ddae55bcc8bfb7aaeefd80ac3617233', 'adamshdhdd@dgg.bbb'),
(65, 26, 0, '', '435f75af3a36f952c7142149270d5d25', '2021-02-15 23:27:43.304943', 'b664aeb86404e18f280a2f927bf18072', 'adamshdhdd@dgg.bbb'),
(66, 26, 0, 'pbkdf2_sha256$216000$sWQMsaJ1mE1q$1CpWl2uRUNurtjrVmMwUVUX9R4mFCT3la0kie5TvAvQ=', 'f32dd81e34c294238b540d56de1c1950', '2021-02-15 23:28:20.778187', 'b0059577e8476a8ba2186b708e0eacfb', 'adamshdhdd@dgg.bbb');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_userlogs`
--

CREATE TABLE `auth_user_userlogs` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `device` varchar(255) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user_userlogs`
--

INSERT INTO `auth_user_userlogs` (`id`, `user_id`, `ip`, `country`, `device`, `date_added`) VALUES
(1, 2, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0', '2021-01-10 17:36:25.880375'),
(2, 3, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0', '2021-01-10 17:42:51.856336'),
(7, 6, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', '2021-01-14 00:01:59.948879'),
(8, 4, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75', '2021-01-19 05:42:09.873595'),
(9, 6, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36', '2021-02-02 20:59:08.555868'),
(10, 4, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0', '2021-02-05 01:28:08.149280'),
(11, 3, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56', '2021-02-05 03:59:50.195114'),
(12, 6, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36', '2021-02-06 04:08:17.091998'),
(13, 7, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63', '2021-02-06 14:08:14.979552'),
(14, 8, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63', '2021-02-06 14:12:00.330154'),
(15, 9, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63', '2021-02-06 14:15:49.928191'),
(16, 10, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63', '2021-02-06 14:24:11.545917'),
(17, 11, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63', '2021-02-06 14:24:45.521931'),
(18, 12, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63', '2021-02-06 14:25:19.177621'),
(19, 13, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63', '2021-02-06 14:26:53.916068'),
(20, 14, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63', '2021-02-06 14:30:19.670067'),
(21, 15, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63', '2021-02-06 14:31:35.589991'),
(22, 16, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63', '2021-02-06 14:38:11.888339'),
(23, 17, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63', '2021-02-06 14:40:47.648270'),
(24, 20, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63', '2021-02-06 15:10:25.793073'),
(25, 21, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63', '2021-02-06 15:11:55.087542'),
(26, 22, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0', '2021-02-15 19:37:54.799885'),
(27, 22, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0', '2021-02-15 20:08:57.060196'),
(28, 24, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0', '2021-02-15 20:26:32.338646'),
(29, 25, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0', '2021-02-15 20:45:34.284925'),
(30, 26, '127.0.0.1', 'Undefined', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36', '2021-02-15 21:14:41.947640');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(20, 'auth_user', 'resetpassword'),
(8, 'auth_user', 'userlogs'),
(5, 'contenttypes', 'contenttype'),
(17, 'messenger', 'messages'),
(6, 'sessions', 'session'),
(14, 'site_settings', 'currentprice'),
(7, 'site_settings', 'sitesettings'),
(9, 'transactions', 'transactions'),
(19, 'users', 'cards'),
(18, 'users', 'referrals'),
(16, 'users', 'users'),
(13, 'vendor', 'paymentmethods'),
(12, 'vendor', 'vendors'),
(15, 'wallet', 'accountnums'),
(10, 'wallet', 'proofs'),
(11, 'wallet', 'wallets');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-01-09 06:25:04.004820'),
(2, 'auth', '0001_initial', '2021-01-09 06:25:04.528383'),
(3, 'admin', '0001_initial', '2021-01-09 06:25:06.813064'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-01-09 06:25:07.615339'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-01-09 06:25:07.637495'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-01-09 06:25:07.969742'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-01-09 06:25:08.333199'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-01-09 06:25:08.371002'),
(9, 'auth', '0004_alter_user_username_opts', '2021-01-09 06:25:08.402218'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-01-09 06:25:08.618414'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-01-09 06:25:08.618414'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-01-09 06:25:08.656223'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-01-09 06:25:08.740883'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-01-09 06:25:08.834643'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-01-09 06:25:08.856788'),
(16, 'auth', '0011_update_proxy_permissions', '2021-01-09 06:25:08.888040'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-01-09 06:25:08.919290'),
(18, 'sessions', '0001_initial', '2021-01-09 06:25:09.004015'),
(21, 'auth_user', '0001_initial', '2021-01-09 20:55:40.204376'),
(22, 'site_settings', '0001_initial', '2021-01-10 17:49:46.522574'),
(23, 'transactions', '0001_initial', '2021-01-11 10:40:34.942422'),
(24, 'wallet', '0001_initial', '2021-01-11 10:40:35.158656'),
(25, 'vendor', '0001_initial', '2021-01-11 20:36:41.073598'),
(26, 'vendor', '0002_auto_20210112_1946', '2021-01-12 11:47:07.528778'),
(27, 'vendor', '0003_paymentmethods', '2021-01-13 10:17:44.072601'),
(28, 'wallet', '0002_wallets_pin', '2021-01-13 14:40:36.694964'),
(29, 'vendor', '0004_vendors_buying_at', '2021-01-13 23:15:43.858140'),
(30, 'site_settings', '0002_currentprice', '2021-01-14 12:16:25.154269'),
(31, 'site_settings', '0003_auto_20210114_2025', '2021-01-14 12:25:39.422695'),
(32, 'wallet', '0003_accountnums', '2021-01-14 18:17:54.039426'),
(33, 'wallet', '0004_accountnums_number', '2021-01-14 18:34:38.420105'),
(34, 'users', '0001_initial', '2021-01-20 07:52:25.178126'),
(35, 'users', '0002_auto_20210120_1553', '2021-01-20 07:53:29.910699'),
(36, 'messenger', '0001_initial', '2021-01-21 15:54:08.190653'),
(37, 'transactions', '0002_auto_20210123_0113', '2021-01-22 17:13:26.891576'),
(38, 'users', '0003_referrals', '2021-02-04 23:14:50.449761'),
(39, 'users', '0004_cards', '2021-02-04 23:59:42.894946'),
(40, 'auth_user', '0002_resetpassword', '2021-02-06 07:51:33.158372'),
(41, 'auth_user', '0003_resetpassword_unique', '2021-02-06 08:45:45.543041'),
(42, 'auth_user', '0004_resetpassword_email', '2021-02-06 08:51:04.009124');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('15wrrp2hqp11vwsjlrp8gr05sr3o0wru', '.eJxVjMsOwiAQRf-FtSEyvF267zeQAQapGkhKuzL-uzbpQrf3nHNfLOC21rANWsKc2YUpdvrdIqYHtR3kO7Zb56m3dZkj3xV-0MGnnul5Pdy_g4qjfusSswIkigSKlISis1UlOXROAEjhrT7LVBxGkY0WJA0ZD4m89KClVez9AfwlN7A:1l7iQK:IoTdFt1nuOBJ4hBGYJID7y8nPUa8-8_vxi7ie-7VANY', '2021-02-18 17:28:08.233975'),
('8sbugdtwa849o0g9453q0lhcgpur30r2', '.eJxVjEEOwiAQRe_C2hCnAyO4dO8ZyMCgVA0kpV0Z726bdKHb_977bxV4mUtYep7CKOqsBlKH3zFyeua6EXlwvTedWp2nMepN0Tvt-tokvy67-3dQuJe1Nh7QJxRDR-scSIrREN9YbMzgxIuAdcgeZGD0J6BVRATLlBgtkfp8Af9LN3U:1lBgFX:Q5LKS4tM1PZnkStd8VbquB4e1e4A9UnPVd45UfaEEEo', '2021-03-01 15:57:23.138261'),
('8ujgksp4lhgxjti2r7nqoyytbha632pr', '.eJxVjDsOwyAQBe9CHaFdm2_K9D4DAhaCkwgkY1dR7h5bcpG0M_Pemzm_rcVtPS1uJnZlil1-WfDxmeoh6OHrvfHY6rrMgR8JP23nU6P0up3t30HxvexrFAYVkpLBg4UsrSTYgRiDtmqwhJm0hii0NhoRcJSQRDR2oAjGZ2SfL6WjNlM:1l1cKj:SX68sZRDDWKdv5IVGd4_CUUaBWioZceAnBnb8IuqR0k', '2021-02-01 21:45:09.949437'),
('c6kdi9ow2nfa55xb9pcirikh78ibu8fm', '.eJxVjDsOwyAQBe9CHaFdm2_K9D4DAhaCkwgkY1dR7h5bcpG0M_Pemzm_rcVtPS1uJnZlil1-WfDxmeoh6OHrvfHY6rrMgR8JP23nU6P0up3t30HxvexrFAYVkpLBg4UsrSTYgRiDtmqwhJm0hii0NhoRcJSQRDR2oAjGZ2SfL6WjNlM:1l87Or:W06hCI8ikQHUP7lldD41yT843mlHYtxD7UuckxjEvrU', '2021-02-19 20:08:17.217895'),
('dyn0cxcm7eym76xnabixo5wh3w40f99f', '.eJxVjDkOwjAUBe_iGlmOlxgo6TmD9Rd_HEC2FCcV4u4QKQW0b2beSyVYl5LWnuc0sTorG9Thd0SgR64b4TvUW9PU6jJPqDdF77Tra-P8vOzu30GBXr41MaKzHKIYJBLDXmwcJQzROUDx4gOS2MzuBDm4MALjcSBrPEeK7NX7A0CeOUo:1lBdHK:6HsuU6n9tjcp_tx5E7qP6s0g73PWOhfzogJqLnL0O24', '2021-03-01 12:47:02.211688'),
('ob2n47j8wjro8zg3i2lpeek9a3vdr4lm', '.eJxVjDsOwyAQBe9CHaFdm2_K9D4DAhaCkwgkY1dR7h5bcpG0M_Pemzm_rcVtPS1uJnZlil1-WfDxmeoh6OHrvfHY6rrMgR8JP23nU6P0up3t30HxvexrFAYVkpLBg4UsrSTYgRiDtmqwhJm0hii0NhoRcJSQRDR2oAjGZ2SfL6WjNlM:1kzikG:XgaNbfhlHe3FK2VYxbyAtTI7ycgq-1iyIvck8h-YmY0', '2021-01-27 16:11:40.371651'),
('u5uccxwrdfbwj88l1vurij2sefitnji1', '.eJxVjDsOwyAQBe9CHaFdm2_K9D4DAhaCkwgkY1dR7h5bcpG0M_Pemzm_rcVtPS1uJnZlil1-WfDxmeoh6OHrvfHY6rrMgR8JP23nU6P0up3t30HxvexrFAYVkpLBg4UsrSTYgRiDtmqwhJm0hii0NhoRcJSQRDR2oAjGZ2SfL6WjNlM:1l6vGu:XcbaA2jBuc8v3BnUYgS33h2bNZq0G3fg85sRpZeLI-U', '2021-02-16 12:59:08.741489'),
('x2p4xwcg6r1hhfsyfas25l1gy82ma945', '.eJxVjDsOwjAQBe_iGllOsusPJT1nsHbXNg6gRIqTCnF3iJQC2jcz76UibWuNW8tLHJM6K1Sn341JHnnaQbrTdJu1zNO6jKx3RR-06euc8vNyuH8HlVr91r5A9uC5OBMCJQ5kUQbT8wDCgEmg9J31HVjxPYotjqlISIhIBlxQ7w_sBzfq:1kzcqH:cFxwj-hkb75OMdcsf5TS5hmsWpC_9jQWkka6rn0tKog', '2021-01-27 09:53:29.116077'),
('zaz8pmy7gd1r4utafopqaztvq1fajdyr', '.eJxVjMsOwiAQRf-FtSEyvF267zeQAQapGkhKuzL-uzbpQrf3nHNfLOC21rANWsKc2YUpdvrdIqYHtR3kO7Zb56m3dZkj3xV-0MGnnul5Pdy_g4qjfusSswIkigSKlISis1UlOXROAEjhrT7LVBxGkY0WJA0ZD4m89KClVez9AfwlN7A:1l2wHN:Xco3rwvYTU7kYNWjUfROJhYnbQKaa4__UJQSpf0VSYI', '2021-02-05 13:15:09.579856');

-- --------------------------------------------------------

--
-- Table structure for table `messenger_messages`
--

CREATE TABLE `messenger_messages` (
  `id` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `sender_id` int(11) DEFAULT NULL,
  `message` varchar(255) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `seen` int(11) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `messenger_messages`
--

INSERT INTO `messenger_messages` (`id`, `parent_id`, `user_id`, `receiver_id`, `sender_id`, `message`, `photo`, `seen`, `date_added`) VALUES
(1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0000-00-00 00:00:00.000000'),
(22, 2, 2, 4, 2, 'Hi bro. hope you are good?', '', 0, '2021-01-22 10:45:00.570987'),
(23, 2, 4, 2, 4, 'Hi , I see you', '', 0, '2021-01-22 10:57:40.598049'),
(24, 24, 6, 4, 6, 'Testing the microphone', '', 0, '2021-01-22 11:01:58.715575'),
(25, 24, 6, 4, 6, 'I hope you received this message?', '', 0, '2021-01-22 11:02:36.906597'),
(26, 26, 4, 3, 4, 'Hi vendor. I want to purchase nithcoin please', '', 0, '2021-02-05 03:57:16.270182'),
(27, 26, 3, 4, 3, 'Okay. How much of Nithcoin?', '', 0, '2021-02-05 04:00:30.530460'),
(28, 26, 4, 3, 4, '500', '', 0, '2021-02-05 04:15:24.926500');

-- --------------------------------------------------------

--
-- Table structure for table `site_settings_currentprice`
--

CREATE TABLE `site_settings_currentprice` (
  `id` int(11) NOT NULL,
  `currency` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL,
  `ntc` varchar(255) DEFAULT NULL,
  `usd` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `site_settings_currentprice`
--

INSERT INTO `site_settings_currentprice` (`id`, `currency`, `amount`, `date_added`, `ntc`, `usd`) VALUES
(1, NULL, NULL, '2021-01-21 20:28:25.000000', '0.001', '1000');

-- --------------------------------------------------------

--
-- Table structure for table `site_settings_sitesettings`
--

CREATE TABLE `site_settings_sitesettings` (
  `id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `altphone` varchar(255) DEFAULT NULL,
  `sub_title` varchar(254) DEFAULT NULL,
  `symbol` varchar(254) DEFAULT NULL,
  `maintenance` varchar(54) DEFAULT NULL,
  `logo` varchar(100) DEFAULT NULL,
  `favicon` varchar(100) DEFAULT NULL,
  `signup_msg` varchar(500) DEFAULT NULL,
  `login_auth_msg` varchar(500) DEFAULT NULL,
  `password_reset_msg` varchar(500) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `site_settings_sitesettings`
--

INSERT INTO `site_settings_sitesettings` (`id`, `title`, `address`, `email`, `altphone`, `sub_title`, `symbol`, `maintenance`, `logo`, `favicon`, `signup_msg`, `login_auth_msg`, `password_reset_msg`, `phone`, `date_added`) VALUES
(1, 'NITHCOIN', 'nithcoin.com', 'support@nithcoin.com', '0987654321', 'Alternative Banking', 'NTC', '0', NULL, NULL, NULL, NULL, NULL, '0123456789', '2021-01-20 01:50:13.000000');

-- --------------------------------------------------------

--
-- Table structure for table `transactions_transactions`
--

CREATE TABLE `transactions_transactions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `amount` double DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `transaction_id` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL,
  `receiver` varchar(255) DEFAULT NULL,
  `sender` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transactions_transactions`
--

INSERT INTO `transactions_transactions` (`id`, `user_id`, `email`, `amount`, `type`, `transaction_id`, `status`, `date_added`, `receiver`, `sender`) VALUES
(9, 4, 'ffggg@gggg.vvv', 0.045, 'Sent', '783819336112233', 1, '2021-01-23 01:17:14.474160', '6794825241', '9743311209'),
(10, 6, NULL, 0.045, 'Received', '783819336112233', 1, '2021-01-23 01:17:14.485233', '6794825241', '9743311209'),
(11, 4, 'ffggg@gggg.vvv', 0.045, 'Sent', '78381933614554', 1, '2021-01-23 01:17:14.474160', '3451234565', '4545455466'),
(12, 25, 'adamsondamilola@gmail.com', NULL, 'Deposit', '2977175818', 0, '2021-02-15 21:00:47.978128', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users_cards`
--

CREATE TABLE `users_cards` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `account` varchar(255) DEFAULT NULL,
  `card_id` varchar(255) NOT NULL,
  `card_pin` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `due_date` datetime(6) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users_referrals`
--

CREATE TABLE `users_referrals` (
  `id` int(11) NOT NULL,
  `invitee` int(11) DEFAULT NULL,
  `invited` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `is_verified` int(11) NOT NULL DEFAULT 0,
  `date_added` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users_referrals`
--

INSERT INTO `users_referrals` (`id`, `invitee`, `invited`, `status`, `is_verified`, `date_added`) VALUES
(1, 6, 20, 0, 0, '2021-02-06 15:10:25.736976'),
(2, 6, 21, 0, 0, '2021-02-06 15:11:55.072549'),
(3, 25, 26, 0, 1, '2021-02-15 21:14:41.942642');

-- --------------------------------------------------------

--
-- Table structure for table `users_users`
--

CREATE TABLE `users_users` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `city` varchar(150) DEFAULT NULL,
  `mobile` varchar(25) DEFAULT NULL,
  `altmobile` varchar(25) DEFAULT NULL,
  `profile` varchar(100) DEFAULT NULL,
  `cover` varchar(100) DEFAULT NULL,
  `full_face` varchar(100) DEFAULT NULL,
  `id_card` varchar(100) DEFAULT NULL,
  `proof_of_residence` varchar(100) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users_users`
--

INSERT INTO `users_users` (`id`, `user_id`, `email`, `firstname`, `lastname`, `country`, `city`, `mobile`, `altmobile`, `profile`, `cover`, `full_face`, `id_card`, `proof_of_residence`, `date_added`) VALUES
(2, 4, 'ffggg@gggg.vvv', 'Green', 'Gorey', 'Ghana', 'Kumasi', '+123456789', NULL, 'users/testimonial-5.jpg', '', '', '', '', '2021-01-20 18:29:07.633547'),
(3, 25, 'adamsondamilola@gmail.com', 'Adams', 'Adams', 'Angola', 'Zamn', '+798765432167', NULL, '', '', '', '', '', '2021-02-15 20:50:24.047625'),
(4, 26, 'adamshdhdd@dgg.bbb', NULL, NULL, NULL, NULL, NULL, NULL, '', '', '', '', '', '2021-02-15 22:14:13.187709');

-- --------------------------------------------------------

--
-- Table structure for table `vendor_paymentmethods`
--

CREATE TABLE `vendor_paymentmethods` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `method` varchar(255) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `vendor_vendors`
--

CREATE TABLE `vendor_vendors` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `city` varchar(150) DEFAULT NULL,
  `mobile` varchar(25) DEFAULT NULL,
  `whatsapp` varchar(25) DEFAULT NULL,
  `profile` varchar(100) DEFAULT NULL,
  `cover` varchar(100) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL,
  `full_face` varchar(100) DEFAULT NULL,
  `id_card` varchar(100) DEFAULT NULL,
  `minimum` double DEFAULT NULL,
  `proof_of_residence` varchar(100) DEFAULT NULL,
  `selling_at` double DEFAULT NULL,
  `buying_at` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vendor_vendors`
--

INSERT INTO `vendor_vendors` (`id`, `user_id`, `email`, `firstname`, `lastname`, `country`, `city`, `mobile`, `whatsapp`, `profile`, `cover`, `status`, `date_added`, `full_face`, `id_card`, `minimum`, `proof_of_residence`, `selling_at`, `buying_at`) VALUES
(1, 2, 'eeeeeeeeeee', 'ewweew', 'wsdsdssd', 'Spain', 'Rome', '22222222333', '+14444444555', 'vendors/testimonial-2.jpg', NULL, 1, '2021-01-12 05:14:45.000000', NULL, NULL, 44, NULL, 10, 14),
(2, 3, 'sam', 'sam', 'wasu', 'Spain', 'Rome', '22222222333', '+4444444555', NULL, NULL, 1, '2021-01-12 05:14:45.000000', NULL, NULL, 33, NULL, 12, 6),
(5, 6, 'vendor1@vendor.com', 'First', 'Vendor', 'United Kingdom', 'Manchested', '+7777777777', '+5656565656', 'vendors/8.jpg', '', 0, '2021-01-13 03:49:26.696581', '', '8.jpg', 67, '', 8, 19),
(6, 4, 'ffggg@gggg.vvv', 'ghgshsgg', 'fgsdgdgsdgg', 'Argentina', 'fsfsfsfsf', NULL, NULL, '', '', 0, '2021-02-06 04:23:44.083119', '', '', NULL, '', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `wallet_accountnums`
--

CREATE TABLE `wallet_accountnums` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `label` varchar(255) DEFAULT NULL,
  `balance` double DEFAULT NULL,
  `sent` double DEFAULT NULL,
  `received` double DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL,
  `number` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `wallet_accountnums`
--

INSERT INTO `wallet_accountnums` (`id`, `user_id`, `type`, `label`, `balance`, `sent`, `received`, `status`, `date_added`, `number`) VALUES
(1, 6, 'NTC', 'Wello', 0, 0, 0, 1, '2021-01-15 04:16:34.734170', '8734999934'),
(2, 6, 'NTC', 'Wello', 0, 0, 0, 1, '2021-01-15 04:17:58.298802', '5475431034'),
(3, 6, 'NTC', 'ggj', 0, 0, 0, 1, '2021-01-15 04:18:04.996677', '4841481626'),
(4, 6, 'NTC', 'great', 0, 0, 0, 1, '2021-01-15 04:22:40.193471', '5904333360'),
(5, 6, 'NTC', 'great', 0.191, 0, 0.045, 1, '2021-01-15 04:23:30.597163', '6794825241'),
(6, 6, 'NTC', 'ggj', 0, 0, 0, 1, '2021-01-19 05:46:42.994519', '9595740766'),
(7, 4, 'NTC', 'brucels', 0, 0, 0, 1, '2021-01-20 19:10:34.543620', '1328136873'),
(8, 4, 'NTC', 'fisher', 0.8429999999999999, 1.1569999999999998, 0, 1, '2021-01-20 19:12:15.689709', '9743311209'),
(10, 4, 'NTC', 'Default', 0, 0, 0, 1, '2021-01-22 21:19:37.492619', '9293219798'),
(11, 6, 'NTC', 'Default', 0, 0, 0, 1, '2021-01-22 21:20:28.238816', '8199651128'),
(12, 2, 'NTC', 'Default', 0, 0, 0, 1, '2021-01-23 02:32:10.901960', '2222455555'),
(13, 3, 'NTC', 'Default', 0, 0, 0, 1, '2021-02-05 03:59:50.300872', '9c46b710cc6f5c36ce402e40fb160d2c'),
(14, 7, 'NTC', 'Default', 0, 0, 0, 1, '2021-02-06 14:09:49.630506', '8701194694'),
(15, 25, 'NTC', 'Default', 0, 0, 0, 1, '2021-02-15 20:47:02.255663', '2986947545'),
(16, 26, 'NTC', 'Default', 0, 0, 0, 1, '2021-02-15 22:14:03.699241', '6243858417');

-- --------------------------------------------------------

--
-- Table structure for table `wallet_proofs`
--

CREATE TABLE `wallet_proofs` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `transaction_id` varchar(255) DEFAULT NULL,
  `pop` varchar(100) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `wallet_proofs`
--

INSERT INTO `wallet_proofs` (`id`, `user_id`, `email`, `transaction_id`, `pop`, `status`, `date_added`) VALUES
(2, 4, NULL, NULL, 'proofs/7.jpg', 0, '2021-01-11 21:52:18.875198'),
(3, 25, NULL, NULL, 'proofs/testimonial-5.jpg', 0, '2021-02-15 21:00:47.978128');

-- --------------------------------------------------------

--
-- Table structure for table `wallet_wallets`
--

CREATE TABLE `wallet_wallets` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `balance` double DEFAULT NULL,
  `sent` double DEFAULT NULL,
  `received` double DEFAULT NULL,
  `commission` double DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `date_added` datetime(6) NOT NULL,
  `pin` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `wallet_wallets`
--

INSERT INTO `wallet_wallets` (`id`, `user_id`, `type`, `balance`, `sent`, `received`, `commission`, `status`, `date_added`, `pin`) VALUES
(1, 6, 'NTC', 0.191, 0, 0.191, 0, 1, '2021-01-13 06:37:18.728486', 'pbkdf2_sha256$216000$LSUMPr4dEABO$j9MLVovZZos7meEKfSKfR5+OtXbTbCppMHRWzOFPTeQ='),
(2, 5, 'NTC', 0, 0, 0, 0, 1, '2021-01-13 17:53:29.031436', NULL),
(3, 4, 'NTC', 0.8429999999999999, 1.1569999999999998, 0, 0, 1, '2021-01-19 05:42:09.880597', 'pbkdf2_sha256$216000$4iUbr327wivE$W17Hs/mp1F6/scYtAuvLppgjI5vUaYFFCoMB/EmXbT4='),
(4, 2, 'NTC', 0, 0, 0, 0, 1, '2021-01-22 04:54:17.721146', NULL),
(5, 3, 'NTC', 0, 0, 0, 0, 1, '2021-02-05 03:59:50.210740', NULL),
(6, 7, 'NTC', 0, 0, 0, 0, 1, '2021-02-06 14:09:49.564549', NULL),
(7, 25, 'NTC', 0, 0, 0, 0.001, 1, '2021-02-15 20:47:02.135733', NULL),
(8, 26, 'NTC', 0, 0, 0, 0, 1, '2021-02-15 22:11:39.626753', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_resetpassword`
--
ALTER TABLE `auth_user_resetpassword`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_user_userlogs`
--
ALTER TABLE `auth_user_userlogs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `messenger_messages`
--
ALTER TABLE `messenger_messages`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `site_settings_currentprice`
--
ALTER TABLE `site_settings_currentprice`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `site_settings_sitesettings`
--
ALTER TABLE `site_settings_sitesettings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transactions_transactions`
--
ALTER TABLE `transactions_transactions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users_cards`
--
ALTER TABLE `users_cards`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `card_id` (`card_id`);

--
-- Indexes for table `users_referrals`
--
ALTER TABLE `users_referrals`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users_users`
--
ALTER TABLE `users_users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vendor_paymentmethods`
--
ALTER TABLE `vendor_paymentmethods`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vendor_vendors`
--
ALTER TABLE `vendor_vendors`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wallet_accountnums`
--
ALTER TABLE `wallet_accountnums`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `number` (`number`);

--
-- Indexes for table `wallet_proofs`
--
ALTER TABLE `wallet_proofs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wallet_wallets`
--
ALTER TABLE `wallet_wallets`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_resetpassword`
--
ALTER TABLE `auth_user_resetpassword`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;

--
-- AUTO_INCREMENT for table `auth_user_userlogs`
--
ALTER TABLE `auth_user_userlogs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `messenger_messages`
--
ALTER TABLE `messenger_messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `site_settings_currentprice`
--
ALTER TABLE `site_settings_currentprice`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `site_settings_sitesettings`
--
ALTER TABLE `site_settings_sitesettings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `transactions_transactions`
--
ALTER TABLE `transactions_transactions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `users_cards`
--
ALTER TABLE `users_cards`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_referrals`
--
ALTER TABLE `users_referrals`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users_users`
--
ALTER TABLE `users_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `vendor_paymentmethods`
--
ALTER TABLE `vendor_paymentmethods`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=127;

--
-- AUTO_INCREMENT for table `vendor_vendors`
--
ALTER TABLE `vendor_vendors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `wallet_accountnums`
--
ALTER TABLE `wallet_accountnums`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `wallet_proofs`
--
ALTER TABLE `wallet_proofs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `wallet_wallets`
--
ALTER TABLE `wallet_wallets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
