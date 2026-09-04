"""
Fitness function example — a rule a robot enforces so humans don't have to.

THE RULE (from ADR-0004, our topic-security decision):
    Only approved services may subscribe to the 'bids' topic.
    (Remember: anyone who subscribes to a topic can silently READ every bid.
     That was the trade-off we accepted — but only for a controlled list.)

Instead of hoping nobody breaks the rule, this check runs in the build
pipeline (CI). If an unapproved service subscribes, the build FAILS.
That's what a fitness function is: an automated check that an architecture
decision still holds.
"""

APPROVED_SUBSCRIBERS = {"bid_capture", "bid_tracking", "bid_analytics"}


def check_subscriber(service_name: str, topic: str) -> None:
    if topic == "bids" and service_name not in APPROVED_SUBSCRIBERS:
        # Fail loudly — break the build, not the architecture
        raise SystemExit(
            f"FITNESS FUNCTION FAILED: '{service_name}' may not subscribe to "
            f"'bids'. See ADR-0004 — add it to the approved list *with a new ADR* "
            f"first, or remove the subscription."
        )
    print(f"OK: '{service_name}' on '{topic}' is allowed.")


# Demo — comment these out and wire `check_subscriber` into your real build:
if __name__ == "__main__":
    check_subscriber("bid_tracking", "bids")      # passes
    check_subscriber("rogue_scraper", "bids")     # fails the build
