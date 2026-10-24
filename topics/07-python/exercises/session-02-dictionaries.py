"""Python L1 Session 02 exercises: dictionaries.

Implement each function, then run this file with Python 3. The assertions are
the self-checks; do not replace them with hard-coded results.
"""


def service_owner(service):
    """Return the owner of a service; owner is a required field."""
    raise NotImplementedError("Implement exercise 1")


def optional_review_date(service):
    """Return the review date, or 'not recorded' if it is absent."""
    raise NotImplementedError("Implement exercise 2")


def set_service_status(service, status):
    """Return a copy of service with its status updated."""
    raise NotImplementedError("Implement exercise 3")


def check_exercises():
    service = {
        "id": "payments-api",
        "owner": "Commerce",
        "tier": 1,
        "status": "healthy",
    }

    assert service_owner(service) == "Commerce"
    assert optional_review_date(service) == "not recorded"
    assert optional_review_date({**service, "last_review": "2026-10-01"}) == "2026-10-01"

    updated = set_service_status(service, "degraded")
    assert updated == {**service, "status": "degraded"}
    assert updated is not service
    assert service["status"] == "healthy"


if __name__ == "__main__":
    check_exercises()
    print("All dictionary exercises passed.")
