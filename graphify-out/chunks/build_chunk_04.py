import json

# ============================================================
# Build nodes and edges for chunk 4 of 6
# ============================================================

# === EXISTING CONCEPT IDs FROM CHUNKS 1-3 (stable) ===
existing_concepts = [
    "concept_moon_phase", "concept_lunar_cycle", "concept_sun_moon_angle",
    "concept_moon_phase_new_moon", "concept_moon_phase_waxing_crescent",
    "concept_moon_phase_first_quarter", "concept_moon_phase_waxing_gibbous",
    "concept_moon_phase_full_moon", "concept_moon_phase_waning_gibbous",
    "concept_moon_phase_last_quarter", "concept_moon_phase_waning_crescent",
    "concept_tithi", "concept_shukla_paksha", "concept_krishna_paksha",
    "concept_nanda_tithi", "concept_bhadra_tithi", "concept_jaya_tithi",
    "concept_rikta_tithi", "concept_purna_tithi", "concept_tithi_archetype",
    "concept_tithi_calculation", "concept_tithi_lord",
    "concept_moon_sign", "concept_moon",
    "concept_sun", "concept_jupiter", "concept_saturn",
    "concept_rahu", "concept_ketu",
    # From chunk 1: houses, signs, planets
    "concept_aries", "concept_taurus", "concept_gemini", "concept_cancer",
    "concept_leo", "concept_virgo", "concept_libra", "concept_scorpio",
    "concept_sagittarius", "concept_capricorn", "concept_aquarius", "concept_pisces",
    "concept_house_1", "concept_house_2", "concept_house_3", "concept_house_4",
    "concept_house_5", "concept_house_6", "concept_house_7", "concept_house_8",
    "concept_house_9", "concept_house_10", "concept_house_11", "concept_house_12",
    "concept_mars", "concept_venus", "concept_mercury",
    "concept_neptune", "concept_uranus", "concept_pluto",
    "concept_ascendant", "concept_midheaven",
    "concept_case_study",
]

