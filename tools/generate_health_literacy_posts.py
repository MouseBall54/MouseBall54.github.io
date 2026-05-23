#!/usr/bin/env python3
"""Generate paired Health Literacy posts and local SVG context images."""

from __future__ import annotations

import html
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
POST_DATE = "2026-05-19"
LAST_MODIFIED_AT = "2026-05-23T15:00:00+09:00"
KO_CATEGORY = "ko_Health_Literacy"
EN_CATEGORY = "en_Health_Literacy"


SOURCES = {
    "cdc_activity": {
        "ko": "CDC Physical Activity Basics",
        "en": "CDC Physical Activity Basics",
        "url": "https://www.cdc.gov/physical-activity-basics/index.html",
    },
    "cdc_sleep": {
        "ko": "CDC Sleep and Sleep Disorders",
        "en": "CDC Sleep and Sleep Disorders",
        "url": "https://www.cdc.gov/sleep/about/index.html",
    },
    "who_diet": {
        "ko": "WHO Healthy Diet Fact Sheet",
        "en": "WHO Healthy Diet Fact Sheet",
        "url": "https://www.who.int/news-room/fact-sheets/detail/healthy-diet",
    },
    "cdc_bp": {
        "ko": "CDC High Blood Pressure",
        "en": "CDC High Blood Pressure",
        "url": "https://www.cdc.gov/high-blood-pressure/about/index.html",
    },
    "cdc_diabetes": {
        "ko": "CDC Prediabetes Risk Test",
        "en": "CDC Prediabetes Risk Test",
        "url": "https://www.cdc.gov/prediabetes/risktest/index.html",
    },
    "cdc_resp": {
        "ko": "CDC Respiratory Virus Prevention",
        "en": "CDC Respiratory Virus Prevention",
        "url": "https://www.cdc.gov/respiratory-viruses/prevention/index.html",
    },
    "cdc_vaccines": {
        "ko": "CDC Vaccines and Immunizations",
        "en": "CDC Vaccines and Immunizations",
        "url": "https://www.cdc.gov/vaccines/index.html",
    },
    "fda_food": {
        "ko": "FDA Safe Food Handling",
        "en": "FDA Safe Food Handling",
        "url": "https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling",
    },
    "med_otc": {
        "ko": "MedlinePlus Over-the-Counter Medicines",
        "en": "MedlinePlus Over-the-Counter Medicines",
        "url": "https://medlineplus.gov/overthecountermedicines.html",
    },
    "cdc_antibiotic": {
        "ko": "CDC Antibiotic Use",
        "en": "CDC Antibiotic Use",
        "url": "https://www.cdc.gov/antibiotic-use/index.html",
    },
    "med_back": {
        "ko": "MedlinePlus Back Pain",
        "en": "MedlinePlus Back Pain",
        "url": "https://medlineplus.gov/backpain.html",
    },
    "med_headache": {
        "ko": "MedlinePlus Headache",
        "en": "MedlinePlus Headache",
        "url": "https://medlineplus.gov/headache.html",
    },
    "med_heartburn": {
        "ko": "MedlinePlus Heartburn",
        "en": "MedlinePlus Heartburn",
        "url": "https://medlineplus.gov/heartburn.html",
    },
    "med_stress": {
        "ko": "MedlinePlus Stress",
        "en": "MedlinePlus Stress",
        "url": "https://medlineplus.gov/stress.html",
    },
    "nimh_anxiety": {
        "ko": "NIMH Anxiety Disorders",
        "en": "NIMH Anxiety Disorders",
        "url": "https://www.nimh.nih.gov/health/topics/anxiety-disorders",
    },
    "nimh_depression": {
        "ko": "NIMH Depression",
        "en": "NIMH Depression",
        "url": "https://www.nimh.nih.gov/health/topics/depression",
    },
    "med_dehydration": {
        "ko": "MedlinePlus Dehydration",
        "en": "MedlinePlus Dehydration",
        "url": "https://medlineplus.gov/dehydration.html",
    },
    "med_fever": {
        "ko": "MedlinePlus Fever",
        "en": "MedlinePlus Fever",
        "url": "https://medlineplus.gov/fever.html",
    },
    "med_firstaid": {
        "ko": "MedlinePlus First Aid",
        "en": "MedlinePlus First Aid",
        "url": "https://medlineplus.gov/firstaid.html",
    },
    "cdc_sun": {
        "ko": "CDC Sun Safety",
        "en": "CDC Sun Safety",
        "url": "https://www.cdc.gov/skin-cancer/sun-safety/index.html",
    },
    "cdc_hearing": {
        "ko": "CDC Hearing Loss Prevention",
        "en": "CDC Hearing Loss Prevention",
        "url": "https://www.cdc.gov/hearing-loss/prevention/index.html",
    },
    "cdc_oral": {
        "ko": "CDC Oral Health",
        "en": "CDC Oral Health",
        "url": "https://www.cdc.gov/oral-health/prevention/index.html",
    },
    "cdc_weight": {
        "ko": "CDC Healthy Weight and Growth",
        "en": "CDC Healthy Weight and Growth",
        "url": "https://www.cdc.gov/healthy-weight-growth/index.html",
    },
    "med_allergy": {
        "ko": "MedlinePlus Allergy",
        "en": "MedlinePlus Allergy",
        "url": "https://medlineplus.gov/allergy.html",
    },
    "myhealthfinder": {
        "ko": "ODPHP MyHealthfinder",
        "en": "ODPHP MyHealthfinder",
        "url": "https://odphp.health.gov/myhealthfinder",
    },
    "med_family_history": {
        "ko": "MedlinePlus Family History",
        "en": "MedlinePlus Family History",
        "url": "https://medlineplus.gov/familyhistory.html",
    },
}


