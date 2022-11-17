-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-11-2022 a las 15:37:39
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `rh`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `documentos`
--

CREATE TABLE `documentos` (
  `iddocumentos` int(20) NOT NULL,
  `descripciondocumentos` varchar(50) NOT NULL,
  `juego` varchar(70) DEFAULT NULL,
  `usuario` varchar(70) DEFAULT NULL,
  `discord` varchar(70) DEFAULT NULL,
  `tipo` varchar(70) DEFAULT NULL,
  `horario` time(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `documentos`
--

INSERT INTO `documentos` (`iddocumentos`, `descripciondocumentos`, `juego`, `usuario`, `discord`, `tipo`, `horario`) VALUES
(5, 'xbox', NULL, NULL, NULL, NULL, NULL),
(6, 'xbox', NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escolaridad`
--

CREATE TABLE `escolaridad` (
  `idescolaridad` int(20) NOT NULL,
  `descripcionescolaridad` varchar(50) NOT NULL,
  `edad` varchar(2) DEFAULT NULL,
  `genero` varchar(70) DEFAULT NULL,
  `correo` varchar(70) DEFAULT NULL,
  `fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `escolaridad`
--

INSERT INTO `escolaridad` (`idescolaridad`, `descripcionescolaridad`, `edad`, `genero`, `correo`, `fecha`) VALUES
(11, 'juana', '70', 'Multiplayer', 'thejean@gmail', '2014-03-04');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `documentos`
--
ALTER TABLE `documentos`
  ADD PRIMARY KEY (`iddocumentos`);

--
-- Indices de la tabla `escolaridad`
--
ALTER TABLE `escolaridad`
  ADD PRIMARY KEY (`idescolaridad`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `documentos`
--
ALTER TABLE `documentos`
  MODIFY `iddocumentos` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `escolaridad`
--
ALTER TABLE `escolaridad`
  MODIFY `idescolaridad` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
