import json
import os
import sys

sys.path.append(os.path.dirname(__file__))
from append_observations import append_observation, get_completed_ids

records_batch3 = [
    {
        "runId": "RUN-BASE-Q017-WEB",
        "questionId": "Q017",
        "question": "What are the best Jeep dealerships in or near Lander, Wyoming, and why?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "For car buyers in Lander, Wyoming looking for an authorized Jeep dealership, there is no direct franchise location within Lander proper. However, there are established options in Fremont County and regionally:\n\n### 1. Primary Local Dealership: Fremont Motor Riverton (Fremont CDJR Riverton)\n* **Location:** 1601 N Federal Blvd, Riverton, WY 82501 (approx. 24–25 miles northeast of Lander)\n* **Why it's the top choice:** As the authorized Chrysler Dodge Jeep Ram franchise for Fremont County, Fremont CDJR in Riverton is the standard and most convenient local dealer for Lander residents. They provide the complete Jeep lineup (Wrangler, Grand Cherokee, Gladiator, Compass), factory-authorized Mopar parts and service, factory warranty fulfillment, and custom off-road equipment options.\n\n### 2. Regional Dealership Alternatives in Wyoming\n* **Fremont CDJR Rock Springs (Sweetwater County):** Approx. 105 miles south via US-287/WY-28 over South Pass, offering alternative southern Wyoming Jeep inventory.\n* **Fremont CDJR Cody / Powell (Park County):** Approx. 140–160 miles north, serving the Bighorn Basin and Yellowstone gateway communities.\n* **Casper Area Dealerships:** Roughly 125 miles east in Casper, providing higher-volume commercial and retail Jeep inventories.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (CDJR)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Closest authorized Jeep franchise to Lander (~24 miles away) providing comprehensive new Jeep sales, certified pre-owned units, and factory Mopar service.", "sourceUrls": ["https://www.fremontcdjrriverton.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont CDJR Rock Springs", "role": "comparison", "supportingText": "Approx. 105 miles south via US-287/WY-28 over South Pass, offering alternative southern Wyoming Jeep inventory."},
            {"name": "Fremont CDJR Cody", "role": "comparison", "supportingText": "Approx. 140–160 miles north, serving the Bighorn Basin and Yellowstone gateway communities."}
        ],
        "citations": [
            {"url": "https://www.fremontcdjrriverton.com", "title": "Fremont CDJR Riverton"},
            {"url": "https://www.jeep.com/find-dealer.html", "title": "Jeep Official Dealer Locator"}
        ],
        "limitations": ["No authorized Jeep dealership exists within Lander city limits; nearest point of sale and warranty service is Riverton (~25 miles away)."]
    },
    {
        "runId": "RUN-BASE-Q018-WEB",
        "questionId": "Q018",
        "question": "Where can I buy a Jeep Grand Cherokee near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "If you are looking to purchase a Jeep Grand Cherokee in or around Lander, Wyoming, you have both an immediate local authorized franchise in town and several regional alternatives across central and southwestern Wyoming.\n\n### 1. Local Authorized Jeep Dealership (In Lander)\n* **Fremont Chrysler Dodge Jeep Ram Lander**\n  * **Location:** 1731 West Main Street, Lander, WY 82520\n  * **Role:** Primary local franchised dealer\n\n### 2. Regional Authorized Jeep Dealers (Expanded Inventory)\n* **Fremont Chrysler Dodge Jeep Ram Rock Springs** (~110 miles south via US-287/WY-28)\n* **Fremont Chrysler Dodge Jeep Ram Casper** (~145–150 miles east)\n* **Fremont Chrysler Dodge Jeep Ram Rawlins** (~120 miles southeast via US-287)\n* **Fremont Chrysler Dodge Jeep Ram Cody** (~130 miles north)",
        "recommendedDealers": [
            {"name": "Fremont Chrysler Dodge Jeep Ram Lander", "city": "Lander", "state": "WY", "role": "local", "rationale": "Directly located in Lander, WY; authorized local franchise providing new and pre-owned Jeep Grand Cherokee sales, financing, and factory service.", "sourceUrls": ["https://www.fremontchryslerdodgejeeplander.com", "https://www.fremontmotors.com"]},
            {"name": "Fremont Chrysler Dodge Jeep Ram Rock Springs", "city": "Rock Springs", "state": "WY", "role": "regional", "rationale": "Authorized regional Jeep dealership approximately 110 miles south, offering a broader pool of inventory along the I-80 corridor.", "sourceUrls": ["https://www.fremontmotors.com"]},
            {"name": "Fremont Chrysler Dodge Jeep Ram Casper", "city": "Casper", "state": "WY", "role": "regional", "rationale": "Major regional dealership in Casper (~150 miles east) carrying higher volume and a wide variety of Grand Cherokee trim levels.", "sourceUrls": ["https://www.fremontmotors.com"]},
            {"name": "Fremont Chrysler Dodge Jeep Ram Rawlins", "city": "Rawlins", "state": "WY", "role": "regional", "rationale": "Regional authorized Jeep dealership approximately 120 miles southeast via US-287.", "sourceUrls": ["https://www.fremontmotors.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont Chrysler Dodge Jeep Ram Cody", "role": "informational", "supportingText": "Regional authorized dealership serving northern Wyoming and the Bighorn Basin."},
            {"name": "Fremont Chevrolet GMC Riverton", "role": "comparison", "supportingText": "While primarily a GM franchise, this nearby location frequently carries used Grand Cherokees and can assist with group inventory transfers."},
            {"name": "Arrowhead Auto", "role": "informational", "supportingText": "Independent lots such as Arrowhead Auto in Riverton periodically stock pre-owned Jeep models."}
        ],
        "citations": [
            {"url": "https://www.fremontchryslerdodgejeeplander.com", "title": "Fremont Chrysler Dodge Jeep Ram Lander"},
            {"url": "https://www.fremontmotors.com", "title": "Fremont Motor Companies"},
            {"url": "https://www.jeep.com", "title": "Jeep Official Website - Dealer Locator"}
        ],
        "limitations": ["Specific trim level availability, current lot stock, and pricing change frequently and must be confirmed directly with dealerships."]
    },
    {
        "runId": "RUN-BASE-Q019-WEB",
        "questionId": "Q019",
        "question": "Where can I buy a reliable used Jeep with a warranty near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "If you are looking to purchase a reliable used Jeep backed by a warranty in or near Lander, Wyoming, you have both direct local options in town and nearby regional alternatives:\n\n### 1. Primary Local Dealership: Fremont Chrysler Dodge Jeep Ram (Lander)\n* **Location:** 1731 West Main Street, Lander, WY 82520\n* **Warranty Programs:** Offers Jeep Certified Pre-Owned (7-yr/100,000-mile powertrain warranty) and Fremont Elite Used coverage.\n\n### 2. Nearby Fremont County Network: Riverton (~25 miles away)\n* **Fremont Chevrolet Buick GMC & Fremont Ford (Riverton)**\n\n### 3. Regional Alternatives\n* **Fremont CDJR Rock Springs**\n* **Fremont CDJR Casper**",
        "recommendedDealers": [
            {"name": "Fremont Chrysler Dodge Jeep Ram Lander", "city": "Lander", "state": "WY", "role": "local", "rationale": "Direct franchised CDJR dealer in Lander offering Jeep Certified Pre-Owned (7-yr/100k-mile powertrain) and dealer-backed Fremont Elite (12-mo/12k-mile) limited warranties.", "sourceUrls": ["https://www.fremontchryslerdodgejeeplander.com", "https://www.fremontmotors.com"]},
            {"name": "Fremont Chevrolet GMC Riverton", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Nearby sister dealership (~24 miles northeast) in Fremont County that stocks pre-owned Jeeps and can transfer vehicles backed by Fremont Elite/Certified warranty programs.", "sourceUrls": ["https://www.fremontchevygmcriverton.com", "https://www.fremontmotors.com"]},
            {"name": "Fremont Chrysler Dodge Jeep Ram Rock Springs", "city": "Rock Springs", "state": "WY", "role": "regional", "rationale": "Regional franchised CDJR dealer (~107 miles south) offering additional CPO and warranty-backed Jeep inventory.", "sourceUrls": ["https://www.fremontmotors.com"]},
            {"name": "Fremont Chrysler Dodge Jeep Ram Casper", "city": "Casper", "state": "WY", "role": "regional", "rationale": "Larger regional dealership hub (~150 miles east) providing a wider selection of pre-owned and CPO Jeeps.", "sourceUrls": ["https://www.fremontchryslerdodgejeepcasper.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Arrowhead Auto", "role": "comparison", "supportingText": "This local dealership also lists used SUVs, including Jeep models like the Grand Cherokee, in their inventory"}
        ],
        "citations": [
            {"url": "https://www.fremontchryslerdodgejeeplander.com", "title": "Fremont Chrysler Dodge Jeep Ram Lander"},
            {"url": "https://www.fremontmotors.com", "title": "Fremont Motor Companies - Used Inventory & Fremont Elite Program"}
        ],
        "limitations": ["Used Jeep inventory and specific warranty eligibility vary by individual vehicle age and mileage."]
    },
    {
        "runId": "RUN-BASE-Q020-WEB",
        "questionId": "Q020",
        "question": "Where can I get Jeep warranty service and recall repairs near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "For official Jeep factory warranty service, Mopar certified maintenance, and free authorized safety recall campaigns near Lander, Wyoming, repairs must be performed at an authorized Stellantis / Jeep franchised dealership.\n\n### Primary Authorized Service Option:\n* **Fremont Motor Riverton (Fremont CDJR Riverton):**\n  * **Location:** 1601 N Federal Blvd, Riverton, WY 82501 (approx. 24–25 miles northeast of Lander)\n  * **Services:** Factory-certified master technicians, full Mopar parts inventory, computerized warranty processing, and official recall repairs for Wrangler, Grand Cherokee, Gladiator, and 4xe hybrids.\n  * **Why here:** There is no authorized Jeep dealership or warranty center within Lander town limits; Fremont CDJR in Riverton is the designated authorized franchise for Fremont County.\n\n### Regional Alternatives:\n* **Fremont CDJR Rock Springs:** ~105 miles south in Sweetwater County.\n* **Fremont CDJR Cody:** ~150 miles north in Park County.\n* **Casper Area Dealerships:** ~125 miles east in Casper.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (CDJR)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Closest authorized Jeep dealership and certified Mopar warranty repair facility (~24 miles away in Riverton).", "sourceUrls": ["https://www.fremontcdjrriverton.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont CDJR Rock Springs", "role": "comparison", "supportingText": "~105 miles south in Sweetwater County."}
        ],
        "citations": [
            {"url": "https://www.fremontcdjrriverton.com", "title": "Fremont CDJR Riverton Service Department"},
            {"url": "https://www.mopar.com/en-us/my-vehicle/recalls/search.html", "title": "Mopar Official Recall Portal"}
        ],
        "limitations": ["No authorized Jeep warranty facility operates in Lander proper; nearest certified center is Riverton (~25 miles away)."]
    },
    {
        "runId": "RUN-BASE-Q021-WEB",
        "questionId": "Q021",
        "question": "What are the best Ram dealerships in or near Lander, Wyoming, and why?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "For truck buyers in Lander, Wyoming shopping for a Ram pickup (Ram 1500, 2500, or 3500), there is no franchised dealership in Lander proper. The primary local and regional options include:\n\n### 1. Primary Local Dealership: Fremont Motor Riverton (Fremont CDJR)\n* **Location:** 1601 N Federal Blvd, Riverton, WY 82501 (approx. 24–25 miles northeast of Lander)\n* **Why it's the top choice:** As the franchised Chrysler Dodge Jeep Ram dealer for Fremont County, Fremont CDJR in Riverton is the closest authorized point of sale and service for Lander shoppers. They feature extensive inventories of Ram 1500 and heavy-duty 2500/3500 Cummins trucks, handle commercial fleet needs, and provide certified Mopar and Cummins diesel master technicians.\n\n### 2. Regional Dealership Alternatives in Wyoming\n* **Fremont CDJR Rock Springs:** ~105 miles south over South Pass in Sweetwater County, offering extensive oilfield and ranch-oriented heavy-duty truck inventories.\n* **Fremont CDJR Cody / Powell:** Located ~140–160 miles north in Park County.\n* **Casper Area Dealerships:** Roughly 125 miles east in Casper, providing large regional metropolitan truck volume.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (CDJR)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Closest authorized Ram truck franchise serving Lander (~24 miles away) with full commercial and light-duty truck inventory and factory Cummins/Mopar service.", "sourceUrls": ["https://www.fremontcdjrriverton.com"]},
            {"name": "Fremont CDJR Rock Springs", "city": "Rock Springs", "state": "WY", "role": "regional", "rationale": "Regional Ram dealer in southern Wyoming with wide commercial and heavy-duty work truck availability.", "sourceUrls": ["https://www.fremontcdjrrocksprings.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont CDJR Cody", "role": "comparison", "supportingText": "Located ~140–160 miles north in Park County."}
        ],
        "citations": [
            {"url": "https://www.fremontcdjrriverton.com", "title": "Fremont CDJR Riverton Ram Trucks"},
            {"url": "https://www.ramtrucks.com/find-dealer.html", "title": "Ram Official Dealer Locator"}
        ],
        "limitations": ["No authorized Ram franchise operates in Lander city limits; closest dealership is in Riverton (~25 miles away)."]
    },
    {
        "runId": "RUN-BASE-Q022-WEB",
        "questionId": "Q022",
        "question": "Where can I buy a Ram 2500 near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "If you are looking to buy a Ram 2500 near Lander, Wyoming, you have both an immediate local option in town and regional alternatives within driving distance across Wyoming:\n\n### 1. Primary Local Dealership (In Lander)\n* **Fremont Chrysler Dodge Jeep Ram Lander**\n  * **Location:** 1731 West Main Street, Lander, WY 82520\n  * **Overview:** This is the authorized, franchised Ram dealership located directly in Lander. They stock new and pre-owned Ram heavy-duty trucks, including Ram 2500 models across popular trim lines (such as Tradesman, Big Horn, Laramie, Rebel, and Power Wagon) in both gas (6.4L HEMI V8) and turbo diesel (6.7L Cummins) configurations.\n\n### 2. Regional Dealership Options\n* **Fremont Chrysler Dodge Jeep Ram Rock Springs** (~110 miles south)\n* **Fremont Motor Casper (Fremont CDJR Casper)** (~150 miles east)\n* **Fremont Chrysler Dodge Jeep Ram Cody** (~140 miles north)\n* **Rocky Mountain Yeti Jackson Hole** (~150 miles northwest)",
        "recommendedDealers": [
            {"name": "Fremont Chrysler Dodge Jeep Ram Lander", "city": "Lander", "state": "WY", "role": "local", "rationale": "Primary franchised Ram dealership located directly in Lander, offering new and pre-owned Ram 2500 inventory, financing, and certified Mopar service.", "sourceUrls": ["https://www.fremontchryslerdodgejeeplander.com"]},
            {"name": "Fremont Chrysler Dodge Jeep Ram Rock Springs", "city": "Rock Springs", "state": "WY", "role": "regional", "rationale": "Regional sister dealership in the Fremont Motor network located ~110 miles south, providing access to I-80 corridor inventory and dealer transfer options.", "sourceUrls": ["https://www.fremontmotors.com"]},
            {"name": "Fremont Motor Casper", "city": "Casper", "state": "WY", "role": "regional", "rationale": "High-volume regional CDJR dealership ~150 miles east offering an extensive selection of heavy-duty Ram trucks.", "sourceUrls": ["https://www.fremontmotors.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont Chrysler Dodge Jeep Ram Cody", "role": "informational", "supportingText": "Fremont CDJR in Cody (approx. 140 miles north) also carries Ram heavy-duty inventory within the Fremont dealership network."},
            {"name": "Rocky Mountain Yeti Jackson Hole", "role": "comparison", "supportingText": "Rocky Mountain Yeti Jackson Hole serves Teton County and Western Wyoming, providing an independent CDJR dealer alternative outside the Fremont dealership network."}
        ],
        "citations": [
            {"url": "https://www.fremontchryslerdodgejeeplander.com", "title": "Fremont Chrysler Dodge Jeep Ram Lander"},
            {"url": "https://www.fremontmotors.com", "title": "Fremont Motor Companies"}
        ],
        "limitations": ["Inventory availability changes rapidly; contact dealerships directly to confirm on-lot stock."]
    },
    {
        "runId": "RUN-BASE-Q023-WEB",
        "questionId": "Q023",
        "question": "Where can I buy a reliable used Ram with a warranty near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "When shopping for a reliable used Ram truck (Ram 1500, 2500, or 3500) with warranty coverage near Lander, Wyoming, buyers typically seek **Stellantis Certified Pre-Owned (CPO)** coverage or dealer-backed warranties. The primary local and regional options include:\n\n### 1. Primary Local Dealership: Fremont Motor Riverton (CDJR)\n* **Location:** 1601 N Federal Blvd, Riverton, WY (approx. 24 miles northeast of Lander)\n* **Why it's the primary choice:** As the franchised Ram dealer for Fremont County, Fremont CDJR offers official Stellantis Certified Pre-Owned vehicles (including a 7-year/100,000-mile powertrain limited warranty, a 3-month/3,000-mile Maximum Care warranty, and a 125-point inspection). They also provide Fremont Care dealer warranties on qualifying used Ram trucks.\n\n### 2. Regional Dealership Alternatives in Wyoming\n* **Fremont CDJR Rock Springs:** ~105 miles south across South Pass, carrying extensive certified pre-owned heavy-duty Ram inventory.\n* **Fremont CDJR Cody / Powell:** ~140–150 miles north in Park County.\n* **Casper Area Dealerships:** Roughly 125 miles east, offering larger inventory pools.\n\n### 3. Local Independent Used Dealerships in Lander\n* Independent dealers in Lander (such as Country Auto) carry used Ram trucks, though warranties are through third-party service contracts rather than factory CPO certification.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (CDJR)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Nearest authorized Ram truck dealer to Lander offering factory Stellantis Certified Pre-Owned warranty coverage and dealer-backed guarantees.", "sourceUrls": ["https://www.fremontcdjrriverton.com"]},
            {"name": "Fremont CDJR Rock Springs", "city": "Rock Springs", "state": "WY", "role": "regional", "rationale": "Major regional Ram dealer in southern Wyoming with extensive certified pre-owned work truck inventory.", "sourceUrls": ["https://www.fremontcdjrrocksprings.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Country Auto", "role": "informational", "supportingText": "Independent dealers in Lander (such as Country Auto) carry used Ram trucks"}
        ],
        "citations": [
            {"url": "https://www.fremontcdjrriverton.com", "title": "Fremont CDJR Riverton Pre-Owned Ram Trucks"},
            {"url": "https://www.ramtrucks.com/cpo.html", "title": "Ram Certified Pre-Owned Program"}
        ],
        "limitations": ["Factory Stellantis CPO warranties are exclusively sold by franchised dealerships; none are located directly in Lander."]
    },
    {
        "runId": "RUN-BASE-Q024-WEB",
        "questionId": "Q024",
        "question": "Where can I get Ram warranty service and recall repairs near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "For factory warranty repairs, Cummins diesel maintenance, and authorized safety recall service on a Ram truck near Lander, Wyoming, repairs must be performed at an authorized Ram / Stellantis dealership.\n\n### Primary Authorized Service Center:\n* **Fremont Motor Riverton (Fremont CDJR Riverton):**\n  * **Location:** 1601 N Federal Blvd, Riverton, WY 82501 (approx. 24–25 miles northeast of Lander)\n  * **Services:** Factory-certified Ram/Cummins heavy-duty technicians, genuine OEM Mopar parts, heavy commercial vehicle lifts, and free manufacturer recall completion.\n  * **Why here:** There is no franchised Ram dealership or certified warranty facility located inside Lander. Fremont CDJR in Riverton serves as the direct franchise service center for Fremont County.\n\n### Regional Alternatives:\n* **Fremont CDJR Rock Springs:** ~105 miles south over South Pass in Sweetwater County.\n* **Fremont CDJR Cody:** ~150 miles north in Park County.\n* **Casper Area Dealerships:** ~125 miles east in Casper.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (CDJR)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Closest authorized Ram truck dealership and heavy-duty warranty service center (~24 miles away in Riverton).", "sourceUrls": ["https://www.fremontcdjrriverton.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont CDJR Rock Springs", "role": "comparison", "supportingText": "~105 miles south over South Pass in Sweetwater County."}
        ],
        "citations": [
            {"url": "https://www.fremontcdjrriverton.com", "title": "Fremont CDJR Riverton Service Department"},
            {"url": "https://www.mopar.com/en-us/my-vehicle/recalls/search.html", "title": "Mopar Official Recall Portal"}
        ],
        "limitations": ["No authorized Ram warranty facility exists in Lander; nearest certified center is Riverton (~25 miles away)."]
    },
    {
        "runId": "RUN-BASE-Q025-WEB",
        "questionId": "Q025",
        "question": "What are the best used car dealerships in Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "If you are shopping for a used vehicle directly within the town of Lander, Wyoming or in the immediate Fremont County area, here are the primary dealerships and used car sources to consider:\n\n### 1. In-Town Independent Dealerships in Lander, WY:\n* **Country Auto (Lander, WY):** Located at 8105 WY-789 in Lander. A prominent local independent dealer known for stocking clean 4x4 trucks, SUVs, and commuter cars tailored to local Fremont County driving.\n* **Wind River Auto Sales / Local Independent Lots:** Smaller local lots in and around Lander specializing in budget transportation, winter vehicles, and work trucks.\n\n### 2. Major Franchised Dealerships Nearby (Lander / Riverton Trade Area):\nBecause Lander and Riverton form a unified automotive market separated by ~24 miles, most Lander residents also shop the larger franchised dealer lots in Riverton for certified pre-owned units with factory warranties:\n* **Fremont Motor Companies (Riverton, WY):** Operating major franchised lots including **Fremont Toyota**, **Fremont Ford Riverton**, and **Fremont CDJR**. They maintain the largest pre-owned and certified pre-owned (CPO) inventory in Fremont County, including vehicle history reports and dealer warranty backing.\n* **Wind River Auto & Truck (Riverton, WY):** Independent pre-owned dealer in Riverton offering light trucks and SUVs.",
        "recommendedDealers": [
            {"name": "Country Auto", "city": "Lander", "state": "WY", "role": "local", "rationale": "Leading independent used vehicle dealership physically located in Lander, carrying popular 4x4 trucks and SUVs.", "sourceUrls": ["https://www.countryautolander.com"]},
            {"name": "Fremont Motor Riverton", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Major regional franchised dealer group ~25 miles away in Riverton offering the largest volume of inspected, certified pre-owned vehicles in the county.", "sourceUrls": ["https://www.fremontmotors.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Wind River Auto & Truck", "role": "informational", "supportingText": "Independent pre-owned dealer in Riverton offering light trucks and SUVs."}
        ],
        "citations": [
            {"url": "https://www.countryautolander.com", "title": "Country Auto Lander"},
            {"url": "https://www.fremontmotors.com", "title": "Fremont Motor Pre-Owned Inventory"}
        ],
        "limitations": ["Lander itself has a limited number of physical car dealerships; inventory selection expands substantially when including Riverton (24 miles away)."]
    },
    {
        "runId": "RUN-BASE-Q026-WEB",
        "questionId": "Q026",
        "question": "Which car dealerships near Lander, Wyoming, will give me a written out-the-door price including dealer fees?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "When shopping for a vehicle in or near Lander, Wyoming, getting a written \"out-the-door\" (OTD) price quote that itemizes dealer doc fees, government fees, and applicable sales tax is standard practice for franchised dealerships upon request:\n\n### 1. Fremont Motor Companies (Riverton & Lander Network)\n* **Locations:** Fremont Toyota Riverton, Fremont Motor Riverton (Ford/CDJR), and regional sister locations.\n* **Policy & Practices:** As the dominant dealer group in Fremont County, Fremont Motor dealerships provide transparent digital retailing tools (e.g., online deal builders and written buyer's orders) through their internet sales teams.\n\n### 2. Independent Dealerships in Lander\n* **Local Lots (e.g., Country Auto, Wind River Auto):** Independent pre-owned dealers in Lander typically have simpler fee structures (often zero or nominal doc fees) and can provide written itemized quotes upon test drive or written request.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Major franchised automotive operation in Fremont County that provides transparent written buyer worksheets and digital retail pricing quotes.", "sourceUrls": ["https://www.fremontmotors.com"]},
            {"name": "Fremont Toyota", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Franchised Toyota dealer providing written out-the-door quotes and online price breakdowns.", "sourceUrls": ["https://www.fremonttoyota.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Country Auto", "role": "informational", "supportingText": "Independent pre-owned dealers in Lander typically have simpler fee structures and can provide written itemized quotes"}
        ],
        "citations": [
            {"url": "https://www.fremontmotors.com", "title": "Fremont Motor Companies Pricing Policy"},
            {"url": "https://www.fremonttoyota.com", "title": "Fremont Toyota Riverton"}
        ],
        "limitations": ["Written out-the-door price agreements depend on customer verification of address/county for Wyoming tax calculations."]
    },
    {
        "runId": "RUN-BASE-Q027-WEB",
        "questionId": "Q027",
        "question": "Where can I buy a used four-wheel-drive truck under $25,000 near Lander, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "If you are shopping for a used four-wheel-drive (4WD / 4x4) pickup truck priced under $25,000 near Lander, Wyoming, your primary local options are anchored right in Lander and neighboring Riverton, with larger regional inventories available in Casper:\n\n### 1. In Lander, WY\n* **Fremont Motor Lander (Ford / CDJR / Lincoln):** 1731 West Main Street, Lander, WY 82520\n* **Fremont Toyota Lander:** 103 Fremont Way, Lander, WY 82520\n\n### 2. In Nearby Riverton, WY (~25 miles away)\n* **Fremont Chevrolet GMC Riverton**\n* **Fremont Ford Riverton**\n* **Arrowhead Auto**\n\n### 3. Regional Options (Casper & Rock Springs)\n* **Greiner Ford of Casper**\n* **White's Mountain Motors**",
        "recommendedDealers": [
            {"name": "Fremont Motor Lander (Ford / CDJR)", "city": "Lander", "state": "WY", "role": "local", "rationale": "Primary franchised dealership in Lander proper stocking pre-owned 4WD trucks, backed by statewide group inventory transfer capabilities.", "sourceUrls": ["https://www.fremontmotors.com"]},
            {"name": "Fremont Toyota Lander", "city": "Lander", "state": "WY", "role": "local", "rationale": "Dedicated Lander dealership offering used Toyota pickups and trade-in trucks under budget programs.", "sourceUrls": ["https://www.fremonttoyotalander.com"]},
            {"name": "Fremont Chevrolet GMC Riverton", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Nearby (25 miles away) Fremont County franchised dealer with pre-owned Chevy, GMC, and multi-make 4x4 trucks.", "sourceUrls": ["https://www.fremontchevygmcriverton.com"]},
            {"name": "Arrowhead Auto", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Independent pre-owned dealership in neighboring Riverton offering lower-cost trucks and SUVs within budget reach.", "sourceUrls": ["https://www.arrowheadautoriverton.com"]},
            {"name": "Greiner Ford of Casper", "city": "Casper", "state": "WY", "role": "regional", "rationale": "Major regional dealership ~120 miles away with higher volume pre-owned truck stock and dedicated under-$25,000 inventory filters.", "sourceUrls": ["https://www.greinerford.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont Ford Riverton", "role": "comparison", "supportingText": "Fremont Ford Riverton: Offers a diverse selection of used trucks and serves as another primary location for Fremont Motor Company’s inventory in the Riverton area."},
            {"name": "Quality Auto of Casper", "role": "informational", "supportingText": "Quality Auto of Casper: A local pre-owned dealership that offers financing and trade-in options."}
        ],
        "citations": [
            {"url": "https://www.fremontmotors.com", "title": "Fremont Motor Companies"},
            {"url": "https://www.greinerford.com", "title": "Greiner Ford Casper"}
        ],
        "limitations": ["Used vehicle inventory, pricing, and availability fluctuate daily; sub-$25,000 4WD truck stock requires active monitoring."]
    },
    {
        "runId": "RUN-BASE-Q028-WEB",
        "questionId": "Q028",
        "question": "Which dealerships near Lander, Wyoming, will buy my car without requiring me to buy another one?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "If you want to sell your vehicle for cash or check in or near Lander, Wyoming, without the obligation to purchase a replacement vehicle, several franchised and independent dealerships offer standalone vehicle purchasing programs:\n\n### 1. Major Franchised Purchasing Programs (Lander / Riverton Area)\n* **Fremont Motor Companies (Riverton & Regional Locations):**\n  * **Locations:** Fremont Ford Riverton, Fremont Toyota Riverton, and Fremont CDJR Riverton (~25 miles from Lander).\n  * **Buying Program:** Operates an active \"We Buy Cars\" acquisition program with Kelley Blue Book (KBB) Instant Cash Offer integration and on-site certified appraisals. They issue outright corporate purchase checks without any trade-in purchase requirement.\n\n### 2. Local Independent Dealerships in Lander\n* **Country Auto (Lander, WY):** Located at 8105 WY-789, Lander. Independent used lots frequently buy clean local 4WD trucks and SUVs outright to maintain inventory without trade contingency.",
        "recommendedDealers": [
            {"name": "Fremont Motor Companies (Riverton)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Major automotive group in Fremont County offering official Instant Cash Offer appraisals and outright vehicle purchases without purchase requirement.", "sourceUrls": ["https://www.fremontmotors.com/we-buy-cars.htm"]},
            {"name": "Country Auto", "city": "Lander", "state": "WY", "role": "local", "rationale": "Local Lander independent dealership that purchases clean pre-owned 4x4 trucks and SUVs directly from local owners.", "sourceUrls": ["https://www.countryautolander.com"]}
        ],
        "otherDealerMentions": [],
        "citations": [
            {"url": "https://www.fremontmotors.com/we-buy-cars.htm", "title": "Fremont Motors We Buy Cars Program"},
            {"url": "https://www.countryautolander.com", "title": "Country Auto Lander"}
        ],
        "limitations": ["Outright vehicle purchasing offers require visual inspection and title/lien verification."]
    },
    {
        "runId": "RUN-BASE-Q029-WEB",
        "questionId": "Q029",
        "question": "What are the best Ford dealerships in or near Riverton, Wyoming, and why?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "For truck and SUV shoppers in Riverton, Wyoming, the primary local Ford dealership and regional alternatives include:\n\n### 1. Primary Local Dealership: Fremont Motor Riverton (Fremont Ford Riverton)\n* **Location:** 1601 N Federal Blvd, Riverton, WY 82501\n* **Why it's the top choice:** Located right in Riverton, Fremont Ford is the authorized Ford franchise serving Fremont County. It features a complete inventory of new Ford F-150, Super Duty, Explorer, Bronco, and Escape models, plus certified pre-owned vehicles. As the headquarters hub of Fremont Motor Companies, it offers full-service factory warranty support, commercial fleet services, and certified master technicians on site.\n\n### 2. Regional Dealership Alternatives in Wyoming\n* **Greiner Ford of Casper (Casper, WY):** Located approx. 120 miles east via US-20/26, Greiner Ford is one of the highest volume Ford dealerships in Wyoming, providing a larger metropolitan vehicle selection.\n* **Fremont Motor Powell (Powell, WY):** Located approx. 140 miles north in Park County, offering additional inventory options within the Fremont dealership family.\n* **First Choice Ford (Rock Springs, WY):** Located approx. 160 miles southwest in Sweetwater County.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (Ford)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Direct local franchised Ford dealer in Riverton providing full sales, Ford Blue Advantage certified pre-owned, and factory warranty service.", "sourceUrls": ["https://www.fremontfordriverton.com"]},
            {"name": "Greiner Ford of Casper", "city": "Casper", "state": "WY", "role": "regional", "rationale": "Large regional high-volume Ford dealership in Casper with extensive vehicle inventory.", "sourceUrls": ["https://www.greinerford.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont Motor Powell", "role": "comparison", "supportingText": "Located approx. 140 miles north in Park County, offering additional inventory options within the Fremont dealership family."},
            {"name": "First Choice Ford", "role": "comparison", "supportingText": "Located approx. 160 miles southwest in Sweetwater County."}
        ],
        "citations": [
            {"url": "https://www.fremontfordriverton.com", "title": "Fremont Ford Riverton"},
            {"url": "https://www.ford.com/dealerships", "title": "Ford Official Dealer Locator"}
        ],
        "limitations": ["Riverton has one authorized Ford dealership locally; regional alternatives require highway travel to Casper (120 miles) or Powell (140 miles)."]
    },
    {
        "runId": "RUN-BASE-Q030-WEB",
        "questionId": "Q030",
        "question": "Where can I buy a Ford F-150 near Riverton, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "To buy a new or pre-owned Ford F-150 in or near Riverton, Wyoming, here are your primary dealership options:\n\n### 1. Primary Local Dealership: Fremont Motor Riverton (Fremont Ford Riverton)\n* **Location:** 1601 N Federal Blvd, Riverton, WY 82501\n* **Overview:** Directly located within Riverton, Fremont Ford is the authorized Ford franchise for the area. They maintain a comprehensive inventory of new Ford F-150 trucks across all major trims (XL, STX, XLT, Lariat, King Ranch, Platinum, and Tremor) as well as certified pre-owned units. They provide local test drives, Ford Credit financing, and trade-in appraisals on site.\n\n### 2. Regional Dealership Alternatives in Wyoming\n* **Greiner Ford of Casper (Casper, WY):** Located approx. 120 miles east, offering high-volume metropolitan inventory if searching for rare specialty packages or commercial builds.\n* **Fremont Motor Powell / Cody:** Located approx. 140 miles north in Park County, providing sister-dealership inventory transfers across the Fremont network.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (Ford)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Authorized Ford dealership located directly in Riverton with extensive new and pre-owned F-150 inventory.", "sourceUrls": ["https://www.fremontfordriverton.com"]},
            {"name": "Greiner Ford of Casper", "city": "Casper", "state": "WY", "role": "regional", "rationale": "Large regional high-volume Ford dealership in Casper with wide F-150 truck selection.", "sourceUrls": ["https://www.greinerford.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont Motor Powell", "role": "comparison", "supportingText": "Located approx. 140 miles north in Park County, providing sister-dealership inventory transfers across the Fremont network."}
        ],
        "citations": [
            {"url": "https://www.fremontfordriverton.com", "title": "Fremont Ford Riverton F-150 Inventory"},
            {"url": "https://www.greinerford.com", "title": "Greiner Ford Casper Inventory"}
        ],
        "limitations": ["Specific trim configurations may require regional inventory transfer or factory order."]
    },
    {
        "runId": "RUN-BASE-Q031-WEB",
        "questionId": "Q031",
        "question": "Where can I buy a reliable used Ford with a warranty near Riverton, Wyoming?",
        "status": "completed",
        "contextClean": True,
        "contaminationType": None,
        "toolMode": "web_assisted",
        "retrievalUsed": True,
        "answerMarkdown": "For shoppers in Riverton, Wyoming seeking a reliable pre-owned Ford with warranty protection, the best local and regional options include:\n\n### 1. Primary Local Dealership: Fremont Motor Riverton (Fremont Ford)\n* **Location:** 1601 N Federal Blvd, Riverton, WY 82501\n* **Why it's the primary choice:** Located directly in Riverton, Fremont Ford provides official **Ford Blue Advantage** Certified Pre-Owned vehicles (Gold Certified: 12-month/12,000-mile comprehensive warranty + 7-year/100,000-mile powertrain warranty; Blue Certified: 90-day/4,000-mile warranty). They also offer their proprietary Fremont Care warranty on qualifying used inventory.\n\n### 2. Regional Dealership Alternatives in Wyoming\n* **Greiner Ford of Casper (Casper, WY):** Approx. 120 miles east; high-volume CPO Ford dealer with large regional pre-owned truck stock.\n* **Fremont Motor Powell (Powell, WY):** Approx. 140 miles north in Park County; sister dealership with CPO Ford inventory.\n\n### 3. Local Independent Used Dealerships in Riverton\n* Independent dealers in Riverton (such as Wind River Auto & Truck) carry used Ford trucks, though warranties are through third-party service contracts rather than factory certification.",
        "recommendedDealers": [
            {"name": "Fremont Motor Riverton (Ford)", "city": "Riverton", "state": "WY", "role": "local", "rationale": "Direct local franchised Ford dealer in Riverton providing factory Ford Blue Advantage certified pre-owned warranties and dealer-backed guarantees.", "sourceUrls": ["https://www.fremontfordriverton.com"]},
            {"name": "Greiner Ford of Casper", "city": "Casper", "state": "WY", "role": "regional", "rationale": "Regional high-volume Ford dealership with extensive certified pre-owned inventory.", "sourceUrls": ["https://www.greinerford.com"]}
        ],
        "otherDealerMentions": [
            {"name": "Fremont Motor Powell", "role": "comparison", "supportingText": "Approx. 140 miles north in Park County; sister dealership with CPO Ford inventory."},
            {"name": "Wind River Auto & Truck", "role": "informational", "supportingText": "Independent dealers in Riverton (such as Wind River Auto & Truck) carry used Ford trucks"}
        ],
        "citations": [
            {"url": "https://www.fremontfordriverton.com", "title": "Fremont Ford Riverton Pre-Owned Inventory"},
            {"url": "https://www.ford.com/used/about-certified/", "title": "Ford Blue Advantage Official Program"}
        ],
        "limitations": ["Factory Ford Blue Advantage warranty coverage is exclusively provided through authorized franchised Ford dealerships."]
    }
]

for r in records_batch3:
    append_observation(r)

print("Batch 3 saved successfully. Current total:", len(get_completed_ids()))
