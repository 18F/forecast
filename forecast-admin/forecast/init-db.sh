#!/bin/sh

./manage.py load_opportunities -p
./manage.py load_opportunities -a USAID -f forecast/data/usaid.csv -p
./manage.py load_opportunities -a Education -f forecast/data/education.csv -p
./manage.py load_opportunities -a State -f forecast/data/state.csv -p
./manage.py load_opportunities -a SSA -f forecast/data/ssa.csv -p
./manage.py load_opportunities -a Treasury -f forecast/data/treasury.csv -p
