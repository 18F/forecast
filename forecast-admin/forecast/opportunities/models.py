from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField, PhoneNumberField
from opportunities.validators import validate_NAICS


# Create your models here.
class Office(models.Model):
    organization = models.CharField(max_length=30)
    region = models.CharField(max_length=30)

    def __str__(self):
        return "%s (%s)" % (self.organization, self.region)


class OSBU_Advisor(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return "%s (%s)" % (self.name, self.email)

    class Meta:
        verbose_name = "OSBU Advisor"


class Opportunity(models.Model):
    AWARD_STATUS_CHOICES = (
        (0, "Awarded"),
        (1, "Award Pending"),
        (2, "Solicitation Issued"),
        (3, "Drafting Solicitation"),
        (4, "Solicitation Closed"),
        (5, "Planning"),
        (7, "Cancelled"),
        (8, "Evaluation Stage"),
        (9, "Option Exercise Pending"),
        (10, "Option Exercised"),
      )

    SOCIOECONOMIC_CHOICES = (
        (0, "Small Business"),
        (1, "Small Disadvantaged Business (includes Section 8a)"),
        (2, "Woman-Owned Small Business"),
        (3, "HUBZone Small Business"),
        (4, "Service Disabled Veteran-owned Small Business"),
        (5, "Multiple Small Business Categories"),
        (6, "Other Than Small"),
        (7, "AbilityOne"),
        (8, "To Be Determined"),
        (9, "To Be Determined-BPA"),
        (10, "To Be Determined-IDIQ")
    )

    CONTRACT_TYPE_CHOICES = (
        (0, "Fixed Price with Economic Price Adjustment"),
        (1, "Fixed Price Incentive"),
        (2, "Fixed Price Award Fee"),
        (3, "Cost Plus Award Fee"),
        (4, "Cost No Fee"),
        (5, "Cost Sharing"),
        (6, "Cost Plus Fixed Fee"),
        (7, "Cost Plus Incentive Fee"),
        (8, "Time and Materials"),
        (9, "Labor Hours"),
        (10, "Order Dependent"),
        (11, "To Be Determined"),
        (12, "Interagency Agreement")
    )

    PROCUREMENT_METHOD_CHOICES = (
        (0, "GSA Schedule"),
        (1, "Government-wide Agency Contract-GWAC"),
        (2, "Basic Ordering Agreement"),
        (3, "Blanket Purchase Agreement-BPA"),
        (4, "Multi-Agency Contract"),
        (5, "BPA Call"),
        (6, "Purchase Order"),
        (7, "Definitive Contract"),
        (8, "Ability One"),
        (9, "Indefinite Delivery Indefinite Quantity-IDIQ"),
        (10, "Negotiated"),
        (11, "Sealed Bid"),
        (12, "Contract"),
        (13, "Commercial Item Contract"),
        (14, "GSA Schedules Program BPA"),
        (15, "Indefinite Delivery Vehicle (IDV)"),
        (16, "Purchase Order"),
        (17, "Order under IDV"),
        (18, "Order under GSA Schedules Program"),
        (19, "Order under GSA Schedules Program BPA"),
        (20, "To Be Determined"),
        (21, "Definitive Contract other than IDV"),
        (22, "Indefinite Delivery Vehicle Base Contract"),
        (23, "Order under GSA Federal Supply Schedules Program"),
        (24, "Order under IDV"),
        (25, "Purchase Order"),
        (26, "Contract modification"),
        (27, "Call Order under GSA Schedules BPA"),
    )

    COMPETITION_CHOICES = (
        (0, "Sole Source"),
        (1, "Full and Open"),
        (2, "Set-Aside"),
        (3, "Partial Small Business Set-Aside"),
        (4, "A/E Procedures"),
        (5, "Full and Open Competition"),
        (6, "Not Available for Competition (e.g., 8a sole source, HUBZone & \
            SDVOSB sole source, Ability One, all > SAT)"),
        (7, "Not Competed (e.g., sole source, urgency, etc., all > SAT)"),
        (8, "Full and Open after exclusion of sources (competitive small \
            business set-asides, competitive 8a)"),
        (9, "Follow On to Competed Action"),
        (10, "Competed under SAP"),
        (11, "Not Competed under SAP (e.g., Urgent, Sole source, Logical \
            Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)"),
        (12, "Competitive Delivery Order Fair Opportunity Provided"),
        (13, "Non-Competitive Delivery Order"),
        (14, "Fair Opportunity"),
        (15, "Sole-Source"),
        (16, "Limited Sources"),
        (17, "To Be Determined"),
        (18, "Competitive Schedule Buy"),
        (19, "Full and Open after exclusion of sources (competitive small \
             business set-asides, competitive 8a)"),
        (20, "Full and Open Competition Unrestricted"),
        (21, "Not Available for Competition (e.g., 8a sole source, HUBZone & \
            SDVOSB sole source, Ability One, all > SAT)"),
        (22, "Not Competed (e.g., sole source, urgency, etc., all > SAT)"),
        (23, "Not Competed under SAP (e.g., Urgent, Sole source, Logical \
             Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)"),
        (24, "A/E Procedures"),
        (25, "Competed under SAP"),
        (26, "Follow On to Competed Action (FAR 6.302-1)"),
        (27, "Competitive Delivery Order - Fair Opportunity Provided"),
        (28, "Non-Competitive Delivery Order"),
        (29, "Limited Sources FSS Order"),
        (30, "Competitive Schedule Buy"),
        (31, "Partial Small Business Set-Aside")
     )

    NEW_REQUIREMENT_CHOICES = (
        (0, "New Requirement"),
        (1, "Option"),
        (2, "To Be Determined"),
        (3, "Recompete")
    )

    FUNDING_AGENCY_CHOICES = (
        (0, "GSA funded"),
        (1, "GSA funded-PBS"),
        (2, "GSA funded-FAS"),
        (3, "GSA funded-IAD"),
        (4, "GSA funded-Other"),
        (5, "Non-GSA funded"),
        (6, "Both"),
        (7, "To Be Determined")
    )

    office = models.ForeignKey(Office, blank=True, null=True)
    award_status = models.CharField(max_length=50, default=0,
                                    choices=AWARD_STATUS_CHOICES)
    description = models.CharField("Product or Service Description",
                                   max_length=200)
    place_of_performance_city = models.CharField(max_length=100,
                                                 default="Washington")
    place_of_performance_state = USStateField(default="DC")
    naics = models.CharField("Primary NAICS Code",
                             max_length=5, blank=True, null=True,
                             validators=[validate_NAICS])
    socioeconomic = models.CharField("Socioeconomic Category", max_length=50,
                                     choices=SOCIOECONOMIC_CHOICES,
                                     default=8)
    procurement_method = models.CharField("Procurement Method", max_length=200,
                                          choices=PROCUREMENT_METHOD_CHOICES,
                                          default=20)
    contract_type = models.CharField("Contract Type", max_length=200,
                                     choices=CONTRACT_TYPE_CHOICES,
                                     default=11)
    competition_strategy = models.CharField(max_length=200,
                                            choices=COMPETITION_CHOICES,
                                            default=17)
    price_min = models.CharField(max_length=200, blank=True, null=True)
    price_max = models.CharField(max_length=200, blank=True, null=True)
    delivery_order_value = models.CharField(max_length=200,
                                            blank=True, null=True)
    incumbent_name = models.CharField("Incumbent Contractor Name",
                                      max_length=200, blank=True, null=True)
    new_requirement = models.CharField(max_length=200,
                                       choices=NEW_REQUIREMENT_CHOICES,
                                       default=2)
    funding_agency = models.CharField(max_length=200,
                                      choices=FUNDING_AGENCY_CHOICES,
                                      default=7)
    estimated_solicitation_date = models.DateField(blank=True, null=True)
    fedbizopps_link = models.CharField(max_length=200, blank=True, null=True)
    estimated_fiscal_year = models.CharField(max_length=200,
                                             blank=True, null=True)
    estimated_fiscal_year_quarter = models.CharField(max_length=200,
                                                     blank=True, null=True)
    point_of_contact_name = models.CharField(max_length=200,
                                             blank=True, null=True)
    point_of_contact_email = models.EmailField(max_length=200,
                                               blank=True, null=True)
    point_of_contact_phone = PhoneNumberField(blank=True, null=True)
    osbu_advisor = models.ForeignKey(OSBU_Advisor, blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return "%s (%s)" % (self.description, self.estimated_fiscal_year)

    class Meta:
        verbose_name_plural = "Opportunities"
