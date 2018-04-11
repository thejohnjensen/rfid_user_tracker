# rfid_user_tracker
Build a RFID system that manages riders on a bus.

## User Stories:

USER:
1. As a user I want to be able to scan my card on an RFID reader to check on the bus - allowing the bus driver to know where I am supposed to get off.
    * [ ] RFID arduino scanner to simulate hardware.
    * [x] Must be able to send data to database.
    * [x] Database with users and bus stops.
2. As a user I want to be able to scan my card when I exit the bus to show I got off at the right destination.
    * [ ] Need to update DB as students exit the bus, maybe an active table?
3. As a user I want the bus driver to have a list of all students that are supposed to be on their bus, students actually on their bus, and notifications when students are supposed to get off.
    * [x] Simple front end with table showing list of students for that route, as they check in they become active(highlight?), as their destination i reached notification to driver is sent (highlight row?)
4. As a user I want to be able to access my previous trips to see: location on, location off, date and time.
    * [ ] user login to see their history.
    
DEVELOPER:
1. As a developer I want to use tools comparable to what Zonar’s team is using: Flask, PostgreSQL, Google Cloud, Docker, Pandas
2. As a developer I want to gain more architecture design experience so that my architecture will be simple yet scalable.
3. As a developer I want to follow common Agile methodology.
4. As a developer I want to demonstrate my domain knowledge.
5. As a developer I want to follow the SOLID principles for OOP design.
