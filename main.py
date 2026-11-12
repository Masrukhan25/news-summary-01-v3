#!/usr/bin/env python3
"""Make.fun bounty entry: news-summary-01 world news summary for Wednesday 11 November 2026."""

import os

SUMMARY = (
    "World news, Wednesday 11 November 2026.\n"
    "\n"
    "1. Nvidia's board prepared to oust CEO Jensen Huang, the WSJ reported, after his affair "
    "with Alice Huang, suspected of spying for China and tied to $7.5bn of chips to China; "
    "the NYT reported a second affair with VP Kimberly Powell. Shares fell 8.6% to ~$159.\n"
    "2. Abu Dhabi talks ended with no ceasefire but agreed a big prisoner swap; Ukraine "
    "rejected Donbas demands. Envoys head to Moscow Thursday.\n"
    "3. Russia hit six Ukrainian substations and a Chornomorsk market (3 killed, 11 wounded); "
    "Ukraine damaged five tanks at Ust-Luga.\n"
    "4. NATO jets scrambled after four drones entered Baltic airspace; a US soldier was held "
    "in Britain on Russia-spying suspicion.\n"
    "5. Eisenkot was tasked to form Israel's government as the 26th Knesset was sworn in "
    "(67 vs 46 for Netanyahu).\n"
    "6. Seven killed in Gaza, including a father and his 13-year-old son; strikes hit "
    "southern Lebanon; Saudi Arabia intercepted seven Houthi missiles/drones at Riyadh.\n"
    "7. Trump paused Iran strikes; Rubio said no major combat was needed. Three Iran-backed "
    "operatives were charged over 20 plots including RAF Fairford; Bessent moved to a base "
    "after threats.\n"
    "8. The House blocked Hegseth's impeachment 211-204; Democrat Scott Colom won the "
    "Mississippi Senate race.\n"
    "9. COP31 opened in Antalya with 102 leaders; Guterres warned of a path to destruction; "
    "five nations backed solar expansion.\n"
    "10. S&P 500 +1.31% to 7,619.38; Nasdaq +1.60% to 25,466.19; Brent crude $92.76 (+1.39%).\n"
    "11. Spain's first general strike in 14 years drew 4m workers protesting housing costs.\n"
    "12. Poland began two days of mourning for six Krakow mass-shooting victims.\n"
    "13. The UK's top court struck down Trinidad and Tobago's colonial-era gay-sex ban.\n"
    "14. Delhi's post-Diwali air averaged 299; young pupils shifted to hybrid classes.\n"
    "15. The D.C. Council fell one vote short of letting driverless taxis carry paying "
    "passengers.\n"
    "16. CloudSEK: a Kazakhstan-tied group used AI to steal over 2,000 Tajikistan security "
    "documents."
)


def main() -> None:
    length = len(SUMMARY)
    if not (1 <= length <= 2000):
        raise ValueError(f"Summary length {length} is not between 1 and 2000 characters.")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(SUMMARY)


if __name__ == "__main__":
    main()
