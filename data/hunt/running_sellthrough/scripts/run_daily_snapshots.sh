#!/bin/bash
# Repeat the two cheap snapshots daily from now to Nov 19 so a trend exists before the finals. Run from data/hunt/running_sellthrough.
# Writes dated files (never overwrites). No login, no personal data.
D=$(date -u +%F)
python3 -I scripts/pull_amazon_bestsellers.py raw "$D" 679360011
python3 -I scripts/pull_fleetfeet_sizeruns.py "raw/fleetfeet_upc_$D.csv.gz" "mens-nike-pegasus-42,womens-nike-pegasus-42,mens-nike-vomero-18,womens-nike-vomero-18,mens-nike-vomero-plus,womens-nike-vomero-plus,mens-nike-vomero-premium,womens-nike-vomero-premium,mens-nike-pegasus-plus-2,womens-nike-pegasus-plus-2,mens-hoka-bondi-9,womens-hoka-bondi-9,mens-hoka-clifton-11,womens-hoka-clifton-11,mens-brooks-ghost-18,womens-brooks-ghost-18,mens-brooks-glycerin-23,womens-brooks-glycerin-23,mens-asics-novablast-6,womens-asics-novablast-6,mens-asics-gel-nimbus-28,womens-asics-gel-nimbus-28,mens-saucony-ride-19,womens-saucony-ride-19,mens-on-cloudmonster-3,womens-on-cloudmonster-3"
