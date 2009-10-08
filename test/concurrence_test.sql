use concurrence_test;

CREATE TABLE `tbltest` (
  `test_id` int(11) NOT NULL,
  `test_string` varchar(1024) NOT NULL,
  `test_blob` longblob NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

CREATE TABLE `tblautoincint` (
  `test_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `test_string` varchar(1024) NOT NULL,
  PRIMARY KEY(test_id)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

CREATE TABLE `tblautoincbigint` (
  `test_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `test_string` varchar(1024) NOT NULL,
  PRIMARY KEY(test_id)  
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

GRANT ALL on concurrence_test.* to 'concurrence_test'@'localhost' identified by 'concurrence_test';
