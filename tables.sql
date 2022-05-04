CREATE TABLE VISITOR(
  Visitor_name VARCHAR(30),
  user_name VARCHAR(30),
  password VARCHAR(30),
  address VARCHAR(30),
  city VARCHAR(30),
  email_id VARCHAR(30),
  phone_number VARCHAR(30),
  V_id INTEGER NOT NULL AUTO_INCREMENT,
  infected BOOL,
  PRIMARY KEY(V_id)
);

CREATE TABLE PLACE(
  Place_name VARCHAR(30),
  user_name VARCHAR(30),
  password VARCHAR(30),
  address VARCHAR(30),
  city VARCHAR(30),
  email_id VARCHAR(30),
  qr VARCHAR(30),
  phone_number VARCHAR(30),
  P_id INTEGER NOT NULL AUTO_INCREMENT,
  PRIMARY KEY(P_id)
);

CREATE TABLE VISITOR_TO_PLACE(
  visit_id INTEGER NOT NULL AUTO_INCREMENT,
  
  entry_date DATE,
  exit_date DATE,
  entry_time VARCHAR(30),
  exit_time VARCHAR(30),
  V_id INTEGER NOT NULL,
  P_id INTEGER NOT NULL,
  PRIMARY KEY(visit_id),
  FOREIGN KEY(V_id) REFERENCES VISITOR(V_id) ON DELETE CASCADE,
  FOREIGN KEY(P_id) REFERENCES PLACE(P_id) ON DELETE CASCADE
);

CREATE TABLE AGENT(
  user__name VARCHAR(30),
  password_address VARCHAR(30),
  Agent_id INTEGER NOT NULL AUTO_INCREMENT,
  PRIMARY KEY(Agent_id)
);

CREATE TABLE HOSPITAL(
  Hospital_name VARCHAR(30),
  user_name VARCHAR(30),
  password VARCHAR(30),
  address VARCHAR(30),
  city VARCHAR(30),
  email_id VARCHAR(30),
  phone_number VARCHAR(30),
  H_id INTEGER NOT NULL AUTO_INCREMENT,
  PRIMARY KEY(H_id)
);