# ============================================================
# Document definitions
# ============================================================
docs = [
    {
        "id": "_posts_tithi_moon_sign_moon_house",
        "label": "ดิถีกับ Moon Sign และ Moon House: จังหวะของใจเกิดขึ้นที่ไหนในชีวิต",
        "slug": "2026-05-31-tithi-moon-sign-moon-house",
        "tags": ["astrology", "tithi", "moon-sign", "moon-house", "birth-chart", "interpretation"],
        "order": 62
    },
    {
        "id": "_posts_waxing_waning_moon",
        "label": "ข้างขึ้น–ข้างแรมในดวงกำเนิด: จันทร์กำลังออกไปสร้างโลก หรือกำลังกลับมาทำความเข้าใจโลก",
        "slug": "2026-05-31-waxing-waning-moon",
        "tags": ["astrology", "waxing-moon", "waning-moon", "tithi", "birth-chart", "lunar-cycle"],
        "order": 57
    },
    {
        "id": "_posts_full_moon_release_by_sign",
        "label": "Full Moon Release by Sign: ปล่อยวางให้ตรงราศีของจันทร์เพ็ญ",
        "slug": "2026-06-01-full-moon-release-by-sign",
        "tags": ["astrology", "full-moon", "manifestation", "release", "letting-go", "moon-sign"],
        "order": 66
    },
    {
        "id": "_posts_how_to_manifest_with_moon_phase",
        "label": "How to Manifest with Moon Phase: ใช้จังหวะข้างขึ้น–ข้างแรมเพื่อออกแบบชีวิต",
        "slug": "2026-06-01-how-to-manifest-with-moon-phase",
        "tags": ["astrology", "moon-phase", "manifestation", "new-moon", "full-moon", "intention-setting"],
        "order": 63
    },
    {
        "id": "_posts_manifest_with_moon_sign",
        "label": "เพิ่มพลัง Manifest ด้วย Moon Sign: เมื่อ Moon Phase บอกจังหวะเวลา และ Moon Sign บอกคุณภาพของพลังงาน",
        "slug": "2026-06-01-manifest-with-moon-sign",
        "tags": ["astrology", "moon-sign", "moon-phase", "manifestation", "intention-setting", "ritual"],
        "order": 64
    },
    {
        "id": "_posts_moon_journal_prompts_by_phase_and_house",
        "label": "Moon Journal Prompts for Every Phase and House: คำถามเขียนบันทึกตามเฟสจันทร์และเรือนในดวงกำเนิด",
        "slug": "2026-06-01-moon-journal-prompts-by-phase-and-house",
        "tags": ["moon-journal", "moon-phase", "moon-house", "writing-prompts", "self-reflection", "manifestation"],
        "order": 70
    },
    {
        "id": "_posts_moon_manifestation_by_house",
        "label": "Moon Manifestation by House: เมื่อดวงจันทร์บอกว่าพื้นที่ชีวิตด้านใดกำลังถูกเปิดใช้งาน",
        "slug": "2026-06-01-moon-manifestation-by-house",
        "tags": ["moon-house", "moon-sign", "moon-phase", "manifestation", "astrology"],
        "order": 69
    },
    {
        "id": "_posts_new_moon_manifestation_by_sign",
        "label": "New Moon Manifestation by Sign: ตั้งเจตนาใหม่ให้ตรงราศีของจันทร์ดับ",
        "slug": "2026-06-01-new-moon-manifestation-by-sign",
        "tags": ["astrology", "new-moon", "manifestation", "moon-sign", "intention-setting", "ritual"],
        "order": 65
    },
    {
        "id": "_posts_waning_moon_release_by_sign",
        "label": "Waning Moon Release by Sign: ข้างแรมคือช่วงลด เคลียร์ ปรับ และเตรียมเริ่มใหม่",
        "slug": "2026-06-01-waning-moon-release-by-sign",
        "tags": ["waning-moon", "moon-phase", "release", "letting-go", "moon-sign"],
        "order": 68
    },
    {
        "id": "_posts_waxing_moon_action_by_sign",
        "label": "Waxing Moon Action by Sign: หลังตั้งเจตนาแล้ว ควรลงมือทำอย่างไรตามราศีจันทร์",
        "slug": "2026-06-01-waxing-moon-action-by-sign",
        "tags": ["waxing-moon", "moon-phase", "action", "manifestation", "moon-sign"],
        "order": 67
    },
    {
        "id": "_posts_beyond_the_moon",
        "label": "Beyond the Moon: วางแผนชีวิตระยะยาวด้วย Moon Cycle, Solar Return และ Annual Profection",
        "slug": "2026-06-06-beyond-the-moon",
        "tags": ["moon", "solar-return", "annual-profection", "planning", "long-term", "manifestation"],
        "order": 74
    },
    {
        "id": "_posts_moon_manifestation_calendar",
        "label": "Moon Manifestation Calendar: วิธีวางแผนชีวิตรายเดือนด้วย New Moon, Full Moon และ Moon House",
        "slug": "2026-06-06-moon-manifestation-calendar",
        "tags": ["moon", "calendar", "planning", "new-moon", "full-moon", "monthly", "manifestation"],
        "order": 73
    },
    {
        "id": "_posts_moon_manifestation_worksheet_examples",
        "label": "ตัวอย่างการใช้ Moon Manifestation Worksheet",
        "slug": "2026-06-06-moon-manifestation-worksheet-examples",
        "tags": ["moon", "worksheet", "examples", "new-moon", "full-moon", "house", "manifestation"],
        "order": 72
    },
    {
        "id": "_posts_moon_manifestation_worksheet",
        "label": "Moon Manifestation Worksheet",
        "slug": "2026-06-06-moon-manifestation-worksheet",
        "tags": ["moon", "worksheet", "manifestation", "journal", "new-moon", "full-moon"],
        "order": 71
    },
    {
        "id": "_posts_annual_profection_for_beginners",
        "label": "Annual Profection for Beginners: วิธีหาเรือนประจำปีและ Lord of the Year เพื่อวางแผนชีวิตตามจังหวะอายุ",
        "slug": "2026-06-10-annual-profection-for-beginners",
        "tags": ["annual-profection", "lord-of-the-year", "planning", "yearly-theme", "beginner"],
        "order": 75
    },
    {
        "id": "_posts_lord_of_the_year",
        "label": "Lord of the Year: ดาวเจ้าปีบอกวิธีใช้พลังของปีอย่างไร",
        "slug": "2026-06-10-lord-of-the-year",
        "tags": ["lord-of-the-year", "annual-profection", "yearly-theme", "planning", "time-lord"],
        "order": 76
    },
    {
        "id": "_posts_solar_return_for_life_planning",
        "label": "Solar Return for Life Planning: อ่านดวงวันเกิดประจำปีเพื่อวางธีมชีวิต",
        "slug": "2026-06-10-solar-return-for-life-planning",
        "tags": ["solar-return", "annual-profection", "yearly-theme", "planning", "life-planning"],
        "order": 77
    },
    {
        "id": "_posts_astrological_life_planning_system",
        "label": "Astrological Life Planning System: รวมทุกเครื่องมือให้เป็นระบบเดียว",
        "slug": "2026-06-14-astrological-life-planning-system",
        "tags": ["Astrology Life Planning", "Nodes", "Progressed Moon", "Solar Return", "Annual Profection", "Moon Cycle", "Jupiter", "Saturn", "Eclipses"],
        "order": 85
    },
    {
        "id": "_posts_astrology_planner_case_study_1",
        "label": "Astrology Planner Case Study 1: One Year Life Planning",
        "slug": "2026-06-14-astrology-planner-case-study-1",
        "tags": ["Astrology", "Case Study", "Life Planning", "Annual Profection", "Solar Return", "Nodes", "Mercury", "Moon Cycle"],
        "order": 86
    },
    {
        "id": "_posts_astrology_planner_case_study_2",
        "label": "Astrology Planner Case Study 2: A Year of Transition",
        "slug": "2026-06-14-astrology-planner-case-study-2",
        "tags": ["Astrology", "Case Study", "Life Planning", "Nodes", "Annual Profection", "Mercury", "Jupiter", "Saturn", "Uranus", "Pluto", "Eclipses"],
        "order": 87
    },
    {
        "id": "_posts_eclipses_life_turning_points",
        "label": "Eclipses and Life Turning Points: ใช้สุริยุปราคา–จันทรุปราคาอ่านจุดเปลี่ยนชีวิตราย 6 เดือน",
        "slug": "2026-06-14-eclipses-life-turning-points",
        "tags": ["Eclipse", "Solar Eclipse", "Lunar Eclipse", "Nodes", "Turning Points", "Life Planning"],
        "order": 81
    },
    {
        "id": "_posts_jupiter_saturn_transits_planning",
        "label": "Jupiter and Saturn Transits for Life Planning: วางแผนการเติบโตและโครงสร้างชีวิตระยะ 1–3 ปี",
        "slug": "2026-06-14-jupiter-saturn-transits-planning",
        "tags": ["jupiter-transit", "saturn-transit", "life-planning", "long-term-planning", "growth", "structure"],
        "order": 79
    },
    {
        "id": "_posts_nodes_karmic_direction",
        "label": "The Nodes and Karmic Direction: ราหู–เกตุบอกทิศทางการเติบโตและสิ่งที่ต้องปล่อยอย่างไร",
        "slug": "2026-06-14-nodes-karmic-direction",
        "tags": ["North Node", "South Node", "Rahu", "Ketu", "Karmic Direction", "Life Path", "Nodes"],
        "order": 82
    },
    {
        "id": "_posts_north_node_by_house",
        "label": "North Node by House: เส้นทางเติบโตของชีวิตทั้ง 12 เรือน",
        "slug": "2026-06-14-north-node-by-house",
        "tags": ["North Node", "Rahu", "Growth Zone", "House", "Life Path", "Personal Growth"],
        "order": 83
    },
    {
        "id": "_posts_progressed_moon_guide",
        "label": "Progressed Moon Guide: ฤดูกาลทางใจระยะ 2–3 ปี",
        "slug": "2026-06-14-progressed-moon-guide",
        "tags": ["progressed-moon", "secondary-progressions", "emotional-seasons", "long-term-planning", "inner-growth"],
        "order": 80
    },
]

