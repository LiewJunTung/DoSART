CREATE TABLE `Log` (
	`l_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`l_ip`	TEXT,
	`l_os`	INTEGER REFERENCES OperatingSystem(os_id),
	`l_port`	INTEGER,
	`l_method`	INTEGER REFERENCES attackMethod(atk_id),
	`l_atkduration`	INTEGER,
	`l_sensitivity`	INTEGER,
	`l_fixapplied`	TEXT,
	`l_status`	TEXT,
	`l_result`	TEXT,
	`l_img`	TEXT,
	`l_timestamp`	DATETIME DEFAULT 'CURRENT_TIMESTAMP'
);