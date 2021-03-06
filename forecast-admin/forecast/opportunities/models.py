from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, RegexValidator

from localflavor.us.models import USStateField, PhoneNumberField
from localflavor.us.us_states import US_STATES, US_TERRITORIES
from django_countries.fields import CountryField
from django_countries import countries
from opportunities.validators import validate_NAICS

from datetime import date


# Create your models here.
class OfficeManager(models.Manager):
    def get_by_natural_key(self, office_id):
        return self.get(id=office_id)

class Office(models.Model):
    REGIONS = (
        ("Region 1", "Region 1"),
        ("Region 2", "Region 2"),
        ("Region 3", "Region 3"),
        ("Region 4", "Region 4"),
        ("Region 5", "Region 5"),
        ("Region 6", "Region 6"),
        ("Region 7", "Region 7"),
        ("Region 8", "Region 8"),
        ("Region 9", "Region 9"),
        ("Region 10", "Region 10"),
        ("National Capital Region", "National Capital Region"),
        ("Central Office", "Central Office")
    )

    objects = OfficeManager()

    organization = models.CharField(max_length=100, blank=False)
    region = models.CharField(max_length=100, blank=False, choices=REGIONS)

    def natural_key(self):
        return (self.organization, self.region)

    def __str__(self):
        return "%s (%s)" % (self.organization, self.region)

    class Meta:
        ordering = ["organization"]


# The OSBU Advisor is the Office of Small Business Utilization specialist
# who is responsible for the forecast data...
class OSBUAdvisorManager(models.Manager):
    def get_by_natural_key(self, advisor_id):
        return self.get(id=advisor_id)

class OSBUAdvisor(models.Model):
    objects = OSBUAdvisorManager()

    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)

    def natural_key(self):
        return (self.name, self.email, self.phone)

    def __str__(self):
        return "%s (%s, %s)" % (self.name, self.email, self.phone)

    class Meta:
        verbose_name = "OSBU Advisor"