# ============================================================
# NEW CONCEPT definitions for this chunk
# ============================================================
new_concepts = [
    # Moon House concepts
    {"id": "concept_moon_house", "label": "Moon House — บ้าน/เรือนของดวงจันทร์ในดวงกำเนิด"},
    {"id": "concept_moon_house_manifestation", "label": "Moon House Manifestation — การmanifestตามเรือนจันทร์"},

    # Waxing / Waning
    {"id": "concept_waxing_moon", "label": "Waxing Moon / ข้างขึ้น — จันทร์กำลังเคลื่อนออกจากอาทิตย์"},
    {"id": "concept_waning_moon", "label": "Waning Moon / ข้างแรม — จันทร์กำลังเคลื่อนกลับเข้าหาอาทิตย์"},

    # Manifestation concepts
    {"id": "concept_manifestation", "label": "Manifestation — การตั้งเจตนาและลงมือทำตามจังหวะจักรวาล"},
    {"id": "concept_intention_setting", "label": "Intention Setting — การตั้งเจตนา"},
    {"id": "concept_full_moon_release", "label": "Full Moon Release — การปล่อยวางในวันเพ็ญ"},
    {"id": "concept_waxing_moon_action", "label": "Waxing Moon Action — การลงมือทำในช่วงข้างขึ้น"},
    {"id": "concept_waning_moon_release", "label": "Waning Moon Release — การปล่อยวางในช่วงข้างแรม"},
    {"id": "concept_new_moon_manifestation", "label": "New Moon Manifestation — การตั้งเจตนาในจันทร์ดับ"},

    # Moon Journal
    {"id": "concept_moon_journal", "label": "Moon Journal — การเขียนบันทึกตามจังหวะจันทร์"},
    {"id": "concept_self_reflection", "label": "Self Reflection — การสะท้อนตนเองผ่านจังหวะจันทร์"},

    # Worksheet & Calendar
    {"id": "concept_moon_manifestation_worksheet", "label": "Moon Manifestation Worksheet — แบบฟอร์มปฏิบัติรายเดือนตามจันทร์"},
    {"id": "concept_moon_manifestation_calendar", "label": "Moon Manifestation Calendar — ปฏิทินวางแผนรายเดือนตามจันทร์"},

    # Annual Profection / Lord of the Year
    {"id": "concept_annual_profection", "label": "Annual Profection — ระบบหาเรือนประจำปีตามอายุ"},
    {"id": "concept_lord_of_the_year", "label": "Lord of the Year / ดาวเจ้าปี — ดาวเคราะห์ที่ปกครองเรือนประจำปี"},
    {"id": "concept_yearly_theme", "label": "Yearly Theme — ธีมประจำปีจากProfection"},
    {"id": "concept_profection_year", "label": "Profection Year — ปีแห่งการเปิดใช้งานเรือนใดเรือนหนึ่ง"},
    {"id": "concept_time_lord", "label": "Time Lord — ดาวเคราะห์ที่ปกครองช่วงเวลา"},

    # Solar Return
    {"id": "concept_solar_return", "label": "Solar Return — ดวงอาทิตย์กลับคืนสู่ตำแหน่งเดิมวันเกิด"},
    {"id": "concept_solar_return_reading", "label": "Solar Return Reading — การอ่านดวงปีจาก Solar Return"},

    # Progressed Moon
    {"id": "concept_progressed_moon", "label": "Progressed Moon / จันทร์ก้าวหน้า — ฤดูกาลทางใจ 2-3 ปี"},
    {"id": "concept_secondary_progression", "label": "Secondary Progression — ระบบก้าวหน้าวันเท่าปี"},
    {"id": "concept_emotional_seasons", "label": "Emotional Seasons — ฤดูกาลทางอารมณ์ระยะยาว"},

    # Nodes (Rahu/Ketu)
    {"id": "concept_north_node", "label": "North Node / ราหู — ทิศทางการเติบโต"},
    {"id": "concept_south_node", "label": "South Node / เกตุ — ความคุ้นเคยเดิมที่ควรปล่อย"},
    {"id": "concept_nodes", "label": "Nodes / ราหู-เกตุ — แกนกรรมในดวงชะตา"},
    {"id": "concept_karmic_direction", "label": "Karmic Direction — ทิศทางกรรมผ่าน Nodes"},
    {"id": "concept_north_node_by_house", "label": "North Node by House — ราหูตามเรือนทั้ง 12"},
    {"id": "concept_south_node_by_house", "label": "South Node by House — เกตุตามเรือนทั้ง 12"},
    {"id": "concept_growth_zone", "label": "Growth Zone — พื้นที่เติบโตของชีวิต"},

    # Eclipses
    {"id": "concept_eclipse", "label": "Eclipse / คราส — จุดเปลี่ยนสำคัญของชีวิต"},
    {"id": "concept_solar_eclipse", "label": "Solar Eclipse / สุริยุปราคา — New Moon ใกล้ Nodes"},
    {"id": "concept_lunar_eclipse", "label": "Lunar Eclipse / จันทรุปราคา — Full Moon ใกล้ Nodes"},
    {"id": "concept_turning_points", "label": "Life Turning Points — จุดเปลี่ยนชีวิตราย 6 เดือน"},

    # Jupiter / Saturn Transits
    {"id": "concept_jupiter_transit", "label": "Jupiter Transit — การเคลื่อนของดาวพฤหัส การขยายตัว"},
    {"id": "concept_saturn_transit", "label": "Saturn Transit — การเคลื่อนของดาวเสาร์ โครงสร้าง ความรับผิดชอบ"},
    {"id": "concept_long_term_planning", "label": "Long-term Planning — การวางแผนระยะยาว 1-3 ปี"},
    {"id": "concept_growth_structure_cycle", "label": "Growth-Structure Cycle — รอบขยายตัวและสร้างฐาน"},

    # Life Planning System
    {"id": "concept_astrological_life_planning_system", "label": "Astrological Life Planning System — ระบบวางแผนชีวิตด้วยโหราศาสตร์"},
    {"id": "concept_astrology_planner", "label": "Astrology Planner — แบบฟอร์มวางแผนชีวิตด้วยโหราศาสตร์"},
    {"id": "concept_one_year_life_planning", "label": "One Year Life Planning — การวางแผนชีวิต 1 ปีด้วยโหราศาสตร์"},
]

