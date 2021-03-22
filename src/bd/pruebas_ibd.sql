-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 01-12-2020 a las 17:49:03
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `Biblioteca`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autor`
--

CREATE TABLE `autor` (
  `IDautor` smallint(6) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `pais` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `autor`
--

INSERT INTO `autor` (`IDautor`, `nombre`, `pais`) VALUES
(1, 'Abraham Silberschatz', 'Israel'),
(2, 'Henry F. Korth', 'Estados Unidos'),
(3, 'S. Sudarshan', 'India'),
(25, 'Ma. Consuelo Jimenez', 'México'),
(56, 'José G. Mendoza', 'Italia'),
(69, 'Ezequiel Ander Egg', 'Alemania');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escribe`
--

CREATE TABLE `escribe` (
  `IDlibro` smallint(6) NOT NULL,
  `IDautor` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `escribe`
--

INSERT INTO `escribe` (`IDlibro`, `IDautor`) VALUES
(1, 1),
(1, 2),
(1, 3),
(19, 56),
(101, 25),
(234, 69);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante`
--

CREATE TABLE `estudiante` (
  `IDestudiante` smallint(6) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `telefono` varchar(10) NOT NULL,
  `carrera` varchar(15) NOT NULL,
  `fechaNacimiento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estudiante`
--

INSERT INTO `estudiante` (`IDestudiante`, `nombre`, `direccion`, `telefono`, `carrera`, `fechaNacimiento`) VALUES
(1, 'Irving Cruz Matías', 'Av. Ignacio Morones Prieto 4500', '8112345678', 'Computación', '2000-01-01'),
(46, 'José Armando Berlanga Mendoza', 'Iris 114 colonia Cuahtemoc', '8127248808', 'Contabilidad', '2001-02-11'),
(98, 'Fresia Milipza Perez Garza', 'Cto Versalles 157 sec Frances', '8123313209', 'Arte', '2001-06-10');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libro`
--

CREATE TABLE `libro` (
  `IDLibro` smallint(6) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `editorial` varchar(30) NOT NULL,
  `area` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `libro`
--

INSERT INTO `libro` (`IDLibro`, `titulo`, `editorial`, `area`) VALUES
(1, 'Fundamentos de Bases de Datos', 'McGraw-Hill', 'Computación'),
(19, 'Fundamentos del arte', 'Editorial Santillana', 'Arte'),
(101, 'Introducción a raptor', 'Ediciones DeLaurel', 'Computación'),
(234, 'Introducción a las leyes II', 'Editorial Geometría', 'Derecho');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamo`
--

CREATE TABLE `prestamo` (
  `IDestudiante` smallint(6) NOT NULL,
  `IDlibro` smallint(6) NOT NULL,
  `fechaPrestamo` date NOT NULL,
  `fechaDevolucion` date DEFAULT NULL,
  `devuelto` bit(1) DEFAULT b'0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `prestamo`
--

INSERT INTO `prestamo` (`IDestudiante`, `IDlibro`, `fechaPrestamo`, `fechaDevolucion`, `devuelto`) VALUES
(1, 1, '2020-11-30', '2020-11-30', b'1'),
(46, 101, '2020-11-27', '2020-12-01', b'1'),
(98, 19, '2020-12-01', '2020-12-12', b'0'),
(98, 234, '2020-12-01', '2020-12-12', b'1');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `autor`
--
ALTER TABLE `autor`
  ADD PRIMARY KEY (`IDautor`);

--
-- Indices de la tabla `escribe`
--
ALTER TABLE `escribe`
  ADD PRIMARY KEY (`IDlibro`,`IDautor`),
  ADD KEY `IdAutor` (`IDautor`);

--
-- Indices de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`IDestudiante`);

--
-- Indices de la tabla `libro`
--
ALTER TABLE `libro`
  ADD PRIMARY KEY (`IDLibro`);

--
-- Indices de la tabla `prestamo`
--
ALTER TABLE `prestamo`
  ADD PRIMARY KEY (`IDestudiante`,`IDlibro`,`fechaPrestamo`),
  ADD KEY `IdLibro` (`IDlibro`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `autor`
--
ALTER TABLE `autor`
  MODIFY `IDautor` smallint(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=70;

--
-- AUTO_INCREMENT de la tabla `libro`
--
ALTER TABLE `libro`
  MODIFY `IDLibro` smallint(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=235;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `escribe`
--
ALTER TABLE `escribe`
  ADD CONSTRAINT `escribe_ibfk_1` FOREIGN KEY (`IDautor`) REFERENCES `autor` (`IDautor`),
  ADD CONSTRAINT `escribe_ibfk_2` FOREIGN KEY (`IDlibro`) REFERENCES `libro` (`IDLibro`);

--
-- Filtros para la tabla `prestamo`
--
ALTER TABLE `prestamo`
  ADD CONSTRAINT `prestamo_ibfk_1` FOREIGN KEY (`IDestudiante`) REFERENCES `estudiante` (`IDestudiante`),
  ADD CONSTRAINT `prestamo_ibfk_2` FOREIGN KEY (`IDlibro`) REFERENCES `libro` (`IDLibro`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
