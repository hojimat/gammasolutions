# Models and database structure
## Overview
The dash app has three main types of actors: Driver, Broker, Shipper. All of them share address, phone, and contact info. The latter two inherit from Company model. These three actors engage in transactions via Orders. Each order stems from Shipper who goes to Broker who gives load to the Driver. Order covers all load and route information. Driver has a truck and a trailer as part of an Equipment class. There are also Documents that belong to Order (bill of lading, invoice), Driver (license, insurance etc.), and Broker/Shipper (agreement etc.) 

## Why no formsets for dynamic creation of Equipment?
Because adding equipment will be the least frequent operation ever. There will be at most 10 drivers with 1 truck and 2 trailers, which makes it 30 entries at most. Separate entry avoids complexity and formsets.
Plus page view instead of table view allows for image or document uploads.
