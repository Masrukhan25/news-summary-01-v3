# news-summary-01

A small, deterministic program that writes a single world-news summary for Wednesday 11 November 2026 to `entry.txt` inside the output directory (default `/output`, or the directory set by `MAKEFUN_OUTPUT_DIR`). The summary is 1995 characters covering 16 ranked stories, written in a sober editorial voice, with contested claims attributed to their sources.

## Stories covered, in order

1. Nvidia's board prepares to oust CEO Jensen Huang amid affair and espionage allegations
2. Abu Dhabi trilateral talks: no ceasefire, but the war's largest prisoner swap agreed
3. Russian strikes on Ukrainian power substations and a Chornomorsk market
4. NATO jets scrambled; a US soldier held in Britain on Russia-spying suspicion
5. Gadi Eisenkot tasked with forming Israel's new government
6. Killings in Gaza and Houthi missile interceptions aimed at Riyadh
7. Iran: Trump pauses fresh strikes, three operatives charged, Bessent moves to a base
8. US politics: Hegseth impeachment blocked; Scott Colom wins Mississippi Senate race
9. COP31 opens in Antalya
10. Markets: S&P 500, Nasdaq, and Brent crude
11. Spain's first general strike in 14 years
12. Poland's national mourning for Krakow shooting victims
13. UK court strikes down Trinidad and Tobago's gay-sex ban
14. Poor air quality in Delhi after Diwali
15. Washington driverless-taxis measure falls one vote short
16. Kazakhstan-tied AI hacking group steals Tajikistan security documents

## Sources

Reuters, New York Times, Wall Street Journal, The Information, Associated Press, UNFCCC, and wire reporting of 11 November 2026.

## How to run

```bash
python3 main.py
```

The program writes `entry.txt` to `/output` by default. Override with `export MAKEFUN_OUTPUT_DIR=/path/to/output`.
