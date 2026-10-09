# Malta Trip Planner - Thunderpick CS2 Finals

This repository contains the organized, verified trip planner for the **Thunderpick World Championship 2026** trip to Malta, **13th–19th October 2026**.

## Project Scope
The goal of this planner is to provide a comprehensive guide for transportation, food, activities, everyday life for a US traveler, radio sports broadcasts, and an expense planner. All information is line-by-line verified to ensure zero hallucinations.

## Data Structure
The project follows a strict parallel-workstream design, separating data (`data/`) from presentation (`pages/`):
- **`data/*.json`**: Contains the raw, structured, and verified facts for each category.
- **`pages/*.html`**: Renders the information in an easy-to-read, mobile-friendly format.
- **`docs/`**: Contains the working plans, schemas, and status trackers.

## Site Navigation
- [Executive Summary](index.html)
- [Transport](pages/transport.html)
- [Food & Cafes](pages/food.html)
- [Activities & Landmarks](pages/activities.html)
- [Everyday Life (US Traveler)](pages/everyday.html)
- [Radio Sports Broadcasts](pages/radio.html)
- [Expense Planner](pages/expenses.html)

## Limitations & Open Questions
- Flight costs cannot be finalized until the specific departure airport and itinerary are provided.
- BBC World Service sports broadcast schedules specifically for the weekend of October 17-18, 2026, will not be confirmed until closer to the date, although TalkSport on DAB+ is verified to carry EPL matches.
- All pricing (ride shares, food) is based on verified current rates but may fluctuate slightly during the event week due to surge pricing.

## Verification
All claims have been verified through official websites, verified social media accounts, or reputable local reviews. No unverified guesses have been presented as fact.
