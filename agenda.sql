-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-09-2022 a las 03:11:20
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
-- Base de datos: `agenda`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comenta`
--

CREATE TABLE `comenta` (
  `id` int(50) NOT NULL,
  `usuario` varchar(70) NOT NULL,
  `correo` varchar(80) NOT NULL,
  `comentarios` varchar(300) NOT NULL,
  `telefono` varchar(40) DEFAULT NULL,
  `asunto` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `comenta`
--

INSERT INTO `comenta` (`id`, `usuario`, `correo`, `comentarios`, `telefono`, `asunto`) VALUES
(9, 'jean', 'thejeanpollo@gmail.com', 'Me robo el corazon mi novia hermosa', '4491422521', 'robo');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `comenta`
--
ALTER TABLE `comenta`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `comenta`
--
ALTER TABLE `comenta`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