class Opportunity(models.Model):
    AWARD_STATUS_CHOICES = (
        ("Award Pending", "Award Pending"),
        ("Awarded", "Awarded"),
        ("Cancelled", "Cancelled"),
        ("Drafting Solicitation", "Drafting Solicitation"),
        ("Evaluation Stage", "Evaluation Stage"),
        ("Option Exercise Pending", "Option Exercise Pending"),
        ("Option Exercised", "Option Exercised"),
        ("Planning", "Planning"),
        ("Solicitation Closed", "Solicitation Closed"),
        ("Solicitation Issued", "Solicitation Issued"),
      )

    SOCIOECONOMIC_CHOICES = (
        ("AbilityOne", "AbilityOne"),
        ("HUBZone Small Business", "HUBZone Small Business"),
        ("Multiple Small Business Categories",
            "Multiple Small Business Categories"),
        ("Other Than Small", "Other Than Small"),
        ("Service Disabled Veteran-owned Small Business",
            "Service Disabled Veteran-owned Small Business"),
        ("Small Business", "Small Business"),
        ("Small Disadvantaged Business (includes Section 8a)",
            "Small Disadvantaged Business (includes Section 8a)"),
        ("To Be Determined-BPA", "To Be Determined-BPA"),
        ("To Be Determined-IDIQ", "To Be Determined-IDIQ"),
        ("To Be Determined", "To Be Determined"),
        ("Veteran-owned Small Business", "Veteran-owned Small Business"),
        ("Woman-Owned Small Business", "Woman-Owned Small Business"),
    )

    CONTRACT_TYPE_CHOICES = (
        ("Cost No Fee", "Cost No Fee"),
        ("Cost Plus Award Fee", "Cost Plus Award Fee"),
        ("Cost Plus Fixed Fee", "Cost Plus Fixed Fee"),
        ("Cost Plus Incentive Fee", "Cost Plus Incentive Fee"),
        ("Cost Sharing", "Cost Sharing"),
        ("Fixed Price","Fixed Price"),
        ("Fixed Price Award Fee", "Fixed Price Award Fee"),
        ("Fixed Price Incentive", "Fixed Price Incentive"),
        ("Fixed Price Labor Hours","Fixed Price Labor Hours"),
        ("Fixed Price Level of Effort","Fixed Price Level of Effort"),
        ("Fixed Price Time and Materials","Fixed Price Time and Materials"),
        ("Fixed Price with Economic Price Adjustment",
            "Fixed Price with Economic Price Adjustment"),
        ("Interagency Agreement", "Interagency Agreement"),
        ("Labor Hours", "Labor Hours"),
        ("Labor Hours and Time and Materials","Labor Hours and Time and Materials"),
        ("Order Dependent", "Order Dependent"),
        ("Time and Materials", "Time and Materials"),
        ("To Be Determined", "To Be Determined"),
    )

    PROCUREMENT_METHOD_CHOICES = (
        ("GSA Schedule", "GSA Schedule"),
        ("Government-wide Agency Contract-GWAC",
            "Government-wide Agency Contract-GWAC"),
        ("Basic Ordering Agreement", "Basic Ordering Agreement"),
        ("Blanket Purchase Agreement-BPA", "Blanket Purchase Agreement-BPA"),
        ("Multi-Agency Contract", "Multi-Agency Contract"),
        ("BPA Call", "BPA Call"),
        ("Purchase Order", "Purchase Order"),
        ("Definitive Contract", "Definitive Contract"),
        ("Ability One", "Ability One"),
        ("Indefinite Delivery Indefinite Quantity-IDIQ",
            "Indefinite Delivery Indefinite Quantity-IDIQ"),
        ("Negotiated", "Negotiated"),
        ("Sealed Bid", "Sealed Bid"),
        ("Contract", "Contract"),
        ("Commercial Item Contract", "Commercial Item Contract"),
        ("GSA Schedules Program BPA", "GSA Schedules Program BPA"),
        ("Indefinite Delivery Vehicle (IDV)",
            "Indefinite Delivery Vehicle (IDV)"),
        ("Purchase Order", "Purchase Order"),
        ("Order under IDV", "Order under IDV"),
        ("Order under GSA Schedules Program",
            "Order under GSA Schedules Program"),
        ("Order under GSA Schedules Program BPA",
            "Order under GSA Schedules Program BPA"),
        ("To Be Determined", "To Be Determined"),
        ("Definitive Contract other than IDV",
            "Definitive Contract other than IDV"),
        ("Indefinite Delivery Vehicle Base Contract",
            "Indefinite Delivery Vehicle Base Contract"),
        ("Order under GSA Federal Supply Schedules Program",
            "Order under GSA Federal Supply Schedules Program"),
        ("Order under IDV", "Order under IDV"),
        ("Purchase Order", "Purchase Order"),
        ("Contract modification", "Contract modification"),
        ("Ability One", "Ability One"),
        ("Call Order under GSA Schedules BPA",
            "Call Order under GSA Schedules BPA"),
        ("To Be Determined", "To Be Determined"),
        ("GSA Schedule Contract", "GSA Schedule Contract"),
        ("Negotiated", "Negotiated"),
        ("Sealed Bid", "Sealed Bid"),
        ("Government-wide Agency Contract-GWAC",
            "Government-wide Agency Contract-GWAC"),
        ("Commercial Item Contract", "Commercial Item Contract"),
        ("GSA Schedules Program BPA", "GSA Schedules Program BPA"),
        ("Basic Ordering Agreement", "Basic Ordering Agreement"),
        ("Blanket Purchase Agreement-BPA", "Blanket Purchase Agreement-BPA"),
        ("Multi-Agency Contract", "Multi-Agency Contract")
      )

    COMPETITION_CHOICES = (
        ("Sole Source", "Sole Source"),
        ("Full and Open", "Full and Open"),
        ("Set-Aside", "Set-Aside"),
        ("Partial Small Business Set-Aside",
            "Partial Small Business Set-Aside"),
        ("A/E Procedures", "A/E Procedures"),
        ("Full and Open Competition", "Full and Open Competition"),
        ("Not Available for Competition (e.g., 8a sole source, HUBZone & \
            SDVOSB sole source, Ability One, all > SAT)",
            "Not Available for Competition (e.g., 8a sole source, HUBZone & \
            SDVOSB sole source, Ability One, all > SAT)"),
        ("Not Competed (e.g., sole source, urgency, etc., all > SAT)",
            "Not Competed (e.g., sole source, urgency, etc., all > SAT)"),
        ("Full and Open after exclusion of sources (competitive small \
            business set-asides, competitive 8a)",
            "Full and Open after exclusion of sources (competitive small \
            business set-asides, competitive 8a)"),
        ("Follow On to Competed Action", "Follow On to Competed Action"),
        ("Competed under SAP", "Competed under SAP"),
        ("Not Competed under SAP (e.g., Urgent, Sole source, Logical \
            Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)",
            "Not Competed under SAP (e.g., Urgent, Sole source, Logical \
            Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)"),
        ("Competitive Delivery Order Fair Opportunity Provided",
            "Competitive Delivery Order Fair Opportunity Provided"),
        ("Non-Competitive Delivery Order", "Non-Competitive Delivery Order"),
        ("Fair Opportunity", "Fair Opportunity"),
        ("Sole-Source", "Sole-Source"),
        ("Limited Sources", "Limited Sources"),
        ("To Be Determined", "To Be Determined"),
        ("Competitive Schedule Buy", "Competitive Schedule Buy"),
        ("Full and Open after exclusion of sources (competitive small business \
            set-asides, competitive 8a)",
            "Full and Open after exclusion of sources (competitive small \
            business set-asides, competitive 8a)"),
        ("Full and Open Competition Unrestricted",
            "Full and Open Competition Unrestricted"),
        ("Not Available for Competition (e.g., 8a sole source, HUBZone & \
            SDVOSB sole source, Ability One, all > SAT)",
            "Not Available for Competition (e.g., 8a sole source, HUBZone & \
            SDVOSB sole source, Ability One, all > SAT)"),
        ("Not Competed (e.g., sole source, urgency, etc., all > SAT)",
            "Not Competed (e.g., sole source, urgency, etc., all > SAT)"),
        ("Not Competed under SAP (e.g., Urgent, Sole source, Logical \
            Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)",
            "Not Competed under SAP (e.g., Urgent, Sole source, Logical \
            Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)"),
        ("A/E Procedures", "A/E Procedures"),
        ("Competed under SAP", "Competed under SAP"),
        ("Follow On to Competed Action (FAR 6.302-1)",
            "Follow On to Competed Action (FAR 6.302-1)"),
        ("To Be Determined", "To Be Determined"),
        ("Limited Sources FSS Order", "Limited Sources FSS Order"),
        ("Competitive Schedule Buy", "Competitive Schedule Buy"),
        ("Partial Small Business Set-Aside",
            "Partial Small Business Set-Aside")
     )

    NEW_REQUIREMENT_CHOICES = (
        ("New Requirement", "New Requirement"),
        ("Option", "Option"),
        ("To Be Determined", "To Be Determined"),
        ("Recompete", "Recompete")
    )

    FUNDING_AGENCY_CHOICES = (
        ("GSA funded", "GSA funded"),
        ("GSA funded-PBS", "GSA funded-PBS"),
        ("GSA funded-FAS", "GSA funded-FAS"),
        ("GSA funded-IAD", "GSA funded-IAD"),
        ("GSA funded-Other", "GSA funded-Other"),
        ("Non-GSA funded", "Non-GSA funded"),
        ("Both", "Both"),
        ("To Be Determined", "To Be Determined")
    )

    CURRENT_YEAR = date.today().year
    FISCAL_YEARS = (
        (CURRENT_YEAR, CURRENT_YEAR),
        (CURRENT_YEAR+1, CURRENT_YEAR+1),
        (CURRENT_YEAR+2, CURRENT_YEAR+2),
        (CURRENT_YEAR+3, CURRENT_YEAR+3),
        (CURRENT_YEAR+4, CURRENT_YEAR+4)
    )

    FISCAL_QUARTERS = (
        ("1st", "1st"),
        ("2nd", "2nd"),
        ("3rd", "3rd"),
        ("4th", "4th"),
        ("To Be Determined", "To Be Determined")
    )

    NON_STATE_OPTIONS = (
        ("TBD", "TBD"),
        ("Regionwide", "Regionwide"),
        ("Various", "Various"),
        ("International", "International")
    )
    STATES = NON_STATE_OPTIONS+US_STATES+US_TERRITORIES
    COUNTRIES = countries

    office = models.ForeignKey(Office, blank=True, null=True)
    agency = models.CharField(max_length=100, default="GSA", editable=False)
    award_status = models.CharField(max_length=50, default="Planning",
                                    choices=AWARD_STATUS_CHOICES, blank=False)
    description = models.CharField("Product or Service Description",
                                   max_length=1000, blank=False)
    place_of_performance_city = models.CharField(max_length=100,
                                                 default="Washington", blank=False)
    place_of_performance_state = models.CharField(max_length=100,
                                                  choices=STATES, default="DC")
    place_of_performance_country = models.CharField(max_length=100,
                                                    choices=COUNTRIES,
                                                    default="US",
                                                    blank=False)
    naics = models.CharField("Primary NAICS Code",
                             max_length=6, blank=False, null=True,
                             validators=[validate_NAICS])
    socioeconomic = models.CharField("Socioeconomic Category", max_length=100,
                                     choices=SOCIOECONOMIC_CHOICES,
                                     default="To Be Determined", blank=False)
    procurement_method = models.CharField("Procurement Method", max_length=200,
                                          choices=PROCUREMENT_METHOD_CHOICES,
                                          default="To Be Determined")
    contract_type = models.CharField("Contract Type", max_length=200,
                                     choices=CONTRACT_TYPE_CHOICES,
                                     default="To Be Determined")
    competition_strategy = models.CharField(max_length=200,
                                            choices=COMPETITION_CHOICES,
                                            default="To Be Determined")
    dollar_value_min = models.DecimalField(max_length=200, decimal_places=2,
                                    max_digits=16, blank=False, null=True,
                                    validators=[RegexValidator(regex="\d*(\.\d\d)?",
                                        message="Please enter a dollar value.")])
    dollar_value_max = models.DecimalField(max_length=200, decimal_places=2,
                                    max_digits=16, blank=False, null=True)
    including_options = models.BooleanField(default=False)
    delivery_order_value = models.CharField(max_length=200,
                                            blank=True, null=True)
    incumbent_name = models.CharField("Incumbent Contractor Name",
                                      max_length=400, blank=True, null=True)
    new_requirement = models.CharField(max_length=200,
                                       choices=NEW_REQUIREMENT_CHOICES,
                                       default="To Be Determined", blank=False)
    funding_agency = models.CharField(max_length=200,
                                      choices=FUNDING_AGENCY_CHOICES,
                                      default="To Be Determined", blank=False)
    estimated_solicitation_date = models.DateField(blank=False, null=True)
    fedbizopps_link = models.CharField(max_length=200, blank=True, null=True)
    estimated_fiscal_year = models.IntegerField(default=2016,
                                                choices=FISCAL_YEARS, blank=False)
    estimated_fiscal_year_quarter = models.CharField(max_length=50,
        default="To Be Determined", choices=FISCAL_QUARTERS
    )
    # Note: This can probably get split out into another model
    point_of_contact_name = models.CharField(max_length=200,
                                             blank=False, null=True)
    point_of_contact_email = models.EmailField(max_length=200,
                                               blank=False, null=True)
    point_of_contact_phone = PhoneNumberField(blank=True, null=True)
    osbu_advisor = models.ForeignKey(OSBUAdvisor, blank=False, null=True,
                                    verbose_name="OSBU Advisor")
    additional_information = models.TextField(blank=True, null=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return "%s (%s)" % (self.description, self.estimated_fiscal_year)

    def clean(self):
        super(Opportunity, self).clean()

        if self.place_of_performance_country == 'US' and not self.place_of_performance_state:
            raise ValidationError('A state is required for opportunities in the US')

    class Meta:
        verbose_name = "Procurement"
        verbose_name_plural = "Procurements"
        ordering = ["office"]