TOPICS = [
    {
        "slug": "sleep-routine-adults",
        "ko_title": "성인 수면 루틴 만들기: 잠이 안 올 때 먼저 바꿀 환경과 시간표",
        "en_title": "Adult Sleep Routine: Environment and Timing Before Sleep Hacks",
        "ko_summary": "수면 관리는 특별한 보조제보다 일정한 기상 시간, 빛 노출, 카페인 시간, 침실 환경을 반복해서 조정하는 생활 루틴에서 시작한다.",
        "en_summary": "Sleep management starts with repeatable routines such as wake time, light exposure, caffeine timing, and bedroom environment before special hacks.",
        "ko_focus": "수면 문제는 하루의 마지막 문제가 아니라 하루 전체의 리듬 문제일 때가 많습니다.",
        "en_focus": "Sleep problems often reflect the whole day's rhythm, not only what happens at bedtime.",
        "ko_actions": ["기상 시간을 먼저 고정합니다.", "오후 늦은 카페인과 긴 낮잠을 점검합니다.", "침실의 빛, 소음, 온도를 기록합니다."],
        "en_actions": ["Fix wake time first.", "Review late caffeine and long naps.", "Track bedroom light, noise, and temperature."],
        "ko_signals": ["기상 시간 변동", "오후 카페인", "침실 빛", "낮잠 길이"],
        "signals": ["wake-time drift", "late caffeine", "bedroom light", "nap length"],
        "sources": ["cdc_sleep", "med_stress"],
        "tags": ["Sleep", "Health Habits", "Stress", "Routine"],
    },
    {
        "slug": "walking-activity-start",
        "ko_title": "걷기 운동 시작법: 150분 목표보다 지속 가능한 첫 주 만들기",
        "en_title": "Starting a Walking Plan: Build the First Sustainable Week",
        "ko_summary": "운동은 목표 시간을 크게 잡는 것보다 현재 활동량을 기준으로 작은 걷기 블록을 쌓는 편이 지속 가능하다.",
        "en_summary": "Physical activity is easier to sustain when you build small walking blocks from your current baseline instead of starting with an intimidating target.",
        "ko_focus": "처음부터 완벽한 운동 계획을 세우면 중단도 빨라집니다. 첫 주에는 반복 가능한 시간과 장소가 더 중요합니다.",
        "en_focus": "A perfect plan can fail quickly. In the first week, repeatable time and place matter more than intensity.",
        "ko_actions": ["현재 하루 걸음이나 걷는 시간을 기록합니다.", "점심 후 10분처럼 고정된 블록을 만듭니다.", "통증이나 숨참 정도를 함께 적습니다."],
        "en_actions": ["Record current steps or walking minutes.", "Create a fixed block such as 10 minutes after lunch.", "Track pain and breathlessness as context."],
        "ko_signals": ["현재 활동량", "고정 시간대", "숨참 정도", "통증 변화"],
        "signals": ["current activity level", "fixed time block", "breathlessness", "pain change"],
        "sources": ["cdc_activity", "cdc_weight"],
        "tags": ["Physical Activity", "Walking", "Health Habits", "Weight"],
    },
    {
        "slug": "strength-training-basics",
        "ko_title": "근력운동 초보 기준: 무게보다 자세와 회복을 먼저 보기",
        "en_title": "Strength Training Basics: Form and Recovery Before Heavier Weight",
        "ko_summary": "근력운동은 무거운 무게보다 기본 동작, 통증 없는 범위, 회복일, 점진적 증가를 안전하게 관리하는 것이 먼저다.",
        "en_summary": "Strength training starts with basic movements, pain-free range, recovery days, and gradual progression before heavier weights.",
        "ko_focus": "근력은 나이와 상관없이 일상 기능을 지키는 자산이지만, 무리한 시작은 통증과 중단으로 이어질 수 있습니다.",
        "en_focus": "Strength supports daily function across ages, but overdoing the start can lead to pain and stopping.",
        "ko_actions": ["체중 동작으로 자세를 먼저 배웁니다.", "운동 다음 날 통증과 피로를 기록합니다.", "주당 횟수보다 회복 가능성을 먼저 봅니다."],
        "en_actions": ["Learn form with bodyweight movements first.", "Record next-day soreness and fatigue.", "Prioritize recovery over weekly session count."],
        "ko_signals": ["자세 흔들림", "관절 통증", "회복일 부족", "무게 증가 속도"],
        "signals": ["form breakdown", "joint pain", "limited recovery", "weight progression"],
        "sources": ["cdc_activity", "cdc_weight"],
        "tags": ["Strength Training", "Exercise", "Health Habits", "Recovery"],
    },
    {
        "slug": "healthy-diet-plate",
        "ko_title": "건강한 식단 접시 구성: 탄수화물 끊기보다 균형을 먼저 보기",
        "en_title": "Healthy Plate Basics: Balance Before Cutting Entire Food Groups",
        "ko_summary": "건강한 식단은 특정 영양소를 악마화하기보다 채소, 통곡물, 단백질, 건강한 지방, 수분을 균형 있게 배치하는 방식에서 시작한다.",
        "en_summary": "A healthy diet starts with balanced vegetables, whole grains, protein, healthy fats, and fluids rather than demonizing one nutrient.",
        "ko_focus": "극단적인 식단은 짧게는 쉬워 보여도 사회생활과 장기 유지에서 무너질 수 있습니다.",
        "en_focus": "Extreme diets can look simple at first but often fail under social and long-term routines.",
        "ko_actions": ["매 끼니에 채소와 단백질 자리를 먼저 둡니다.", "정제 곡물과 통곡물 비중을 비교합니다.", "음료와 간식까지 하루 전체로 봅니다."],
        "en_actions": ["Give vegetables and protein a visible place first.", "Compare refined and whole-grain choices.", "Include drinks and snacks in the full-day view."],
        "ko_signals": ["채소 부족", "단백질 누락", "음료 칼로리", "간식 빈도"],
        "signals": ["low vegetables", "missing protein", "drink calories", "snack frequency"],
        "sources": ["who_diet", "cdc_weight"],
        "tags": ["Nutrition", "Healthy Diet", "Weight", "Health Habits"],
    },
    {
        "slug": "sodium-label-reading",
        "ko_title": "나트륨 표시 읽기: 짠맛보다 하루 총량을 먼저 보기",
        "en_title": "Reading Sodium Labels: Daily Total Before Salty Taste",
        "ko_summary": "나트륨은 짠맛이 강한 음식에만 있는 것이 아니라 빵, 소스, 가공식품처럼 자주 먹는 음식에서 누적될 수 있다.",
        "en_summary": "Sodium does not come only from obviously salty foods; it can accumulate through bread, sauces, and processed foods eaten often.",
        "ko_focus": "한 번의 외식보다 매일 반복되는 소스와 가공식품이 총량을 키울 수 있습니다.",
        "en_focus": "Daily sauces and processed foods can matter more than one occasional restaurant meal.",
        "ko_actions": ["영양성분표의 1회 제공량을 먼저 확인합니다.", "소스와 국물 섭취 빈도를 기록합니다.", "비슷한 제품끼리 나트륨 함량을 비교합니다."],
        "en_actions": ["Check serving size before the sodium number.", "Track sauce and broth frequency.", "Compare sodium across similar products."],
        "ko_signals": ["1회 제공량", "소스 사용량", "가공식품 빈도", "국물 섭취"],
        "signals": ["serving size", "sauce amount", "processed food frequency", "broth intake"],
        "sources": ["who_diet", "cdc_bp"],
        "tags": ["Nutrition", "Sodium", "Blood Pressure", "Food Labels"],
    },
    {
        "slug": "added-sugar-drinks",
        "ko_title": "당류 음료 줄이기: 간식보다 먼저 컵 안의 당을 보기",
        "en_title": "Reducing Sugary Drinks: Check the Cup Before the Snack",
        "ko_summary": "당류 섭취는 디저트뿐 아니라 커피음료, 주스, 탄산음료, 에너지음료에서 빠르게 늘어날 수 있다.",
        "en_summary": "Added sugars can rise quickly through coffee drinks, juice, soda, and energy drinks, not only desserts.",
        "ko_focus": "음료는 씹지 않기 때문에 섭취량을 과소평가하기 쉽습니다. 먼저 자주 마시는 컵을 바꾸는 편이 현실적입니다.",
        "en_focus": "Drinks are easy to underestimate because they do not feel like food. Start with the cup you repeat most often.",
        "ko_actions": ["하루 음료 목록을 적습니다.", "무가당, 작은 사이즈, 물 대체 중 하나를 고릅니다.", "피로해서 마시는 음료와 습관으로 마시는 음료를 구분합니다."],
        "en_actions": ["List daily drinks.", "Choose unsweetened, smaller size, or water replacement.", "Separate fatigue drinks from habit drinks."],
        "ko_signals": ["달달한 커피", "주스", "에너지음료", "야식 음료"],
        "signals": ["sweet coffee", "juice", "energy drinks", "late-night drinks"],
        "sources": ["who_diet", "cdc_weight"],
        "tags": ["Nutrition", "Sugar", "Weight", "Health Habits"],
    },
    {
        "slug": "hydration-dehydration-signs",
        "ko_title": "수분 부족 신호 읽기: 갈증보다 소변색과 상황을 같이 보기",
        "en_title": "Hydration and Dehydration Signs: Context Beyond Thirst",
        "ko_summary": "수분 관리는 물을 많이 마시는 경쟁이 아니라 더위, 운동, 질병, 소변색, 어지러움 같은 상황 신호를 함께 보는 일이다.",
        "en_summary": "Hydration is not a contest to drink the most water; it is reading heat, activity, illness, urine color, dizziness, and context together.",
        "ko_focus": "갈증은 유용한 신호지만 운동, 더위, 고령, 질병 상황에서는 늦게 느껴질 수 있습니다.",
        "en_focus": "Thirst is useful, but it may be delayed during heat, exercise, older age, or illness.",
        "ko_actions": ["더운 날과 운동일에는 수분 계획을 미리 둡니다.", "소변색, 어지러움, 입마름을 함께 봅니다.", "질병 중 구토·설사가 있으면 의료진 안내를 확인합니다."],
        "en_actions": ["Plan fluids before heat and exercise.", "Read urine color, dizziness, and dry mouth together.", "Seek medical guidance when illness includes vomiting or diarrhea."],
        "ko_signals": ["진한 소변", "입마름", "어지러움", "구토·설사"],
        "signals": ["dark urine", "dry mouth", "dizziness", "vomiting or diarrhea"],
        "sources": ["med_dehydration", "cdc_activity"],
        "tags": ["Hydration", "Dehydration", "Heat", "Health Habits"],
    },
    {
        "slug": "heat-illness-prevention",
        "ko_title": "폭염 건강 루틴: 물, 그늘, 휴식, 취약시간을 한 번에 보기",
        "en_title": "Heat Illness Prevention: Water, Shade, Rest, and Timing Together",
        "ko_summary": "폭염 대응은 물만 마시는 문제가 아니라 활동 시간, 그늘, 휴식, 의복, 기존 질환, 고령자 돌봄을 함께 조정하는 일이다.",
        "en_summary": "Heat safety requires activity timing, shade, rest, clothing, existing conditions, and care for vulnerable people, not only drinking water.",
        "ko_focus": "더위는 천천히 누적되므로 괜찮다고 느낄 때 미리 줄이는 편이 안전합니다.",
        "en_focus": "Heat stress can build gradually, so adjusting before you feel unwell is safer.",
        "ko_actions": ["가장 더운 시간대의 야외활동을 줄입니다.", "휴식 간격과 그늘 위치를 정합니다.", "혼자 사는 가족이나 이웃의 안부를 확인합니다."],
        "en_actions": ["Reduce outdoor activity during the hottest hours.", "Set rest intervals and shade locations.", "Check on family or neighbors living alone."],
        "ko_signals": ["폭염특보", "어지러움", "과도한 땀", "혼자 있는 고령자"],
        "signals": ["heat alert", "dizziness", "heavy sweating", "older adult alone"],
        "sources": ["med_dehydration", "cdc_sun"],
        "tags": ["Heat Safety", "Hydration", "Public Health", "Family Care"],
    },
    {
        "slug": "blood-pressure-home-check",
        "ko_title": "가정 혈압 측정 루틴: 한 번의 숫자보다 기록 패턴 보기",
        "en_title": "Home Blood Pressure Checks: Look for Patterns, Not One Number",
        "ko_summary": "혈압은 한 번의 측정보다 올바른 자세, 같은 시간대, 반복 기록, 의료진과의 공유가 더 중요한 생활 지표다.",
        "en_summary": "Blood pressure is more useful as a repeated record with proper position, consistent timing, and clinician review than as one isolated reading.",
        "ko_focus": "높거나 낮은 한 번의 숫자에만 반응하면 불안이 커질 수 있습니다. 측정 조건과 반복 패턴을 같이 봐야 합니다.",
        "en_focus": "Reacting to one high or low number can increase anxiety. Measurement conditions and repeated patterns matter.",
        "ko_actions": ["측정 전 휴식과 자세를 일정하게 둡니다.", "아침·저녁 같은 시간대를 정합니다.", "증상이나 약 복용 변화를 같이 기록합니다."],
        "en_actions": ["Keep rest and position consistent before measuring.", "Use repeatable morning and evening windows.", "Record symptoms or medication changes with readings."],
        "ko_signals": ["측정 자세", "시간대", "반복 패턴", "동반 증상"],
        "signals": ["measurement position", "time of day", "repeated pattern", "symptoms"],
        "sources": ["cdc_bp", "myhealthfinder"],
        "tags": ["Blood Pressure", "Heart Health", "Health Tracking", "Prevention"],
    },
    {
        "slug": "prediabetes-risk-screen",
        "ko_title": "당뇨병 전단계 위험 읽기: 체중보다 가족력과 검사 주기까지 보기",
        "en_title": "Prediabetes Risk: Look Beyond Weight to Family History and Screening",
        "ko_summary": "당뇨병 전단계 위험은 체중만으로 판단하기 어렵고 가족력, 활동량, 혈압, 나이, 검사 결과를 함께 봐야 한다.",
        "en_summary": "Prediabetes risk cannot be read from weight alone; family history, activity, blood pressure, age, and test results all matter.",
        "ko_focus": "증상이 없다는 이유로 위험이 없는 것은 아닙니다. 검사와 생활습관 기록이 조기 대응의 출발점입니다.",
        "en_focus": "No symptoms does not always mean no risk. Screening and habit tracking are the starting point for early action.",
        "ko_actions": ["가족력과 최근 검사 결과를 모읍니다.", "활동량과 식사 패턴을 2주 기록합니다.", "검사 주기는 의료진과 상의합니다."],
        "en_actions": ["Collect family history and recent test results.", "Track activity and eating patterns for two weeks.", "Discuss screening interval with a clinician."],
        "ko_signals": ["가족력", "활동 부족", "혈압", "검사 결과"],
        "signals": ["family history", "low activity", "blood pressure", "test results"],
        "sources": ["cdc_diabetes", "cdc_activity", "who_diet"],
        "tags": ["Prediabetes", "Diabetes", "Prevention", "Health Tracking"],
    },
    {
        "slug": "respiratory-virus-prevention",
        "ko_title": "호흡기 바이러스 예방 루틴: 손씻기, 환기, 마스크, 휴식 판단",
        "en_title": "Respiratory Virus Prevention: Hands, Air, Masks, and Staying Home",
        "ko_summary": "호흡기 감염 예방은 한 가지 방법이 아니라 손위생, 환기, 증상 시 휴식, 마스크, 백신 같은 여러 층을 상황에 맞게 조합하는 일이다.",
        "en_summary": "Respiratory virus prevention is layered: hand hygiene, ventilation, staying home when sick, masks, and vaccines depending on context.",
        "ko_focus": "증상이 가벼워도 주변 사람에게는 위험할 수 있습니다. 개인 편의와 공동체 보호를 함께 봐야 합니다.",
        "en_focus": "Even mild symptoms can matter for others. Personal convenience and community protection need to be weighed together.",
        "ko_actions": ["증상이 있으면 일정과 접촉을 줄입니다.", "실내 환기와 손위생을 습관화합니다.", "고위험군을 만날 때는 예방층을 더합니다."],
        "en_actions": ["Reduce contacts and plans when symptomatic.", "Make ventilation and hand hygiene routine.", "Add layers when meeting higher-risk people."],
        "ko_signals": ["기침·발열", "실내 밀집", "고위험군 접촉", "환기 부족"],
        "signals": ["cough or fever", "crowded indoor setting", "higher-risk contact", "poor ventilation"],
        "sources": ["cdc_resp", "cdc_vaccines"],
        "tags": ["Respiratory Viruses", "Prevention", "Public Health", "Vaccines"],
    },
    {
        "slug": "vaccination-record-review",
        "ko_title": "성인 예방접종 기록 점검: 기억보다 기록과 일정표를 믿기",
        "en_title": "Adult Vaccination Record Review: Use Records, Not Memory",
        "ko_summary": "성인 예방접종은 어릴 때 맞은 기억만으로 충분하지 않으며 나이, 직업, 여행, 질환, 임신 여부에 따라 필요한 접종이 달라질 수 있다.",
        "en_summary": "Adult vaccination needs can change with age, work, travel, medical conditions, and pregnancy; memory alone is not enough.",
        "ko_focus": "예방접종은 개인 선택만이 아니라 가족과 공동체의 감염 위험을 함께 줄이는 도구입니다.",
        "en_focus": "Vaccination is both personal protection and a way to reduce risk for family and community.",
        "ko_actions": ["접종 기록을 한 곳에 모읍니다.", "나이와 상황별 권장 일정을 확인합니다.", "기저질환이나 임신 가능성은 의료진에게 알립니다."],
        "en_actions": ["Gather vaccination records in one place.", "Check recommendations by age and situation.", "Tell clinicians about medical conditions or pregnancy possibility."],
        "ko_signals": ["접종 기록 공백", "여행 계획", "직업 노출", "기저질환"],
        "signals": ["record gap", "travel plan", "work exposure", "medical condition"],
        "sources": ["cdc_vaccines", "myhealthfinder"],
        "tags": ["Vaccines", "Prevention", "Health Records", "Public Health"],
    },
    {
        "slug": "food-safety-four-steps",
        "ko_title": "식중독 예방 4단계: 손, 분리, 조리온도, 냉장 시간을 지키기",
        "en_title": "Four Food Safety Steps: Clean, Separate, Cook, and Chill",
        "ko_summary": "식중독 예방은 좋은 재료보다 손 씻기, 교차오염 방지, 충분한 가열, 적절한 냉장 시간을 반복하는 과정에 달려 있다.",
        "en_summary": "Food safety depends on repeated habits: cleaning, preventing cross-contamination, cooking thoroughly, and chilling properly.",
        "ko_focus": "냄새와 맛만으로 안전을 판단하기 어렵습니다. 조리 과정과 보관 시간이 더 신뢰할 만한 기준입니다.",
        "en_focus": "Smell and taste are not reliable safety tests. Process and storage time are better controls.",
        "ko_actions": ["생고기와 채소 도마를 분리합니다.", "조리 후 실온 방치 시간을 줄입니다.", "남은 음식은 날짜를 표시해 보관합니다."],
        "en_actions": ["Separate cutting boards for raw meat and produce.", "Limit room-temperature time after cooking.", "Label leftovers with dates."],
        "ko_signals": ["교차오염", "실온 방치", "덜 익힌 음식", "오래된 남은 음식"],
        "signals": ["cross-contamination", "room-temperature storage", "undercooking", "old leftovers"],
        "sources": ["fda_food", "med_firstaid"],
        "tags": ["Food Safety", "Prevention", "Home Health", "Public Health"],
    },
    {
        "slug": "otc-medicine-label",
        "ko_title": "일반의약품 라벨 읽기: 같은 성분 중복 복용을 피하는 법",
        "en_title": "Reading OTC Medicine Labels: Avoiding Duplicate Ingredients",
        "ko_summary": "일반의약품은 쉽게 살 수 있지만 같은 성분 중복, 복용 간격, 기존 질환, 다른 약과의 상호작용을 확인해야 안전하다.",
        "en_summary": "Over-the-counter medicines are accessible, but safety still requires checking duplicate ingredients, timing, conditions, and interactions.",
        "ko_focus": "감기약, 진통제, 알레르기약은 서로 다른 제품처럼 보여도 성분이 겹칠 수 있습니다.",
        "en_focus": "Cold medicines, pain relievers, and allergy products can look different while sharing ingredients.",
        "ko_actions": ["제품명보다 유효성분을 먼저 봅니다.", "같은 성분이 든 다른 약을 함께 먹는지 확인합니다.", "임신, 만성질환, 다른 처방약이 있으면 전문가에게 확인합니다."],
        "en_actions": ["Read active ingredients before brand names.", "Check whether another medicine contains the same ingredient.", "Ask a professional when pregnant, chronically ill, or taking prescriptions."],
        "ko_signals": ["유효성분 중복", "복용 간격", "졸림 경고", "기존 처방약"],
        "signals": ["duplicate active ingredient", "dose timing", "drowsiness warning", "existing prescription"],
        "sources": ["med_otc", "myhealthfinder"],
        "tags": ["Medicine Safety", "OTC", "Health Literacy", "Prevention"],
    },
    {
        "slug": "antibiotics-when-not-needed",
        "ko_title": "항생제가 필요하지 않을 때: 감기와 바이러스 감염을 구분해 묻기",
        "en_title": "When Antibiotics Are Not Needed: Asking Better Questions About Viral Illness",
        "ko_summary": "항생제는 세균 감염 치료에 쓰이는 약이며 감기 같은 바이러스 감염에는 도움이 되지 않을 수 있어 필요한 경우를 의료진과 확인해야 한다.",
        "en_summary": "Antibiotics treat bacterial infections and may not help viral illnesses such as common colds, so the right question is when they are actually needed.",
        "ko_focus": "빨리 낫고 싶은 마음 때문에 항생제를 요구하면 부작용과 내성 문제를 키울 수 있습니다.",
        "en_focus": "Wanting to recover quickly can lead to pressure for antibiotics, but unnecessary use can create side effects and resistance concerns.",
        "ko_actions": ["증상 기간, 발열, 악화 양상을 기록합니다.", "항생제가 필요한 근거를 의료진에게 묻습니다.", "처방받았다면 지시된 방식대로 복용합니다."],
        "en_actions": ["Track duration, fever, and worsening pattern.", "Ask what evidence suggests antibiotics are needed.", "If prescribed, take them as directed."],
        "ko_signals": ["바이러스 의심", "증상 악화", "부작용", "복용 지시"],
        "signals": ["possible viral illness", "worsening symptoms", "side effects", "use instructions"],
        "sources": ["cdc_antibiotic", "med_otc"],
        "tags": ["Antibiotics", "Medicine Safety", "Respiratory Illness", "Health Literacy"],
    },
    {
        "slug": "back-pain-seek-care",
        "ko_title": "허리 통증 기록법: 쉬어도 되는 통증과 확인해야 할 신호",
        "en_title": "Back Pain Tracking: When to Watch and When to Seek Care",
        "ko_summary": "허리 통증은 흔하지만 다리 힘 빠짐, 감각 이상, 배뇨 문제, 외상 후 통증처럼 확인이 필요한 신호를 구분해야 한다.",
        "en_summary": "Back pain is common, but warning signals such as leg weakness, numbness, bladder problems, or pain after injury need careful attention.",
        "ko_focus": "통증 강도만 적으면 원인을 파악하기 어렵습니다. 시작 상황, 움직임, 신경 증상, 일상 제한을 함께 기록해야 합니다.",
        "en_focus": "Pain intensity alone is not enough. Record onset, movement triggers, nerve symptoms, and daily limitation.",
        "ko_actions": ["통증 시작 시점과 계기를 적습니다.", "다리 저림, 힘 빠짐, 배뇨 변화가 있는지 확인합니다.", "악화되거나 신경 증상이 있으면 의료진에게 상담합니다."],
        "en_actions": ["Write when and how pain started.", "Check for leg numbness, weakness, or bladder changes.", "Seek clinical guidance if worsening or nerve symptoms appear."],
        "ko_signals": ["다리 힘 빠짐", "감각 이상", "외상", "배뇨 변화"],
        "signals": ["leg weakness", "numbness", "injury", "bladder change"],
        "sources": ["med_back", "myhealthfinder"],
        "tags": ["Back Pain", "Pain Tracking", "Health Literacy", "Warning Signs"],
    },
    {
        "slug": "headache-migraine-red-flags",
        "ko_title": "두통과 편두통 기록법: 평소와 다른 두통을 구분하기",
        "en_title": "Headache and Migraine Tracking: Spotting What Is Different",
        "ko_summary": "두통은 흔하지만 갑작스럽고 심한 두통, 신경 증상, 발열, 외상 후 두통처럼 평소와 다른 양상은 빠르게 확인해야 한다.",
        "en_summary": "Headaches are common, but sudden severe pain, neurologic symptoms, fever, or headache after injury should be treated differently from a usual pattern.",
        "ko_focus": "반복 두통은 패턴을 보면 관리가 쉬워집니다. 그러나 평소와 다른 두통은 기록보다 확인이 먼저입니다.",
        "en_focus": "Recurring headaches become easier to discuss with patterns, but a different or severe headache needs attention before journaling.",
        "ko_actions": ["시작 시간, 위치, 강도, 동반 증상을 기록합니다.", "수면, 식사, 스트레스, 화면시간을 함께 봅니다.", "갑작스러운 심한 두통이나 신경 증상은 즉시 도움을 구합니다."],
        "en_actions": ["Record start time, location, intensity, and symptoms.", "Track sleep, meals, stress, and screen time.", "Seek urgent help for sudden severe headache or neurologic symptoms."],
        "ko_signals": ["갑작스러운 심한 두통", "시야 이상", "마비·말 어눌함", "발열 동반"],
        "signals": ["sudden severe headache", "vision changes", "weakness or speech trouble", "fever"],
        "sources": ["med_headache", "myhealthfinder"],
        "tags": ["Headache", "Migraine", "Warning Signs", "Health Tracking"],
    },
    {
        "slug": "heartburn-warning-signs",
        "ko_title": "속쓰림과 흉통 구분 질문: 반복되는 불편감을 기록하는 법",
        "en_title": "Heartburn or Chest Pain: Questions for Repeating Discomfort",
        "ko_summary": "속쓰림처럼 느껴지는 불편감도 흉통, 호흡곤란, 식은땀, 팔·턱 통증과 함께 나타나면 즉시 확인해야 한다.",
        "en_summary": "Discomfort that feels like heartburn needs urgent attention if it appears with chest pain, shortness of breath, sweating, or arm or jaw pain.",
        "ko_focus": "소화 문제와 심장 문제는 스스로 구분하기 어려울 수 있으므로 위험 신호를 보수적으로 봐야 합니다.",
        "en_focus": "Digestive and heart-related symptoms can be hard to separate, so warning signs should be handled conservatively.",
        "ko_actions": ["불편감의 위치, 식사와의 관계, 지속 시간을 적습니다.", "흉통·호흡곤란·식은땀 동반 여부를 확인합니다.", "새롭거나 심한 흉부 증상은 응급 도움을 고려합니다."],
        "en_actions": ["Record location, relation to meals, and duration.", "Check for chest pain, shortness of breath, or sweating.", "Consider emergency help for new or severe chest symptoms."],
        "ko_signals": ["흉통", "호흡곤란", "식은땀", "팔·턱 통증"],
        "signals": ["chest pain", "shortness of breath", "sweating", "arm or jaw pain"],
        "sources": ["med_heartburn", "myhealthfinder"],
        "tags": ["Heartburn", "Chest Pain", "Warning Signs", "Health Literacy"],
    },
    {
        "slug": "stress-body-signal",
        "ko_title": "스트레스 신체 신호 읽기: 피로, 수면, 식욕, 통증을 한 장에 보기",
        "en_title": "Reading Body Signals of Stress: Fatigue, Sleep, Appetite, and Pain",
        "ko_summary": "스트레스는 기분만의 문제가 아니라 수면, 식욕, 소화, 통증, 집중력 변화로 나타날 수 있어 신체 신호를 함께 봐야 한다.",
        "en_summary": "Stress is not only a mood issue; it can show up through sleep, appetite, digestion, pain, and concentration changes.",
        "ko_focus": "스트레스를 의지력 문제로만 보면 회복 전략이 늦어집니다. 몸의 신호를 기록하면 부담의 패턴이 보입니다.",
        "en_focus": "Treating stress only as willpower delays recovery. Tracking body signals can reveal patterns of overload.",
        "ko_actions": ["수면, 식욕, 소화, 통증 변화를 일주일 기록합니다.", "스트레스 사건과 신체 반응 사이의 간격을 봅니다.", "일상 기능이 무너지면 도움을 요청합니다."],
        "en_actions": ["Track sleep, appetite, digestion, and pain for a week.", "Look at timing between stressors and body responses.", "Ask for help when daily function starts breaking down."],
        "ko_signals": ["수면 변화", "식욕 변화", "소화 불편", "집중력 저하"],
        "signals": ["sleep change", "appetite change", "digestive discomfort", "low concentration"],
        "sources": ["med_stress", "nimh_anxiety"],
        "tags": ["Stress", "Mental Health", "Health Tracking", "Sleep"],
    },
    {
        "slug": "anxiety-seek-help",
        "ko_title": "불안이 생활을 방해할 때: 걱정과 도움 요청 사이의 기준",
        "en_title": "When Anxiety Disrupts Life: A Practical Threshold for Seeking Help",
        "ko_summary": "불안은 누구나 느끼지만 회피, 수면 문제, 신체 증상, 일상 기능 저하가 지속되면 혼자 버티기보다 도움을 요청해야 한다.",
        "en_summary": "Anxiety is common, but persistent avoidance, sleep problems, physical symptoms, or impaired daily function are reasons to seek support.",
        "ko_focus": "불안의 크기보다 생활이 얼마나 좁아졌는지가 중요한 신호가 될 수 있습니다.",
        "en_focus": "The size of fear matters less than how much life has narrowed around it.",
        "ko_actions": ["피하게 된 장소와 일을 적습니다.", "수면, 식사, 신체 증상을 함께 기록합니다.", "자해 생각이나 안전 문제가 있으면 즉시 도움을 구합니다."],
        "en_actions": ["List places or tasks you started avoiding.", "Track sleep, eating, and physical symptoms together.", "Seek immediate help for self-harm thoughts or safety concerns."],
        "ko_signals": ["회피 증가", "수면 장애", "가슴 두근거림", "일상 기능 저하"],
        "signals": ["increased avoidance", "sleep disruption", "racing heart", "impaired daily function"],
        "sources": ["nimh_anxiety", "med_stress"],
        "tags": ["Anxiety", "Mental Health", "Warning Signs", "Support"],
    },
    {
        "slug": "depression-warning-signs",
        "ko_title": "우울 신호 점검: 기분보다 기능 변화와 안전을 먼저 보기",
        "en_title": "Depression Warning Signs: Function and Safety Before Mood Labels",
        "ko_summary": "우울은 슬픔만이 아니라 흥미 감소, 수면·식욕 변화, 피로, 집중력 저하, 자해 생각처럼 기능과 안전의 변화로 나타날 수 있다.",
        "en_summary": "Depression can show up as loss of interest, sleep or appetite change, fatigue, poor concentration, or thoughts of self-harm, not only sadness.",
        "ko_focus": "감정 이름을 붙이기 어렵더라도 생활 기능이 무너지고 있다면 도움을 요청할 충분한 이유가 됩니다.",
        "en_focus": "Even if the feeling is hard to name, declining function is enough reason to seek help.",
        "ko_actions": ["흥미, 수면, 식욕, 에너지 변화를 기록합니다.", "일·학업·관계에 생긴 영향을 적습니다.", "자해 생각이 있으면 즉시 응급 도움이나 위기 상담을 찾습니다."],
        "en_actions": ["Track interest, sleep, appetite, and energy changes.", "Write the impact on work, school, or relationships.", "Seek urgent crisis support for self-harm thoughts."],
        "ko_signals": ["흥미 감소", "수면·식욕 변화", "집중력 저하", "자해 생각"],
        "signals": ["loss of interest", "sleep or appetite change", "poor concentration", "self-harm thoughts"],
        "sources": ["nimh_depression", "med_stress"],
        "tags": ["Depression", "Mental Health", "Warning Signs", "Support"],
    },
    {
        "slug": "allergy-symptom-tracker",
        "ko_title": "알레르기 증상 기록법: 계절, 음식, 약, 환경을 함께 보기",
        "en_title": "Allergy Symptom Tracking: Season, Food, Medicine, and Environment Together",
        "ko_summary": "알레르기 증상은 계절, 실내 환경, 음식, 약, 반려동물, 야외활동과 연결될 수 있어 패턴 기록이 진료 상담에 도움이 된다.",
        "en_summary": "Allergy symptoms may connect with season, indoor environment, food, medicine, pets, or outdoor activity, so pattern tracking helps conversations with clinicians.",
        "ko_focus": "원인을 추측으로 단정하면 불필요한 제한이 늘어날 수 있습니다. 반복되는 조건을 기록하는 편이 더 안전합니다.",
        "en_focus": "Guessing a cause can lead to unnecessary restrictions. Repeated-condition tracking is safer.",
        "ko_actions": ["증상 시간, 장소, 음식, 약, 날씨를 함께 적습니다.", "호흡곤란이나 전신 반응은 즉시 도움을 구합니다.", "새 약 복용 후 반응은 의료진에게 알립니다."],
        "en_actions": ["Record time, place, food, medicine, and weather together.", "Seek urgent help for breathing difficulty or whole-body reactions.", "Tell clinicians about reactions after new medicines."],
        "ko_signals": ["재채기·가려움", "호흡곤란", "새 음식", "새 약"],
        "signals": ["sneezing or itching", "breathing difficulty", "new food", "new medicine"],
        "sources": ["med_allergy", "med_otc"],
        "tags": ["Allergy", "Symptom Tracking", "Medicine Safety", "Warning Signs"],
    },
    {
        "slug": "sun-safety-uv-routine",
        "ko_title": "자외선 안전 루틴: 선크림만이 아니라 시간과 옷까지 보기",
        "en_title": "Sun Safety Routine: Sunscreen, Timing, Clothing, and Shade",
        "ko_summary": "자외선 관리는 선크림 하나로 끝나지 않으며 야외 시간, 그늘, 모자와 긴 옷, 재도포 습관을 함께 관리해야 한다.",
        "en_summary": "Sun protection is not only sunscreen; it includes timing, shade, hats, protective clothing, and reapplication habits.",
        "ko_focus": "흐린 날에도 자외선 노출이 있을 수 있으므로 날씨 느낌보다 야외 활동 시간과 노출 부위를 봐야 합니다.",
        "en_focus": "Cloudy weather can still involve UV exposure, so outdoor time and exposed skin matter more than how the day feels.",
        "ko_actions": ["야외활동 시간과 그늘 계획을 먼저 정합니다.", "모자, 선글라스, 긴 옷을 함께 준비합니다.", "선크림은 충분한 양과 재도포를 계획합니다."],
        "en_actions": ["Plan outdoor timing and shade first.", "Use hats, sunglasses, and protective clothing.", "Plan enough sunscreen and reapplication."],
        "ko_signals": ["한낮 야외활동", "그늘 부족", "노출 부위", "재도포 누락"],
        "signals": ["midday outdoor time", "limited shade", "exposed skin", "missed reapplication"],
        "sources": ["cdc_sun", "med_dehydration"],
        "tags": ["Sun Safety", "Skin Health", "Prevention", "Outdoor Health"],
    },
    {
        "slug": "hearing-protection-noise",
        "ko_title": "청력 보호 습관: 이어폰 볼륨보다 노출 시간을 함께 보기",
        "en_title": "Hearing Protection Habits: Volume and Exposure Time Together",
        "ko_summary": "청력 손상 위험은 소리 크기뿐 아니라 노출 시간, 휴식, 귀마개 사용, 작업·공연 환경이 함께 결정한다.",
        "en_summary": "Hearing risk depends on loudness, exposure time, rest breaks, hearing protection, and work or concert environments together.",
        "ko_focus": "소음은 불편하다고 느끼는 순간보다 더 일찍 영향을 줄 수 있습니다. 반복 노출을 관리해야 합니다.",
        "en_focus": "Noise can affect hearing before it feels intolerable. Repeated exposure is the issue to manage.",
        "ko_actions": ["이어폰 볼륨과 사용 시간을 함께 줄입니다.", "공연·작업장에서는 귀마개를 준비합니다.", "귀울림이나 먹먹함이 반복되면 확인합니다."],
        "en_actions": ["Reduce both earbud volume and listening time.", "Bring hearing protection to concerts or noisy work.", "Check repeated ringing or muffled hearing."],
        "ko_signals": ["귀울림", "먹먹함", "긴 노출 시간", "귀마개 없음"],
        "signals": ["ringing", "muffled hearing", "long exposure", "no hearing protection"],
        "sources": ["cdc_hearing", "myhealthfinder"],
        "tags": ["Hearing", "Prevention", "Noise", "Health Habits"],
    },
    {
        "slug": "oral-health-daily-routine",
        "ko_title": "성인 구강건강 루틴: 칫솔질, 치실, 당 섭취, 검진을 묶어 보기",
        "en_title": "Adult Oral Health Routine: Brushing, Flossing, Sugar, and Checkups",
        "ko_summary": "구강건강은 양치 횟수만이 아니라 치실, 당 섭취 빈도, 흡연, 정기 검진, 잇몸 출혈 같은 신호를 함께 봐야 한다.",
        "en_summary": "Oral health depends on more than brushing frequency; flossing, sugar frequency, smoking, checkups, and gum bleeding matter too.",
        "ko_focus": "치아 문제는 통증이 생긴 뒤에는 비용과 치료 부담이 커질 수 있어 예방 루틴이 중요합니다.",
        "en_focus": "Dental problems can become costly and harder to treat after pain starts, so preventive routines matter.",
        "ko_actions": ["양치와 치실 사용 시간을 고정합니다.", "단 음료와 간식 빈도를 줄입니다.", "잇몸 출혈이나 통증은 검진에서 공유합니다."],
        "en_actions": ["Set fixed brushing and flossing times.", "Reduce sugary drink and snack frequency.", "Share gum bleeding or pain during checkups."],
        "ko_signals": ["잇몸 출혈", "치통", "단 음료", "검진 공백"],
        "signals": ["gum bleeding", "tooth pain", "sugary drinks", "checkup gap"],
        "sources": ["cdc_oral", "who_diet"],
        "tags": ["Oral Health", "Dental Care", "Prevention", "Nutrition"],
    },
    {
        "slug": "healthy-weight-non-scale",
        "ko_title": "체중 관리의 비체중 지표: 숫자보다 허리, 체력, 수면, 혈압 보기",
        "en_title": "Healthy Weight Beyond the Scale: Waist, Fitness, Sleep, and Blood Pressure",
        "ko_summary": "체중 관리는 체중계 숫자만으로 판단하기보다 허리둘레, 체력, 식사 패턴, 수면, 혈압, 지속 가능한 습관을 함께 봐야 한다.",
        "en_summary": "Weight management should include waist, fitness, eating patterns, sleep, blood pressure, and sustainable habits, not only the scale.",
        "ko_focus": "빠른 감량보다 오래 유지되는 행동 변화가 건강 결과에 더 중요할 수 있습니다.",
        "en_focus": "Long-lasting behavior change can matter more than rapid weight loss.",
        "ko_actions": ["체중 외에 허리, 활동량, 수면을 같이 기록합니다.", "식단 제한보다 반복 가능한 식사 구조를 만듭니다.", "혈압·혈당 등 건강 지표는 의료진과 확인합니다."],
        "en_actions": ["Track waist, activity, and sleep alongside weight.", "Build repeatable meal structure before restriction.", "Review blood pressure or glucose markers with clinicians."],
        "ko_signals": ["허리둘레", "체력 변화", "수면", "혈압"],
        "signals": ["waist size", "fitness change", "sleep", "blood pressure"],
        "sources": ["cdc_weight", "who_diet", "cdc_activity"],
        "tags": ["Healthy Weight", "Prevention", "Nutrition", "Exercise"],
    },
    {
        "slug": "first-aid-emergency-plan",
        "ko_title": "가정 응급상황 계획: 전화번호, 약, 병력, 대피 동선을 한 곳에",
        "en_title": "Home First Aid Plan: Contacts, Medicines, Conditions, and Exit Routes",
        "ko_summary": "응급상황에서는 기억보다 준비된 정보가 중요하므로 가족 연락처, 복용약, 병력, 알레르기, 병원, 대피 동선을 한 곳에 정리해야 한다.",
        "en_summary": "In emergencies, prepared information beats memory: contacts, medicines, conditions, allergies, hospitals, and exit routes should be organized.",
        "ko_focus": "응급상황은 생각보다 빠르게 진행되므로 평소에 말로 정한 계획보다 보이는 문서와 공유 위치가 더 유용합니다.",
        "en_focus": "Emergencies move fast, so visible documents and shared locations are more useful than verbal plans.",
        "ko_actions": ["가족별 약, 알레르기, 병력을 한 장으로 만듭니다.", "응급 연락처와 병원 정보를 휴대폰과 종이에 둡니다.", "심각한 증상이나 안전 문제가 있으면 지역 응급번호로 연락합니다."],
        "en_actions": ["Create a one-page list of medicines, allergies, and conditions.", "Keep emergency contacts in phone and paper form.", "Use local emergency services for serious symptoms or safety threats."],
        "ko_signals": ["의식 저하", "호흡곤란", "심한 출혈", "알레르기 반응"],
        "signals": ["confusion or unconsciousness", "breathing difficulty", "severe bleeding", "allergic reaction"],
        "sources": ["med_firstaid", "med_family_history"],
        "tags": ["First Aid", "Emergency Plan", "Family Health", "Health Records"],
    },
    {
        "slug": "fever-monitoring-basics",
        "ko_title": "열이 날 때 기록할 것: 체온 숫자보다 나이, 증상, 지속시간",
        "en_title": "Fever Monitoring Basics: Age, Symptoms, and Duration Beyond the Number",
        "ko_summary": "열은 체온 숫자 하나보다 나이, 동반 증상, 지속시간, 수분 섭취, 기저질환 여부를 함께 봐야 판단이 안전하다.",
        "en_summary": "Fever should be read with age, symptoms, duration, fluid intake, and underlying conditions, not only one temperature number.",
        "ko_focus": "특히 영유아, 고령자, 면역저하자, 심한 증상이 있는 경우에는 보수적으로 전문가 안내를 확인해야 합니다.",
        "en_focus": "Infants, older adults, immunocompromised people, or severe symptoms require more conservative guidance.",
        "ko_actions": ["체온, 측정 시간, 측정 방법을 기록합니다.", "호흡곤란, 의식 변화, 탈수 신호를 함께 봅니다.", "고위험군이나 심한 증상은 의료진에게 확인합니다."],
        "en_actions": ["Record temperature, time, and measurement method.", "Watch breathing difficulty, confusion, and dehydration signs.", "Seek clinical guidance for high-risk people or severe symptoms."],
        "ko_signals": ["지속 시간", "탈수 신호", "호흡곤란", "고위험군"],
        "signals": ["duration", "dehydration signs", "breathing difficulty", "high-risk person"],
        "sources": ["med_fever", "med_dehydration"],
        "tags": ["Fever", "Symptom Tracking", "Warning Signs", "Family Health"],
    },
    {
        "slug": "doctor-visit-question-list",
        "ko_title": "진료 전 질문 목록 만들기: 증상, 약, 목표를 짧게 정리하기",
        "en_title": "Doctor Visit Question List: Symptoms, Medicines, and Goals in One Page",
        "ko_summary": "짧은 진료시간을 잘 쓰려면 증상 시작일, 악화·완화 요인, 복용약, 알레르기, 가장 궁금한 질문을 미리 정리해야 한다.",
        "en_summary": "A short medical visit works better when symptom timeline, triggers, medicines, allergies, and top questions are prepared in advance.",
        "ko_focus": "진료실에서는 긴장해서 중요한 정보를 빠뜨리기 쉽습니다. 한 장 메모가 대화의 질을 높입니다.",
        "en_focus": "People often forget key details under appointment stress. A one-page note improves the conversation.",
        "ko_actions": ["증상 시작일과 변화 흐름을 적습니다.", "복용약, 영양제, 알레르기를 목록화합니다.", "이번 진료에서 꼭 결정할 질문 3개를 정합니다."],
        "en_actions": ["Write symptom start date and change over time.", "List medicines, supplements, and allergies.", "Choose three questions to answer during the visit."],
        "ko_signals": ["증상 타임라인", "복용약 목록", "검사 결과", "질문 우선순위"],
        "signals": ["symptom timeline", "medicine list", "test results", "question priority"],
        "sources": ["myhealthfinder", "med_family_history"],
        "tags": ["Doctor Visit", "Health Records", "Health Literacy", "Prevention"],
    },
    {
        "slug": "family-health-records",
        "ko_title": "가족 건강기록 정리: 병력, 약, 알레르기, 접종 기록을 찾기 쉽게",
        "en_title": "Family Health Records: Conditions, Medicines, Allergies, and Vaccines",
        "ko_summary": "가족 건강기록은 응급상황과 진료 준비에 도움이 되며 병력, 복용약, 알레르기, 접종 기록, 가족력을 찾기 쉽게 정리해야 한다.",
        "en_summary": "Family health records help emergencies and appointments when conditions, medicines, allergies, vaccinations, and family history are easy to find.",
        "ko_focus": "기록은 완벽할 필요가 없습니다. 찾을 수 있는 위치와 최신 업데이트 날짜가 더 중요합니다.",
        "en_focus": "The record does not need to be perfect. Location and last updated date matter most.",
        "ko_actions": ["가족별 병력, 약, 알레르기를 한 장으로 만듭니다.", "접종 기록과 검사 결과 위치를 표시합니다.", "변경이 있을 때 업데이트 날짜를 남깁니다."],
        "en_actions": ["Create one page for each person's conditions, medicines, and allergies.", "Mark where vaccine and test records are stored.", "Add an update date whenever something changes."],
        "ko_signals": ["복용약 변경", "새 알레르기", "접종 기록", "가족력"],
        "signals": ["medicine change", "new allergy", "vaccine record", "family history"],
        "sources": ["med_family_history", "cdc_vaccines", "myhealthfinder"],
        "tags": ["Health Records", "Family Health", "Vaccines", "Prevention"],
    },
]


