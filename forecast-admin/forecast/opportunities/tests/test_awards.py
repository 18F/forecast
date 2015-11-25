from opportunities.models import Office, Opportunity
import pytest


# Test to make sure that the NAICS code is 5 digits long
@pytest.mark.django_db
def test_enforce_NAICS_code():
    opportunity = Opportunity()
    assert False
