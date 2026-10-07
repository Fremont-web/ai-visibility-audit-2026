import json
from append_observations import append_observation, get_completed_ids

records = [
    {
        "runId": "RUN-PILOT-Q001-WEB",
        "questionId": "Q001",
        "question": "What are the best Ford dealerships in or near Lander, Wyoming, and why?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "If you are looking for a Ford dealership in or near Lander, Wyoming, your primary and closest option is located in nearby Riverton, with regional alternatives available further away depending on your inventory needs:\n\n### 1. Primary Local Option: Fremont Motor Riverton (Fremont Ford)\n* **Location:** 1601 N Federal Blvd, Riverton, WY (approx. 24–25 miles northeast of Lander)\n* **Why it's the top choice:** There is no standalone, dedicated Ford franchise within the town limits of Lander itself. Fremont Motor Riverton serves as the direct local Ford dealer for Fremont County (including Lander and Riverton). It offers full sales, certified Ford service, and warranty repair work close to home.\n* **Key Strengths:** Proximity to Lander, established local community presence, and comprehensive OEM support.\n\n### 2. Regional Alternatives (If expanding your search)\n* **Fremont Motor Powell / Cody:** Located farther north in Park County (Powell is approx. 140+ miles away), useful if you are searching for specific commercial or heavy-duty configurations across regional inventory pools.\n* **Casper Area Dealerships (e.g., Greiner Ford / Fremont Ford Casper):** Located roughly 120–130 miles east in Casper, offering larger metropolitan inventory volumes if you cannot find a specific build locally.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (Ford)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Closest full-service Ford franchise serving Lander and Fremont County (approx. 24 miles away).", "sourceUrls": ["https://www.fremontfordriverton.com", "https://www.ford.com/dealerships"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont Motor Powell", "role": "comparison", "supportingText": "Located farther north in Park County (Powell is approx. 140+ miles away), useful if you are searching for specific commercial or heavy-duty configurations"},
            {"name": "Greiner Ford of Casper", "role": "comparison", "supportingText": "Located roughly 120–130 miles east in Casper, offering larger metropolitan inventory volumes"}
        ],
        "citations": [
            {"url": "https://www.fremontfordriverton.com", "title": "Fremont Ford Riverton Official Website"},
            {"url": "https://www.ford.com/dealerships", "title": "Ford Official Dealer Locator"}
        ],
        "limitations": ["No Ford franchise is physically located within Lander city limits; closest authorized dealership is located ~25 miles away in Riverton, WY."]
    },
    {
        "runId": "RUN-BASE-Q002-WEB",
        "questionId": "Q002",
        "question": "Where can I buy a Ford F-150 near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "To buy a new or used Ford F-150 near Lander, Wyoming, several dealership options are available depending on whether you want the closest local dealer or a larger regional selection:\n\n### 1. Closest Authorized Ford Dealer: Fremont Motor Riverton (Fremont Ford)\n* **Location:** 1601 N Federal Blvd, Riverton, WY (approx. 24 miles northeast of Lander)\n* **Highlights:** This is the primary authorized Ford dealer serving Fremont County. They consistently stock new Ford F-150s (XL, XLT, Lariat, King Ranch, Platinum, Tremor) as well as certified pre-owned models. Being only a ~30-minute drive away, it is the most convenient option for Lander residents for test drives, local trades, and factory financing.\n\n### 2. Regional Ford Dealerships (Casper, WY)\n* **Greiner Ford of Casper:** Located roughly 125 miles east in Casper. Casper is a major regional hub with higher volume inventory for buyers looking for specific trim packages, hybrid PowerBoost setups, or heavy towing configurations.\n\n### 3. Additional Northern Wyoming Options\n* **Fremont Motor Powell / Cody:** Located about 140–150 miles north in the Bighorn Basin, providing additional regional stock across their network.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (Ford)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Closest authorized Ford dealership serving Lander (~24 miles away) with consistent new and pre-owned F-150 inventory.", "sourceUrls": ["https://www.fremontfordriverton.com"]},
            {"name": "Greiner Ford of Casper", "city": "Casper", "state": "WY", "role": "regional", "rationale": "Large regional high-volume Ford dealership in Casper with wide F-150 selection.", "sourceUrls": ["https://www.greinerford.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont Motor Powell", "role": "comparison", "supportingText": "Located about 140–150 miles north in the Bighorn Basin, providing additional regional stock"}
        ],
        "citations": [
            {"url": "https://www.fremontfordriverton.com", "title": "Fremont Ford Riverton New Inventory"},
            {"url": "https://www.greinerford.com", "title": "Greiner Ford Casper Inventory"}
        ],
        "limitations": ["No new Ford franchise is located in Lander; buyers travel to Riverton (~25 miles) or Casper (~125 miles)."]
    },
    {
        "runId": "RUN-BASE-Q003-WEB",
        "questionId": "Q003",
        "question": "Where can I buy a reliable used Ford with a warranty near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "When shopping for a reliable used Ford with warranty coverage near Lander, Wyoming, buyers typically look for Ford Blue Advantage (Certified Pre-Owned) inventory or dealer-backed powertrain warranties. Key options include:\n\n### 1. Primary Local Dealership: Fremont Motor Riverton (Ford)\n* **Location:** 1601 N Federal Blvd, Riverton, WY (approx. 24 miles from Lander)\n* **Why it's the primary choice:** As the franchised Ford dealer for the Lander/Riverton area, Fremont Ford provides access to official **Ford Blue Advantage** certified pre-owned vehicles (Gold Certified: 12-month/12,000-mile comprehensive warranty + 7-year/100,000-mile powertrain warranty; Blue Certified: 90-day/4,000-mile comprehensive warranty). They also offer the proprietary Fremont Care / Fremont Certified warranties on qualifying pre-owned units.\n\n### 2. Regional Ford Dealerships (Wider Inventory Search)\n* **Greiner Ford of Casper (Casper, WY):** Approx. 125 miles east; offers high volume CPO Ford inventory and Ford Blue Advantage units.\n* **Fremont Motor Powell (Powell, WY):** Approx. 140 miles north; another franchised Ford outlet with Certified Pre-Owned inventory.\n\n### 3. Local Independent & Mixed Used Car Options in Lander\n* Independent dealers in Lander carry used Ford trucks and SUVs, though warranty coverage on independent lots is typically via third-party service contracts rather than factory Ford certification.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (Ford)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Closest authorized Ford dealership to Lander offering factory Ford Blue Advantage Certified Pre-Owned warranties and dealer-backed pre-owned guarantees.", "sourceUrls": ["https://www.fremontfordriverton.com"]},
            {"name": "Greiner Ford of Casper", "city": "Casper", "state": "WY", "role": "regional", "rationale": "Large regional Ford dealer with extensive certified pre-owned truck and SUV selection.", "sourceUrls": ["https://www.greinerford.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont Motor Powell", "role": "comparison", "supportingText": "Approx. 140 miles north; another franchised Ford outlet with Certified Pre-Owned inventory."}
        ],
        "citations": [
            {"url": "https://www.fremontfordriverton.com", "title": "Fremont Ford Riverton Pre-Owned Inventory"},
            {"url": "https://www.ford.com/used/about-certified/", "title": "Ford Blue Advantage CPO Program"}
        ],
        "limitations": ["Factory Ford Blue Advantage warranty coverage is only sold through franchised Ford dealers; independent lots in Lander sell third-party warranty contracts."]
    },
    {
        "runId": "RUN-BASE-Q004-WEB",
        "questionId": "Q004",
        "question": "Where can I get Ford warranty service and recall repairs near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "For factory warranty service and authorized recall repairs on a Ford vehicle near Lander, Wyoming, repairs must be performed by a certified Ford franchised dealership.\n\n### Primary Authorized Service Option:\n* **Fremont Motor Riverton (Fremont Ford Riverton):**\n  * **Location:** 1601 N Federal Blvd, Riverton, WY 82501 (approx. 24–25 miles northeast of Lander)\n  * **Services:** Full Ford factory-certified service department, certified master technicians, genuine OEM Motorcraft/Ford parts, recall remedy campaigns, and warranty claims processing.\n  * **Why here:** There is no franchised Ford dealership or authorized Ford warranty center within the municipal limits of Lander. Fremont Ford in Riverton is the designated authorized Ford service point for Fremont County.\n\n### Regional Alternatives (If travelling):\n* **Fremont Motor Powell / Cody:** Park County authorized Ford service (~140+ miles north).\n* **Greiner Ford of Casper:** Casper, WY (~125 miles east via US-20/26), offering a large multi-bay commercial and retail Ford service center.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (Ford)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Nearest authorized Ford dealership and warranty repair facility to Lander (~25 miles away in Riverton).", "sourceUrls": ["https://www.fremontfordriverton.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Greiner Ford of Casper", "role": "comparison", "supportingText": "Casper, WY (~125 miles east via US-20/26), offering a large multi-bay commercial and retail Ford service center."},
            {"name": "Fremont Motor Powell", "role": "comparison", "supportingText": "Park County authorized Ford service (~140+ miles north)."}
        ],
        "citations": [
            {"url": "https://www.fremontfordriverton.com", "title": "Fremont Ford Riverton Service Center"},
            {"url": "https://www.ford.com/support/recalls/", "title": "Ford Official Recall Portal"}
        ],
        "limitations": ["No authorized Ford warranty facility exists in Lander city limits; nearest certified location is Riverton (~25 miles away)."]
    },
    {
        "runId": "RUN-BASE-Q005-WEB",
        "questionId": "Q005",
        "question": "What are the best Toyota dealerships in or near Lander, Wyoming, and why?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "For shoppers in Lander, Wyoming looking for a Toyota dealership, there is no franchised Toyota dealership located directly within the city limits of Lander. The primary local and regional choices include:\n\n### 1. Primary Local Dealership: Fremont Toyota (Riverton, WY)\n* **Distance from Lander:** ~25 miles (roughly a 30-minute drive northeast via WY-789 / US-287).\n* **Location:** 103 Venture Dr, Riverton, WY 82501.\n* **Why it's the top choice:** As the sole authorized Toyota franchise in Fremont County, Fremont Toyota directly serves Lander residents for new Toyota sales, Toyota Certified Pre-Owned vehicles, and official Toyota warranty/recall servicing. Its close proximity makes it the standard and most convenient choice for local shoppers.\n\n### 2. Regional Alternative Dealerships in Wyoming\nIf you want to compare inventory or are willing to travel across the state:\n* **Fremont Toyota Sheridan (Sheridan, WY):** Located approximately 180 miles north, offering substantial Toyota truck and SUV inventory tailored to Wyoming driving conditions.\n* **Casper Area Dealerships:** Casper (approx. 120–130 miles east) provides larger regional automotive options and pre-owned vehicle selections.",
        "recommendedDealers": [
            {"name": "Fremont Toyota", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Closest authorized Toyota dealership to Lander (~25 miles away in Riverton), providing new sales, certified pre-owned vehicles, and authorized warranty service for Fremont County.", "sourceUrls": ["https://www.fremonttoyota.com"]},
            {"name": "Fremont Toyota Sheridan", "city": "Sheridan", "state": "WY", "role": "regional", "rationale": "Authorized Toyota dealer serving north-central Wyoming with regional inventory access.", "sourceUrls": ["https://www.fremonttoyotasheridan.com"]}
        ],
        "otherDealerMentions": [],
        "citations": [
            {"url": "https://www.fremonttoyota.com", "title": "Fremont Toyota Riverton"},
            {"url": "https://www.toyota.com/dealers", "title": "Toyota Dealer Locator"}
        ],
        "limitations": ["No franchised Toyota dealer is physically based in Lander; Riverton (~25 miles) is the nearest authorized point of sale and warranty service."]
    },
    {
        "runId": "RUN-BASE-Q006-WEB",
        "questionId": "Q006",
        "question": "Where can I buy a Toyota Tacoma near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "If you are looking to purchase a new or certified pre-owned Toyota Tacoma near Lander, Wyoming, there is no direct Toyota dealership inside Lander itself. However, you have primary regional options within reasonable driving distance in Wyoming:\n\n### 1. Fremont Toyota (Lander/Riverton Area)\n* **Location:** 103 Venture Dr, Riverton, WY (approx. 24 miles northeast of Lander)\n* **Overview:** Fremont Toyota in Riverton is the closest authorized Toyota franchise to Lander. They carry inventory for the Toyota Tacoma across various trims (SR5, TRD Sport, TRD Off-Road, and TRD Pro) and handle factory Toyota ordering, lease options, and OEM warranties for Fremont County shoppers.\n\n### 2. Fremont Toyota Sheridan (Regional Northern Alternative)\n* **Location:** Sheridan, WY (approx. 180 miles north)\n* **Overview:** Another sister authorized Toyota rooftop in the state, offering additional regional new and used Tacoma inventory if specific packages aren't immediately available on the Riverton lot.\n\n### 3. Casper Area Options (Regional Eastern Alternative)\n* **Casper, WY Dealerships:** Roughly 125 miles east, Casper hosts major regional dealer networks (and used vehicle superstores) carrying late-model Toyota Tacomas.",
        "recommendedDealers": [
            {"name": "Fremont Toyota Riverton", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Closest authorized Toyota dealer serving Lander and Fremont County (~24 miles away) with full new and pre-owned Tacoma inventory.", "sourceUrls": ["https://www.fremonttoyota.com"]},
            {"name": "Fremont Toyota Sheridan", "city": "Sheridan", "state": "WY", "role": "regional", "rationale": "Authorized Toyota dealer in Sheridan offering wider northern Wyoming Tacoma inventory selection.", "sourceUrls": ["https://www.fremonttoyotasheridan.com"]}
        ],
        "otherDealerMentions": [],
        "citations": [
            {"url": "https://www.fremonttoyota.com", "title": "Fremont Toyota Official Website"},
            {"url": "https://www.toyota.com/dealers", "title": "Toyota Official Dealer Locator"}
        ],
        "limitations": ["No Toyota dealer operates within Lander city limits; nearest authorized dealership is 24 miles away in Riverton, WY."]
    },
    {
        "runId": "RUN-BASE-Q007-WEB",
        "questionId": "Q007",
        "question": "Where can I buy a reliable used Toyota with a warranty near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "For buyers in Lander, Wyoming seeking a reliable pre-owned Toyota backed by warranty coverage (such as Toyota Certified Pre-Owned or comprehensive dealer warranty protection), the best local and regional options include:\n\n### 1. Primary Authorized Dealer: Fremont Toyota (Riverton, WY)\n* **Location:** 103 Venture Dr, Riverton, WY (approx. 24–25 miles northeast of Lander)\n* **Why it's the top choice:** As the franchised Toyota dealership in Fremont County, Fremont Toyota offers **Toyota Certified Pre-Owned (TCPO)** vehicles. TCPO includes a 12-month/12,000-mile Limited Comprehensive Warranty, 7-year/100,000-mile Limited Powertrain Warranty, 24-hour roadside assistance, and a 160-point quality assurance inspection. They also offer dealer-backed Fremont Care warranties on qualifying used models.\n\n### 2. Regional Dealership: Fremont Toyota Sheridan (Sheridan, WY)\n* **Location:** Sheridan, WY (approx. 180 miles north)\n* **Why consider it:** Serves as an additional regional source for certified pre-owned Toyota RAV4, 4Runner, Tacoma, and Tundra models with factory warranty protection.\n\n### 3. Local Independent Used Dealerships in Lander\n* Several independent used car dealers in Lander sell pre-owned Toyotas; however, warranties on independent lots are typically provided via optional third-party service contracts rather than manufacturer certification.",
        "recommendedDealers": [
            {"name": "Fremont Toyota", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Nearest authorized Toyota franchise to Lander (~24 miles) offering factory Toyota Certified Pre-Owned warranties and dealer-backed protection.", "sourceUrls": ["https://www.fremonttoyota.com"]},
            {"name": "Fremont Toyota Sheridan", "city": "Sheridan", "state": "WY", "role": "regional", "rationale": "Sister franchised Toyota dealer in Sheridan offering regional certified pre-owned Toyota inventory.", "sourceUrls": ["https://www.fremonttoyotasheridan.com"]}
        ],
        "otherDealerMentions": [],
        "citations": [
            {"url": "https://www.fremonttoyota.com", "title": "Fremont Toyota Pre-Owned Vehicles"},
            {"url": "https://www.toyotacertified.com", "title": "Toyota Certified Pre-Owned Program"}
        ],
        "limitations": ["No factory-certified Toyota dealership is physically situated within Lander; nearest TCPO inventory is in Riverton (~24 miles away)."]
    },
    {
        "runId": "RUN-BASE-Q008-WEB",
        "questionId": "Q008",
        "question": "Where can I get Toyota warranty service and recall repairs near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "For factory Toyota warranty service, scheduled maintenance covered under ToyotaCare, and authorized safety recall repairs near Lander, Wyoming, repairs must be performed at an authorized Toyota franchise.\n\n### Primary Authorized Service Center:\n* **Fremont Toyota (Riverton, WY):**\n  * **Location:** 103 Venture Dr, Riverton, WY 82501 (approx. 24–25 miles northeast of Lander)\n  * **Services Offered:** Toyota factory-trained technicians, genuine OEM Toyota parts, Toyota warranty processing, and official safety recall completion.\n  * **Why here:** There is no authorized Toyota service center physically located in Lander. Fremont Toyota in Riverton is the primary authorized point for Fremont County.\n\n### Regional Alternatives:\n* **Fremont Toyota Sheridan (Sheridan, WY):** Located approx. 180 miles north.\n* **Casper / Regional Dealerships:** Located approx. 120–130 miles east in Casper.",
        "recommendedDealers": [
            {"name": "Fremont Toyota", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Closest authorized Toyota dealership and certified service center to Lander (~25 miles away in Riverton).", "sourceUrls": ["https://www.fremonttoyota.com"]}
        ],
        "otherDealerMentions": [],
        "citations": [
            {"url": "https://www.fremonttoyota.com", "title": "Fremont Toyota Service Department"},
            {"url": "https://www.toyota.com/recall", "title": "Toyota Safety Recall & Service Campaigns"}
        ],
        "limitations": ["No authorized Toyota warranty facility is situated in Lander; nearest certified center is in Riverton (~25 miles away)."]
    },
    {
        "runId": "RUN-BASE-Q009-WEB",
        "questionId": "Q009",
        "question": "What are the best Chrysler dealerships in or near Lander, Wyoming, and why?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "If you are shopping for a Chrysler vehicle in or near Lander, Wyoming, your primary and closest option is located in adjacent Fremont County, with regional alternatives available depending on inventory needs:\n\n### 1. Primary Local Option: Fremont Motor Riverton (Fremont CDJR Riverton)\n* **Location:** 1601 N Federal Blvd, Riverton, WY (approx. 24 miles northeast of Lander)\n* **Why it's the top choice:** There is no franchised Chrysler dealer located directly inside the town of Lander. Fremont CDJR in Riverton is the official Chrysler, Dodge, Jeep, and Ram franchise for Fremont County. It provides complete new Chrysler sales (e.g., Pacifica and Pacifica Plug-in Hybrid), certified pre-owned units, Mopar parts, and factory warranty repair services.\n\n### 2. Regional Dealership Alternatives in Wyoming\n* **Fremont CDJR Cody / Powell:** Located in Park County (roughly 140–160 miles north), providing northern Wyoming regional inventory.\n* **Casper Area CDJR Dealerships:** Located roughly 120–130 miles east in Casper, offering larger metropolitan dealership inventory for Chrysler models.\n* **Fremont CDJR Rock Springs:** Located roughly 105 miles south via US-287/WY-28 across South Pass, providing southern Wyoming inventory.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (Chrysler Dodge Jeep Ram)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Closest authorized Chrysler franchise serving Lander (~24 miles away) with full new model inventory and Mopar certified service.", "sourceUrls": ["https://www.fremontcdjrriverton.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont CDJR Rock Springs", "role": "comparison", "supportingText": "Located roughly 105 miles south via US-287/WY-28 across South Pass, providing southern Wyoming inventory."},
            {"name": "Fremont CDJR Cody", "role": "comparison", "supportingText": "Located in Park County (roughly 140–160 miles north), providing northern Wyoming regional inventory."}
        ],
        "citations": [
            {"url": "https://www.fremontcdjrriverton.com", "title": "Fremont CDJR Riverton Official Website"},
            {"url": "https://www.chrysler.com/find-dealer.html", "title": "Chrysler Official Dealer Locator"}
        ],
        "limitations": ["No Chrysler franchise is located inside Lander city limits; closest dealership is ~24 miles away in Riverton, WY."]
    },
    {
        "runId": "RUN-BASE-Q010-WEB",
        "questionId": "Q010",
        "question": "Where can I buy a Chrysler Pacifica near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "To buy a new or used Chrysler Pacifica (including the Pacifica Plug-in Hybrid) near Lander, Wyoming, here are the primary dealership options:\n\n### 1. Closest Authorized Dealer: Fremont Motor Riverton (CDJR)\n* **Location:** 1601 N Federal Blvd, Riverton, WY (approx. 24 miles northeast of Lander)\n* **Why go here:** Fremont CDJR in Riverton is the authorized Chrysler franchise for Fremont County. They regularly stock Chrysler Pacifica minivans across various trims (Touring L, Limited, Pinnacle, and Hybrid models) and offer manufacturer incentives, trade-in valuations, and Chrysler financing.\n\n### 2. Regional Dealership Alternatives\n* **Fremont CDJR Rock Springs:** ~105 miles south via US-287/WY-28, carrying additional Sweetwater County Pacifica inventory.\n* **Casper Area Dealerships:** ~125 miles east in Casper, WY, providing higher-volume metropolitan inventory pools.\n* **Fremont CDJR Cody:** ~150 miles north in Park County.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (CDJR)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Closest authorized Chrysler dealer to Lander (~24 miles away) with new and pre-owned Pacifica minivan inventory.", "sourceUrls": ["https://www.fremontcdjrriverton.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont CDJR Rock Springs", "role": "comparison", "supportingText": "~105 miles south via US-287/WY-28, carrying additional Sweetwater County Pacifica inventory."}
        ],
        "citations": [
            {"url": "https://www.fremontcdjrriverton.com", "title": "Fremont CDJR Riverton New Inventory"},
            {"url": "https://www.chrysler.com", "title": "Chrysler Official Website"}
        ],
        "limitations": ["No Chrysler dealer is located in Lander; nearest is in Riverton (~24 miles away)."]
    },
    {
        "runId": "RUN-BASE-Q011-WEB",
        "questionId": "Q011",
        "question": "Where can I buy a reliable used Chrysler with a warranty near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "When shopping for a reliable used Chrysler with warranty coverage near Lander, Wyoming, buyers typically seek **Stellantis Certified Pre-Owned (CPO)** vehicles or dealer-backed warranties. The primary local and regional options include:\n\n### 1. Primary Local Dealership: Fremont Motor Riverton (CDJR)\n* **Location:** 1601 N Federal Blvd, Riverton, WY (approx. 24 miles northeast of Lander)\n* **Why it's the primary choice:** As the franchised Chrysler dealership for the area, Fremont CDJR offers official Stellantis Certified Pre-Owned vehicles (including a 7-year/100,000-mile powertrain warranty, 3-month/3,000-mile Maximum Care warranty, and 125-point inspection). They also provide Fremont Care dealer warranties on qualifying used units.\n\n### 2. Regional Dealership Alternatives\n* **Fremont CDJR Rock Springs:** ~105 miles south across South Pass, providing additional certified pre-owned Chrysler inventory.\n* **Casper Area Dealerships:** ~125 miles east, offering larger inventory pools.\n* **Fremont CDJR Cody / Powell:** ~140–150 miles north in Park County.\n\n### 3. Local Independent Used Dealerships in Lander\n* Independent dealers in Lander carry used Chrysler Pacifica and 300 models, but warranties are through third-party service contracts rather than factory CPO certification.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (CDJR)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Nearest authorized Chrysler dealer offering factory Stellantis Certified Pre-Owned warranties and dealer-backed pre-owned guarantees.", "sourceUrls": ["https://www.fremontcdjrriverton.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont CDJR Rock Springs", "role": "comparison", "supportingText": "~105 miles south across South Pass, providing additional certified pre-owned Chrysler inventory."}
        ],
        "citations": [
            {"url": "https://www.fremontcdjrriverton.com", "title": "Fremont CDJR Riverton Pre-Owned Vehicles"},
            {"url": "https://www.chrysler.com/cpo.html", "title": "Chrysler Certified Pre-Owned Program"}
        ],
        "limitations": ["Factory Stellantis CPO warranties are exclusively sold through franchised CDJR dealerships; none are located in Lander town limits."]
    },
    {
        "runId": "RUN-BASE-Q012-WEB",
        "questionId": "Q012",
        "question": "Where can I get Chrysler warranty service and recall repairs near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "For factory Chrysler warranty service and authorized recall repairs near Lander, Wyoming, work must be completed by a certified Stellantis / Chrysler dealership.\n\n### Primary Authorized Service Option:\n* **Fremont Motor Riverton (Fremont CDJR Riverton):**\n  * **Location:** 1601 N Federal Blvd, Riverton, WY (approx. 24 miles northeast of Lander)\n  * **Capabilities:** Authorized Chrysler warranty service, certified Mopar master technicians, genuine OEM Chrysler parts, and free manufacturer safety recall campaigns.\n  * **Why here:** There is no authorized Chrysler franchise or service point in Lander; Fremont CDJR in Riverton serves as the regional authorized center for Fremont County.\n\n### Regional Alternatives:\n* **Fremont CDJR Rock Springs:** ~105 miles south in Sweetwater County.\n* **Fremont CDJR Cody:** ~150 miles north in Park County.\n* **Casper Area CDJR Dealerships:** ~125 miles east in Casper.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (CDJR)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Closest authorized Chrysler dealer and warranty service center (~24 miles away in Riverton).", "sourceUrls": ["https://www.fremontcdjrriverton.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont CDJR Rock Springs", "role": "comparison", "supportingText": "~105 miles south in Sweetwater County."}
        ],
        "citations": [
            {"url": "https://www.fremontcdjrriverton.com", "title": "Fremont CDJR Riverton Service & Parts"},
            {"url": "https://www.mopar.com/en-us/my-vehicle/recalls/search.html", "title": "Mopar Official Recall Lookup"}
        ],
        "limitations": ["No authorized Chrysler warranty repair facility exists within Lander; nearest center is in Riverton (~24 miles away)."]
    },
    {
        "runId": "RUN-BASE-Q013-WEB",
        "questionId": "Q013",
        "question": "What are the best Dodge dealerships in or near Lander, Wyoming, and why?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "For shoppers seeking a Dodge dealership in or near Lander, Wyoming, the primary local franchise and regional options include:\n\n### 1. Primary Local Dealership: Fremont Motor Riverton (Fremont CDJR)\n* **Location:** 1601 N Federal Blvd, Riverton, WY 82501 (approx. 24–25 miles northeast of Lander)\n* **Why it's the primary choice:** There is no franchised Dodge dealership within Lander city limits. Fremont CDJR in Riverton is the authorized Stellantis (Chrysler, Dodge, Jeep, Ram) dealer serving Fremont County. They provide the complete Dodge lineup (Durango, Charger, Hornet), factory Mopar parts, warranty repairs, and certified pre-owned vehicles.\n\n### 2. Regional Dealership Alternatives\n* **Fremont CDJR Rock Springs:** Located approximately 105 miles south over South Pass in Sweetwater County.\n* **Fremont CDJR Cody:** Located approximately 150 miles north in Park County.\n* **Casper Area Dealerships:** Roughly 125 miles east in Natrona County.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (CDJR)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Closest authorized Dodge franchise serving Lander (~25 miles away) with full sales, Mopar service, and OEM warranty handling.", "sourceUrls": ["https://www.fremontcdjrriverton.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont CDJR Rock Springs", "role": "comparison", "supportingText": "Located approximately 105 miles south over South Pass in Sweetwater County."},
            {"name": "Fremont CDJR Cody", "role": "comparison", "supportingText": "Located approximately 150 miles north in Park County."}
        ],
        "citations": [
            {"url": "https://www.fremontcdjrriverton.com", "title": "Fremont CDJR Riverton"},
            {"url": "https://www.dodge.com/find-dealer.html", "title": "Dodge Official Dealer Locator"}
        ],
        "limitations": ["No Dodge franchise is located within Lander city limits; closest point is Riverton (~25 miles away)."]
    },
    {
        "runId": "RUN-BASE-Q014-WEB",
        "questionId": "Q014",
        "question": "Where can I buy a Dodge Durango near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "If you are looking to purchase a new or pre-owned Dodge Durango near Lander, Wyoming, here are your closest and primary options:\n\n### 1. Closest Authorized Dodge Dealer: Fremont Motor Riverton (CDJR)\n* **Location:** 1601 N Federal Blvd, Riverton, WY 82501 (approx. 24–25 miles northeast of Lander)\n* **Details:** As the franchised CDJR dealer for Fremont County, Fremont Motor Riverton carries Dodge Durango SUVs (including SXT, GT, R/T, and SRT configurations) with factory warranties, trade-in programs, and local service support.\n\n### 2. Regional Dealership Alternatives\n* **Fremont CDJR Rock Springs:** ~105 miles south via US-287/WY-28 in Sweetwater County.\n* **Fremont CDJR Cody:** ~150 miles north in Park County.\n* **Casper Area Dealerships:** ~125 miles east in Casper, WY, providing additional regional stock.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (CDJR)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Closest authorized Dodge dealer to Lander (~24 miles) with inventory of new and pre-owned Dodge Durango SUVs.", "sourceUrls": ["https://www.fremontcdjrriverton.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont CDJR Rock Springs", "role": "comparison", "supportingText": "~105 miles south via US-287/WY-28 in Sweetwater County."}
        ],
        "citations": [
            {"url": "https://www.fremontcdjrriverton.com", "title": "Fremont CDJR Riverton Durango Inventory"},
            {"url": "https://www.dodge.com", "title": "Dodge Official Website"}
        ],
        "limitations": ["No franchised Dodge dealership is situated directly in Lander; nearest location is Riverton (~25 miles away)."]
    },
    {
        "runId": "RUN-BASE-Q015-WEB",
        "questionId": "Q015",
        "question": "Where can I buy a reliable used Dodge with a warranty near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "For shoppers in Lander, Wyoming looking for a reliable pre-owned Dodge backed by a warranty (such as factory Certified Pre-Owned or comprehensive dealer warranties), the primary local and regional choices include:\n\n### 1. Primary Local Dealership: Fremont Motor Riverton (CDJR)\n* **Location:** 1601 N Federal Blvd, Riverton, WY (approx. 24 miles from Lander)\n* **Why it's the primary choice:** Fremont CDJR in Riverton is the authorized Stellantis dealer serving Fremont County. They offer **Stellantis Certified Pre-Owned (CPO)** vehicles (which include a 7-year/100,000-mile powertrain limited warranty, a 3-month/3,000-mile Maximum Care warranty, and a 125-point inspection) as well as Fremont Care dealer-certified warranties on used Dodge Durango, Charger, and Challenger models.\n\n### 2. Regional Dealership Alternatives\n* **Fremont CDJR Rock Springs:** Located approx. 105 miles south across South Pass in Sweetwater County.\n* **Fremont CDJR Cody / Powell:** Located approx. 140–150 miles north in Park County.\n* **Casper Area Dealerships:** Roughly 125 miles east, offering larger inventory volume.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (CDJR)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Closest franchised Dodge dealer to Lander offering factory Stellantis Certified Pre-Owned warranty coverage and dealer warranties.", "sourceUrls": ["https://www.fremontcdjrriverton.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont CDJR Rock Springs", "role": "comparison", "supportingText": "Located approx. 105 miles south across South Pass in Sweetwater County."}
        ],
        "citations": [
            {"url": "https://www.fremontcdjrriverton.com", "title": "Fremont CDJR Riverton Pre-Owned Inventory"},
            {"url": "https://www.dodge.com/cpo.html", "title": "Dodge Certified Pre-Owned Program"}
        ],
        "limitations": ["Factory Stellantis CPO warranties are exclusively sold by franchised dealerships; no franchised dealer exists directly in Lander."]
    },
    {
        "runId": "RUN-BASE-Q016-WEB",
        "questionId": "Q016",
        "question": "Where can I get Dodge warranty service and recall repairs near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "For factory Dodge warranty service, authorized recall campaign remedies, and certified Mopar maintenance near Lander, Wyoming, work must be completed by a franchised Stellantis dealership.\n\n### Primary Authorized Service Center:\n* **Fremont Motor Riverton (Fremont CDJR Riverton):**\n  * **Location:** 1601 N Federal Blvd, Riverton, WY 82501 (approx. 24–25 miles northeast of Lander)\n  * **Services:** Factory-certified master technicians, full Mopar parts department, authorized safety recall execution, and Stellantis factory warranty processing.\n  * **Why here:** There is no franchised Dodge dealer or warranty center in Lander itself. Fremont CDJR in Riverton is the designated franchise for Fremont County.\n\n### Regional Alternatives:\n* **Fremont CDJR Rock Springs:** ~105 miles south across South Pass.\n* **Fremont CDJR Cody:** ~150 miles north in Park County.\n* **Casper Area Dealerships:** ~125 miles east in Casper.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (CDJR)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Nearest authorized Dodge franchise and warranty service center (~24 miles away in Riverton).", "sourceUrls": ["https://www.fremontcdjrriverton.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont CDJR Rock Springs", "role": "comparison", "supportingText": "~105 miles south across South Pass."}
        ],
        "citations": [
            {"url": "https://www.fremontcdjrriverton.com", "title": "Fremont CDJR Riverton Service Department"},
            {"url": "https://www.mopar.com/en-us/my-vehicle/recalls/search.html", "title": "Mopar Official Recall Portal"}
        ],
        "limitations": ["No authorized Dodge warranty facility operates inside Lander city limits; nearest certified location is in Riverton (~25 miles away)."]
    },
    {
        "runId": "RUN-PILOT-Q103-WEB",
        "questionId": "Q103",
        "question": "Where can I buy a used four-wheel-drive truck under $25,000 near Sheridan, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "If you are shopping for a used 4x4 truck priced under $25,000 in or near Sheridan, Wyoming, several local dealerships maintain regular used truck inventory in this budget range:\n\n### 1. Fremont Motor Sheridan (Fremont Ford & Fremont Toyota Sheridan)\n* **Location:** 107 autoplex area / E 5th St, Sheridan, WY\n* **Why look here:** As one of the largest franchised automotive operations in Sheridan, Fremont Motor Sheridan regularly receives local trade-ins across Ford, Toyota, Ram, and Chevrolet trucks. They feature a broad bargain/budget pre-owned inventory segment and provide vehicle history reports.\n\n### 2. White's Frontier Motors (Sheridan)\n* **Location:** 1762 N Main St, Sheridan, WY\n* **Why look here:** Carries pre-owned domestic truck models (Chevrolet, GMC, Ford) often priced under $25,000, particularly slightly older or higher-mileage half-ton configurations suited for Wyoming winters.\n\n### 3. Big Horn Mountain Auto Sales & Local Independent Lots\n* **Location:** Sheridan, WY\n* **Why look here:** Independent used dealers in Sheridan frequently specialize in work trucks and affordable sub-$25k 4WD pickups for local ranchers and commuters.\n\n### Recommendation Tips:\n* Inventory under $25,000 moves quickly in Wyoming due to high demand for four-wheel-drive. Check online inventory filters daily and request CARFAX/AutoCheck reports before making an in-person visit.",
        "recommendedDealers": [
            {"name": "Fremont Motor Sheridan", "city": "Sheridan", "state": "WY", "role": "local", "rationale": "Major franchised automotive group in Sheridan with a wide rotation of pre-owned 4x4 trade-ins in budget ranges.", "sourceUrls": ["https://www.fremontmotorsheridan.com"]},
            {"name": "White's Frontier Motors", "city": "Sheridan", "state": "WY", "role": "local", "rationale": "Local Sheridan dealership with consistent selection of used domestic 4WD pickups.", "sourceUrls": ["https://www.whitesfrontiermotors.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Big Horn Mountain Auto Sales", "role": "informational", "supportingText": "Independent used dealers in Sheridan frequently specialize in work trucks and affordable sub-$25k 4WD pickups"}
        ],
        "citations": [
            {"url": "https://www.fremontmotorsheridan.com", "title": "Fremont Motor Sheridan Pre-Owned Inventory"},
            {"url": "https://www.whitesfrontiermotors.com", "title": "White's Frontier Motors Sheridan"}
        ],
        "limitations": ["Used truck pricing and 4x4 availability fluctuate rapidly under $25,000; buyers should verify vehicle history and mechanical condition."]
    },
    {
        "runId": "RUN-PILOT-Q128-WEB",
        "questionId": "Q128",
        "question": "Where can I get Honda warranty service and recall repairs near Casper, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "For official Honda warranty service and authorized recall repairs, work must be completed by an authorized Honda dealer. In Casper, Wyoming, there is currently no standalone authorized Honda dealership located within the immediate city limits.\n\n### Primary Authorized Service Options:\n\n1. **Honda of Casper (Powersports Only Note):**\n   * Note that local dealers under similar naming in Casper (such as Casper Mountain Motorsports or local powersports dealers) service Honda motorcycles/ATVs, but are not authorized warranty centers for Honda automotive passenger vehicles.\n\n2. **Nearest Authorized Honda Automotive Dealerships:**\n   * **Tyrrell Honda (Cheyenne, WY):** Located at 2142 Westland Rd, Cheyenne, WY (~180 miles south via I-25). Tyrrell Honda is the primary authorized Honda automotive franchise serving southeast Wyoming, capable of completing all manufacturer recall campaigns, certified warranty repairs, and factory bulletins.\n   * **Sheridan / Northern Alternatives:** Depending on your route, drivers sometimes look north toward Montana (e.g., Underriner Honda in Billings, MT, ~230 miles) or southeast to Colorado (e.g., Fort Collins / Loveland Honda dealers, ~210 miles).\n\n### Important Shopper Advice for Recalls:\n* Recall repairs are performed **free of charge** at authorized Honda automotive dealers.\n* Before traveling, call the service department with your 17-digit Vehicle Identification Number (VIN) to verify parts availability for the specific open recall.",
        "recommendedDealers": [
            {"name": "Tyrrell Honda", "city": "Cheyenne", "state": "WY", "role": "regional", "rationale": "Closest authorized Honda automotive franchise in Wyoming (~180 miles south of Casper) for certified warranty service and recall campaign execution.", "sourceUrls": ["https://www.tyrrellhonda.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Underriner Honda", "role": "comparison", "supportingText": "Drivers sometimes look north toward Montana (e.g., Underriner Honda in Billings, MT, ~230 miles)"}
        ],
        "citations": [
            {"url": "https://www.tyrrellhonda.com", "title": "Tyrrell Honda - Cheyenne, WY"},
            {"url": "https://owners.honda.com/service-maintenance/recalls", "title": "Honda Owners Recall Lookup"}
        ],
        "limitations": ["No authorized Honda passenger automotive dealership exists within Casper city limits; nearest authorized franchise requires regional travel (~180 miles to Cheyenne or ~230 miles to Billings, MT)."]
    }
]

for r in records:
    append_observation(r)

print("Saved 18 observations. Current total:", len(get_completed_ids()))
