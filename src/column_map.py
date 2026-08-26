"""
SES 2564 (2021) column name mapping: original field code -> readable snake_case name.

Sources:
  Datadic SES 2564/4.Record 01 หน้า 1-14.xls   (Iden + Record 01 sheets)
  Datadic SES 2564/5.Record 02 หน้า 15-21.xls
  Datadic SES 2564/6.Record 03 หน้า 22-26.xls
  Datadic SES 2564/7.Record 04-11 หน้า 27-42.xls
  Datadic SES 2564/8.Record 12 หน้า 43-45.xls
  Datadic SES 2564/9.Record 13-14 หน้า 46-50.xls
  Datadic SES 2564/10.Record 15-17 หน้า 51-65.xls
  Datadic SES 2564/11.Record 18 หน้า 66-71.xls
  Datadic SES 2564/12.Record 25 หน้า 72-73.xls
"""

COLUMN_MAP: dict[str, str] = {

    # ── IDENTIFICATION (Iden sheet) ──────────────────────────────────────────
    "REG":        "region",                         # 1=BKK 2=Central 3=North 4=NE 5=South
    "CWT":        "province",                       # changwat code (Appendix A)
    "AMP":        "district",                       # amphoe code
    "TMB":        "subdistrict",                    # tambon code
    "AREA":       "area_type",                      # 1=municipal 2=non-municipal
    "EA":         "enum_district",                  # enumeration district no.
    "VIL":        "village_no",
    "PSU_NO":     "psu_no",                         # primary sample unit no.
    "HH_NO":      "hh_no",                          # sample household no. within PSU
    "ENUM":       "enum_result",                    # enumeration result code
    "ENUM24":     "enum24_remark",                  # remark for ENUM=24
    "New_hh_no":  "household_id",                   # new unique household number
    "NEW_HH_NO":  "household_id",                   # alias — actual CSV header is all-caps
    "ID_CODE 1":  "enumerator_id",
    "ID_CODE 2":  "coder_id",

    # ── REC01 — HOUSEHOLD SUMMARY ────────────────────────────────────────────
    "REC":        "record_no",
    "SUB":        "sub_record_no",

    # A-series: household-level summary
    "A01":        "enum_month",                     # enumeration month (1-12)
    "A02":        "n_workers_incl_servants",        # no. of income-earning members incl. servants
    "A02_1":      "n_workers_excl_servants",        # no. of income-earning members excl. servants
    "A03":        "socioeconomic_class",            # household socio-economic class

    "A04":        "n_members_incl_servants",        # household size incl. servants
    "A04_1":      "n_members_excl_servants",        # household size excl. servants
    "A05":        "n_wage_employees",               # no. of members earning wages/salaries (for REC13)
    "A06":        "n_nonfarm_business_operators",   # no. of members in non-farm business (for REC14)

    # Expenditure aggregates (monthly averages, baht)
    "A07":        "monthly_expenditure_household",  # total expenditure per household
    "A08":        "monthly_consumption_expenditure",# consumption expenditure per household
    "A09":        "monthly_food_tobacco_expenditure",# food, beverages & tobacco per household
    "A10":        "monthly_expenditure_percapita",  # total expenditure per capita
    "A11":        "monthly_consumption_percapita",  # consumption expenditure per capita
    "A12":        "monthly_food_tobacco_percapita", # food, beverages & tobacco per capita

    # Income aggregates (monthly averages, baht)
    "A13":        "monthly_income_household",       # total income per household
    "A14":        "monthly_current_income_household",# current income per household
    "A15":        "monthly_income_percapita",       # *** TARGET: total income per capita excl. servants ***
    "A15_1":      "monthly_income_percapita_incl",  # total income per capita incl. servants
    "A16":        "monthly_current_income_percapita",# current income per capita excl. servants
    "A16_1":      "monthly_current_income_percapita_incl",  # current income per capita incl. servants

    # Income by source (A17-A51)
    "A17":        "wages_last_month",               # 1) wages & salaries last month
    "A18":        "wages_monthly_avg",              # 1) wages & salaries monthly avg
    "A19":        "business_profit_last_month",     # 2) net profit from business last month
    "A20":        "business_profit_monthly_avg",    # 2) net profit from business monthly avg
    "A21":        "farm_profit_last_month",         # 3) net profit from farming last month
    "A22":        "farm_profit_monthly_avg",        # 3) net profit from farming monthly avg
    "A23":        "pension_last_month",             # 4) pensions & annuities last month
    "A24":        "pension_monthly_avg",            # 4) pensions & annuities monthly avg
    "A25":        "work_compensation_last_month",   # 5) work compensation last month
    "A26":        "work_compensation_monthly_avg",  # 5) work compensation monthly avg
    "A27":        "private_transfers_last_month",   # 6) money assistance from outside HH last month
    "A28":        "private_transfers_monthly_avg",  # 6) money assistance from outside HH monthly avg
    "A29":        "govt_social_assist_last_month",  # 7) govt social assistance for elderly/disabled last month
    "A30":        "govt_social_assist_monthly_avg", # 7) govt social assistance monthly avg
    "A31":        "rent_income_last_month",         # 8) rental income last month
    "A32":        "rent_income_monthly_avg",        # 8) rental income monthly avg
    "A33":        "interest_dividends_last_month",  # 9) interest/dividends last month
    "A34":        "interest_dividends_monthly_avg", # 9) interest/dividends monthly avg
    "A35":        "private_lending_interest_last_month",  # 10) interest from private lending last month
    "A36":        "private_lending_interest_monthly_avg", # 10) interest from private lending monthly avg
    "A37":        "total_money_income_last_month",  # sum of all money income last month
    "A38":        "total_money_income_monthly_avg", # sum of all money income monthly avg
    "A39":        "imputed_rent",                   # 11) imputed rent of free-occupied house (in-kind)
    "A40":        "inkind_goods_services",          # 12) in-kind goods & services received unpaid
    "A41":        "inkind_food_beverages",          # 13) in-kind food & beverages received unpaid
    "A42":        "scholarship_last_month",         # 14) education scholarship last month
    "A43":        "scholarship_monthly_avg",        # 14) education scholarship monthly avg
    "A44":        "gifts_inheritance_last_month",   # 15) inheritance & gifts last month
    "A45":        "gifts_inheritance_monthly_avg",  # 15) inheritance & gifts monthly avg
    "A46":        "insurance_proceeds_last_month",  # 16) insurance proceeds last month
    "A47":        "insurance_proceeds_monthly_avg", # 16) insurance proceeds monthly avg
    "A48":        "other_receipts_last_month",      # 17) lottery, gambling, commissions last month
    "A49":        "other_receipts_monthly_avg",     # 17) other receipts monthly avg
    "A50":        "total_other_receipts_last_month",# sum of other receipts last month
    "A51":        "total_other_receipts_monthly_avg",# sum of other receipts monthly avg
    "A52":        "sampling_weight",                # survey sampling weight (4 decimal places)
    "A53":        "debt_repayment_monthly",         # monthly debt repayment

    # Consumption expenditure subtotals (generated aggregates)
    "CON_EX 1":   "consumption_expend_cash",        # consumption expend paid by cash
    "CON_EX 2":   "consumption_expend_inkind",      # consumption expend in-kind
    "CON_EX 3":   "consumption_expend_total",       # total consumption expenditure
    "NCON_EX1":   "nonconsumption_expend_cash",     # non-consumption expend paid by cash
    "NCON_EX2":   "nonconsumption_expend_inkind",   # non-consumption expend in-kind
    "NCON_EX3":   "nonconsumption_expend_total",    # total non-consumption expenditure
    "FB_EX 1":    "food_expend_cash",               # food & beverage expend cash
    "FB_EX 2":    "food_expend_inkind",             # food & beverage expend in-kind
    "FB_EX 3":    "food_expend_total",              # total food & beverage expenditure
    "TP_EX 1":    "tobacco_expend_cash",            # tobacco expenditure cash
    "TP_EX 2":    "tobacco_expend_inkind",          # tobacco expenditure in-kind
    "TP_EX 3":    "tobacco_expend_total",           # total tobacco expenditure

    # Income source totals
    "WS1":        "total_wages_last_month",         # total wages & salaries (money) last month
    "WS2":        "total_wages_monthly_avg",        # total wages & salaries monthly avg
    "PB1":        "total_business_profit_last_month",# total net business profit last month
    "PB2":        "total_business_profit_monthly_avg",# total net business profit monthly avg
    "PA1":        "total_farm_profit_last_month",   # total net farm profit last month
    "PA2":        "total_farm_profit_monthly_avg",  # total net farm profit monthly avg

    # C-series: household characteristics summary
    "C01":        "hh_head_sex",                    # sex of HH head (1=male 2=female)
    "C02":        "hh_head_age",                    # age of HH head
    "C03":        "hh_head_marital_status",         # marital status of HH head
    "C04":        "hh_head_education",              # highest education level of HH head
    "C05":        "n_members_under15",              # members aged < 15
    "C06":        "n_members_over60",               # members aged >= 60
    "C07":        "n_disabled_total",               # total disabled persons in HH
    "C08":        "n_disabled_since_birth",         # disabled since birth
    "C09":        "n_disabled_after_birth",         # disabled after birth
    "C10":        "n_govt_medical_welfare",         # members with govt/state enterprise medical welfare
    "C11":        "n_universal_health_card",        # members with universal health (gold) card
    "C12":        "n_social_security_card",         # members with social security medical card (m.33/39)
    "C13":        "n_informal_worker_ss_card",      # members with social security card (m.40)
    "C14":        "n_private_health_insurance",     # members with private health insurance
    "C15":        "n_employer_welfare",             # members with employer welfare
    "C16":        "n_other_medical_welfare",        # members with other medical welfare
    "C17":        "n_elderly_pension",              # members receiving elderly social pension
    "C18":        "n_disability_assistance",        # members receiving disability assistance
    "C19":        "n_free_school_lunch",            # members receiving free school lunch
    "C20":        "n_govt_scholarship",             # members receiving govt scholarship
    "C21":        "n_welfare_govt_card",            # members with welfare government card (low income)
    "C22":        "n_child_subsidy",                # members receiving child subsidy (0-6 yrs)
    "C23":        "n_other_govt_fund",              # members receiving other govt funds
    "C24":        "n_govt_education_loan",          # members with govt education loan
    "C25":        "n_people_bank_loan",             # members with people bank loan
    "C26":        "n_village_fund_loan",            # members with village fund loan
    "C27":        "n_other_govt_loan",              # members with other govt fund loan

    # ── REC02 — HOUSEHOLD MEMBERS (individual-level) ─────────────────────────
    "HM01":       "member_serial_no",               # member serial number in HH
    "HM01N":      "member_name",                    # member name
    "HM01_1":     "respondent_serial_no",           # serial no. of main respondent
    "HM02":       "relationship_to_head",           # relationship to household head
    "HM03":       "sex",                            # sex (1=male 2=female)
    "HM04":       "age",                            # age in years
    "HM05":       "religion",                       # religion code
    "HM06":       "language",                       # language spoken in household
    "HM07":       "disability_type",                # disability status & type
    "HM08":       "can_self_care",                  # can take care of self in daily life
    "HM09":       "can_travel_alone",               # can go out without assistant
    "HM10":       "marital_status",                 # marital status
    "HM11":       "lives_with_parents",             # whether stays with parents
    "HM12":       "years_apart_from_parents",       # years not living with father/mother
    "HM13":       "reason_apart_from_parents",      # reason not staying with parents
    "HM14":       "school_attendance",              # school attendance status
    "HM15":       "education_attainment",           # highest education level completed
    "HM16":       "education_major",                # major/field of study
    "HM17":       "education_current_level",        # current level of schooling
    "HM18":       "education_tuition_fees",         # tuition/school fees (annual)
    "HM19":       "education_uniform_cost",         # uniform cost (annual)
    "HM20":       "education_books_cost",           # books & equipment cost (annual)
    "HM21":       "education_transport_cost",       # transport to school cost (annual)
    "HM22":       "govt_medical_welfare",           # govt/state enterprise medical welfare (0/1)
    "HM23":       "universal_health_card",          # universal health (gold) card (0/1)
    "HM24":       "social_security_card",           # social security medical card m.33/39 (0/1)
    "HM25":       "informal_worker_ss_card",        # social security card m.40 (0/1)
    "HM26":       "private_health_insurance",       # private health insurance (0/1)
    "HM27":       "employer_welfare",               # employer welfare (0/1)
    "HM28":       "other_medical_welfare",          # other medical welfare (0/1)
    "HM29":       "elderly_pension",                # social pension for elderly (0/1-5)
    "HM30":       "disability_assistance",          # disability assistance (0/1-5)
    "HM31":       "free_school_lunch",              # free school lunch/supplementary food (0/1-5)
    "HM32":       "govt_scholarship",               # government scholarship (0/1-5)
    "HM33":       "welfare_govt_card",              # welfare government card (0/1-5)
    "HM34":       "child_subsidy",                  # child subsidy 0-6 yrs (0/1-5)
    "HM35":       "other_govt_funds",               # other government fund programmes (0/1-5)
    "HM36":       "govt_education_loan",            # govt education loan (0/1)
    "HM37":       "people_bank_loan",               # people bank loan (0/1)
    "HM38":       "village_fund_loan",              # village fund scheme loan (0/1)
    "HM39":       "other_govt_loan",                # other govt fund loan (0/1)
    "HM40":       "primary_occupation_code",        # primary occupation code (Appendix D)
    "HM41":       "work_status",                    # employment/work status
    "HM42":       "industry_type",                  # type of industry (Appendix E)
    "HM43":       "secondary_occupation_code",      # secondary occupation code
    "HM44":       "secondary_work_status",          # secondary employment status
    "HM45":       "secondary_industry_type",        # secondary industry type

    # ── REC03 — HOUSING CHARACTERISTICS ─────────────────────────────────────
    "HH01":       "dwelling_type",                  # type of dwelling
    "HH02":       "construction_material",          # building material
    "HH03":       "tenure",                         # ownership/tenure status
    "HH04":       "rent_payer",                     # who pays the rent
    "HH05":       "monthly_rent_or_estimated",      # monthly rent or estimated rental value
    "HH06":       "dwelling_used_for_business",     # dwelling partly used for business (0/1)
    "HH07":       "n_rooms_total",                  # total rooms (excl. bathroom)
    "HH08":       "n_bedrooms",                     # number of bedrooms
    "HH09":       "has_electricity",                # electricity in dwelling (0/1)
    "HH10":       "cooking_fuel",                   # cooking fuel type
    "HH11":       "drinking_water_source",          # drinking water source
    "HH12":       "general_water_source",           # water supply for general use
    "HH13":       "garbage_disposal_1st",           # primary garbage disposal method
    "HH14":       "garbage_disposal_2nd",           # secondary garbage disposal method
    "HH15":       "toilet_facility",                # toilet facility type
    # Vehicles owned
    "HH16":       "owns_bicycle",
    "HH17":       "owns_motorcycle",
    "HH18":       "owns_automobile",
    "HH19":       "owns_pickup_van",
    "HH20":       "owns_other_truck",
    "HH21":       "owns_motorboat",
    # Durables owned
    "HH22":       "owns_bed",
    "HH23":       "owns_gas_stove",
    "HH24":       "owns_electric_stove",
    "HH25":       "owns_microwave",
    "HH26_1":     "owns_electric_pot",
    "HH26_2":     "owns_kettle",
    "HH27":       "owns_refrigerator",
    "HH28":       "owns_electric_iron",
    "HH29_1":     "owns_rice_cooker",
    "HH29_2":     "owns_electric_pan",
    "HH30":       "owns_electric_fan",
    "HH31":       "owns_radio",
    "HH32_1":     "owns_crt_tv",
    "HH32_2":     "owns_lcd_led_tv",
    "HH33":       "owns_vcd_dvd_player",
    "HH34":       "owns_washing_machine",
    "HH35":       "owns_air_conditioner",
    "HH36":       "owns_water_heater",
    "HH37":       "owns_home_computer",
    "HH38":       "has_internet_connection",
    "HH39":       "owns_telephone",
    "HH40":       "n_mobile_phones",
    "HH41":       "n_smartphones",
    "HH42":       "n_fluorescent_bulbs",
    "HH43":       "n_incandescent_bulbs",
    "HH44":       "n_cfl_bulbs",
    "HH45":       "n_led_e27_bulbs",
    "HH46":       "n_led_t8_bulbs",
    "HH47":       "n_internet_users",              # members who used internet in past 12 months

    # ── REC04 — HOUSING EXPENDITURE (cash/in-kind suffix a / bc) ─────────────
    "EG01a":      "housing_rent_cash",              # 1.1 house rent / estimated rental - cash
    "EG01bc":     "housing_rent_inkind",
    "EG02a":      "dwelling_repair_cash",           # 1.2 repair of dwelling - cash
    "EG02bc":     "dwelling_repair_inkind",
    "EG03a":      "plumbing_install_cash",          # 1.3 plumbing installation/repair - cash
    "EG03bc":     "plumbing_install_inkind",
    "EG04a":      "electrical_install_cash",        # 1.4 electrical installation/repair - cash
    "EG04bc":     "electrical_install_inkind",
    "EG05a":      "tools_equipment_cash",           # 1.5 tools & equipment - cash
    "EG05bc":     "tools_equipment_inkind",

    # ── REC05 — HOUSEHOLD OPERATION ─────────────────────────────────────────
    "EG06a":      "furniture_cash",                 # 2.1 furniture - cash
    "EG06bc":     "furniture_inkind",
    "EG07a":      "cooking_appliance_cash",         # 2.1 cooking stove/microwave/rice cooker - cash
    "EG07bc":     "cooking_appliance_inkind",
    "EG08a":      "blender_kettle_cash",            # 2.1 grinder/blender/electric pot - cash
    "EG08bc":     "blender_kettle_inkind",
    "EG09a":      "washer_heater_pump_cash",        # 2.1 washing machine/water heater/pump - cash
    "EG09bc":     "washer_heater_pump_inkind",
    "EG10a":      "ac_fridge_fan_cash",             # 2.1 air conditioner/refrigerator/fan - cash
    "EG10bc":     "ac_fridge_fan_inkind",
    "EG11a":      "other_major_appliance_cash",     # 2.1 other major equipment - cash
    "EG11bc":     "other_major_appliance_inkind",
    "EG12a":      "appliance_repair_cash",          # 2.1 repairing/maintenance - cash
    "EG12bc":     "appliance_repair_inkind",
    "EG13a":      "bedding_cloth_cash",             # 2.2 bedding & furnishing cloth - cash
    "EG13bc":     "bedding_cloth_inkind",
    "EG14a":      "kitchen_cloth_cash",             # 2.2 kitchen/dining cloth - cash
    "EG14bc":     "kitchen_cloth_inkind",
    "EG15a":      "other_household_cloth_cash",     # 2.2 other household cloth - cash
    "EG15bc":     "other_household_cloth_inkind",
    "EG16a":      "kitchen_appliance_small_cash",   # 2.3 pans/pots etc. - cash
    "EG16bc":     "kitchen_appliance_small_inkind",
    "EG17a":      "flask_tank_sink_cash",           # 2.3 hot/cold flask, tank, sink - cash
    "EG17bc":     "flask_tank_sink_inkind",
    "EG18a":      "electricity_bill_cash",          # 2.4 electricity - cash
    "EG18bc":     "electricity_bill_inkind",
    "EG19a":      "cooking_gas_cash",               # 2.4 cooking gas - cash
    "EG19bc":     "cooking_gas_inkind",
    "EG20a":      "other_gas_cash",                 # 2.4 gas for other purposes - cash
    "EG20bc":     "other_gas_inkind",
    "EG21a":      "charcoal_wood_cash",             # 2.4 charcoal and wood - cash
    "EG21bc":     "charcoal_wood_inkind",
    "EG22a":      "kerosene_cash",                  # 2.4 kerosene - cash
    "EG22bc":     "kerosene_inkind",
    "EG23a":      "lighting_accessories_cash",      # 2.4 lighting accessories - cash
    "EG23bc":     "lighting_accessories_inkind",
    "EG24a":      "water_supply_cash",              # 2.4 water supply - cash
    "EG24bc":     "water_supply_inkind",
    "EG25a":      "cleaning_tools_cash",            # 2.5 mops/brooms/brushes - cash
    "EG25bc":     "cleaning_tools_inkind",
    "EG26a":      "detergent_cash",                 # 2.5 detergent/softener - cash
    "EG26bc":     "detergent_inkind",
    "EG27a":      "liquid_detergent_cash",          # 2.5 liquid detergent/polishes - cash
    "EG27bc":     "liquid_detergent_inkind",

    # ── REC06 — CLOTHING & PERSONAL CARE ────────────────────────────────────
    "EG28a":      "servant_wages_member_cash",      # 3.1 servant wages (HH member) - cash
    "EG28bc":     "servant_wages_member_inkind",
    "EG29a":      "servant_wages_outside_cash",     # 3.2 servant wages (non-member) - cash
    "EG29bc":     "servant_wages_outside_inkind",
    "EG30a":      "clothing_shirts_pants_cash",     # 4.1 shirts/skirts/trousers - cash
    "EG30bc":     "clothing_shirts_pants_inkind",
    "EG31a":      "sportswear_cash",                # 4.2 sportswear - cash
    "EG31bc":     "sportswear_inkind",
    "EG32a":      "loincloth_underwear_cash",       # 4.3 loincloth/sarong/underwear - cash
    "EG32bc":     "loincloth_underwear_inkind",
    "EG33a":      "other_clothing_cash",            # 4.4 other clothing - cash
    "EG33bc":     "other_clothing_inkind",
    "EG34a":      "tailoring_cash",                 # 4.5 sewing/repair/altering - cash
    "EG34bc":     "tailoring_inkind",
    "EG35a":      "laundry_cash",                   # 4.6 laundry/dry cleaning/clothing rental - cash
    "EG35bc":     "laundry_inkind",
    "EG36a":      "shoes_cash",                     # 5.1 shoes (all types) - cash
    "EG36bc":     "shoes_inkind",
    "EG37a":      "sport_shoes_cash",               # 5.2 sport shoes - cash
    "EG37bc":     "sport_shoes_inkind",
    "EG38a":      "shoe_repair_cash",               # 5.3 shoe repair/rental/cleaning - cash
    "EG38bc":     "shoe_repair_inkind",
    "EG39a":      "soap_toothpaste_cash",           # 6.1 soap/toothpaste/shampoo - cash
    "EG39bc":     "soap_toothpaste_inkind",
    "EG40a":      "comb_razor_cash",                # 6.1 comb/brushes/razor - cash
    "EG40bc":     "comb_razor_inkind",
    "EG41a":      "cosmetics_cash",                 # 6.1 cosmetics - cash
    "EG41bc":     "cosmetics_inkind",
    "EG42a":      "watch_handbag_cash",             # 6.1 watch/handbag/luggage/sunglasses - cash
    "EG42bc":     "watch_handbag_inkind",
    "EG43a":      "other_personal_supply_cash",     # 6.1 other personal supplies - cash
    "EG43bc":     "other_personal_supply_inkind",
    "EG44a":      "personal_supply_repair_cash",    # 6.1 personal supply repair - cash
    "EG44bc":     "personal_supply_repair_inkind",
    "EG45a":      "beauty_services_cash",           # 6.2 beauty services - cash
    "EG45bc":     "beauty_services_inkind",
    "EG46a":      "other_personal_services_cash",   # 6.2 other personal services - cash
    "EG46bc":     "other_personal_services_inkind",

    # ── REC07 — MEDICAL & HEALTH CARE ───────────────────────────────────────
    "EG47a":      "modern_medicine_cash",           # 7.1 modern medicine - cash
    "EG47bc":     "modern_medicine_inkind",
    "EG48a":      "herbal_medicine_cash",           # 7.1 traditional/herbal medicine - cash
    "EG48bc":     "herbal_medicine_inkind",
    "EG49a":      "contraceptives_cash",            # 7.1 contraceptives/condoms - cash
    "EG49bc":     "contraceptives_inkind",
    "EG50a":      "vitamins_supplements_cash",      # 7.1 vitamins/supplements - cash
    "EG50bc":     "vitamins_supplements_inkind",
    "EG51a":      "first_aid_kit_cash",             # 7.1 first-aid kit/medical equipment - cash
    "EG51bc":     "first_aid_kit_inkind",
    "EG52_1a":    "public_hospital_outpatient_cash",# 7.2 public hospital outpatient - cash
    "EG52_1bc":   "public_hospital_outpatient_inkind",
    "EG52_2a":    "health_center_outpatient_cash",  # 7.2 public health center outpatient - cash
    "EG52_2bc":   "health_center_outpatient_inkind",
    "EG53_1a":    "private_hospital_outpatient_cash",# 7.2 private hospital outpatient - cash
    "EG53_1bc":   "private_hospital_outpatient_inkind",
    "EG53_2a":    "clinic_outpatient_cash",         # 7.2 clinic outpatient - cash
    "EG53_2bc":   "clinic_outpatient_inkind",
    "EG54a":      "traditional_healer_cash",        # 7.2 traditional healer/herbal treatment - cash
    "EG54bc":     "traditional_healer_inkind",
    "EG55a":      "dental_clinic_cash",             # 7.2 dental clinic - cash
    "EG55bc":     "dental_clinic_inkind",
    "EG56a":      "optometry_cash",                 # 7.2 optometry/glasses - cash
    "EG56bc":     "optometry_inkind",
    "EG57a":      "health_checkup_cash",            # 7.2 annual checkup/pregnancy - cash
    "EG57bc":     "health_checkup_inkind",
    "EG58_1a":    "public_hospital_inpatient_cash", # 7.3 public hospital inpatient - cash
    "EG58_1bc":   "public_hospital_inpatient_inkind",
    "EG58_2a":    "health_center_inpatient_cash",   # 7.3 health center inpatient - cash
    "EG58_2bc":   "health_center_inpatient_inkind",
    "EG59_1a":    "private_hospital_inpatient_cash",# 7.3 private hospital inpatient - cash
    "EG59_1bc":   "private_hospital_inpatient_inkind",
    "EG59_2a":    "clinic_inpatient_cash",          # 7.3 clinic inpatient - cash
    "EG59_2bc":   "clinic_inpatient_inkind",
    "EG60a":      "other_medical_expense_cash",     # 7.3 other medical expense - cash
    "EG60bc":     "other_medical_expense_inkind",

    # ── REC08 — TRANSPORTATION & COMMUNICATION ──────────────────────────────
    "EG61a":      "automobile_purchase_cash",       # 8.1 automobile/van/pickup purchase - cash
    "EG61bc":     "automobile_purchase_inkind",
    "EG62a":      "motorcycle_bicycle_purchase_cash",# 8.1 motorcycle/bicycle purchase - cash
    "EG62bc":     "motorcycle_bicycle_purchase_inkind",
    "EG63a":      "vehicle_equipment_install_cash", # 8.1 vehicle equipment installation - cash
    "EG63bc":     "vehicle_equipment_install_inkind",
    "EG64a":      "tire_battery_cash",              # 8.2 tire/battery - cash
    "EG64bc":     "tire_battery_inkind",
    "EG65a":      "engine_oil_cash",                # 8.2 engine oil/lubricant - cash
    "EG65bc":     "engine_oil_inkind",
    "EG66a":      "vehicle_overhaul_cash",          # 8.2 overhaul/repair - cash
    "EG66bc":     "vehicle_overhaul_inkind",
    "EG67a":      "driving_license_cash",           # 8.2 driver training/license/registration - cash
    "EG67bc":     "driving_license_inkind",
    "EG68a":      "crash_helmet_cash",              # 8.2 crash helmet - cash
    "EG68bc":     "crash_helmet_inkind",
    "EG69a":      "car_wash_cash",                  # 8.2 car wash/lubrication/tyre repair - cash
    "EG69bc":     "car_wash_inkind",
    "EG70a":      "vehicle_maintenance_cash",       # 8.2 vehicle maintenance/others - cash
    "EG70bc":     "vehicle_maintenance_inkind",
    "EG71a":      "public_transport_cash",          # 8.3 bus/boat/train/BTS/plane - cash
    "EG71bc":     "public_transport_inkind",
    "EG72a":      "school_staff_bus_cash",          # 8.3 school bus/staff bus - cash
    "EG72bc":     "school_staff_bus_inkind",
    "EG73a":      "taxi_tricycle_cash",             # 8.3 taxi/tricycle/motorcycle taxi - cash
    "EG73bc":     "taxi_tricycle_inkind",
    "EG74a":      "gasoline_cash",                  # 8.3 unleaded gasoline - cash
    "EG74bc":     "gasoline_inkind",
    "EG7501a":    "gasohol_91_cash",                # 8.3 gasohol 91 - cash
    "EG7501bc":   "gasohol_91_inkind",
    "EG7502a":    "gasohol_95_cash",                # 8.3 gasohol 95 - cash
    "EG7502bc":   "gasohol_95_inkind",
    "EG7503a":    "gasohol_e20_cash",               # 8.3 gasohol E20 - cash
    "EG7503bc":   "gasohol_e20_inkind",
    "EG7504a":    "gasohol_e85_cash",               # 8.3 gasohol E85 - cash
    "EG7504bc":   "gasohol_e85_inkind",
    "EG76a":      "ngv_gas_cash",                   # 8.3 NGV gas - cash
    "EG76bc":     "ngv_gas_inkind",
    "EG77a":      "lpg_gas_cash",                   # 8.3 LPG gas - cash
    "EG77bc":     "lpg_gas_inkind",
    "EG7801a":    "diesel_b7_cash",                 # 8.3 diesel B7 - cash
    "EG7801bc":   "diesel_b7_inkind",
    "EG7802a":    "diesel_cash",                    # 8.3 diesel - cash
    "EG7802bc":   "diesel_inkind",
    "EG7803a":    "diesel_b7_premium_cash",         # 8.3 diesel B7 premium - cash
    "EG7803bc":   "diesel_b7_premium_inkind",
    "EG781a":     "biodiesel_b5_cash",              # 8.3 bio-diesel B5 - cash
    "EG781bc":    "biodiesel_b5_inkind",
    "EG782a":     "alt_fuel_cash",                  # 8.3 other alternative fuel - cash
    "EG782bc":    "alt_fuel_inkind",

    # ── REC09 — TRAVEL & COMMUNICATION ──────────────────────────────────────
    "EG79a":      "special_travel_cash",            # 8.4 visiting hometown/religious travel - cash
    "EG79bc":     "special_travel_inkind",
    "EG80a":      "personal_trip_cash",             # 8.4 personal trip domestic/outbound - cash
    "EG80bc":     "personal_trip_inkind",
    "EG81a":      "package_tour_cash",              # 8.4 package tour - cash
    "EG81bc":     "package_tour_inkind",
    "EG82a":      "souvenir_domestic_cash",         # 8.4 souvenir on domestic trip - cash
    "EG82bc":     "souvenir_domestic_inkind",
    "EG83a":      "souvenir_outbound_cash",         # 8.4 souvenir domestic/outbound - cash
    "EG83bc":     "souvenir_outbound_inkind",
    "EG84_1a":    "telephone_purchase_cash",        # 8.5 telephone purchase - cash
    "EG84_1bc":   "telephone_purchase_inkind",
    "EG84_2a":    "mobile_phone_purchase_cash",     # 8.5 mobile phone purchase - cash
    "EG84_2bc":   "mobile_phone_purchase_inkind",
    "EG85_1a":    "landline_service_cash",          # 8.5 landline/public phone service - cash
    "EG85_1bc":   "landline_service_inkind",
    "EG85_2a":    "mobile_service_cash",            # 8.5 mobile phone service - cash
    "EG85_2bc":   "mobile_service_inkind",
    "EG86_1a":    "home_internet_cash",             # 8.5 home internet - cash
    "EG86_1bc":   "home_internet_inkind",
    "EG86_2a":    "mobile_internet_cash",           # 8.5 mobile internet - cash
    "EG86_2bc":   "mobile_internet_inkind",
    "EG87a":      "other_communication_cash",       # 8.5 other communication - cash
    "EG87bc":     "other_communication_inkind",
    "EG88a":      "public_tuition_fees_cash",       # 9.1 public school tuition fees - cash
    "EG88bc":     "public_tuition_fees_inkind",
    "EG89a":      "private_tuition_fees_cash",      # 9.2 private school tuition fees - cash
    "EG89bc":     "private_tuition_fees_inkind",
    "EG90a":      "school_books_supplies_cash",     # 9.3 textbooks & supplies - cash
    "EG90bc":     "school_books_supplies_inkind",
    "EG91a":      "extra_tuition_cash",             # 9.4 extra tuition/music/dance - cash
    "EG91bc":     "extra_tuition_inkind",
    "EG92a":      "other_education_cash",           # 9.5 other education expenses - cash
    "EG92bc":     "other_education_inkind",

    # ── REC10 — RECREATION & RELIGIOUS ACTIVITIES ───────────────────────────
    "EG93a":      "tv_radio_player_cash",           # 10.1 TV/radio/VCD/DVD - cash
    "EG93bc":     "tv_radio_player_inkind",
    "EG94a":      "camera_projector_cash",          # 10.1 camera/camcorder/projector - cash
    "EG94bc":     "camera_projector_inkind",
    "EG95a":      "satellite_cable_tv_cash",        # 10.1 satellite dish/cable TV - cash
    "EG95bc":     "satellite_cable_tv_inkind",
    "EG96a":      "computer_equipment_cash",        # 10.1 computer & equipment - cash
    "EG96bc":     "computer_equipment_inkind",
    "EG97a":      "sport_equipment_cash",           # 10.1 sport & fitness equipment - cash
    "EG97bc":     "sport_equipment_inkind",
    "EG98a":      "recreation_repair_cash",         # 10.1 repair/maintenance of recreation items - cash
    "EG98bc":     "recreation_repair_inkind",
    "EG99a":      "toys_cash",                      # 10.2 toys - cash
    "EG99bc":     "toys_inkind",
    "EG100a":     "pets_cash",                      # 10.2 pets & pet equipment - cash
    "EG100bc":    "pets_inkind",
    "EG101a":     "plants_flowers_cash",            # 10.2 plants/shrubs/flowers - cash
    "EG101bc":    "plants_flowers_inkind",
    "EG102a":     "cable_tv_membership_cash",       # 10.2 cable TV membership/photography - cash
    "EG102bc":    "cable_tv_membership_inkind",
    "EG103a":     "recreation_maintenance_cash",    # 10.2 repair/maintenance/others - cash
    "EG103bc":    "recreation_maintenance_inkind",
    "EG104a":     "cinema_sports_events_cash",      # 10.3 cinema/sports/arts admission - cash
    "EG104bc":    "cinema_sports_events_inkind",
    "EG105a":     "amusement_park_zoo_cash",        # 10.3 amusement parks/zoo - cash
    "EG105bc":    "amusement_park_zoo_inkind",
    "EG106a":     "sport_fees_cash",                # 10.3 sport fees/rates - cash
    "EG106bc":    "sport_fees_inkind",
    "EG107a":     "other_recreation_admission_cash",# 10.3 other recreation admission - cash
    "EG107bc":    "other_recreation_admission_inkind",
    "EG108a":     "newspapers_books_cash",          # 10.4 newspapers/magazines/books - cash
    "EG108bc":    "newspapers_books_inkind",
    "EG109a":     "library_fees_cash",              # 10.4 library fees - cash
    "EG109bc":    "library_fees_inkind",
    "EG110a":     "religious_donations_cash",       # 10.4 temple offerings/religious expenses - cash
    "EG110bc":    "religious_donations_inkind",
    "EG111a":     "ceremony_expenses_cash",         # 11 wedding/birthday/ceremonies - cash
    "EG111bc":    "ceremony_expenses_inkind",

    # ── REC11 — NON-CONSUMPTION EXPENDITURE ─────────────────────────────────
    "EG112a":     "taxes_fees_fines_cash",          # 1 taxes/fees/fines - cash
    "EG112bc":    "taxes_fees_fines_inkind",
    "EG113a":     "career_membership_cash",         # 2 career/professional membership - cash
    "EG113bc":    "career_membership_inkind",
    "EG114a":     "remittance_out_cash",            # 3 money/goods sent to other HH - cash
    "EG114bc":    "remittance_out_inkind",
    "EG115a":     "donation_ngo_cash",              # 4 donations to NGO/organisations - cash
    "EG115bc":    "donation_ngo_inkind",
    "EG116a":     "other_contributions_cash",       # 5 temple donations/contributions - cash
    "EG116bc":    "other_contributions_inkind",
    "EG117_1a":   "insurance_premium_cash",         # 6 insurance premiums (excl. saving) - cash
    "EG117_1bc":  "insurance_premium_inkind",
    "EG117_2a":   "health_insurance_premium_cash",  # 6 health insurance premium - cash
    "EG117_2bc":  "health_insurance_premium_inkind",
    "EG117_3a":   "social_security_contrib_cash",   # 6 social security contribution - cash
    "EG117_3bc":  "social_security_contrib_inkind",
    "EG118a":     "lottery_gambling_cash",          # 7 lottery/gambling - cash
    "EG118bc":    "lottery_gambling_inkind",
    "EG119a":     "interest_payment_cash",          # 8 interest payment - cash
    "EG119bc":    "interest_payment_inkind",
    "EG120a":     "other_nonconsumption_cash",      # 9 other non-consumption expenses - cash
    "EG120bc":    "other_nonconsumption_inkind",

    # ── REC12 — FOOD & BEVERAGE EXPENDITURE ─────────────────────────────────
    "EF01a":      "food_grains_cereals_cash",       # 1 grains & cereal products - cash
    "EF01bc":     "food_grains_cereals_inkind",
    "EF02a":      "food_meat_poultry_cash",         # 2 meat & poultry - cash
    "EF02bc":     "food_meat_poultry_inkind",
    "EF03a":      "food_fish_seafood_cash",         # 3 fish & seafood - cash
    "EF03bc":     "food_fish_seafood_inkind",
    "EF04a":      "food_dairy_eggs_cash",           # 4 milk/cheese/eggs - cash
    "EF04bc":     "food_dairy_eggs_inkind",
    "EF04_1bc":   "food_school_milk_inkind",        # 4 complementary milk for students (free)
    "EF05a":      "food_oils_fats_cash",            # 5 oil & fat - cash
    "EF05bc":     "food_oils_fats_inkind",
    "EF06a":      "food_fruits_nuts_cash",          # 6 fruits & nuts - cash
    "EF06bc":     "food_fruits_nuts_inkind",
    "EF07a":      "food_vegetables_cash",           # 7 vegetables - cash
    "EF07bc":     "food_vegetables_inkind",
    "EF08a":      "food_sugar_sweets_cash",         # 8 sugar & sweets - cash
    "EF08bc":     "food_sugar_sweets_inkind",
    "EF09a":      "food_spices_cash",               # 9 spices & condiments - cash
    "EF09bc":     "food_spices_inkind",
    "EF10a":      "bev_nonalc_semi_cash",           # 10 non-alcoholic beverages semi-prepared - cash
    "EF10bc":     "bev_nonalc_semi_inkind",
    "EF11a":      "bev_nonalc_ready_cash",          # 10 non-alcoholic beverages ready-made - cash
    "EF11bc":     "bev_nonalc_ready_inkind",
    "EF12a":      "food_prepared_home_cash",        # 11 prepared food consumed at home - cash
    "EF12bc":     "food_prepared_home_inkind",
    "EF13a":      "food_away_total_cash",           # 12 food away from home total - cash
    "EF13bc":     "food_away_total_inkind",
    "EF13_1a":    "food_away_breakfast_cash",       # 12 breakfast away from home - cash
    "EF13_1bc":   "food_away_breakfast_inkind",
    "EF13_2a":    "food_away_lunch_cash",           # 12 lunch away from home - cash
    "EF13_2bc":   "food_away_lunch_inkind",
    "EF13_3a":    "food_away_dinner_cash",          # 12 dinner away from home - cash
    "EF13_3bc":   "food_away_dinner_inkind",
    "EF14a":      "bev_alcoholic_home_cash",        # 13 alcoholic beverages at home - cash
    "EF14bc":     "bev_alcoholic_home_inkind",
    "EF15a":      "bev_alcoholic_away_cash",        # 13 alcoholic beverages away from home - cash
    "EF15bc":     "bev_alcoholic_away_inkind",
    "EF16a":      "tobacco_cigarettes_cash",        # 14 cigarettes/tobacco - cash
    "EF16bc":     "tobacco_cigarettes_inkind",
    "EF17a":      "tobacco_betel_snuff_cash",       # 14 betel/snuff/other tobacco - cash
    "EF17bc":     "tobacco_betel_snuff_inkind",

    # ── REC13 — WAGE & SALARY INCOME (iw_ prefix) ───────────────────────────
    "IW01":       "iw_member_serial_no",            # member serial no. (wage earner)
    "IW01_1":     "iw_member_name",
    "IW02":       "iw_occupation_code",             # occupation code (Appendix D)
    "IW03":       "iw_socioeconomic_class",         # socio-economic class (generated)
    "IW03_1":     "iw_industry_type",               # industry type code
    "IW04":       "iw_months_worked",               # months worked in this occupation
    "IW05":       "iw_wage_type",                   # type of wage (piece/hour/day/week/month)
    "IW06":       "iw_wage_rate_cash",              # wage rate in cash
    "IW07":       "iw_days_per_month",              # days worked per month
    "IW08":       "iw_hours_per_day",               # hours worked per day
    "IW09":       "iw_pieces_per_month",            # pieces per month (piece-rate workers)
    "IW10":       "iw_wages_last_month",            # wages & salaries last month
    "IW11":       "iw_overtime_bonus_last_month",   # overtime & bonus last month
    "IW12":       "iw_wages_past12m",               # wages & salaries past 12 months
    "IW13":       "iw_overtime_bonus_past12m",      # overtime & bonus past 12 months
    "IW14":       "iw_welfare_value_past12m",       # total welfare value from employment past 12 months

    # ── REC14 — BUSINESS INCOME (ib_ prefix) ────────────────────────────────
    "IB01":       "ib_member_serial_no",            # member serial no. (business operator)
    "IB01_1":     "ib_member_name",
    "IB02":       "ib_occupation_code",             # occupation code
    "IB03":       "ib_socioeconomic_class",         # socio-economic class (generated)
    "IB03_1":     "ib_industry_type",               # industry type code
    "IB05":       "ib_months_operating",            # months operating this business
    "IB06":       "ib_total_workers",               # total workers incl. entrepreneur
    "IB07":       "ib_n_employees",                 # number of employees
    "IB08":       "ib_gross_receipts_past12m",      # gross money receipts past 12 months
    "IB0901":     "ib_cost_raw_materials",          # operating cost: raw materials
    "IB0902":     "ib_cost_rent",                   # operating cost: office/vehicle rent
    "IB0903":     "ib_cost_fuel_electricity",       # operating cost: fuel/electricity/oil/gas
    "IB0904":     "ib_cost_wages_paid",             # operating cost: wages paid to employees
    "IB0905":     "ib_cost_medical_employees",      # operating cost: medical services for employees
    "IB0906":     "ib_cost_interest_insurance",     # operating cost: loan interest/insurance
    "IB0907":     "ib_cost_taxes_other",            # operating cost: business taxes & others
    "IB09":       "ib_total_operating_cost",        # total operating cost
    "IB10":       "ib_home_produced_goods_used",    # value of home-produced goods used in HH
    "IB11":       "ib_profit_share_pct",            # profit share % (if partnership)

    # ── REC15 — FARM INCOME (ia_ prefix) ────────────────────────────────────
    "IA01":       "ia_socioeconomic_class",         # socio-economic class (generated)
    "IA02":       "ia_member_serial_no",            # member serial no. (farmer)
    "IA02_1":     "ia_member_name",
    "IA03_1":     "ia_farm_type_code",              # type of farm/agricultural activity
    "IA04":       "ia_land_owned_rai",              # owned land area (rai, tarangwa)
    "IA05":       "ia_land_rented_rai",             # rented land area (rai, tarangwa)
    "IA06":       "ia_public_land_rai",             # public/other land area (rai, tarangwa)
    "IA07":       "ia_n_farm_workers",              # no. of household members working in farm
    "IA08":       "ia_agri_service_income_cash",    # income from renting animals/tools/agri services (cash)
    "IA09":       "ia_agri_service_inkind_sold",    # in-kind agri services: sold
    "IA10":       "ia_agri_service_inkind_consumed",# in-kind agri services: consumed/other
    "IA11":       "ia_crops_total_value",           # total value of harvested crops
    "IA12":       "ia_crops_sold",                  # crops sold
    "IA13":       "ia_crops_consumed",              # crops for household consumption
    "IA14":       "ia_crops_other_use",             # crops for other uses
    "IA15":       "ia_livestock_total_value",       # total value of livestock products
    "IA16":       "ia_livestock_sold",              # livestock products sold
    "IA17":       "ia_livestock_consumed",          # livestock products consumed
    "IA18":       "ia_livestock_other_use",         # livestock products other use
    "IA19":       "ia_livestock_initial_value",     # value of livestock at start of period
    "IA20":       "ia_fishery_total_value",         # value from fishery/hunting/forestry
    "IA21":       "ia_fishery_sold",                # fishery products sold
    "IA22":       "ia_fishery_consumed",            # fishery products consumed
    "IA23":       "ia_fishery_other_use",           # fishery products other use
    "IA24":       "ia_imputed_land_rent",           # estimated rental value of own land
    "IA2502":     "ia_land_rent_paid_cash",         # 11.2 land rental paid in cash
    "IA2602":     "ia_land_rent_own_produce",       # 11.2 land rental paid with own produce
    "IA2702":     "ia_land_rent_received_assist",   # 11.2 land rental received as assistance
    "IA2503":     "ia_equipment_cost_cash",         # 11.3 equipment/animals cost cash
    "IA2603":     "ia_equipment_cost_produce",      # 11.3 equipment cost own produce
    "IA2703":     "ia_equipment_cost_assist",       # 11.3 equipment cost assistance
    "IA2504":     "ia_fuel_water_cost_cash",        # 11.4 fuel/electricity/irrigation cash
    "IA2604":     "ia_fuel_water_cost_produce",     # 11.4 fuel cost own produce
    "IA2704":     "ia_fuel_water_cost_assist",      # 11.4 fuel cost assistance
    "IA2505":     "ia_fertilizer_pesticide_cash",   # 11.5 fertilizer/pesticides cash
    "IA2605":     "ia_fertilizer_pesticide_produce",# 11.5 fertilizer own produce
    "IA2705":     "ia_fertilizer_pesticide_assist", # 11.5 fertilizer assistance
    "IA2506":     "ia_seeds_chicks_cash",           # 11.6 seeds/chicks/piglets cash
    "IA2606":     "ia_seeds_chicks_produce",        # 11.6 seeds own produce
    "IA2706":     "ia_seeds_chicks_assist",         # 11.6 seeds assistance
    "IA2507":     "ia_animal_feed_cash",            # 11.7 animal feed cash
    "IA2607":     "ia_animal_feed_produce",         # 11.7 animal feed own produce
    "IA2707":     "ia_animal_feed_assist",          # 11.7 animal feed assistance
    "IA2508":     "ia_farm_wages_paid_cash",        # 11.8 wages for farm workers cash
    "IA2608":     "ia_farm_wages_paid_produce",     # 11.8 farm wages own produce
    "IA2708":     "ia_farm_wages_paid_assist",      # 11.8 farm wages assistance
    "IA2509":     "ia_other_farm_cost_cash",        # 11.9 other farm expenses cash
    "IA2609":     "ia_other_farm_cost_produce",     # 11.9 other farm expenses own produce
    "IA2709":     "ia_other_farm_cost_assist",      # 11.9 other farm expenses assistance
    "IA25":       "ia_total_farm_cost_cash",        # total farm operating cost paid in cash
    "IA26":       "ia_total_farm_cost_produce",     # total farm cost paid with own produce
    "IA27":       "ia_total_farm_cost_assist",      # total farm cost received as assistance
    "IA28":       "ia_farm_gross_receipt_last_month",# gross farm receipt last month
    "IA29":       "ia_farm_expenditure_last_month", # farm expenditure last month

    # ── REC16 — OTHER INCOME SOURCES (io_ prefix) ───────────────────────────
    "IO01":       "io_socioeconomic_class_14",      # socio-economic class items 1-4 (generated)
    "IO02":       "io_pension_cash_past12m",        # pensions/annuities cash past 12 months
    "IO03":       "io_work_compensation_cash_past12m",# work compensation cash past 12 months
    "IO04":       "io_private_transfer_cash_past12m",# private transfers cash past 12 months
    "IO05":       "io_govt_social_assist_cash_past12m",# govt social assistance total cash 12m
    "IO05_1":     "io_elderly_pension_cash_past12m",# 4.1 elderly pension cash 12m
    "IO05_2":     "io_disability_assist_cash_past12m",# 4.2 disability assistance cash 12m
    "IO05_3":     "io_welfare_card_cash_past12m",   # 4.3 welfare card cash 12m
    "IO05_4":     "io_child_subsidy_cash_past12m",  # 4.4 child subsidy (0-6 yr) cash 12m
    "IO05_5":     "io_paotang_app_cash_past12m",    # 4.5 Paotang app govt programme cash 12m
    "IO05_6":     "io_other_govt_assist_cash_past12m",# 4.6 other govt assistance cash 12m
    "IO06":       "io_scholarship_cash_past12m",    # 5 scholarship cash past 12 months
    "IO07":       "io_socioeconomic_class_69",      # socio-economic class items 6-9 (generated)
    "IO08":       "io_rental_income_cash_past12m",  # 6 rental income cash past 12 months
    "IO09":       "io_copyright_cash_past12m",      # 7 copyright/licence income cash 12m
    "IO10":       "io_bank_interest_cash_past12m",  # 8 bank interest/dividends cash 12m
    "IO11":       "io_private_lending_interest_cash_past12m",# 9 private loan interest cash 12m
    "IO12":       "io_gifts_inheritance_cash_past12m",# 10 gifts & inheritance cash 12m
    "IO13":       "io_insurance_proceeds_cash_past12m",# 11 insurance proceeds cash 12m
    "IO14":       "io_other_income_cash_past12m",   # 12 other income (lottery etc.) cash 12m

    # ── REC17 — ASSETS & LIABILITIES (ad_ prefix) ───────────────────────────
    "AD01_1":     "asset_value_living_dwelling",    # value of living dwelling
    "AD01_2":     "asset_value_vacation_home",      # value of temporary/vacation dwelling
    "AD02":       "asset_value_business_land",      # value of land/building for business
    "AD03":       "asset_value_vehicles",           # value of vehicles
    "AD04_1":     "asset_financial_saving",         # financial assets for saving
    "AD04_2":     "asset_financial_investment",     # financial assets for investment
    "AD04_3":     "asset_financial_other",          # other financial assets
    "AD05":       "financial_burden_rent_util_school",# difficulty paying rent/utilities/school fees
    "AD06":       "ability_borrow_for_business",    # ability to borrow for business/farm
    "AD07":       "ability_borrow_emergency",       # ability to borrow for emergency
    "AD08":       "has_debt",                       # household has debt (0/1)
    "AD09":       "debt_source_1st",                # 1st source of loan
    "AD10":       "debt_source_2nd",                # 2nd source of loan
    "AD11":       "formal_debt_total",              # total formal debt (end of last month)
    "AD12":       "formal_debt_housing",            # formal debt: housing/land purchase
    "AD13":       "formal_debt_education",          # formal debt: education
    "AD14_1":     "formal_debt_vehicle",            # formal debt: vehicle purchase
    "AD14_2":     "formal_debt_credit_card",        # formal debt: credit card purchases
    "AD14_3":     "formal_debt_other_consumption",  # formal debt: other consumption
    "AD15":       "formal_debt_business",           # formal debt: business
    "AD16":       "formal_debt_farming",            # formal debt: farming
    "AD17":       "formal_debt_other",              # formal debt: other purposes
    "AD18":       "informal_debt_housing",          # informal debt: housing/land
    "AD19":       "informal_debt_education",        # informal debt: education
    "AD20_1":     "informal_debt_vehicle",          # informal debt: vehicle
    "AD20_2":     "informal_debt_credit_card",      # informal debt: credit card
    "AD20_3":     "informal_debt_other_consumption",# informal debt: other consumption
    "AD21":       "informal_debt_business",         # informal debt: business
    "AD22":       "informal_debt_farming",          # informal debt: farming
    "AD23":       "informal_debt_other",            # informal debt: other purposes
    "AD24":       "total_debt_last_month",          # total debt amount last month
    "AD25":       "formal_debt_last_month",         # formal sector debt last month
    "AD26":       "informal_debt_last_month",       # informal sector debt last month

    # ── REC18 — MIGRATION & REMITTANCE (mr_ / mp_ prefix) ───────────────────
    "MR01":       "mr_n_members_moved_out",         # members who moved out past 10 years
    "MR02":       "mr_n_senders_total",             # no. who ever sent money to this HH
    "MR03":       "mr_n_senders_regular",           # no. who regularly send money
    "MR04":       "mr_sender_sex",                  # sex of remittance sender
    "MR05":       "mr_sender_age",                  # age of remittance sender
    "MR06":       "mr_sender_relationship",         # sender's relationship to HH head
    "MR07":       "mr_sender_education",            # sender's education level
    "MR08":       "mr_sender_occupation",           # sender's primary occupation
    "MR09":       "mr_sender_industry",             # sender's industry type
    "MR10":       "mr_reason_moved_out",            # reason for moving out
    "MR11":       "mr_destination",                 # destination after moving out
    "MR12":       "mr_remittance_received_past12m", # amount received from sender past 12 months
    "MR13":       "mr_total_remittance_received",   # total remittance received from relatives
    "MP01":       "mp_n_recipients_total",          # no. of persons HH ever sent money to
    "MP02":       "mp_n_recipients_regular",        # no. HH regularly sends money to
    "MP03":       "mp_recipient_sex",               # sex of remittance recipient
    "MP04":       "mp_recipient_age",               # age of recipient
    "MP05":       "mp_recipient_relationship",      # recipient's relationship to HH head
    "MP06":       "mp_recipient_education",         # recipient's education
    "MP07":       "mp_recipient_occupation",        # recipient's occupation
    "MP08":       "mp_recipient_industry",          # recipient's industry
    "MP09":       "mp_reason_moved_out",            # reason moved out
    "MP10":       "mp_destination",                 # recipient's destination
    "MP11":       "mp_remittance_sent_past12m",     # amount sent to recipient past 12 months
    "MP12":       "mp_total_remittance_sent",       # total money sent to relatives

    # ── REC25 — DEBT REPAYMENT ──────────────────────────────────────────────
    "AE00":       "has_current_debt",               # currently has debt (0/1)
    "AE01":       "repaid_debt_past12m",            # repaid debt in past 12 months (0/1)
    "AE02a":      "debt_repay_housing_cash",        # debt repayment: housing/land (cash)
    "AE02bc":     "debt_repay_housing_inkind",
    "AE03a":      "debt_repay_education_cash",      # debt repayment: education (cash)
    "AE03bc":     "debt_repay_education_inkind",
    "AE04_1a":    "debt_repay_vehicle_cash",        # debt repayment: vehicle (cash)
    "AE04_1bc":   "debt_repay_vehicle_inkind",
    "AE04_2a":    "debt_repay_credit_card_cash",    # debt repayment: credit card (cash)
    "AE04_2bc":   "debt_repay_credit_card_inkind",
    "AE04_3a":    "debt_repay_other_consumption_cash",# debt repayment: other consumption (cash)
    "AE04_3bc":   "debt_repay_other_consumption_inkind",
    "AE05a":      "debt_repay_business_cash",       # debt repayment: non-farm business (cash)
    "AE05bc":     "debt_repay_business_inkind",
    "AE06a":      "debt_repay_farming_cash",        # debt repayment: farming (cash)
    "AE06bc":     "debt_repay_farming_inkind",
    "AE07a":      "debt_repay_other_cash",          # debt repayment: other purposes (cash)
    "AE07bc":     "debt_repay_other_inkind",
    "AE08":       "bought_house_own_saving",        # bought house with own savings past 12 months (0/1)
    "AE09":       "house_purchase_monthly_avg",     # monthly average spent on house purchase
}