# ============================================================
# Build all nodes
# ============================================================
nodes = []

for d in docs:
    nodes.append({
        "id": d["id"],
        "label": d["label"],
        "file_type": "document",
        "source_file": f"_posts/{d['slug']}.md",
        "source_location": None
    })

for c in new_concepts:
    # Only add if not already in existing_concepts
    if c["id"] not in existing_concepts:
        nodes.append({
            "id": c["id"],
            "label": c["label"],
            "file_type": "concept",
            "source_file": None,
            "source_location": None
        })

# Also add tag concepts that are new
tag_concepts = {}
for d in docs:
    for tag in d["tags"]:
        tid = f"concept_tag_{tag.lower().replace(' ', '_').replace('-', '_')}"
        if tid not in tag_concepts:
            tag_concepts[tid] = tag

for tid, tlabel in tag_concepts.items():
    if tid not in existing_concepts and not any(c["id"] == tid for c in new_concepts):
        nodes.append({
            "id": tid,
            "label": f"Tag: {tlabel}",
            "file_type": "concept",
            "source_file": None,
            "source_location": None
        })

# Add category concept
nodes.append({
    "id": "concept_category_astrology",
    "label": "Category: Astrology",
    "file_type": "concept",
    "source_file": None,
    "source_location": None
})

# ============================================================
# Build edges
# ============================================================
edges = []

def tagged_edge(doc_id, tag, src_file):
    tid = f"concept_tag_{tag.lower().replace(' ', '_').replace('-', '_')}"
    return {
        "source": doc_id, "target": tid,
        "relation": "tagged_as", "confidence": "EXTRACTED",
        "confidence_score": 1.0, "source_file": src_file,
        "source_location": None, "weight": 1.0
    }

def cat_edge(doc_id, src_file):
    return {
        "source": doc_id, "target": "concept_category_astrology",
        "relation": "tagged_as", "confidence": "EXTRACTED",
        "confidence_score": 1.0, "source_file": src_file,
        "source_location": None, "weight": 1.0
    }

def ref_edge(doc_id, concept_id, src_file, conf="EXTRACTED", score=1.0):
    return {
        "source": doc_id, "target": concept_id,
        "relation": "references", "confidence": conf,
        "confidence_score": score, "source_file": src_file,
        "source_location": None, "weight": 1.0
    }

def rel_edge(src_concept, tgt_concept, relation="conceptually_related_to", conf="INFERRED", score=0.7):
    return {
        "source": src_concept, "target": tgt_concept,
        "relation": relation, "confidence": conf,
        "confidence_score": score, "source_file": None,
        "source_location": None, "weight": 1.0
    }

def doc_ref_edge(doc_id, target_doc_id, src_file, conf="INFERRED", score=0.8):
    return {
        "source": doc_id, "target": target_doc_id,
        "relation": "references", "confidence": conf,
        "confidence_score": score, "source_file": src_file,
        "source_location": None, "weight": 1.0
    }

