CREATE TABLE `topics` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic_title` varchar(255) NOT NULL,
  `topic_url` varchar(255) NOT NULL,
  `topic_messages_text` longblob NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1580 DEFAULT CHARSET=latin1;
