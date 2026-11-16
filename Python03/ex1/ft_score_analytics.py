#!/usr/bin/env python3

import sys

def main () -> None:
    print("===Player Score Analytics===" )
    scores = process_scores()
    if len(scores) == 0:
        print(
        "No scores provided. "
        "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
            )
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print