# --- Document edges ---
for d in docs:
    src = f"_posts/{d['slug']}.md"
    # category
    edges.append(cat_edge(d["id"], src))
    # tags
    for tag in d["tags"]:
        edges.append(tagged_edge(d["id"], tag, src))

    # Document-to-concept references
    did = d["id"]

    # Map document to key concepts
    if "tithi-moon-sign-moon-house" in did:
        edges.append(ref_edge(did, "concept_tithi", src))
        edges.append(ref_edge(did, "concept_moon_sign", src))
        edges.append(ref_edge(did, "concept_moon_house", src))
        edges.append(ref_edge(did, "concept_tithi_archetype", src))
        edges.append(ref_edge(did, "concept_moon", src))

    elif "waxing-waning-moon" in did:
        edges.append(ref_edge(did, "concept_waxing_moon", src))
        edges.append(ref_edge(did, "concept_waning_moon", src))
        edges.append(ref_edge(did, "concept_tithi", src))
        edges.append(ref_edge(did, "concept_lunar_cycle", src))
        edges.append(ref_edge(did, "concept_moon_phase", src))
        edges.append(ref_edge(did, "concept_shukla_paksha", src))
        edges.append(ref_edge(did, "concept_krishna_paksha", src))

    elif "full-moon-release-by-sign" in did:
        edges.append(ref_edge(did, "concept_moon_phase_full_moon", src))
        edges.append(ref_edge(did, "concept_full_moon_release", src))
        edges.append(ref_edge(did, "concept_manifestation", src))
        edges.append(ref_edge(did, "concept_moon_sign", src))

    elif "how-to-manifest-with-moon-phase" in did:
        edges.append(ref_edge(did, "concept_manifestation", src))
        edges.append(ref_edge(did, "concept_moon_phase", src))
        edges.append(ref_edge(did, "concept_intention_setting", src))
        edges.append(ref_edge(did, "concept_waxing_moon", src))
        edges.append(ref_edge(did, "concept_waning_moon", src))
        edges.append(ref_edge(did, "concept_moon_phase_new_moon", src))
        edges.append(ref_edge(did, "concept_moon_phase_full_moon", src))

    elif "manifest-with-moon-sign" in did:
        edges.append(ref_edge(did, "concept_manifestation", src))
        edges.append(ref_edge(did, "concept_moon_sign", src))
        edges.append(ref_edge(did, "concept_moon_phase", src))
        edges.append(ref_edge(did, "concept_intention_setting", src))

    elif "moon-journal-prompts" in did:
        edges.append(ref_edge(did, "concept_moon_journal", src))
        edges.append(ref_edge(did, "concept_moon_phase", src))
        edges.append(ref_edge(did, "concept_moon_house", src))
        edges.append(ref_edge(did, "concept_self_reflection", src))
        edges.append(ref_edge(did, "concept_manifestation", src))

    elif "moon-manifestation-by-house" in did:
        edges.append(ref_edge(did, "concept_moon_house_manifestation", src))
        edges.append(ref_edge(did, "concept_moon_house", src))
        edges.append(ref_edge(did, "concept_moon_phase", src))
        edges.append(ref_edge(did, "concept_moon_sign", src))
        edges.append(ref_edge(did, "concept_manifestation", src))

    elif "new-moon-manifestation-by-sign" in did:
        edges.append(ref_edge(did, "concept_moon_phase_new_moon", src))
        edges.append(ref_edge(did, "concept_new_moon_manifestation", src))
        edges.append(ref_edge(did, "concept_intention_setting", src))
        edges.append(ref_edge(did, "concept_moon_sign", src))
        edges.append(ref_edge(did, "concept_manifestation", src))

    elif "waning-moon-release-by-sign" in did:
        edges.append(ref_edge(did, "concept_waning_moon", src))
        edges.append(ref_edge(did, "concept_waning_moon_release", src))
        edges.append(ref_edge(did, "concept_moon_phase", src))
        edges.append(ref_edge(did, "concept_moon_sign", src))
        edges.append(ref_edge(did, "concept_manifestation", src))

    elif "waxing-moon-action-by-sign" in did:
        edges.append(ref_edge(did, "concept_waxing_moon", src))
        edges.append(ref_edge(did, "concept_waxing_moon_action", src))
        edges.append(ref_edge(did, "concept_moon_phase", src))
        edges.append(ref_edge(did, "concept_moon_sign", src))
        edges.append(ref_edge(did, "concept_manifestation", src))

    elif "beyond-the-moon" in did:
        edges.append(ref_edge(did, "concept_moon_phase", src))
        edges.append(ref_edge(did, "concept_solar_return", src))
        edges.append(ref_edge(did, "concept_annual_profection", src))
        edges.append(ref_edge(did, "concept_long_term_planning", src))
        edges.append(ref_edge(did, "concept_lunar_cycle", src))

    elif "moon-manifestation-calendar" in did:
        edges.append(ref_edge(did, "concept_moon_manifestation_calendar", src))
        edges.append(ref_edge(did, "concept_moon_phase", src))
        edges.append(ref_edge(did, "concept_moon_house", src))
        edges.append(ref_edge(did, "concept_manifestation", src))

    elif "moon-manifestation-worksheet-examples" in did:
        edges.append(ref_edge(did, "concept_moon_manifestation_worksheet", src))
        edges.append(ref_edge(did, "concept_moon_phase", src))
        edges.append(ref_edge(did, "concept_moon_house", src))
        edges.append(ref_edge(did, "concept_manifestation", src))

    elif "moon-manifestation-worksheet" in did:
        edges.append(ref_edge(did, "concept_moon_manifestation_worksheet", src))
        edges.append(ref_edge(did, "concept_moon_phase", src))
        edges.append(ref_edge(did, "concept_moon_journal", src))
        edges.append(ref_edge(did, "concept_moon_sign", src))
        edges.append(ref_edge(did, "concept_moon_house", src))

    elif "annual-profection-for-beginners" in did:
        edges.append(ref_edge(did, "concept_annual_profection", src))
        edges.append(ref_edge(did, "concept_lord_of_the_year", src))
        edges.append(ref_edge(did, "concept_yearly_theme", src))
        edges.append(ref_edge(did, "concept_profection_year", src))

    elif "lord-of-the-year" in did:
        edges.append(ref_edge(did, "concept_lord_of_the_year", src))
        edges.append(ref_edge(did, "concept_annual_profection", src))
        edges.append(ref_edge(did, "concept_time_lord", src))
        edges.append(ref_edge(did, "concept_yearly_theme", src))

    elif "solar-return-for-life-planning" in did:
        edges.append(ref_edge(did, "concept_solar_return", src))
        edges.append(ref_edge(did, "concept_solar_return_reading", src))
        edges.append(ref_edge(did, "concept_annual_profection", src))
        edges.append(ref_edge(did, "concept_yearly_theme", src))
        edges.append(ref_edge(did, "concept_long_term_planning", src))

    elif "astrological-life-planning-system" in did:
        edges.append(ref_edge(did, "concept_astrological_life_planning_system", src))
        edges.append(ref_edge(did, "concept_moon_phase", src))
        edges.append(ref_edge(did, "concept_annual_profection", src))
        edges.append(ref_edge(did, "concept_solar_return", src))
        edges.append(ref_edge(did, "concept_progressed_moon", src))
        edges.append(ref_edge(did, "concept_jupiter_transit", src))
        edges.append(ref_edge(did, "concept_saturn_transit", src))
        edges.append(ref_edge(did, "concept_eclipse", src))
        edges.append(ref_edge(did, "concept_nodes", src))

    elif "astrology-planner-case-study-1" in did:
        edges.append(ref_edge(did, "concept_case_study", src))
        edges.append(ref_edge(did, "concept_astrology_planner", src))
        edges.append(ref_edge(did, "concept_one_year_life_planning", src))
        edges.append(ref_edge(did, "concept_annual_profection", src))
        edges.append(ref_edge(did, "concept_solar_return", src))
        edges.append(ref_edge(did, "concept_nodes", src))
        edges.append(ref_edge(did, "concept_moon_phase", src))

    elif "astrology-planner-case-study-2" in did:
        edges.append(ref_edge(did, "concept_case_study", src))
        edges.append(ref_edge(did, "concept_astrology_planner", src))
        edges.append(ref_edge(did, "concept_one_year_life_planning", src))
        edges.append(ref_edge(did, "concept_nodes", src))
        edges.append(ref_edge(did, "concept_annual_profection", src))
        edges.append(ref_edge(did, "concept_jupiter_transit", src))
        edges.append(ref_edge(did, "concept_saturn_transit", src))

    elif "eclipses-life-turning-points" in did:
        edges.append(ref_edge(did, "concept_eclipse", src))
        edges.append(ref_edge(did, "concept_solar_eclipse", src))
        edges.append(ref_edge(did, "concept_lunar_eclipse", src))
        edges.append(ref_edge(did, "concept_turning_points", src))
        edges.append(ref_edge(did, "concept_nodes", src))
        edges.append(ref_edge(did, "concept_moon_phase", src))

    elif "jupiter-saturn-transits-planning" in did:
        edges.append(ref_edge(did, "concept_jupiter_transit", src))
        edges.append(ref_edge(did, "concept_saturn_transit", src))
        edges.append(ref_edge(did, "concept_long_term_planning", src))
        edges.append(ref_edge(did, "concept_growth_structure_cycle", src))
        edges.append(ref_edge(did, "concept_annual_profection", src))

    elif "nodes-karmic-direction" in did:
        edges.append(ref_edge(did, "concept_north_node", src))
        edges.append(ref_edge(did, "concept_south_node", src))
        edges.append(ref_edge(did, "concept_nodes", src))
        edges.append(ref_edge(did, "concept_karmic_direction", src))

    elif "north-node-by-house" in did:
        edges.append(ref_edge(did, "concept_north_node", src))
        edges.append(ref_edge(did, "concept_north_node_by_house", src))
        edges.append(ref_edge(did, "concept_growth_zone", src))
        edges.append(ref_edge(did, "concept_nodes", src))
        edges.append(ref_edge(did, "concept_karmic_direction", src))

    elif "progressed-moon-guide" in did:
        edges.append(ref_edge(did, "concept_progressed_moon", src))
        edges.append(ref_edge(did, "concept_secondary_progression", src))
        edges.append(ref_edge(did, "concept_emotional_seasons", src))
        edges.append(ref_edge(did, "concept_long_term_planning", src))

