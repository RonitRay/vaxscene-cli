# vaxscene-cli

A vaccination slot tracker for India's [Co-Win Portal](https://cowin.gov.in) that uses [their publicly available API](https://apisetu.gov.in/public/api/cowin) to find available slots in a particular district and state.

Build instructions:

Prerequisite: Python 3.x

To start:
1. Edit vaxscene-cli.py and change the parameters DISTRICT_ID and AGE_BRACKET. District ID can be fetched using Co-Win's state and district listing web service.


    pip3 install schedule requests datetime playsound
    python3 vaxscene-cli.py

Companion post to understand how this works is at [https://ronitray.xyz/posts/covid-vaccination-tracker](https://ronitray.xyz/posts/covid-vaccination-tracker).