def escape_svg_text(value: str) -> str:
    return html.escape(value, quote=True)


def write_svg(path: Path, title: str, subtitle: str, labels: list[str], palette: tuple[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    label_lines = "\n".join(
        f'<text x="86" y="{326 + index * 40}" fill="#f0fdf4" font-size="23" font-family="Avenir, Verdana, sans-serif">{escape_svg_text(label)}</text>'
        for index, label in enumerate(labels[:5])
    )
    pulses = "\n".join(
        f'<circle cx="{745 + index * 78}" cy="{220 + (index % 2) * 70}" r="{30 + index * 2}" fill="#bbf7d0" fill-opacity="{0.18 + index * 0.04:.2f}"/>'
        for index in range(5)
    )
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675" role="img" aria-labelledby="title desc">
  <title id="title">{escape_svg_text(title)}</title>
  <desc id="desc">{escape_svg_text(subtitle)}</desc>
  <defs>
    <linearGradient id="bg" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="{palette[0]}"/>
      <stop offset="100%" stop-color="{palette[1]}"/>
    </linearGradient>
    <pattern id="grid" width="54" height="54" patternUnits="userSpaceOnUse">
      <path d="M54 0 L0 0 0 54" fill="none" stroke="#ffffff" stroke-opacity="0.08" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="1200" height="675" fill="url(#bg)"/>
  <rect width="1200" height="675" fill="url(#grid)"/>
  <path d="M70 455 H252 L304 360 L374 555 L455 235 L530 455 H1130" fill="none" stroke="#fef9c3" stroke-width="10" stroke-linejoin="round" stroke-linecap="round" opacity="0.88"/>
  {pulses}
  <rect x="62" y="276" width="580" height="268" rx="30" fill="#052e2b" fill-opacity="0.58" stroke="#ffffff" stroke-opacity="0.18"/>
  <text x="72" y="108" fill="#f8fafc" font-size="45" font-family="Avenir, Verdana, sans-serif" font-weight="700">{escape_svg_text(title)}</text>
  <text x="76" y="160" fill="#dcfce7" font-size="25" font-family="Avenir, Verdana, sans-serif">{escape_svg_text(subtitle)}</text>
  {label_lines}
  <text x="76" y="610" fill="#bbf7d0" font-size="22" font-family="Avenir, Verdana, sans-serif">MouseBall54 Health Literacy Guide</text>
</svg>
"""
    path.write_text(svg, encoding="utf-8")


def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {item}" for item in items)


def normalize_markdown(text: str) -> str:
    normalized = "\n".join(line[4:] if line.startswith("    ") else line for line in text.splitlines()).lstrip()
    return normalized.replace("sidebar:\nnav:", "sidebar:\n    nav:") + "\n"


def source_notes(source_keys: list[str], lang: str) -> str:
    return "\n".join(f"- [{SOURCES[key][lang]}]({SOURCES[key]['url']})" for key in source_keys)


def related_links(index: int, lang: str) -> str:
    related = [TOPICS[(index + 1) % len(TOPICS)], TOPICS[(index + 12) % len(TOPICS)]]
    category_path = KO_CATEGORY.lower() if lang == "ko" else EN_CATEGORY.lower()
    if lang == "ko":
        return "\n".join(f"- [{topic['ko_title']}](/{{category}}/{topic['slug']}/)".replace("{category}", category_path) for topic in related)
    return "\n".join(f"- [{topic['en_title']}](/{{category}}/{topic['slug']}/)".replace("{category}", category_path) for topic in related)


def ko_post(topic: dict[str, object], index: int) -> str:
    slug = str(topic["slug"])
    image_dir = f"/images/{POST_DATE}-{slug}"
    signals = "\n".join(f"- **{signal}**: 이 신호가 보이면 기록하고, 악화되거나 안전 문제가 있으면 전문가에게 확인합니다." for signal in topic["ko_signals"])
    actions = "\n".join(f"- {action}" for action in topic["ko_actions"])
    checklist = "\n".join(f"- {action.replace('합니다.', '했는지 확인합니다.')}" for action in topic["ko_actions"])
    return dedent(f"""\
    ---
    layout: single
    title: >
      {topic["ko_title"]}
    seo_title: >
      {topic["ko_title"]}
    date: {POST_DATE}T{8 + index // 3:02d}:{(index % 3) * 20:02d}:00+09:00
    last_modified_at: {LAST_MODIFIED_AT}
    lang: ko
    translation_id: health-literacy-{slug}
    header:
      teaser: {image_dir}/hero.svg
      overlay_image: {image_dir}/hero.svg
      overlay_filter: 0.45
      image_description: >
        건강 리터러시 주제의 핵심 신호와 점검 순서를 요약한 교육용 이미지입니다.
    excerpt: >
      {topic["ko_summary"]}
    seo_description: >
      {topic["ko_summary"]}
    categories:
      - {KO_CATEGORY}
    tags:
    {yaml_list(topic["tags"])}
    ---

    건강 리터러시는 스스로 진단하는 기술이 아니라 **언제 기록하고, 언제 쉬고, 언제 전문가에게 확인해야 하는지**를 구분하는 능력입니다.

    {topic["ko_summary"]}

    이 글은 교육용 정보이며 진단이나 치료 지시가 아닙니다. 심한 증상, 갑작스러운 악화, 호흡곤란, 흉통, 의식 변화, 자해 생각처럼 안전 문제가 있으면 지역 응급번호나 의료기관에 즉시 도움을 요청해야 합니다.

    ![{topic["ko_title"]} 핵심 건강 흐름]({image_dir}/hero.svg)

    ## 왜 중요한가

    {topic["ko_focus"]}

    건강 정보는 많지만 실제 생활에서는 어떤 정보를 먼저 봐야 할지 헷갈리기 쉽습니다. 검색 결과를 따라가기보다 증상, 기간, 생활패턴, 위험 신호를 같은 형식으로 기록하면 의료진과 대화하기도 쉬워집니다.

    핵심은 **한 번의 숫자보다 패턴**, **느낌보다 기능 변화**, **참는 것보다 안전 신호 확인**입니다. 일상 루틴은 가볍게 시작하되, 경고 신호는 보수적으로 다뤄야 합니다.

    ## 먼저 볼 신호

    {signals}

    신호는 혼자 해석하지 않는 편이 좋습니다. 같은 증상도 나이, 임신 여부, 기저질환, 복용약, 최근 감염, 외상 여부에 따라 의미가 달라질 수 있습니다.

    ![{topic["ko_title"]} 점검 체크리스트]({image_dir}/checklist.svg)

    ## 생활 속 실행 순서

    {actions}

    바꾸려는 습관은 작게 시작하세요. 건강 루틴은 강한 결심보다 반복 가능한 시간, 장소, 기록 방식이 오래갑니다.

    ## 전문가에게 확인할 때

    증상이 새롭거나 빠르게 악화되거나, 일상 기능을 크게 방해하거나, 스스로 안전하다고 판단하기 어렵다면 의료진에게 확인하는 편이 안전합니다.

    진료 전에는 시작 시점, 지속시간, 악화·완화 요인, 동반 증상, 복용 중인 약과 영양제를 적어 두세요. 이 정보가 있으면 짧은 진료시간에도 핵심을 전달하기 쉽습니다.

    ## 월간 점검 체크리스트

    {checklist}
    - 증상이나 습관 변화가 일상 기능에 어떤 영향을 주는지 적습니다.
    - 건강 정보는 적용 지역의 공식 자료와 의료진 안내로 다시 확인합니다.

    ## 참고할 공식 자료

    {source_notes(topic["sources"], "ko")}

    ## 함께 보면 좋은 글

    {related_links(index, "ko")}
    """)


def en_post(topic: dict[str, object], index: int) -> str:
    slug = str(topic["slug"])
    image_dir = f"/images/{POST_DATE}-{slug}"
    signals = "\n".join(f"- **{signal}**: record it, and seek professional guidance if it worsens or raises safety concerns." for signal in topic["signals"])
    actions = "\n".join(f"- {action}" for action in topic["en_actions"])
    checklist = "\n".join(f"- Confirm that you can: {action[0].lower() + action[1:]}" for action in topic["en_actions"])
    return dedent(f"""\
    ---
    layout: single
    title: >
      {topic["en_title"]}
    seo_title: >
      {topic["en_title"]}
    date: {POST_DATE}T{8 + index // 3:02d}:{(index % 3) * 20:02d}:00+09:00
    last_modified_at: {LAST_MODIFIED_AT}
    lang: en
    translation_id: health-literacy-{slug}
    header:
      teaser: {image_dir}/hero.svg
      overlay_image: {image_dir}/hero.svg
      overlay_filter: 0.45
      image_description: >
        An educational health literacy image summarizing core signals and check steps for this topic.
    excerpt: >
      {topic["en_summary"]}
    seo_description: >
      {topic["en_summary"]}
    categories:
      - {EN_CATEGORY}
    tags:
    {yaml_list(topic["tags"])}
    ---

    Health literacy is not self-diagnosis. It is the ability to know **what to track, when to rest, and when to ask a professional**.

    {topic["en_summary"]}

    This article is educational and is not diagnosis or treatment advice. If symptoms are severe, suddenly worse, involve breathing trouble, chest pain, confusion, self-harm thoughts, or any immediate safety concern, contact local emergency services or a medical professional right away.

    ![{topic["en_title"]} core health flow]({image_dir}/hero.svg)

    ## Why It Matters

    {topic["en_focus"]}

    Health information is abundant, but real life often makes it hard to decide what to check first. A consistent record of symptoms, duration, habits, and warning signs helps you avoid guessing and improves conversations with clinicians.

    The useful baseline is **patterns over one number**, **function over vague feeling**, and **safety signals over waiting it out**. Lifestyle routines can start small, but warning signs deserve conservative handling.

    ## Signals To Check First

    {signals}

    Signals should not be interpreted in isolation. Age, pregnancy, existing conditions, medicines, recent infection, and injury can change what the same symptom means.

    ![{topic["en_title"]} checklist]({image_dir}/checklist.svg)

    ## Practical Order

    {actions}

    Start small. Health routines last longer when they have a repeatable time, place, and recording method instead of relying on motivation alone.

    ## When To Ask For Help

    If a symptom is new, rapidly worsening, disrupting daily function, or hard to judge safely, professional guidance is the safer route.

    Before a visit, write the start date, duration, triggers, relieving factors, related symptoms, and all medicines or supplements. That makes short appointments more productive.

    ## Monthly Checkup

    {checklist}
    - Write how symptoms or habits affect daily function.
    - Recheck health information through official local guidance and qualified medical professionals.

    ## Source Notes

    {source_notes(topic["sources"], "en")}

    ## Related Reading

    {related_links(index, "en")}
    """)


def category_page(lang: str) -> str:
    if lang == "ko":
        return dedent("""\
        ---
        title: "Health Literacy"
        layout: archive
        permalink: /ko_health_literacy/
        lang: ko
        seo_description: >
          수면, 운동, 식단, 혈압, 당뇨병 전단계, 호흡기 감염 예방, 약 안전, 통증 기록, 정신건강 신호, 응급 준비를 다루는 교육용 건강 리터러시 글 모음입니다.
        sidebar:
            nav: "sidebar-category"
        ---

        Health Literacy 카테고리는 건강 정보를 스스로 진단하는 도구가 아니라, 증상과 생활습관을 더 안전하게 기록하고 필요한 때 전문가에게 연결하기 위한 교육용 글을 모읍니다. 수면, 걷기, 식단, 수분, 혈압, 예방접종, 약 라벨, 통증, 스트레스, 응급 준비처럼 일상에서 자주 검색하는 주제를 다룹니다.

        모든 글은 CDC, WHO, FDA, NIH MedlinePlus, NIMH, ODPHP 같은 공식 자료를 우선 참고합니다. 특정 치료를 지시하지 않으며, 심한 증상이나 안전 문제가 있으면 지역 응급번호나 의료기관에 즉시 문의해야 한다는 원칙을 반복합니다.

        처음 읽는다면 수면 루틴, 걷기 운동, 건강한 식단 글로 생활기반을 잡고, 그다음 혈압 측정, 예방접종 기록, 진료 전 질문 목록 글로 건강 기록 체계를 만들어 보세요.

        ## 먼저 읽기

        - [성인 수면 루틴 만들기](/ko_health_literacy/sleep-routine-adults/)
        - [걷기 운동 시작법](/ko_health_literacy/walking-activity-start/)
        - [진료 전 질문 목록 만들기](/ko_health_literacy/doctor-visit-question-list/)

        ## 최신 글

        {% assign posts = site.categories["ko_Health_Literacy"] %}
        {% for post in posts %}
          {% include archive-single.html type=page.entries_layout %}
        {% endfor %}
        """)
    return dedent("""\
    ---
    title: "Health Literacy"
    layout: archive
    permalink: /en_health_literacy/
    lang: en
    seo_description: >
      Educational health literacy guides on sleep, activity, nutrition, prevention, medicine safety, symptom tracking, mental health signals, and emergency preparation.
    sidebar:
        nav: "sidebar-category"
    ---

    The Health Literacy category helps readers track symptoms and habits more safely, without turning internet reading into self-diagnosis. It covers practical topics such as sleep, walking, nutrition, hydration, blood pressure, vaccines, medicine labels, pain, stress, and emergency preparation.

    The articles prioritize official sources such as CDC, WHO, FDA, NIH MedlinePlus, NIMH, and ODPHP. They do not provide diagnosis or treatment advice. They repeatedly emphasize that severe symptoms, sudden worsening, or safety concerns require local emergency services or qualified medical care.

    Start with sleep routine, walking, and healthy plate basics to build the lifestyle base. Then use blood pressure checks, vaccine record review, and doctor visit question lists to improve health records and clinical conversations.

    ## Start Here

    - [Adult Sleep Routine](/en_health_literacy/sleep-routine-adults/)
    - [Starting a Walking Plan](/en_health_literacy/walking-activity-start/)
    - [Doctor Visit Question List](/en_health_literacy/doctor-visit-question-list/)

    ## Latest Articles

    {% assign posts = site.categories["en_Health_Literacy"] %}
    {% for post in posts %}
      {% include archive-single.html type=page.entries_layout %}
    {% endfor %}
    """)


def main() -> None:
    palettes = [
        ("#064e3b", "#0f766e"),
        ("#14532d", "#0369a1"),
        ("#0f172a", "#047857"),
        ("#164e63", "#4d7c0f"),
        ("#1e293b", "#15803d"),
    ]

    for index, topic in enumerate(TOPICS):
        slug = str(topic["slug"])
        image_path = ROOT / "images" / f"{POST_DATE}-{slug}"
        palette = palettes[index % len(palettes)]

        (ROOT / "_posts" / "ko" / f"{POST_DATE}-{slug}.md").write_text(
            normalize_markdown(ko_post(topic, index)),
            encoding="utf-8",
        )
        (ROOT / "_posts" / "en" / f"{POST_DATE}-{slug}.md").write_text(
            normalize_markdown(en_post(topic, index)),
            encoding="utf-8",
        )
        write_svg(
            image_path / "hero.svg",
            str(topic["en_title"])[:64],
            "Track patterns, warning signs, and when to ask for help",
            list(topic["signals"]),
            palette,
        )
        write_svg(
            image_path / "checklist.svg",
            "Health Literacy Checklist",
            str(topic["en_title"])[:80],
            list(topic["en_actions"]),
            (palette[1], palette[0]),
        )

    (ROOT / "_pages" / f"category-{KO_CATEGORY}.md").write_text(
        normalize_markdown(category_page("ko")),
        encoding="utf-8",
    )
    (ROOT / "_pages" / f"category-{EN_CATEGORY}.md").write_text(
        normalize_markdown(category_page("en")),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