# --- Concept-to-concept edges ---
# Tithi related
ce_pairs = [
    ("concept_tithi", "concept_moon_phase", "conceptually_related_to", "INFERRED", 0.8),
    ("concept_tithi", "concept_sun_moon_angle", "conceptually_related_to", "INFERRED", 0.9),
    ("concept_tithi_archetype", "concept_tithi", "explains", "EXTRACTED", 1.0),
    ("concept_waxing_moon", "concept_shukla_paksha", "conceptually_related_to", "INFERRED", 0.9),
    ("concept_waning_moon", "concept_krishna_paksha", "conceptually_related_to", "INFERRED", 0.9),
    ("concept_moon_house", "concept_moon", "conceptually_related_to", "INFERRED", 0.7),
    ("concept_moon_sign", "concept_moon", "conceptually_related_to", "INFERRED", 0.8),

    # Manifestation cluster
    ("concept_manifestation", "concept_moon_phase", "conceptually_related_to", "INFERRED", 0.8),
    ("concept_manifestation", "concept_intention_setting", "explains", "EXTRACTED", 1.0),
    ("concept_new_moon_manifestation", "concept_moon_phase_new_moon", "conceptually_related_to", "INFERRED", 0.9),
    ("concept_new_moon_manifestation", "concept_manifestation", "explains", "EXTRACTED", 1.0),
    ("concept_full_moon_release", "concept_moon_phase_full_moon", "conceptually_related_to", "INFERRED", 0.9),
    ("concept_full_moon_release", "concept_manifestation", "explains", "EXTRACTED", 1.0),
    ("concept_waxing_moon_action", "concept_waxing_moon", "conceptually_related_to", "INFERRED", 0.9),
    ("concept_waxing_moon_action", "concept_manifestation", "explains", "EXTRACTED", 1.0),
    ("concept_waning_moon_release", "concept_waning_moon", "conceptually_related_to", "INFERRED", 0.9),
    ("concept_waning_moon_release", "concept_manifestation", "explains", "EXTRACTED", 1.0),
    ("concept_moon_house_manifestation", "concept_moon_house", "conceptually_related_to", "INFERRED", 0.8),
    ("concept_moon_house_manifestation", "concept_manifestation", "explains", "EXTRACTED", 1.0),
    ("concept_moon_journal", "concept_self_reflection", "conceptually_related_to", "INFERRED", 0.8),
    ("concept_moon_journal", "concept_moon_phase", "conceptually_related_to", "INFERRED", 0.7),

    # Worksheet & Calendar
    ("concept_moon_manifestation_worksheet", "concept_manifestation", "conceptually_related_to", "INFERRED", 0.8),
    ("concept_moon_manifestation_worksheet", "concept_moon_journal", "conceptually_related_to", "INFERRED", 0.7),
    ("concept_moon_manifestation_calendar", "concept_manifestation", "conceptually_related_to", "INFERRED", 0.8),
    ("concept_moon_manifestation_calendar", "concept_moon_house", "conceptually_related_to", "INFERRED", 0.7),

    # Annual Profection cluster
    ("concept_annual_profection", "concept_profection_year", "explains", "EXTRACTED", 1.0),
    ("concept_annual_profection", "concept_lord_of_the_year", "explains", "EXTRACTED", 1.0),
    ("concept_annual_profection", "concept_yearly_theme", "conceptually_related_to", "INFERRED", 0.8),
    ("concept_lord_of_the_year", "concept_time_lord", "conceptually_related_to", "INFERRED", 0.8),
    ("concept_annual_profection", "concept_moon_phase", "conceptually_related_to", "INFERRED", 0.5),

    # Solar Return
    ("concept_solar_return", "concept_solar_return_reading", "explains", "EXTRACTED", 1.0),
    ("concept_solar_return", "concept_annual_profection", "conceptually_related_to", "INFERRED", 0.8),
    ("concept_solar_return", "concept_yearly_theme", "conceptually_related_to", "INFERRED", 0.7),

    # Nodes cluster
    ("concept_nodes", "concept_north_node", "explains", "EXTRACTED", 1.0),
    ("concept_nodes", "concept_south_node", "explains", "EXTRACTED", 1.0),
    ("concept_nodes", "concept_karmic_direction", "conceptually_related_to", "INFERRED", 0.9),
    ("concept_north_node", "concept_north_node_by_house", "explains", "EXTRACTED", 1.0),
    ("concept_south_node", "concept_south_node_by_house", "explains", "EXTRACTED", 1.0),
    ("concept_north_node", "concept_growth_zone", "conceptually_related_to", "INFERRED", 0.8),

    # Eclipses
    ("concept_eclipse", "concept_solar_eclipse", "explains", "EXTRACTED", 1.0),
    ("concept_eclipse", "concept_lunar_eclipse", "explains", "EXTRACTED", 1.0),
    ("concept_eclipse", "concept_turning_points", "conceptually_related_to", "INFERRED", 0.9),
    ("concept_eclipse", "concept_nodes", "conceptually_related_to", "INFERRED", 0.9),
    ("concept_solar_eclipse", "concept_moon_phase_new_moon", "conceptually_related_to", "INFERRED", 0.9),
    ("concept_lunar_eclipse", "concept_moon_phase_full_moon", "conceptually_related_to", "INFERRED", 0.9),

    # Jupiter/Saturn
    ("concept_jupiter_transit", "concept_jupiter", "conceptually_related_to", "INFERRED", 0.8),
    ("concept_saturn_transit", "concept_saturn", "conceptually_related_to", "INFERRED", 0.8),
    ("concept_jupiter_transit", "concept_growth_structure_cycle", "conceptually_related_to", "INFERRED", 0.7),
    ("concept_saturn_transit", "concept_growth_structure_cycle", "conceptually_related_to", "INFERRED", 0.7),
    ("concept_long_term_planning", "concept_growth_structure_cycle", "explains", "EXTRACTED", 1.0),

    # Progressed Moon
    ("concept_progressed_moon", "concept_secondary_progression", "explains", "EXTRACTED", 1.0),
    ("concept_progressed_moon", "concept_emotional_seasons", "conceptually_related_to", "INFERRED", 0.9),
    ("concept_progressed_moon", "concept_long_term_planning", "conceptually_related_to", "INFERRED", 0.7),

    # Life Planning System
    ("concept_astrological_life_planning_system", "concept_astrology_planner", "conceptually_related_to", "INFERRED", 0.9),
    ("concept_astrology_planner", "concept_one_year_life_planning", "conceptually_related_to", "INFERRED", 0.8),
    ("concept_astrological_life_planning_system", "concept_long_term_planning", "conceptually_related_to", "INFERRED", 0.8),

    # Cross-cluster connections
    ("concept_eclipse", "concept_moon_phase", "conceptually_related_to", "INFERRED", 0.7),
    ("concept_nodes", "concept_karmic_direction", "conceptually_related_to", "INFERRED", 0.8),
    ("concept_moon_manifestation_calendar", "concept_moon_phase", "conceptually_related_to", "INFERRED", 0.7),
    ("concept_one_year_life_planning", "concept_annual_profection", "conceptually_related_to", "INFERRED", 0.7),
    ("concept_one_year_life_planning", "concept_solar_return", "conceptually_related_to", "INFERRED", 0.7),
]

