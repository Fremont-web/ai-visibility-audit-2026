import csv
import json
import re
from pathlib import Path
from urllib.parse import urlparse
from collections import defaultdict, Counter

def normalize_domain(url):
    try:
        domain = urlparse(url).netloc.lower()
        if domain.startswith("www."):
            domain = domain[4:]
        return domain
    except Exception:
        return ""

FREMONT_DOMAINS = {
    "fremontmotors.com",
    "fremontfordlander.com",
    "fremontfordriverton.com",
    "fremontmotorsheridan.com",
    "fremontmotorpowell.com",
    "fremontmotorcody.com",
    "fremontchryslerdodgejeepcasper.com",
    "fremontchryslerdodgejeeprocksprings.com",
    "fremontchryslerdodgejeeprawlins.com",
    "fremontchryslerdodgejeeplander.com",
    "fremontchryslerdodgejeepcody.com",
    "fremonttoyotalander.com",
    "fremonttoyotasheridan.com",
    "fremonthondaofcasper.com",
    "fremontvolkswagencasper.com",
    "fremontcdjrriverton.com",
    "fremontchevygmcriverton.com",
    "sellyourcarwyoming.com"
}

def is_fremont_url(url):
    domain = normalize_domain(url)
    if not domain:
        return False
    return domain in FREMONT_DOMAINS or any(domain.endswith("." + fd) for fd in FREMONT_DOMAINS)

def normalize_dealer_name(raw_name):
    name = raw_name.strip()
    nl = name.lower()

    # Fremont normalizations
    if "fremont" in nl:
        return "Fremont Motor Companies"

    # Competitor normalizations
    if "greiner" in nl:
        return "Greiner Ford of Casper"
    if "whisler" in nl:
        return "Whisler Chevrolet Company"
    if "cowboy" in nl:
        return "Cowboy Chrysler Dodge Jeep Ram"
    if "uinta" in nl:
        return "Uinta Chrysler Dodge Jeep Ram"
    if "first choice" in nl:
        return "First Choice Ford"
    if "sheridan motors" in nl:
        if "gmc" in nl or "buick" in nl:
            return "Sheridan Motors GMC Buick"
        return "Sheridan Motors CDJR"
    if "bob ruwart" in nl:
        return "Bob Ruwart Motors"
    if "lithia" in nl and "billings" in nl:
        if "toyota" in nl:
            return "Lithia Toyota of Billings"
        return "Lithia Chrysler Jeep Dodge of Billings"
    if "denny menholt" in nl:
        return "Denny Menholt Cody"
    if "yellowstone" in nl:
        if "toyota" in nl:
            return "Yellowstone Toyota"
        if "chev" in nl or "gmc" in nl:
            return "Yellowstone Chevrolet GMC"
        return "Yellowstone Motors"
    if "white's energy" in nl or "whites energy" in nl:
        return "White's Energy Motors"
    if "white's frontier" in nl or "whites frontier" in nl:
        return "White's Frontier Motors"
    if "white's mountain" in nl or "whites mountain" in nl:
        if "subaru" in nl:
            return "White's Mountain Subaru"
        if "kia" in nl:
            return "White's Mountain Kia"
        return "White's Mountain Chevrolet"
    if "white family" in nl or "white's auto" in nl or "whites auto" in nl:
        return "White's Automotive Group"
    if "ken garff" in nl:
        if "ford" in nl:
            return "Ken Garff Ford Cheyenne"
        if "toyota" in nl:
            return "Ken Garff Toyota Cheyenne"
        if "hyundai" in nl:
            return "Ken Garff Hyundai Cheyenne"
        return "Ken Garff Cheyenne"
    if "halladay" in nl:
        if "subaru" in nl:
            return "Halladay Subaru"
        if "nissan" in nl:
            return "Halladay Nissan"
        return "Halladay Auto Group"
    if "laramie range" in nl:
        return "Laramie Range Ford"
    if "laramie gm" in nl:
        return "Laramie GM Auto Center"
    if "johnson auto" in nl:
        return "Johnson Auto of Laramie"
    if "skyline" in nl:
        return "Skyline Motors"
    if "tyrrell" in nl:
        if "honda" in nl:
            return "Tyrrell Honda"
        return "Tyrrell Chevrolet Company"
    if "wyoming truck" in nl:
        return "Wyoming Trucks & Cars"
    if "whitlock" in nl:
        return "Whitlock Motors"
    if "307 motor" in nl:
        return "307 Motors"
    if "arrowhead" in nl:
        return "Arrowhead Auto"
    if "brower" in nl:
        return "Brower Brothers Nissan"
    if "rock springs honda" in nl:
        return "Rock Springs Honda Toyota"
    if "rocky mountain yeti" in nl:
        return "Rocky Mountain Yeti Jackson CDJR"
    if "heritage chevrolet" in nl:
        return "Heritage Chevrolet of Evanston"
    if "heritage ford" in nl:
        return "Heritage Ford of Vernal"
    if "quality auto" in nl:
        return "Quality Auto of Casper"
    if "vista toyota" in nl:
        return "Vista Toyota"
    if "vista nissan" in nl:
        return "Vista Nissan"
    if "carmax" in nl:
        return "CarMax"
    if "carvana" in nl:
        return "Carvana"

    # Default: cleaned string
    return re.sub(r"\s+", " ", name)

def is_valid_dealer(canonical_name):
    # Exclude non-dealers (e.g. manufacturer websites, directory aggregators if any)
    lower = canonical_name.lower()
    excluded = {"ford", "chevrolet", "toyota", "jeep", "ram", "chrysler", "dodge", "gmc", "mopar", "edmunds", "kbb", "cargurus", "cars.com", "autotrader", "google", "yelp"}
    return lower not in excluded
