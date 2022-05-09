# Models and database structure
## Overview
The dash app has three main types of actors: Driver, Broker, Shipper. All of them share address, phone, and contact info. The latter two inherit from Company model. These three actors engage in transactions via Orders. Each order stems from Shipper who goes to Broker who gives load to the Driver. Order covers all load and route information. Driver has a truck and a trailer as part of an Equipment class. There are also Documents that belong to Order (bill of lading, invoice), Driver (license, insurance etc.), and Broker/Shipper (agreement etc.) 

## Why three document models?
Documents can belong to Driver, Customer, Order. So, why didn't I use contenttypes and generic relations? Because the database is far more important than the codebase. Combining tables would be far easier in the future than filtering out pieces later on. Plus, adding three Document models is easier to maintain than dealing with headaches of the framework I do not really understand.

