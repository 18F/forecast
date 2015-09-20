# Forecast

A MVP of a better version of http://www.gsa.gov/portal/content/101163.

## Planned Architecture

I currently envision the site to involve three components:

1. An interface for administrators/staff to add new oppportunities (Django admin interface).
2. A read-only REST API (Django-REST).
3. A static site using datatables.

# Front Site Organization

## What's displayed on front and is filterable
GSA Organization
Region
Award Status
Product or Service Description
Place of Performance (City)
Place of Performance (State)
Primary NAICS Code
Estimated Award Fiscal Year and Quarter
Socioeconomic Category

## What should be available on click-through
Contract Type
Procurement Method
Competition Strategy
From (Min)  To (Max)
Delivery Order Value
Incumbent Contractor Name (if applicable)
Contract/Order Number (if applicable)
New Requirement or Exercise of Option or Recompete
Estimated Solicitation Date
Link to Solicitation in FedBizOpps (if available) 
Point of Contact (Name)
Point of Contact (Email Address)
OSBU Small Business Technical Advisor (SBTA)  
Additional Information