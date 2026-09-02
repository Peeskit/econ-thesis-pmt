"""
SES 2564 (2021) column name mapping: actual CSV header -> readable snake_case name.

Generated from ses2564_column_data_dictionary.xlsx
840 entries; all 21 source CSV headers verified.
"""

COLUMN_MAP: dict[str, str] = {
    'AREA': 'area_type',  # 1=municipal 2=non-municipal
    'CWT': 'province',  # changwat code (Appendix A)
    'NEW_HH_NO': 'household_id',  # new unique household number
    'REG': 'region',  # 1=BKK 2=Central 3=North 4=NE 5=South
    'HM01': 'member_serial_no',  # member serial number in HH
    'HM01_1': 'respondent_serial_no',  # serial no. of main respondent
    'HM05': 'religion',  # religion code
    'HM40': 'primary_occupation_code',  # primary occupation code (Appendix D)
    'HM43': 'secondary_occupation_code',  # secondary occupation code
    'IW02': 'iw_occupation_code',  # occupation code (Appendix D)
    'IW03_1': 'iw_industry_type',  # industry type code
    'IB02': 'ib_occupation_code',  # occupation code
    'IB03_1': 'ib_industry_type',  # industry type code
    'IB04': 'ib_work_type_code',  # work type indicator (auxiliary code)
    'IA03_1A': 'ia_farm_type1_code',  # farm activity type code (1st activity)
    'IA03_1B': 'ia_farm_type2_code',  # farm activity type code (2nd activity)
    'IA03_1C': 'ia_farm_type3_code',  # farm activity type code (3rd activity)
    'AMP': 'district',  # amphoe code
    'EA': 'enum_district',  # enumeration district no.
    'ENUM': 'enum_result',  # enumeration result code
    'HH_NO': 'hh_no',  # sample household no. within PSU
    'IA03_1': 'ia_farm_type_code',  # type of farm/agricultural activity
    'ID_CODE 1': 'enumerator_id',
    'ID_CODE 2': 'coder_id',
    'PSU_NO': 'psu_no',  # primary sample unit no.
    'REC': 'record_no',
    'SUB': 'sub_record_no',
    'TMB': 'subdistrict',  # tambon code
    'VIL': 'village_no',
    'A02': 'n_workers_incl_servants',  # no. of income-earning members incl. servants
    'A02_1': 'n_workers_excl_servants',  # no. of income-earning members excl. servants
    'A03': 'socioeconomic_class',  # household socio-economic class
    'A04': 'n_members_incl_servants',  # household size incl. servants
    'A04_1': 'n_members_excl_servants',  # household size excl. servants
    'A05': 'n_wage_employees',  # no. of members earning wages/salaries (for REC13)
    'A06': 'n_nonfarm_business_operators',  # no. of members in non-farm business (for REC14)
    'A07': 'monthly_expenditure_household',  # total expenditure per household
    'A08': 'monthly_consumption_expenditure',  # consumption expenditure per household
    'A09': 'monthly_food_tobacco_expenditure',  # food, beverages & tobacco per household
    'A10': 'monthly_expenditure_percapita',  # total expenditure per capita
    'A11': 'monthly_consumption_percapita',  # consumption expenditure per capita
    'A12': 'monthly_food_tobacco_percapita',  # food, beverages & tobacco per capita
    'A13': 'monthly_income_household',  # total income per household
    'A14': 'monthly_current_income_household',  # current income per household
    'A15': 'monthly_income_percapita',  # *** TARGET: total income per capita excl. servants ***
    'A15_1': 'monthly_income_percapita_incl',  # total income per capita incl. servants
    'A16': 'monthly_current_income_percapita',  # current income per capita excl. servants
    'A16_1': 'monthly_current_income_percapita_incl',  # current income per capita incl. servants
    'A17': 'wages_last_month',  # 1) wages & salaries last month
    'A18': 'wages_monthly_avg',  # 1) wages & salaries monthly avg
    'A19': 'business_profit_last_month',  # 2) net profit from business last month
    'A20': 'business_profit_monthly_avg',  # 2) net profit from business monthly avg
    'A21': 'farm_profit_last_month',  # 3) net profit from farming last month
    'A22': 'farm_profit_monthly_avg',  # 3) net profit from farming monthly avg
    'A23': 'pension_last_month',  # 4) pensions & annuities last month
    'A24': 'pension_monthly_avg',  # 4) pensions & annuities monthly avg
    'A25': 'work_compensation_last_month',  # 5) work compensation last month
    'A26': 'work_compensation_monthly_avg',  # 5) work compensation monthly avg
    'A27': 'private_transfers_last_month',  # 6) money assistance from outside HH last month
    'A28': 'private_transfers_monthly_avg',  # 6) money assistance from outside HH monthly avg
    'A29': 'govt_social_assist_last_month',  # 7) govt social assistance for elderly/disabled last month
    'A30': 'govt_social_assist_monthly_avg',  # 7) govt social assistance monthly avg
    'A31': 'rent_income_last_month',  # 8) rental income last month
    'A32': 'rent_income_monthly_avg',  # 8) rental income monthly avg
    'A33': 'interest_dividends_last_month',  # 9) interest/dividends last month
    'A34': 'interest_dividends_monthly_avg',  # 9) interest/dividends monthly avg
    'A35': 'private_lending_interest_last_month',  # 10) interest from private lending last month
    'A36': 'private_lending_interest_monthly_avg',  # 10) interest from private lending monthly avg
    'A37': 'total_money_income_last_month',  # sum of all money income last month
    'A38': 'total_money_income_monthly_avg',  # sum of all money income monthly avg
    'A39': 'imputed_rent',  # 11) imputed rent of free-occupied house (in-kind)
    'A40': 'inkind_goods_services',  # 12) in-kind goods & services received unpaid
    'A41': 'inkind_food_beverages',  # 13) in-kind food & beverages received unpaid
    'A42': 'scholarship_last_month',  # 14) education scholarship last month
    'A43': 'scholarship_monthly_avg',  # 14) education scholarship monthly avg
    'A44': 'gifts_inheritance_last_month',  # 15) inheritance & gifts last month
    'A45': 'gifts_inheritance_monthly_avg',  # 15) inheritance & gifts monthly avg
    'A46': 'insurance_proceeds_last_month',  # 16) insurance proceeds last month
    'A47': 'insurance_proceeds_monthly_avg',  # 16) insurance proceeds monthly avg
    'A48': 'other_receipts_last_month',  # 17) lottery, gambling, commissions last month
    'A49': 'other_receipts_monthly_avg',  # 17) other receipts monthly avg
    'A50': 'total_other_receipts_last_month',  # sum of other receipts last month
    'A51': 'total_other_receipts_monthly_avg',  # sum of other receipts monthly avg
    'A53': 'debt_repayment_monthly',  # monthly debt repayment
    'C01': 'hh_head_sex',  # sex of HH head (1=male 2=female)
    'C02': 'hh_head_age',  # age of HH head
    'C03': 'hh_head_marital_status',  # marital status of HH head
    'C04': 'hh_head_education',  # highest education level of HH head
    'C05': 'n_members_under15',  # members aged < 15
    'C06': 'n_members_over60',  # members aged >= 60
    'C07': 'n_disabled_total',  # total disabled persons in HH
    'C08': 'n_disabled_since_birth',  # disabled since birth
    'C09': 'n_disabled_after_birth',  # disabled after birth
    'C10': 'n_govt_medical_welfare',  # members with govt/state enterprise medical welfare
    'C11': 'n_universal_health_card',  # members with universal health (gold) card
    'C12': 'n_social_security_card',  # members with social security medical card (m.33/39)
    'C13': 'n_informal_worker_ss_card',  # members with social security card (m.40)
    'C14': 'n_private_health_insurance',  # members with private health insurance
    'C15': 'n_employer_welfare',  # members with employer welfare
    'C16': 'n_other_medical_welfare',  # members with other medical welfare
    'C17': 'n_elderly_pension',  # members receiving elderly social pension
    'C18': 'n_disability_assistance',  # members receiving disability assistance
    'C19': 'n_free_school_lunch',  # members receiving free school lunch
    'C20': 'n_govt_scholarship',  # members receiving govt scholarship
    'C21': 'n_welfare_govt_card',  # members with welfare government card (low income)
    'C22': 'n_child_subsidy',  # members receiving child subsidy (0-6 yrs)
    'C23': 'n_other_govt_fund',  # members receiving other govt funds
    'C24': 'n_govt_education_loan',  # members with govt education loan
    'C25': 'n_people_bank_loan',  # members with people bank loan
    'C26': 'n_village_fund_loan',  # members with village fund loan
    'C27': 'n_other_govt_loan',  # members with other govt fund loan
    'CON_EX1': 'consumption_expend_cash',  # CSV spelling variant of CON_EX 1
    'CON_EX2': 'consumption_expend_inkind',  # CSV spelling variant of CON_EX 2
    'CON_EX3': 'consumption_expend_total',  # CSV spelling variant of CON_EX 3
    'FB_EX1': 'food_expend_cash',  # CSV spelling variant of FB_EX 1
    'FB_EX2': 'food_expend_inkind',  # CSV spelling variant of FB_EX 2
    'FB_EX3': 'food_expend_total',  # CSV spelling variant of FB_EX 3
    'NCON_EX1': 'nonconsumption_expend_cash',  # non-consumption expend paid by cash
    'NCON_EX2': 'nonconsumption_expend_inkind',  # non-consumption expend in-kind
    'NCON_EX3': 'nonconsumption_expend_total',  # total non-consumption expenditure
    'PA1': 'total_farm_profit_last_month',  # total net farm profit last month
    'PA2': 'total_farm_profit_monthly_avg',  # total net farm profit monthly avg
    'PB1': 'total_business_profit_last_month',  # total net business profit last month
    'PB2': 'total_business_profit_monthly_avg',  # total net business profit monthly avg
    'TP_EX1': 'tobacco_expend_cash',  # CSV spelling variant of TP_EX 1
    'TP_EX2': 'tobacco_expend_inkind',  # CSV spelling variant of TP_EX 2
    'TP_EX3': 'tobacco_expend_total',  # CSV spelling variant of TP_EX 3
    'WS1': 'total_wages_last_month',  # total wages & salaries (money) last month
    'WS2': 'total_wages_monthly_avg',  # total wages & salaries monthly avg
    'A52': 'sampling_weight',  # survey sampling weight (4 decimal places)
    'HM02': 'relationship_to_head',  # relationship to household head
    'HM03': 'sex',  # sex (1=male 2=female)
    'HM04': 'age',  # age in years
    'HM06': 'language',  # language spoken in household
    'HM07': 'disability_type',  # disability status & type
    'HM08': 'can_self_care',  # can take care of self in daily life
    'HM09': 'can_travel_alone',  # can go out without assistant
    'HM10': 'marital_status',  # marital status
    'HM11': 'lives_with_parents',  # whether stays with parents
    'HM12': 'years_apart_from_parents',  # years not living with father/mother
    'HM13': 'reason_apart_from_parents',  # reason not staying with parents
    'HM14': 'school_attendance',  # school attendance status
    'HM15': 'education_attainment',  # highest education level completed
    'HM16': 'education_major',  # major/field of study
    'HM17': 'education_current_level',  # current level of schooling
    'HM18': 'education_tuition_fees',  # tuition/school fees (annual)
    'HM19': 'education_uniform_cost',  # uniform cost (annual)
    'HM20': 'education_books_cost',  # books & equipment cost (annual)
    'HM21': 'education_transport_cost',  # transport to school cost (annual)
    'HM22': 'govt_medical_welfare',  # govt/state enterprise medical welfare (0/1)
    'HM23': 'universal_health_card',  # universal health (gold) card (0/1)
    'HM24': 'social_security_card',  # social security medical card m.33/39 (0/1)
    'HM25': 'informal_worker_ss_card',  # social security card m.40 (0/1)
    'HM26': 'private_health_insurance',  # private health insurance (0/1)
    'HM27': 'employer_welfare',  # employer welfare (0/1)
    'HM28': 'other_medical_welfare',  # other medical welfare (0/1)
    'HM29': 'elderly_pension',  # social pension for elderly (0/1-5)
    'HM30': 'disability_assistance',  # disability assistance (0/1-5)
    'HM31': 'free_school_lunch',  # free school lunch/supplementary food (0/1-5)
    'HM32': 'govt_scholarship',  # government scholarship (0/1-5)
    'HM33': 'welfare_govt_card',  # welfare government card (0/1-5)
    'HM34': 'child_subsidy',  # child subsidy 0-6 yrs (0/1-5)
    'HM35': 'other_govt_funds',  # other government fund programmes (0/1-5)
    'HM36': 'govt_education_loan',  # govt education loan (0/1)
    'HM37': 'people_bank_loan',  # people bank loan (0/1)
    'HM38': 'village_fund_loan',  # village fund scheme loan (0/1)
    'HM39': 'other_govt_loan',  # other govt fund loan (0/1)
    'HM41': 'work_status',  # employment/work status
    'HM42': 'industry_type',  # type of industry (Appendix E)
    'HM44': 'secondary_work_status',  # secondary employment status
    'HM45': 'secondary_industry_type',  # secondary industry type
    'HH01': 'dwelling_type',  # type of dwelling
    'HH02': 'construction_material',  # building material
    'HH03': 'tenure',  # ownership/tenure status
    'HH04': 'rent_payer',  # who pays the rent
    'HH05': 'monthly_rent_or_estimated',  # monthly rent or estimated rental value
    'HH06': 'dwelling_used_for_business',  # dwelling partly used for business (0/1)
    'HH07': 'n_rooms_total',  # total rooms (excl. bathroom)
    'HH08': 'n_bedrooms',  # number of bedrooms
    'HH09': 'has_electricity',  # electricity in dwelling (0/1)
    'HH10': 'cooking_fuel',  # cooking fuel type
    'HH11': 'drinking_water_source',  # drinking water source
    'HH12': 'general_water_source',  # water supply for general use
    'HH13': 'garbage_disposal_1st',  # primary garbage disposal method
    'HH14': 'garbage_disposal_2nd',  # secondary garbage disposal method
    'HH15': 'toilet_facility',  # toilet facility type
    'HH16': 'owns_bicycle',
    'HH17': 'owns_motorcycle',
    'HH18': 'owns_automobile',
    'HH19': 'owns_pickup_van',
    'HH20': 'owns_other_truck',
    'HH21': 'owns_motorboat',
    'HH22': 'owns_bed',
    'HH23': 'owns_gas_stove',
    'HH24': 'owns_electric_stove',
    'HH25': 'owns_microwave',
    'HH26_1': 'owns_electric_pot',
    'HH26_2': 'owns_kettle',
    'HH27': 'owns_refrigerator',
    'HH28': 'owns_electric_iron',
    'HH29_1': 'owns_rice_cooker',
    'HH29_2': 'owns_electric_pan',
    'HH30': 'owns_electric_fan',
    'HH31': 'owns_radio',
    'HH32_1': 'owns_crt_tv',
    'HH32_2': 'owns_lcd_led_tv',
    'HH33': 'owns_vcd_dvd_player',
    'HH34': 'owns_washing_machine',
    'HH35': 'owns_air_conditioner',
    'HH36': 'owns_water_heater',
    'HH37': 'owns_home_computer',
    'HH38': 'has_internet_connection',
    'HH39': 'owns_telephone',
    'HH40': 'n_mobile_phones',
    'HH41': 'n_smartphones',
    'HH42': 'n_fluorescent_bulbs',
    'HH43': 'n_incandescent_bulbs',
    'HH44': 'n_cfl_bulbs',
    'HH45': 'n_led_e27_bulbs',
    'HH46': 'n_led_t8_bulbs',
    'HH47': 'n_internet_users',  # members who used internet in past 12 months
    'EG01A': 'housing_rent_cash',  # 1.1 house rent / estimated rental - cash
    'EG01BC': 'housing_rent_inkind',
    'EG02A': 'dwelling_repair_cash',  # 1.2 repair of dwelling - cash
    'EG02BC': 'dwelling_repair_inkind',
    'EG03A': 'plumbing_install_cash',  # 1.3 plumbing installation/repair - cash
    'EG03BC': 'plumbing_install_inkind',
    'EG04A': 'electrical_install_cash',  # 1.4 electrical installation/repair - cash
    'EG04BC': 'electrical_install_inkind',
    'EG05A': 'tools_equipment_cash',  # 1.5 tools & equipment - cash
    'EG05BC': 'tools_equipment_inkind',
    'EG06A': 'furniture_cash',  # 2.1 furniture - cash
    'EG06BC': 'furniture_inkind',
    'EG07A': 'cooking_appliance_cash',  # 2.1 cooking stove/microwave/rice cooker - cash
    'EG07BC': 'cooking_appliance_inkind',
    'EG08A': 'blender_kettle_cash',  # 2.1 grinder/blender/electric pot - cash
    'EG08BC': 'blender_kettle_inkind',
    'EG09A': 'washer_heater_pump_cash',  # 2.1 washing machine/water heater/pump - cash
    'EG09BC': 'washer_heater_pump_inkind',
    'EG10A': 'ac_fridge_fan_cash',  # 2.1 air conditioner/refrigerator/fan - cash
    'EG10BC': 'ac_fridge_fan_inkind',
    'EG11A': 'other_major_appliance_cash',  # 2.1 other major equipment - cash
    'EG11BC': 'other_major_appliance_inkind',
    'EG12A': 'appliance_repair_cash',  # 2.1 repairing/maintenance - cash
    'EG12BC': 'appliance_repair_inkind',
    'EG13A': 'bedding_cloth_cash',  # 2.2 bedding & furnishing cloth - cash
    'EG13BC': 'bedding_cloth_inkind',
    'EG14A': 'kitchen_cloth_cash',  # 2.2 kitchen/dining cloth - cash
    'EG14BC': 'kitchen_cloth_inkind',
    'EG15A': 'other_household_cloth_cash',  # 2.2 other household cloth - cash
    'EG15BC': 'other_household_cloth_inkind',
    'EG16A': 'kitchen_appliance_small_cash',  # 2.3 pans/pots etc. - cash
    'EG16BC': 'kitchen_appliance_small_inkind',
    'EG17A': 'flask_tank_sink_cash',  # 2.3 hot/cold flask, tank, sink - cash
    'EG17BC': 'flask_tank_sink_inkind',
    'EG18A': 'electricity_bill_cash',  # 2.4 electricity - cash
    'EG18BC': 'electricity_bill_inkind',
    'EG19A': 'cooking_gas_cash',  # 2.4 cooking gas - cash
    'EG19BC': 'cooking_gas_inkind',
    'EG20A': 'other_gas_cash',  # 2.4 gas for other purposes - cash
    'EG20BC': 'other_gas_inkind',
    'EG21A': 'charcoal_wood_cash',  # 2.4 charcoal and wood - cash
    'EG21BC': 'charcoal_wood_inkind',
    'EG22A': 'kerosene_cash',  # 2.4 kerosene - cash
    'EG22BC': 'kerosene_inkind',
    'EG23A': 'lighting_accessories_cash',  # 2.4 lighting accessories - cash
    'EG23BC': 'lighting_accessories_inkind',
    'EG24A': 'water_supply_cash',  # 2.4 water supply - cash
    'EG24BC': 'water_supply_inkind',
    'EG25A': 'cleaning_tools_cash',  # 2.5 mops/brooms/brushes - cash
    'EG25BC': 'cleaning_tools_inkind',
    'EG26A': 'detergent_cash',  # 2.5 detergent/softener - cash
    'EG26BC': 'detergent_inkind',
    'EG27A': 'liquid_detergent_cash',  # 2.5 liquid detergent/polishes - cash
    'EG27BC': 'liquid_detergent_inkind',
    'EG28A': 'servant_wages_member_cash',  # 3.1 servant wages (HH member) - cash
    'EG28BC': 'servant_wages_member_inkind',
    'EG29A': 'servant_wages_outside_cash',  # 3.2 servant wages (non-member) - cash
    'EG29BC': 'servant_wages_outside_inkind',
    'EG30A': 'clothing_shirts_pants_cash',  # 4.1 shirts/skirts/trousers - cash
    'EG30BC': 'clothing_shirts_pants_inkind',
    'EG31A': 'sportswear_cash',  # 4.2 sportswear - cash
    'EG31BC': 'sportswear_inkind',
    'EG32A': 'loincloth_underwear_cash',  # 4.3 loincloth/sarong/underwear - cash
    'EG32BC': 'loincloth_underwear_inkind',
    'EG33A': 'other_clothing_cash',  # 4.4 other clothing - cash
    'EG33BC': 'other_clothing_inkind',
    'EG34A': 'tailoring_cash',  # 4.5 sewing/repair/altering - cash
    'EG34BC': 'tailoring_inkind',
    'EG35A': 'laundry_cash',  # 4.6 laundry/dry cleaning/clothing rental - cash
    'EG35BC': 'laundry_inkind',
    'EG36A': 'shoes_cash',  # 5.1 shoes (all types) - cash
    'EG36BC': 'shoes_inkind',
    'EG37A': 'sport_shoes_cash',  # 5.2 sport shoes - cash
    'EG37BC': 'sport_shoes_inkind',
    'EG38A': 'shoe_repair_cash',  # 5.3 shoe repair/rental/cleaning - cash
    'EG38BC': 'shoe_repair_inkind',
    'EG39A': 'soap_toothpaste_cash',  # 6.1 soap/toothpaste/shampoo - cash
    'EG39BC': 'soap_toothpaste_inkind',
    'EG40A': 'comb_razor_cash',  # 6.1 comb/brushes/razor - cash
    'EG40BC': 'comb_razor_inkind',
    'EG41A': 'cosmetics_cash',  # 6.1 cosmetics - cash
    'EG41BC': 'cosmetics_inkind',
    'EG42A': 'watch_handbag_cash',  # 6.1 watch/handbag/luggage/sunglasses - cash
    'EG42BC': 'watch_handbag_inkind',
    'EG43A': 'other_personal_supply_cash',  # 6.1 other personal supplies - cash
    'EG43BC': 'other_personal_supply_inkind',
    'EG44A': 'personal_supply_repair_cash',  # 6.1 personal supply repair - cash
    'EG44BC': 'personal_supply_repair_inkind',
    'EG45A': 'beauty_services_cash',  # 6.2 beauty services - cash
    'EG45BC': 'beauty_services_inkind',
    'EG46A': 'other_personal_services_cash',  # 6.2 other personal services - cash
    'EG46BC': 'other_personal_services_inkind',
    'EG47A': 'modern_medicine_cash',  # 7.1 modern medicine - cash
    'EG47BC': 'modern_medicine_inkind',
    'EG48A': 'herbal_medicine_cash',  # 7.1 traditional/herbal medicine - cash
    'EG48BC': 'herbal_medicine_inkind',
    'EG49A': 'contraceptives_cash',  # 7.1 contraceptives/condoms - cash
    'EG49BC': 'contraceptives_inkind',
    'EG50A': 'vitamins_supplements_cash',  # 7.1 vitamins/supplements - cash
    'EG50BC': 'vitamins_supplements_inkind',
    'EG51A': 'first_aid_kit_cash',  # 7.1 first-aid kit/medical equipment - cash
    'EG51BC': 'first_aid_kit_inkind',
    'EG52A': 'medical_public_outpatient_cash',  # total public hospital outpatient (EG52_1+EG52_2)
    'EG52BC': 'medical_public_outpatient_inkind',
    'EG52_1A': 'public_hospital_outpatient_cash',  # 7.2 public hospital outpatient - cash
    'EG52_1BC': 'public_hospital_outpatient_inkind',
    'EG52_2A': 'health_center_outpatient_cash',  # 7.2 public health center outpatient - cash
    'EG52_2BC': 'health_center_outpatient_inkind',
    'EG53A': 'medical_private_outpatient_cash',  # total private hospital outpatient
    'EG53BC': 'medical_private_outpatient_inkind',
    'EG53_1A': 'private_hospital_outpatient_cash',  # 7.2 private hospital outpatient - cash
    'EG53_1BC': 'private_hospital_outpatient_inkind',
    'EG53_2A': 'clinic_outpatient_cash',  # 7.2 clinic outpatient - cash
    'EG53_2BC': 'clinic_outpatient_inkind',
    'EG54A': 'traditional_healer_cash',  # 7.2 traditional healer/herbal treatment - cash
    'EG54BC': 'traditional_healer_inkind',
    'EG55A': 'dental_clinic_cash',  # 7.2 dental clinic - cash
    'EG55BC': 'dental_clinic_inkind',
    'EG56A': 'optometry_cash',  # 7.2 optometry/glasses - cash
    'EG56BC': 'optometry_inkind',
    'EG57A': 'health_checkup_cash',  # 7.2 annual checkup/pregnancy - cash
    'EG57BC': 'health_checkup_inkind',
    'EG58A': 'medical_public_inpatient_cash',  # total public hospital inpatient
    'EG58BC': 'medical_public_inpatient_inkind',
    'EG58_1A': 'public_hospital_inpatient_cash',  # 7.3 public hospital inpatient - cash
    'EG58_1BC': 'public_hospital_inpatient_inkind',
    'EG58_2A': 'health_center_inpatient_cash',  # 7.3 health center inpatient - cash
    'EG58_2BC': 'health_center_inpatient_inkind',
    'EG59A': 'medical_private_inpatient_cash',  # total private hospital inpatient
    'EG59BC': 'medical_private_inpatient_inkind',
    'EG59_1A': 'private_hospital_inpatient_cash',  # 7.3 private hospital inpatient - cash
    'EG59_1BC': 'private_hospital_inpatient_inkind',
    'EG59_2A': 'clinic_inpatient_cash',  # 7.3 clinic inpatient - cash
    'EG59_2BC': 'clinic_inpatient_inkind',
    'EG60A': 'other_medical_expense_cash',  # 7.3 other medical expense - cash
    'EG60BC': 'other_medical_expense_inkind',
    'EG61A': 'automobile_purchase_cash',  # 8.1 automobile/van/pickup purchase - cash
    'EG61BC': 'automobile_purchase_inkind',
    'EG62A': 'motorcycle_bicycle_purchase_cash',  # 8.1 motorcycle/bicycle purchase - cash
    'EG62BC': 'motorcycle_bicycle_purchase_inkind',
    'EG63A': 'vehicle_equipment_install_cash',  # 8.1 vehicle equipment installation - cash
    'EG63BC': 'vehicle_equipment_install_inkind',
    'EG64A': 'tire_battery_cash',  # 8.2 tire/battery - cash
    'EG64BC': 'tire_battery_inkind',
    'EG65A': 'engine_oil_cash',  # 8.2 engine oil/lubricant - cash
    'EG65BC': 'engine_oil_inkind',
    'EG66A': 'vehicle_overhaul_cash',  # 8.2 overhaul/repair - cash
    'EG66BC': 'vehicle_overhaul_inkind',
    'EG67A': 'driving_license_cash',  # 8.2 driver training/license/registration - cash
    'EG67BC': 'driving_license_inkind',
    'EG68A': 'crash_helmet_cash',  # 8.2 crash helmet - cash
    'EG68BC': 'crash_helmet_inkind',
    'EG69A': 'car_wash_cash',  # 8.2 car wash/lubrication/tyre repair - cash
    'EG69BC': 'car_wash_inkind',
    'EG70A': 'vehicle_maintenance_cash',  # 8.2 vehicle maintenance/others - cash
    'EG70BC': 'vehicle_maintenance_inkind',
    'EG71A': 'public_transport_cash',  # 8.3 bus/boat/train/BTS/plane - cash
    'EG71BC': 'public_transport_inkind',
    'EG72A': 'school_staff_bus_cash',  # 8.3 school bus/staff bus - cash
    'EG72BC': 'school_staff_bus_inkind',
    'EG73A': 'taxi_tricycle_cash',  # 8.3 taxi/tricycle/motorcycle taxi - cash
    'EG73BC': 'taxi_tricycle_inkind',
    'EG74A': 'gasoline_cash',  # 8.3 unleaded gasoline - cash
    'EG74BC': 'gasoline_inkind',
    'EG7501A': 'gasohol_91_cash',  # 8.3 gasohol 91 - cash
    'EG7501BC': 'gasohol_91_inkind',
    'EG7502A': 'gasohol_95_cash',  # 8.3 gasohol 95 - cash
    'EG7502BC': 'gasohol_95_inkind',
    'EG7503A': 'gasohol_e20_cash',  # 8.3 gasohol E20 - cash
    'EG7503BC': 'gasohol_e20_inkind',
    'EG7504A': 'gasohol_e85_cash',  # 8.3 gasohol E85 - cash
    'EG7504BC': 'gasohol_e85_inkind',
    'EG75A': 'fuel_gasohol_cash',  # total gasohol (EG7501–EG7504)
    'EG75BC': 'fuel_gasohol_inkind',
    'EG76A': 'ngv_gas_cash',  # 8.3 NGV gas - cash
    'EG76BC': 'ngv_gas_inkind',
    'EG77A': 'lpg_gas_cash',  # 8.3 LPG gas - cash
    'EG77BC': 'lpg_gas_inkind',
    'EG7801A': 'diesel_b7_cash',  # 8.3 diesel B7 - cash
    'EG7801BC': 'diesel_b7_inkind',
    'EG7802A': 'diesel_cash',  # 8.3 diesel - cash
    'EG7802BC': 'diesel_inkind',
    'EG7803A': 'diesel_b7_premium_cash',  # 8.3 diesel B7 premium - cash
    'EG7803BC': 'diesel_b7_premium_inkind',
    'EG781A': 'biodiesel_b5_cash',  # 8.3 bio-diesel B5 - cash
    'EG781BC': 'biodiesel_b5_inkind',
    'EG782A': 'alt_fuel_cash',  # 8.3 other alternative fuel - cash
    'EG782BC': 'alt_fuel_inkind',
    'EG78A': 'fuel_diesel_cash',  # total diesel (EG7801–EG7803)
    'EG78BC': 'fuel_diesel_inkind',
    'EG79A': 'special_travel_cash',  # 8.4 visiting hometown/religious travel - cash
    'EG79BC': 'special_travel_inkind',
    'EG80A': 'personal_trip_cash',  # 8.4 personal trip domestic/outbound - cash
    'EG80BC': 'personal_trip_inkind',
    'EG81A': 'package_tour_cash',  # 8.4 package tour - cash
    'EG81BC': 'package_tour_inkind',
    'EG82A': 'souvenir_domestic_cash',  # 8.4 souvenir on domestic trip - cash
    'EG82BC': 'souvenir_domestic_inkind',
    'EG83A': 'souvenir_outbound_cash',  # 8.4 souvenir domestic/outbound - cash
    'EG83BC': 'souvenir_outbound_inkind',
    'EG84A': 'telecom_equipment_cash',  # total communication equipment purchase
    'EG84BC': 'telecom_equipment_inkind',
    'EG84_1A': 'telephone_purchase_cash',  # 8.5 telephone purchase - cash
    'EG84_1BC': 'telephone_purchase_inkind',
    'EG84_2A': 'mobile_phone_purchase_cash',  # 8.5 mobile phone purchase - cash
    'EG84_2BC': 'mobile_phone_purchase_inkind',
    'EG85A': 'telecom_phone_service_cash',  # total telephone service
    'EG85BC': 'telecom_phone_service_inkind',
    'EG85_1A': 'landline_service_cash',  # 8.5 landline/public phone service - cash
    'EG85_1BC': 'landline_service_inkind',
    'EG85_2A': 'mobile_service_cash',  # 8.5 mobile phone service - cash
    'EG85_2BC': 'mobile_service_inkind',
    'EG86A': 'telecom_internet_service_cash',  # total internet service
    'EG86BC': 'telecom_internet_service_inkind',
    'EG86_1A': 'home_internet_cash',  # 8.5 home internet - cash
    'EG86_1BC': 'home_internet_inkind',
    'EG86_2A': 'mobile_internet_cash',  # 8.5 mobile internet - cash
    'EG86_2BC': 'mobile_internet_inkind',
    'EG87A': 'other_communication_cash',  # 8.5 other communication - cash
    'EG87BC': 'other_communication_inkind',
    'EG88A': 'public_tuition_fees_cash',  # 9.1 public school tuition fees - cash
    'EG88BC': 'public_tuition_fees_inkind',
    'EG89A': 'private_tuition_fees_cash',  # 9.2 private school tuition fees - cash
    'EG89BC': 'private_tuition_fees_inkind',
    'EG90A': 'school_books_supplies_cash',  # 9.3 textbooks & supplies - cash
    'EG90BC': 'school_books_supplies_inkind',
    'EG91A': 'extra_tuition_cash',  # 9.4 extra tuition/music/dance - cash
    'EG91BC': 'extra_tuition_inkind',
    'EG92A': 'other_education_cash',  # 9.5 other education expenses - cash
    'EG92BC': 'other_education_inkind',
    'EG100A': 'pets_cash',  # 10.2 pets & pet equipment - cash
    'EG100BC': 'pets_inkind',
    'EG101A': 'plants_flowers_cash',  # 10.2 plants/shrubs/flowers - cash
    'EG101BC': 'plants_flowers_inkind',
    'EG102A': 'cable_tv_membership_cash',  # 10.2 cable TV membership/photography - cash
    'EG102BC': 'cable_tv_membership_inkind',
    'EG103A': 'recreation_maintenance_cash',  # 10.2 repair/maintenance/others - cash
    'EG103BC': 'recreation_maintenance_inkind',
    'EG104A': 'cinema_sports_events_cash',  # 10.3 cinema/sports/arts admission - cash
    'EG104BC': 'cinema_sports_events_inkind',
    'EG105A': 'amusement_park_zoo_cash',  # 10.3 amusement parks/zoo - cash
    'EG105BC': 'amusement_park_zoo_inkind',
    'EG106A': 'sport_fees_cash',  # 10.3 sport fees/rates - cash
    'EG106BC': 'sport_fees_inkind',
    'EG107A': 'other_recreation_admission_cash',  # 10.3 other recreation admission - cash
    'EG107BC': 'other_recreation_admission_inkind',
    'EG108A': 'newspapers_books_cash',  # 10.4 newspapers/magazines/books - cash
    'EG108BC': 'newspapers_books_inkind',
    'EG109A': 'library_fees_cash',  # 10.4 library fees - cash
    'EG109BC': 'library_fees_inkind',
    'EG110A': 'religious_donations_cash',  # 10.4 temple offerings/religious expenses - cash
    'EG110BC': 'religious_donations_inkind',
    'EG111A': 'ceremony_expenses_cash',  # 11 wedding/birthday/ceremonies - cash
    'EG111BC': 'ceremony_expenses_inkind',
    'EG93A': 'tv_radio_player_cash',  # 10.1 TV/radio/VCD/DVD - cash
    'EG93BC': 'tv_radio_player_inkind',
    'EG94A': 'camera_projector_cash',  # 10.1 camera/camcorder/projector - cash
    'EG94BC': 'camera_projector_inkind',
    'EG95A': 'satellite_cable_tv_cash',  # 10.1 satellite dish/cable TV - cash
    'EG95BC': 'satellite_cable_tv_inkind',
    'EG96A': 'computer_equipment_cash',  # 10.1 computer & equipment - cash
    'EG96BC': 'computer_equipment_inkind',
    'EG97A': 'sport_equipment_cash',  # 10.1 sport & fitness equipment - cash
    'EG97BC': 'sport_equipment_inkind',
    'EG98A': 'recreation_repair_cash',  # 10.1 repair/maintenance of recreation items - cash
    'EG98BC': 'recreation_repair_inkind',
    'EG99A': 'toys_cash',  # 10.2 toys - cash
    'EG99BC': 'toys_inkind',
    'EG112A': 'taxes_fees_fines_cash',  # 1 taxes/fees/fines - cash
    'EG112BC': 'taxes_fees_fines_inkind',
    'EG113A': 'career_membership_cash',  # 2 career/professional membership - cash
    'EG113BC': 'career_membership_inkind',
    'EG114A': 'remittance_out_cash',  # 3 money/goods sent to other HH - cash
    'EG114BC': 'remittance_out_inkind',
    'EG115A': 'donation_ngo_cash',  # 4 donations to NGO/organisations - cash
    'EG115BC': 'donation_ngo_inkind',
    'EG116A': 'other_contributions_cash',  # 5 temple donations/contributions - cash
    'EG116BC': 'other_contributions_inkind',
    'EG117A': 'insurance_premiums_cash',  # total insurance premiums (EG117_1+2+3)
    'EG117BC': 'insurance_premiums_inkind',
    'EG117_1A': 'insurance_premium_cash',  # 6 insurance premiums (excl. saving) - cash
    'EG117_1BC': 'insurance_premium_inkind',
    'EG117_2A': 'health_insurance_premium_cash',  # 6 health insurance premium - cash
    'EG117_2BC': 'health_insurance_premium_inkind',
    'EG117_3A': 'social_security_contrib_cash',  # 6 social security contribution - cash
    'EG117_3BC': 'social_security_contrib_inkind',
    'EG118A': 'lottery_gambling_cash',  # 7 lottery/gambling - cash
    'EG118BC': 'lottery_gambling_inkind',
    'EG119A': 'interest_payment_cash',  # 8 interest payment - cash
    'EG119BC': 'interest_payment_inkind',
    'EG120A': 'other_nonconsumption_cash',  # 9 other non-consumption expenses - cash
    'EG120BC': 'other_nonconsumption_inkind',
    'EF01A': 'food_grains_cereals_cash',  # 1 grains & cereal products - cash
    'EF01BC': 'food_grains_cereals_inkind',
    'EF02A': 'food_meat_poultry_cash',  # 2 meat & poultry - cash
    'EF02BC': 'food_meat_poultry_inkind',
    'EF03A': 'food_fish_seafood_cash',  # 3 fish & seafood - cash
    'EF03BC': 'food_fish_seafood_inkind',
    'EF04A': 'food_dairy_eggs_cash',  # 4 milk/cheese/eggs - cash
    'EF04BC': 'food_dairy_eggs_inkind',
    'EF04_1BC': 'food_school_milk_inkind',  # 4 complementary milk for students (free)
    'EF05A': 'food_oils_fats_cash',  # 5 oil & fat - cash
    'EF05BC': 'food_oils_fats_inkind',
    'EF06A': 'food_fruits_nuts_cash',  # 6 fruits & nuts - cash
    'EF06BC': 'food_fruits_nuts_inkind',
    'EF07A': 'food_vegetables_cash',  # 7 vegetables - cash
    'EF07BC': 'food_vegetables_inkind',
    'EF08A': 'food_sugar_sweets_cash',  # 8 sugar & sweets - cash
    'EF08BC': 'food_sugar_sweets_inkind',
    'EF09A': 'food_spices_cash',  # 9 spices & condiments - cash
    'EF09BC': 'food_spices_inkind',
    'EF10A': 'bev_nonalc_semi_cash',  # 10 non-alcoholic beverages semi-prepared - cash
    'EF10BC': 'bev_nonalc_semi_inkind',
    'EF11A': 'bev_nonalc_ready_cash',  # 10 non-alcoholic beverages ready-made - cash
    'EF11BC': 'bev_nonalc_ready_inkind',
    'EF12A': 'food_prepared_home_cash',  # 11 prepared food consumed at home - cash
    'EF12BC': 'food_prepared_home_inkind',
    'EF13A': 'food_away_total_cash',  # 12 food away from home total - cash
    'EF13BC': 'food_away_total_inkind',
    'EF13_1A': 'food_away_breakfast_cash',  # 12 breakfast away from home - cash
    'EF13_1BC': 'food_away_breakfast_inkind',
    'EF13_2A': 'food_away_lunch_cash',  # 12 lunch away from home - cash
    'EF13_2BC': 'food_away_lunch_inkind',
    'EF13_3A': 'food_away_dinner_cash',  # 12 dinner away from home - cash
    'EF13_3BC': 'food_away_dinner_inkind',
    'EF14A': 'bev_alcoholic_home_cash',  # 13 alcoholic beverages at home - cash
    'EF14BC': 'bev_alcoholic_home_inkind',
    'EF15A': 'bev_alcoholic_away_cash',  # 13 alcoholic beverages away from home - cash
    'EF15BC': 'bev_alcoholic_away_inkind',
    'EF16A': 'tobacco_cigarettes_cash',  # 14 cigarettes/tobacco - cash
    'EF16BC': 'tobacco_cigarettes_inkind',
    'EF17A': 'tobacco_betel_snuff_cash',  # 14 betel/snuff/other tobacco - cash
    'EF17BC': 'tobacco_betel_snuff_inkind',
    'IW01': 'iw_member_serial_no',  # member serial no. (wage earner)
    'IW03': 'iw_socioeconomic_class',  # socio-economic class (generated)
    'IW04': 'iw_months_worked',  # months worked in this occupation
    'IW05': 'iw_wage_type',  # type of wage (piece/hour/day/week/month)
    'IW06': 'iw_wage_rate_cash',  # wage rate in cash
    'IW07': 'iw_days_per_month',  # days worked per month
    'IW08': 'iw_hours_per_day',  # hours worked per day
    'IW09': 'iw_pieces_per_month',  # pieces per month (piece-rate workers)
    'IW10': 'iw_wages_last_month',  # wages & salaries last month
    'IW11': 'iw_overtime_bonus_last_month',  # overtime & bonus last month
    'IW12': 'iw_wages_past12m',  # wages & salaries past 12 months
    'IW13': 'iw_overtime_bonus_past12m',  # overtime & bonus past 12 months
    'IW14': 'iw_welfare_value_past12m',  # total welfare value from employment past 12 months
    'OCC1': 'iw_n_occupations',  # number of wage occupations for this member
    'IB01': 'ib_member_serial_no',  # member serial no. (business operator)
    'IB03': 'ib_socioeconomic_class',  # socio-economic class (generated)
    'IB05': 'ib_months_operating',  # months operating this business
    'IB06': 'ib_total_workers',  # total workers incl. entrepreneur
    'IB07': 'ib_n_employees',  # number of employees
    'IB08A': 'ib_gross_receipts_past12m',
    'IB08B': 'ib_gross_receipts_last_month',
    'IB0901A': 'ib_cost_raw_materials_past12m',
    'IB0901B': 'ib_cost_raw_materials_last_month',
    'IB0902A': 'ib_cost_rent_past12m',
    'IB0902B': 'ib_cost_rent_last_month',
    'IB0903A': 'ib_cost_fuel_electricity_past12m',
    'IB0903B': 'ib_cost_fuel_electricity_last_month',
    'IB0904A': 'ib_cost_wages_paid_past12m',
    'IB0904B': 'ib_cost_wages_paid_last_month',
    'IB0905A': 'ib_cost_medical_employees_past12m',
    'IB0905B': 'ib_cost_medical_employees_last_month',
    'IB0906A': 'ib_cost_interest_insurance_past12m',
    'IB0906B': 'ib_cost_interest_insurance_last_month',
    'IB0907A': 'ib_cost_taxes_other_past12m',
    'IB0907B': 'ib_cost_taxes_other_last_month',
    'IB09A': 'ib_total_operating_cost_past12m',
    'IB09B': 'ib_total_operating_cost_last_month',
    'IB10': 'ib_home_produced_goods_used',  # value of home-produced goods used in HH
    'IB11': 'ib_profit_share_pct',  # profit share % (if partnership)
    'OCC2': 'ib_n_occupations',  # number of business occupations for this member
    'IA01': 'ia_socioeconomic_class',  # socio-economic class (generated)
    'IA02A': 'ia_member1_serial_no',  # serial no of 1st farming member
    'IA02B': 'ia_member2_serial_no',  # serial no of 2nd farming member
    'IA04A': 'ia_owned_land_rai',
    'IA04B': 'ia_owned_land_sqwa',
    'IA05A': 'ia_rented_land_rai',
    'IA05B': 'ia_rented_land_sqwa',
    'IA06A': 'ia_public_land_rai',
    'IA06B': 'ia_public_land_sqwa',
    'IA07': 'ia_n_farm_workers',  # no. of household members working in farm
    'IA08': 'ia_agri_service_income_cash',  # income from renting animals/tools/agri services (cash)
    'IA09': 'ia_agri_service_inkind_sold',  # in-kind agri services: sold
    'IA10': 'ia_agri_service_inkind_consumed',  # in-kind agri services: consumed/other
    'IA11': 'ia_crops_total_value',  # total value of harvested crops
    'IA12': 'ia_crops_sold',  # crops sold
    'IA13': 'ia_crops_consumed',  # crops for household consumption
    'IA14': 'ia_crops_other_use',  # crops for other uses
    'IA15': 'ia_livestock_total_value',  # total value of livestock products
    'IA16': 'ia_livestock_sold',  # livestock products sold
    'IA17': 'ia_livestock_consumed',  # livestock products consumed
    'IA18': 'ia_livestock_other_use',  # livestock products other use
    'IA19': 'ia_livestock_initial_value',  # value of livestock at start of period
    'IA20': 'ia_fishery_total_value',  # value from fishery/hunting/forestry
    'IA21': 'ia_fishery_sold',  # fishery products sold
    'IA22': 'ia_fishery_consumed',  # fishery products consumed
    'IA23': 'ia_fishery_other_use',  # fishery products other use
    'IA24': 'ia_imputed_land_rent',  # estimated rental value of own land
    'IA25': 'ia_total_farm_cost_cash',  # total farm operating cost paid in cash
    'IA2502': 'ia_land_rent_paid_cash',  # 11.2 land rental paid in cash
    'IA2503': 'ia_equipment_cost_cash',  # 11.3 equipment/animals cost cash
    'IA2504': 'ia_fuel_water_cost_cash',  # 11.4 fuel/electricity/irrigation cash
    'IA2505': 'ia_fertilizer_pesticide_cash',  # 11.5 fertilizer/pesticides cash
    'IA2506': 'ia_seeds_chicks_cash',  # 11.6 seeds/chicks/piglets cash
    'IA2507': 'ia_animal_feed_cash',  # 11.7 animal feed cash
    'IA2508': 'ia_farm_wages_paid_cash',  # 11.8 wages for farm workers cash
    'IA2509': 'ia_other_farm_cost_cash',  # 11.9 other farm expenses cash
    'IA26': 'ia_total_farm_cost_produce',  # total farm cost paid with own produce
    'IA2602': 'ia_land_rent_own_produce',  # 11.2 land rental paid with own produce
    'IA2603': 'ia_equipment_cost_produce',  # 11.3 equipment cost own produce
    'IA2604': 'ia_fuel_water_cost_produce',  # 11.4 fuel cost own produce
    'IA2605': 'ia_fertilizer_pesticide_produce',  # 11.5 fertilizer own produce
    'IA2606': 'ia_seeds_chicks_produce',  # 11.6 seeds own produce
    'IA2607': 'ia_animal_feed_produce',  # 11.7 animal feed own produce
    'IA2608': 'ia_farm_wages_paid_produce',  # 11.8 farm wages own produce
    'IA2609': 'ia_other_farm_cost_produce',  # 11.9 other farm expenses own produce
    'IA27': 'ia_total_farm_cost_assist',  # total farm cost received as assistance
    'IA2702': 'ia_land_rent_received_assist',  # 11.2 land rental received as assistance
    'IA2703': 'ia_equipment_cost_assist',  # 11.3 equipment cost assistance
    'IA2704': 'ia_fuel_water_cost_assist',  # 11.4 fuel cost assistance
    'IA2705': 'ia_fertilizer_pesticide_assist',  # 11.5 fertilizer assistance
    'IA2706': 'ia_seeds_chicks_assist',  # 11.6 seeds assistance
    'IA2707': 'ia_animal_feed_assist',  # 11.7 animal feed assistance
    'IA2708': 'ia_farm_wages_paid_assist',  # 11.8 farm wages assistance
    'IA2709': 'ia_other_farm_cost_assist',  # 11.9 other farm expenses assistance
    'IA28': 'ia_farm_gross_receipt_last_month',  # gross farm receipt last month
    'IA29': 'ia_farm_expenditure_last_month',  # farm expenditure last month
    'IO01': 'io_socioeconomic_class_14',  # socio-economic class items 1-4 (generated)
    'IO02A': 'io_pension_cash_past12m',
    'IO02B': 'io_pension_inkind_past12m',
    'IO02C': 'io_pension_last_month_cash',
    'IO03A': 'io_work_compensation_cash_past12m',
    'IO03B': 'io_work_compensation_inkind_past12m',
    'IO03C': 'io_work_compensation_last_month_cash',
    'IO04A': 'io_private_transfer_cash_past12m',
    'IO04B': 'io_private_transfer_inkind_past12m',
    'IO04C': 'io_private_transfer_last_month_cash',
    'IO05A': 'io_govt_social_assist_cash_past12m',
    'IO05B': 'io_govt_social_assist_inkind_past12m',
    'IO05C': 'io_govt_social_assist_last_month_cash',
    'IO05_1A': 'io_elderly_pension_cash_past12m',
    'IO05_1B': 'io_elderly_pension_inkind_past12m',
    'IO05_1C': 'io_elderly_pension_last_month_cash',
    'IO05_2A': 'io_disability_assist_cash_past12m',
    'IO05_2B': 'io_disability_assist_inkind_past12m',
    'IO05_2C': 'io_disability_assist_last_month_cash',
    'IO05_3A': 'io_welfare_card_cash_past12m',
    'IO05_3B': 'io_welfare_card_inkind_past12m',
    'IO05_3C': 'io_welfare_card_last_month_cash',
    'IO05_4A': 'io_child_subsidy_cash_past12m',
    'IO05_4B': 'io_child_subsidy_inkind_past12m',
    'IO05_4C': 'io_child_subsidy_last_month_cash',
    'IO05_5A': 'io_paotang_app_cash_past12m',
    'IO05_5B': 'io_paotang_app_inkind_past12m',
    'IO05_5C': 'io_paotang_app_last_month_cash',
    'IO05_6A': 'io_other_govt_assist_cash_past12m',
    'IO05_6B': 'io_other_govt_assist_inkind_past12m',
    'IO05_6C': 'io_other_govt_assist_last_month_cash',
    'IO06A': 'io_scholarship_cash_past12m',
    'IO06B': 'io_scholarship_inkind_past12m',
    'IO06C': 'io_scholarship_last_month_cash',
    'IO07': 'io_socioeconomic_class_69',  # socio-economic class items 6-9 (generated)
    'IO07X1': 'io_socioeconomic_subclass1_69',
    'IO07X2': 'io_socioeconomic_subclass2_69',
    'IO08A': 'io_rental_income_cash_past12m',
    'IO08B': 'io_rental_income_inkind_past12m',
    'IO08C': 'io_rental_income_last_month_cash',
    'IO09A': 'io_copyright_cash_past12m',
    'IO09B': 'io_copyright_inkind_past12m',
    'IO09C': 'io_copyright_last_month_cash',
    'IO10A': 'io_bank_interest_cash_past12m',
    'IO10B': 'io_bank_interest_inkind_past12m',
    'IO10C': 'io_bank_interest_last_month_cash',
    'IO11A': 'io_private_lending_interest_cash_past12m',
    'IO11B': 'io_private_lending_interest_inkind_past12m',
    'IO11C': 'io_private_lending_interest_last_month_cash',
    'IO12A': 'io_gifts_inheritance_cash_past12m',
    'IO12B': 'io_gifts_inheritance_inkind_past12m',
    'IO12C': 'io_gifts_inheritance_last_month_cash',
    'IO13A': 'io_insurance_proceeds_cash_past12m',
    'IO13B': 'io_insurance_proceeds_inkind_past12m',
    'IO13C': 'io_insurance_proceeds_last_month_cash',
    'IO14A': 'io_other_income_cash_past12m',
    'IO14B': 'io_other_income_inkind_past12m',
    'IO14C': 'io_other_income_last_month_cash',
    'AD01': 'asset_value_dwelling_total',  # total value of living and temporary/vacation dwellings
    'AD01_1': 'asset_value_living_dwelling',  # value of living dwelling
    'AD01_2': 'asset_value_vacation_home',  # value of temporary/vacation dwelling
    'AD02': 'asset_value_business_land',  # value of land/building for business
    'AD03': 'asset_value_vehicles',  # value of vehicles
    'AD04': 'asset_financial_total',  # total value of financial assets
    'AD04_1': 'asset_financial_saving',  # financial assets for saving
    'AD04_2': 'asset_financial_investment',  # financial assets for investment
    'AD04_3': 'asset_financial_other',  # other financial assets
    'AD05': 'financial_burden_rent_util_school',  # difficulty paying rent/utilities/school fees
    'AD06': 'ability_borrow_for_business',  # ability to borrow for business/farm
    'AD07': 'ability_borrow_emergency',  # ability to borrow for emergency
    'AD08': 'has_debt',  # household has debt (0/1)
    'AD09': 'debt_source_1st',  # 1st source of loan
    'AD10': 'debt_source_2nd',  # 2nd source of loan
    'AD11': 'formal_debt_total',  # total formal debt (end of last month)
    'AD12': 'formal_debt_housing',  # formal debt: housing/land purchase
    'AD13': 'formal_debt_education',  # formal debt: education
    'AD14': 'formal_debt_consumption_total',  # total formal debt for household consumption
    'AD14_1': 'formal_debt_vehicle',  # formal debt: vehicle purchase
    'AD14_2': 'formal_debt_credit_card',  # formal debt: credit card purchases
    'AD14_3': 'formal_debt_other_consumption',  # formal debt: other consumption
    'AD15': 'formal_debt_business',  # formal debt: business
    'AD16': 'formal_debt_farming',  # formal debt: farming
    'AD17': 'formal_debt_other',  # formal debt: other purposes
    'AD18': 'informal_debt_housing',  # informal debt: housing/land
    'AD19': 'informal_debt_education',  # informal debt: education
    'AD20': 'informal_debt_consumption_total',  # total informal debt for household consumption
    'AD20_1': 'informal_debt_vehicle',  # informal debt: vehicle
    'AD20_2': 'informal_debt_credit_card',  # informal debt: credit card
    'AD20_3': 'informal_debt_other_consumption',  # informal debt: other consumption
    'AD21': 'informal_debt_business',  # informal debt: business
    'AD22': 'informal_debt_farming',  # informal debt: farming
    'AD23': 'informal_debt_other',  # informal debt: other purposes
    'AD24': 'total_debt_last_month',  # total debt amount last month
    'AD25': 'formal_debt_last_month',  # formal sector debt last month
    'AD26': 'informal_debt_last_month',  # informal sector debt last month
    'MP01': 'mp_n_recipients_total',  # no. of persons HH ever sent money to
    'MP02': 'mp_n_recipients_regular',  # no. HH regularly sends money to
    'MP03': 'mp_recipient_sex',  # sex of remittance recipient
    'MP04': 'mp_recipient_age',  # age of recipient
    'MP05': 'mp_recipient_relationship',  # recipient's relationship to HH head
    'MP06': 'mp_recipient_education',  # recipient's education
    'MP07': 'mp_recipient_occupation',  # recipient's occupation
    'MP08': 'mp_recipient_industry',  # recipient's industry
    'MP09': 'mp_reason_moved_out',  # reason moved out
    'MP10': 'mp_destination',  # recipient's destination
    'MP11': 'mp_remittance_sent_past12m',  # amount sent to recipient past 12 months
    'MP12': 'mp_total_remittance_sent',  # total money sent to relatives
    'MR01': 'mr_n_members_moved_out',  # members who moved out past 10 years
    'MR02': 'mr_n_senders_total',  # no. who ever sent money to this HH
    'MR03': 'mr_n_senders_regular',  # no. who regularly send money
    'MR04': 'mr_sender_sex',  # sex of remittance sender
    'MR05': 'mr_sender_age',  # age of remittance sender
    'MR06': 'mr_sender_relationship',  # sender's relationship to HH head
    'MR07': 'mr_sender_education',  # sender's education level
    'MR08': 'mr_sender_occupation',  # sender's primary occupation
    'MR09': 'mr_sender_industry',  # sender's industry type
    'MR10': 'mr_reason_moved_out',  # reason for moving out
    'MR11': 'mr_destination',  # destination after moving out
    'MR12': 'mr_remittance_received_past12m',  # amount received from sender past 12 months
    'MR13': 'mr_total_remittance_received',  # total remittance received from relatives
    'NN2': 'mr_sender_sequence_no',  # sequence number (1-3) of migrant who sent money to household
    'NN3': 'mp_recipient_sequence_no',  # sequence number (1-3) of migrant receiving money from household
    'AE00': 'has_current_debt',  # currently has debt (0/1)
    'AE01': 'repaid_debt_past12m',  # repaid debt in past 12 months (0/1)
    'AE02A': 'debt_repay_housing_cash',  # debt repayment: housing/land (cash)
    'AE02BC': 'debt_repay_housing_inkind',
    'AE03A': 'debt_repay_education_cash',  # debt repayment: education (cash)
    'AE03BC': 'debt_repay_education_inkind',
    'AE04A': 'debt_repay_consumption_cash',  # total household consumption debt repaid (generated = AE04_1+2+3, cash)
    'AE04BC': 'debt_repay_consumption_inkind',
    'AE04_1A': 'debt_repay_vehicle_cash',  # debt repayment: vehicle (cash)
    'AE04_1BC': 'debt_repay_vehicle_inkind',
    'AE04_2A': 'debt_repay_credit_card_cash',  # debt repayment: credit card (cash)
    'AE04_2BC': 'debt_repay_credit_card_inkind',
    'AE04_3A': 'debt_repay_other_consumption_cash',  # debt repayment: other consumption (cash)
    'AE04_3BC': 'debt_repay_other_consumption_inkind',
    'AE05A': 'debt_repay_business_cash',  # debt repayment: non-farm business (cash)
    'AE05BC': 'debt_repay_business_inkind',
    'AE06A': 'debt_repay_farming_cash',  # debt repayment: farming (cash)
    'AE06BC': 'debt_repay_farming_inkind',
    'AE07A': 'debt_repay_other_cash',  # debt repayment: other purposes (cash)
    'AE07BC': 'debt_repay_other_inkind',
    'AE08': 'bought_house_own_saving',  # bought house with own savings past 12 months (0/1)
    'AE09': 'house_purchase_monthly_avg',  # monthly average spent on house purchase
    'A01': 'enum_month',  # enumeration month (1-12)
    'CON_EX 1': 'consumption_expend_cash',  # consumption expend paid by cash
    'CON_EX 2': 'consumption_expend_inkind',  # consumption expend in-kind
    'CON_EX 3': 'consumption_expend_total',  # total consumption expenditure
    'ENUM24': 'enum24_remark',  # remark for ENUM=24
    'FB_EX 1': 'food_expend_cash',  # food & beverage expend cash
    'FB_EX 2': 'food_expend_inkind',  # food & beverage expend in-kind
    'FB_EX 3': 'food_expend_total',  # total food & beverage expenditure
    'HM01N': 'member_name',  # member name
    'IA02': 'ia_member_serial_no',  # member serial no. (farmer)
    'IA02_1': 'ia_member_name',
    'IA04': 'ia_land_owned_rai',  # owned land area (rai, tarangwa)
    'IA05': 'ia_land_rented_rai',  # rented land area (rai, tarangwa)
    'IA06': 'ia_public_land_rai',  # public/other land area (rai, tarangwa)
    'IB01_1': 'ib_member_name',
    'IB08': 'ib_gross_receipts_past12m',  # gross money receipts past 12 months
    'IB09': 'ib_total_operating_cost',  # total operating cost
    'IB0901': 'ib_cost_raw_materials',  # operating cost: raw materials
    'IB0902': 'ib_cost_rent',  # operating cost: office/vehicle rent
    'IB0903': 'ib_cost_fuel_electricity',  # operating cost: fuel/electricity/oil/gas
    'IB0904': 'ib_cost_wages_paid',  # operating cost: wages paid to employees
    'IB0905': 'ib_cost_medical_employees',  # operating cost: medical services for employees
    'IB0906': 'ib_cost_interest_insurance',  # operating cost: loan interest/insurance
    'IB0907': 'ib_cost_taxes_other',  # operating cost: business taxes & others
    'IO02': 'io_pension_cash_past12m',  # pensions/annuities cash past 12 months
    'IO03': 'io_work_compensation_cash_past12m',  # work compensation cash past 12 months
    'IO04': 'io_private_transfer_cash_past12m',  # private transfers cash past 12 months
    'IO05': 'io_govt_social_assist_cash_past12m',  # govt social assistance total cash 12m
    'IO05_1': 'io_elderly_pension_cash_past12m',  # 4.1 elderly pension cash 12m
    'IO05_2': 'io_disability_assist_cash_past12m',  # 4.2 disability assistance cash 12m
    'IO05_3': 'io_welfare_card_cash_past12m',  # 4.3 welfare card cash 12m
    'IO05_4': 'io_child_subsidy_cash_past12m',  # 4.4 child subsidy (0-6 yr) cash 12m
    'IO05_5': 'io_paotang_app_cash_past12m',  # 4.5 Paotang app govt programme cash 12m
    'IO05_6': 'io_other_govt_assist_cash_past12m',  # 4.6 other govt assistance cash 12m
    'IO06': 'io_scholarship_cash_past12m',  # 5 scholarship cash past 12 months
    'IO08': 'io_rental_income_cash_past12m',  # 6 rental income cash past 12 months
    'IO09': 'io_copyright_cash_past12m',  # 7 copyright/licence income cash 12m
    'IO10': 'io_bank_interest_cash_past12m',  # 8 bank interest/dividends cash 12m
    'IO11': 'io_private_lending_interest_cash_past12m',  # 9 private loan interest cash 12m
    'IO12': 'io_gifts_inheritance_cash_past12m',  # 10 gifts & inheritance cash 12m
    'IO13': 'io_insurance_proceeds_cash_past12m',  # 11 insurance proceeds cash 12m
    'IO14': 'io_other_income_cash_past12m',  # 12 other income (lottery etc.) cash 12m
    'IW01_1': 'iw_member_name',
    'TP_EX 1': 'tobacco_expend_cash',  # tobacco expenditure cash
    'TP_EX 2': 'tobacco_expend_inkind',  # tobacco expenditure in-kind
    'TP_EX 3': 'tobacco_expend_total',  # total tobacco expenditure
}
