import json

regions = [
  "R1 - New England Region",
  "R2 - Northeast and Caribbean Region",
  "R3 - Mid-Atlantic Region",
  "R4 - Southeast Sunbelt Region",
  "R5 - Great Lakes Region",
  "R6 - The Heartland Region",
  "R7 - Greater Southwest Region",
  "R8 - Rocky Mountain Region",
  "R9 - Pacific Rim Region",
  "R10 - Northwest Arctic Region",
  "NCR - National Capital Region",
  "Central Office"
]

organizations = [
  "PBS-Public Buildings Service",
  "FAS-Federal Acquisition Service",
  "FAS-Office of General Supplies and Services",
  "FAS-Office of Assisted Acquisition Services",
  "CPO-Office of the Chief People Officer",
  "CFO-Chief Financial Officer",
  "OCSIT-Office of Citizen Services and Innovative Technologies",
  "OGP-Office of Government-wide Policy",
  "OAS-Office of Administrative Services",
  "CIO-Office of the Chief Information Officer",
  "FAS-Office of the Chief Information Officer",
  "FAS-Office of Integrated Technology Services",
  "FAS-Office of Strategy Management",
  "FAS-Office of Travel, Motor Vehicle and Card Services",
  "FAS-Office of Customer Accounts and Research"
]

out = []

for reg in regions:
    for org in organizations:
        out.append(
            {
                "model": "opportunities.office",
                "fields": {
                        "organization": org, "region": reg
                }
            }
        )

print(json.dumps(out, indent=2))