for s, t, rel, conf, score in ce_pairs:
    edges.append(rel_edge(s, t, rel, conf, score))

# Document-to-document edges (sequential/related posts)
doc_seq_edges = [
    ("_posts_how_to_manifest_with_moon_phase", "_posts_manifest_with_moon_sign"),
    ("_posts_new_moon_manifestation_by_sign", "_posts_waxing_moon_action_by_sign"),
    ("_posts_waxing_moon_action_by_sign", "_posts_full_moon_release_by_sign"),
    ("_posts_full_moon_release_by_sign", "_posts_waning_moon_release_by_sign"),
    ("_posts_waning_moon_release_by_sign", "_posts_moon_manifestation_by_house"),
    ("_posts_moon_manifestation_by_house", "_posts_moon_journal_prompts_by_phase_and_house"),
    ("_posts_moon_journal_prompts_by_phase_and_house", "_posts_moon_manifestation_worksheet"),
    ("_posts_moon_manifestation_worksheet", "_posts_moon_manifestation_worksheet_examples"),
    ("_posts_moon_manifestation_worksheet_examples", "_posts_moon_manifestation_calendar"),
    ("_posts_moon_manifestation_calendar", "_posts_beyond_the_moon"),
    ("_posts_beyond_the_moon", "_posts_annual_profection_for_beginners"),
    ("_posts_annual_profection_for_beginners", "_posts_lord_of_the_year"),
    ("_posts_lord_of_the_year", "_posts_solar_return_for_life_planning"),
    ("_posts_solar_return_for_life_planning", "_posts_jupiter_saturn_transits_planning"),
    ("_posts_jupiter_saturn_transits_planning", "_posts_progressed_moon_guide"),
    ("_posts_progressed_moon_guide", "_posts_eclipses_life_turning_points"),
    ("_posts_eclipses_life_turning_points", "_posts_nodes_karmic_direction"),
    ("_posts_nodes_karmic_direction", "_posts_north_node_by_house"),
    ("_posts_north_node_by_house", "_posts_south_node_by_house"),  # south node not in this chunk but referenced
    ("_posts_nodes_karmic_direction", "_posts_astrological_life_planning_system"),
    ("_posts_eclipses_life_turning_points", "_posts_astrological_life_planning_system"),
    ("_posts_progressed_moon_guide", "_posts_astrological_life_planning_system"),
    ("_posts_jupiter_saturn_transits_planning", "_posts_astrological_life_planning_system"),
    ("_posts_solar_return_for_life_planning", "_posts_astrological_life_planning_system"),
    ("_posts_annual_profection_for_beginners", "_posts_astrological_life_planning_system"),
    ("_posts_astrological_life_planning_system", "_posts_astrology_planner_case_study_1"),
    ("_posts_astrological_life_planning_system", "_posts_astrology_planner_case_study_2"),
    ("_posts_tithi_moon_sign_moon_house", "_posts_moon_manifestation_by_house"),
    ("_posts_waxing_waning_moon", "_posts_how_to_manifest_with_moon_phase"),
]

# Look up source files
doc_id_to_slug = {d["id"]: d["slug"] for d in docs}

for src_id, tgt_id in doc_seq_edges:
    src_file = f"_posts/{doc_id_to_slug.get(src_id, 'unknown')}.md"
    edges.append(doc_ref_edge(src_id, tgt_id, src_file))

# ============================================================
# Remove duplicate nodes (same ID) keeping first occurrence
# ============================================================
seen_ids = set()
unique_nodes = []
for n in nodes:
    if n["id"] not in seen_ids:
        seen_ids.add(n["id"])
        unique_nodes.append(n)

# ============================================================
# Build final JSON
# ============================================================
result = {
    "nodes": unique_nodes,
    "edges": edges
}

with open("C:\\AstrologyBlog\\graphify-out\\chunks\\result_04.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"Nodes: {len(unique_nodes)}")
print(f"Edges: {len(edges)}")
print("Written to result_04.json")
