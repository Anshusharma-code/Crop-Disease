"""
utils/disease_db.py
───────────────────
Complete disease knowledge base for 38 PlantVillage classes.
Contains symptoms, pathogens, severity, remedies, and prevention.
"""

DISEASE_DATABASE = {
    "Apple___Apple_scab": {
        "common_name": "Apple Scab",
        "crop": "Apple",
        "pathogen": "Venturia inaequalis (Fungus)",
        "symptoms": "Dark, scaly lesions on leaves and fruit. Leaves may curl and drop early.",
        "severity": "High",
        "remedy": [
            "Apply fungicides (Captan, Mancozeb) preventively during wet spring weather",
            "Remove and destroy fallen leaves to reduce overwintering spores",
            "Prune trees to improve air circulation",
            "Plant resistant apple varieties like Liberty or Freedom",
        ],
        "prevention": "Regular dormant sprays with lime sulfur before bud break",
        "conditions": "Cool, wet weather (16-24°C) during early spring"
    },
    "Apple___Black_rot": {
        "common_name": "Apple Black Rot",
        "crop": "Apple",
        "pathogen": "Botryosphaeria obtusa (Fungus)",
        "symptoms": "Circular brown spots on leaves, rotting fruit with black concentric rings",
        "severity": "High",
        "remedy": [
            "Remove mummified fruits and dead wood from trees",
            "Apply copper-based fungicides",
            "Prune out infected branches 10-15 cm below visible infection",
            "Maintain tree vigor through proper nutrition",
        ],
        "prevention": "Sanitation and removal of infected plant material",
        "conditions": "Warm, humid weather; wounds or stress on trees"
    },
    "Apple___Cedar_apple_rust": {
        "common_name": "Cedar Apple Rust",
        "crop": "Apple",
        "pathogen": "Gymnosporangium juniperi-virginianae (Fungus)",
        "symptoms": "Bright orange-yellow spots on upper leaf surface; tube-like structures on underside",
        "severity": "Medium",
        "remedy": [
            "Apply fungicides (Myclobutanil, Propiconazole) from pink bud stage",
            "Remove nearby cedar/juniper trees if possible",
            "Plant rust-resistant apple varieties",
            "Apply protective sprays every 7-10 days during wet weather",
        ],
        "prevention": "Eliminate alternate hosts (cedar trees) within 300m radius",
        "conditions": "Alternating wet and dry periods in spring"
    },
    "Apple___healthy": {
        "common_name": "Healthy Apple",
        "crop": "Apple",
        "pathogen": "None",
        "symptoms": "No disease symptoms present — plant is healthy!",
        "severity": "None",
        "remedy": ["Continue current care practices", "Monitor regularly for early signs of disease"],
        "prevention": "Maintain good cultural practices, balanced fertilization, proper irrigation",
        "conditions": "N/A"
    },
    "Blueberry___healthy": {
        "common_name": "Healthy Blueberry",
        "crop": "Blueberry",
        "pathogen": "None",
        "symptoms": "No disease symptoms present — plant is healthy!",
        "severity": "None",
        "remedy": ["Maintain soil pH 4.5-5.5", "Ensure adequate mulching"],
        "prevention": "Regular monitoring, proper spacing for air circulation",
        "conditions": "N/A"
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "common_name": "Cherry Powdery Mildew",
        "crop": "Cherry",
        "pathogen": "Podosphaera clandestina (Fungus)",
        "symptoms": "White powdery coating on young leaves and shoots; distorted growth",
        "severity": "Medium",
        "remedy": [
            "Apply sulfur-based or potassium bicarbonate fungicides",
            "Neem oil spray as organic alternative",
            "Improve air circulation through pruning",
            "Avoid excessive nitrogen fertilization",
        ],
        "prevention": "Plant resistant varieties; ensure proper spacing",
        "conditions": "High humidity with dry leaf surfaces, warm days and cool nights"
    },
    "Cherry_(including_sour)___healthy": {
        "common_name": "Healthy Cherry",
        "crop": "Cherry",
        "pathogen": "None",
        "symptoms": "No disease symptoms present — plant is healthy!",
        "severity": "None",
        "remedy": ["Continue current care practices"],
        "prevention": "Regular pruning and monitoring",
        "conditions": "N/A"
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "common_name": "Gray Leaf Spot",
        "crop": "Corn / Maize",
        "pathogen": "Cercospora zeae-maydis (Fungus)",
        "symptoms": "Rectangular gray-tan lesions parallel to leaf veins; lesions turn gray with age",
        "severity": "High",
        "remedy": [
            "Apply strobilurin or triazole fungicides at VT/R1 growth stage",
            "Use resistant hybrid varieties",
            "Rotate crops — avoid continuous corn",
            "Tillage to bury infected residue",
        ],
        "prevention": "Crop rotation and use of tolerant hybrids",
        "conditions": "High humidity, warm temperatures (25-30°C), poor air drainage"
    },
    "Corn_(maize)___Common_rust_": {
        "common_name": "Common Rust",
        "crop": "Corn / Maize",
        "pathogen": "Puccinia sorghi (Fungus)",
        "symptoms": "Small, circular to elongated brick-red pustules on both leaf surfaces",
        "severity": "Medium",
        "remedy": [
            "Apply fungicides (Mancozeb, Propiconazole) early in disease development",
            "Plant rust-resistant hybrids",
            "Early planting to avoid peak rust season",
            "Monitor fields regularly during silking",
        ],
        "prevention": "Use resistant varieties; early detection and treatment",
        "conditions": "Cool temperatures (16-23°C), high humidity, heavy dew"
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "common_name": "Northern Leaf Blight",
        "crop": "Corn / Maize",
        "pathogen": "Exserohilum turcicum (Fungus)",
        "symptoms": "Long (5-15 cm), cigar-shaped gray-green lesions on leaves",
        "severity": "High",
        "remedy": [
            "Apply fungicides at early disease onset (before tasseling)",
            "Use resistant hybrids with Ht genes",
            "Crop rotation with non-host crops",
            "Deep tillage to bury infected residue",
        ],
        "prevention": "Plant resistant varieties; avoid late planting dates",
        "conditions": "Moderate temperatures (18-27°C), extended leaf wetness"
    },
    "Corn_(maize)___healthy": {
        "common_name": "Healthy Corn",
        "crop": "Corn / Maize",
        "pathogen": "None",
        "symptoms": "No disease symptoms present — plant is healthy!",
        "severity": "None",
        "remedy": ["Maintain proper nutrition and irrigation"],
        "prevention": "Crop rotation, balanced fertilization, regular scouting",
        "conditions": "N/A"
    },
    "Grape___Black_rot": {
        "common_name": "Grape Black Rot",
        "crop": "Grape",
        "pathogen": "Guignardia bidwellii (Fungus)",
        "symptoms": "Brown circular lesions on leaves; black shriveled mummified berries",
        "severity": "High",
        "remedy": [
            "Apply fungicides (Captan, Mancozeb) starting at bud break",
            "Remove mummified berries and infected plant material",
            "Train vines to improve air circulation",
        ],
        "prevention": "Sanitation of mummified fruit; preventive spray program",
        "conditions": "Warm, wet weather during spring"
    },
    "Grape___Esca_(Black_Measles)": {
        "common_name": "Esca (Black Measles)",
        "crop": "Grape",
        "pathogen": "Phaeomoniella chlamydospora and other fungi",
        "symptoms": "Tiger-stripe pattern on leaves; internal wood discoloration",
        "severity": "Very High",
        "remedy": [
            "No effective chemical treatment available",
            "Remove and destroy severely infected vines",
            "Protect pruning wounds with fungicide or wound sealant",
            "Use certified disease-free planting material",
        ],
        "prevention": "Avoid large pruning wounds; protect cuts immediately after pruning",
        "conditions": "Warm to hot summers; stress conditions"
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "common_name": "Grape Leaf Blight",
        "crop": "Grape",
        "pathogen": "Isariopsis clavispora (Fungus)",
        "symptoms": "Dark brown irregular spots on leaves, often with yellow halos",
        "severity": "Medium",
        "remedy": [
            "Apply copper-based fungicides",
            "Improve vineyard air circulation through canopy management",
            "Remove infected leaves",
            "Avoid overhead irrigation",
        ],
        "prevention": "Good canopy management; balanced nutrition",
        "conditions": "Humid conditions with poor air circulation"
    },
    "Grape___healthy": {
        "common_name": "Healthy Grape",
        "crop": "Grape",
        "pathogen": "None",
        "symptoms": "No disease symptoms present — plant is healthy!",
        "severity": "None",
        "remedy": ["Continue current vineyard management practices"],
        "prevention": "Regular canopy management, proper nutrition, and monitoring",
        "conditions": "N/A"
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "common_name": "Citrus Greening (HLB)",
        "crop": "Orange / Citrus",
        "pathogen": "Candidatus Liberibacter asiaticus (Bacteria)",
        "symptoms": "Asymmetric yellowing of leaves (blotchy mottle); small, lopsided bitter fruit",
        "severity": "Very High — No Cure",
        "remedy": [
            "Remove and destroy infected trees to prevent spread",
            "Control Asian Citrus Psyllid vector with insecticides",
            "Use certified disease-free nursery stock",
            "Nutritional sprays to slow symptom progression",
        ],
        "prevention": "Strict psyllid management; use of disease-free propagation material",
        "conditions": "Presence of Asian Citrus Psyllid vector"
    },
    "Peach___Bacterial_spot": {
        "common_name": "Peach Bacterial Spot",
        "crop": "Peach",
        "pathogen": "Xanthomonas arboricola pv. pruni (Bacteria)",
        "symptoms": "Small, angular water-soaked spots on leaves; shot-hole appearance; lesions on fruit",
        "severity": "High",
        "remedy": [
            "Apply copper-based bactericides during dormancy",
            "Avoid overhead irrigation",
            "Plant in sheltered locations to reduce wind damage",
            "Use resistant varieties when available",
        ],
        "prevention": "Copper sprays during dormant season; wind protection",
        "conditions": "Wet, windy conditions; temperatures 19-28°C"
    },
    "Peach___healthy": {
        "common_name": "Healthy Peach",
        "crop": "Peach",
        "pathogen": "None",
        "symptoms": "No disease symptoms present — plant is healthy!",
        "severity": "None",
        "remedy": ["Maintain balanced fertilization and proper pruning"],
        "prevention": "Regular monitoring; proper spacing for air circulation",
        "conditions": "N/A"
    },
    "Pepper,_bell___Bacterial_spot": {
        "common_name": "Bell Pepper Bacterial Spot",
        "crop": "Bell Pepper",
        "pathogen": "Xanthomonas euvesicatoria (Bacteria)",
        "symptoms": "Small, water-soaked spots on leaves that turn brown with yellow halos",
        "severity": "High",
        "remedy": [
            "Apply copper + mancozeb combination sprays",
            "Use disease-free transplants",
            "Avoid working in fields when plants are wet",
            "Rotate crops for 2-3 years",
        ],
        "prevention": "Use certified seed; crop rotation; avoid overhead watering",
        "conditions": "Warm temperatures (24-30°C), high humidity, rain and wind"
    },
    "Pepper,_bell___healthy": {
        "common_name": "Healthy Bell Pepper",
        "crop": "Bell Pepper",
        "pathogen": "None",
        "symptoms": "No disease symptoms present — plant is healthy!",
        "severity": "None",
        "remedy": ["Continue current crop management"],
        "prevention": "Proper spacing, crop rotation, regular monitoring",
        "conditions": "N/A"
    },
    "Potato___Early_blight": {
        "common_name": "Potato Early Blight",
        "crop": "Potato",
        "pathogen": "Alternaria solani (Fungus)",
        "symptoms": "Dark brown to black lesions with concentric rings (target-board pattern) on older leaves",
        "severity": "Medium",
        "remedy": [
            "Apply fungicides (Chlorothalonil, Mancozeb) at first sign of disease",
            "Ensure adequate potassium nutrition",
            "Remove and destroy infected plant debris",
            "Irrigate in the morning to allow foliage to dry",
        ],
        "prevention": "Use certified seed tubers; adequate plant nutrition; crop rotation",
        "conditions": "Warm temperatures (24-29°C), high humidity, stressed plants"
    },
    "Potato___Late_blight": {
        "common_name": "Potato Late Blight",
        "crop": "Potato",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "symptoms": "Water-soaked pale green lesions turning dark brown; white fuzzy growth on leaf undersides",
        "severity": "Very High",
        "remedy": [
            "Apply fungicides (Metalaxyl, Dimethomorph) immediately at first symptoms",
            "Use forecasting systems to time preventive sprays",
            "Destroy volunteer potato plants",
            "Harvest tubers in dry weather",
        ],
        "prevention": "Plant resistant varieties; monitor weather conditions for disease risk",
        "conditions": "Cool, moist weather (10-25°C), leaf wetness >10 hours"
    },
    "Potato___healthy": {
        "common_name": "Healthy Potato",
        "crop": "Potato",
        "pathogen": "None",
        "symptoms": "No disease symptoms present — plant is healthy!",
        "severity": "None",
        "remedy": ["Use certified seed tubers; maintain balanced nutrition"],
        "prevention": "Crop rotation, proper hilling, regular scouting",
        "conditions": "N/A"
    },
    "Raspberry___healthy": {
        "common_name": "Healthy Raspberry",
        "crop": "Raspberry",
        "pathogen": "None",
        "symptoms": "No disease symptoms present — plant is healthy!",
        "severity": "None",
        "remedy": ["Remove old canes after fruiting"],
        "prevention": "Good air circulation; avoid waterlogging",
        "conditions": "N/A"
    },
    "Soybean___healthy": {
        "common_name": "Healthy Soybean",
        "crop": "Soybean",
        "pathogen": "None",
        "symptoms": "No disease symptoms present — plant is healthy!",
        "severity": "None",
        "remedy": ["Maintain proper row spacing and weed control"],
        "prevention": "Use certified seed; crop rotation",
        "conditions": "N/A"
    },
    "Squash___Powdery_mildew": {
        "common_name": "Squash Powdery Mildew",
        "crop": "Squash",
        "pathogen": "Podosphaera xanthii (Fungus)",
        "symptoms": "White powdery spots on leaves and stems; leaves yellow and die prematurely",
        "severity": "Medium",
        "remedy": [
            "Apply potassium bicarbonate, sulfur, or neem oil sprays",
            "Improve air circulation through wider plant spacing",
            "Water at soil level, not on foliage",
            "Apply milk spray (1:10 ratio) as organic remedy",
        ],
        "prevention": "Plant resistant varieties; avoid high nitrogen; ensure air flow",
        "conditions": "Dry weather with high humidity, temperatures 20-30°C"
    },
    "Strawberry___Leaf_scorch": {
        "common_name": "Strawberry Leaf Scorch",
        "crop": "Strawberry",
        "pathogen": "Diplocarpon earliana (Fungus)",
        "symptoms": "Small, irregular purple spots on upper leaf surface; leaves may appear scorched",
        "severity": "Medium",
        "remedy": [
            "Apply myclobutanil or captan fungicides",
            "Remove and destroy infected leaves",
            "Avoid overhead irrigation",
            "Improve air circulation in planting beds",
        ],
        "prevention": "Use certified transplants; avoid overcrowding",
        "conditions": "Wet weather; dense canopies"
    },
    "Strawberry___healthy": {
        "common_name": "Healthy Strawberry",
        "crop": "Strawberry",
        "pathogen": "None",
        "symptoms": "No disease symptoms present — plant is healthy!",
        "severity": "None",
        "remedy": ["Regular runner removal; proper bed renovation"],
        "prevention": "Use certified transplants; proper plant spacing",
        "conditions": "N/A"
    },
    "Tomato___Bacterial_spot": {
        "common_name": "Tomato Bacterial Spot",
        "crop": "Tomato",
        "pathogen": "Xanthomonas vesicatoria (Bacteria)",
        "symptoms": "Small, dark brown spots with yellow halos on leaves; raised scab-like spots on fruit",
        "severity": "High",
        "remedy": [
            "Apply copper hydroxide sprays preventively",
            "Use disease-free transplants and seeds",
            "Avoid working in wet fields",
            "Practice 2-3 year crop rotation",
        ],
        "prevention": "Hot water seed treatment; copper sprays at transplanting",
        "conditions": "Warm, wet weather; temperatures 24-30°C"
    },
    "Tomato___Early_blight": {
        "common_name": "Tomato Early Blight",
        "crop": "Tomato",
        "pathogen": "Alternaria solani (Fungus)",
        "symptoms": "Dark brown spots with concentric rings on lower older leaves; yellow surrounding tissue",
        "severity": "Medium",
        "remedy": [
            "Apply chlorothalonil or mancozeb fungicides",
            "Stake plants to improve air circulation",
            "Mulch to prevent soil splash",
            "Remove lower infected leaves",
        ],
        "prevention": "Use certified seed; rotate crops; avoid wetting foliage",
        "conditions": "Warm days (24-29°C), cool nights, heavy dew"
    },
    "Tomato___Late_blight": {
        "common_name": "Tomato Late Blight",
        "crop": "Tomato",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "symptoms": "Irregular water-soaked patches on leaves; white mold on leaf undersides; brown firm rot on fruit",
        "severity": "Very High",
        "remedy": [
            "Apply metalaxyl or chlorothalonil immediately",
            "Remove and destroy infected plants",
            "Avoid overhead irrigation",
            "Improve drainage and air circulation",
        ],
        "prevention": "Plant resistant varieties; avoid wet conditions",
        "conditions": "Cool (10-25°C), moist weather with prolonged leaf wetness"
    },
    "Tomato___Leaf_Mold": {
        "common_name": "Tomato Leaf Mold",
        "crop": "Tomato",
        "pathogen": "Passalora fulva (Fungus)",
        "symptoms": "Pale green-yellow spots on upper leaf; olive-green to brown velvety mold on underside",
        "severity": "Medium",
        "remedy": [
            "Reduce humidity by improving ventilation",
            "Apply fungicides (mancozeb, chlorothalonil)",
            "Remove infected leaves",
            "Avoid overhead irrigation",
        ],
        "prevention": "Grow in well-ventilated areas; reduce humidity below 85%",
        "conditions": "High humidity (>85%), moderate temperatures 21-24°C"
    },
    "Tomato___Septoria_leaf_spot": {
        "common_name": "Septoria Leaf Spot",
        "crop": "Tomato",
        "pathogen": "Septoria lycopersici (Fungus)",
        "symptoms": "Small circular spots with dark borders and gray centers; tiny dark dots visible in center",
        "severity": "Medium",
        "remedy": [
            "Apply chlorothalonil or copper fungicides",
            "Remove infected lower leaves",
            "Mulch around plants",
            "Stake and train plants for better air circulation",
        ],
        "prevention": "Crop rotation; use disease-free transplants",
        "conditions": "Warm, wet, humid weather"
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "common_name": "Spider Mite Damage",
        "crop": "Tomato",
        "pathogen": "Tetranychus urticae (Mite)",
        "symptoms": "Tiny yellow/white stippling on upper leaf surface; fine webbing on leaf undersides",
        "severity": "Medium",
        "remedy": [
            "Apply miticides (abamectin, bifenazate)",
            "Spray neem oil or insecticidal soap",
            "Increase humidity around plants",
            "Release predatory mites (Phytoseiulus persimilis)",
        ],
        "prevention": "Avoid water stress; reduce dusty conditions",
        "conditions": "Hot, dry conditions; dusty environments; drought stress"
    },
    "Tomato___Target_Spot": {
        "common_name": "Target Spot",
        "crop": "Tomato",
        "pathogen": "Corynespora cassiicola (Fungus)",
        "symptoms": "Brown spots with concentric rings on leaves, stems and fruit; premature defoliation",
        "severity": "Medium",
        "remedy": [
            "Apply fungicides (azoxystrobin, chlorothalonil)",
            "Improve air circulation",
            "Avoid excess nitrogen",
            "Remove infected plant material",
        ],
        "prevention": "Good sanitation; balanced nutrition; avoid dense planting",
        "conditions": "Warm humid conditions; temperatures 25-32°C"
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "common_name": "Tomato Yellow Leaf Curl Virus",
        "crop": "Tomato",
        "pathogen": "TYLCV (Begomovirus — transmitted by whitefly)",
        "symptoms": "Severe leaf curling and yellowing; stunted growth; flower drop; small fruit",
        "severity": "Very High — No cure",
        "remedy": [
            "Remove and destroy infected plants immediately",
            "Control whitefly vectors with insecticides / yellow sticky traps",
            "Use reflective mulches to repel whiteflies",
            "Plant resistant or tolerant varieties (TY variants)",
        ],
        "prevention": "Whitefly control is key; use virus-free transplants",
        "conditions": "High whitefly populations; hot dry weather"
    },
    "Tomato___Tomato_mosaic_virus": {
        "common_name": "Tomato Mosaic Virus",
        "crop": "Tomato",
        "pathogen": "Tomato Mosaic Virus (ToMV)",
        "symptoms": "Mosaic patterns of light and dark green on leaves; leaf distortion; stunting",
        "severity": "High",
        "remedy": [
            "No cure — remove and destroy infected plants",
            "Disinfect tools with bleach solution (10%)",
            "Wash hands thoroughly after handling infected plants",
            "Control aphid vectors",
        ],
        "prevention": "Use certified virus-free seed; strict hygiene; resistant varieties",
        "conditions": "Transmitted mechanically and by aphids"
    },
    "Tomato___healthy": {
        "common_name": "Healthy Tomato",
        "crop": "Tomato",
        "pathogen": "None",
        "symptoms": "No disease symptoms present — plant is healthy!",
        "severity": "None",
        "remedy": ["Maintain consistent watering and balanced fertilization"],
        "prevention": "Crop rotation, proper staking, regular monitoring",
        "conditions": "N/A"
    },
}


def get_disease_info(disease_key: str) -> dict | None:
    """Get full disease information by class key."""
    return DISEASE_DATABASE.get(disease_key)


def get_all_class_names() -> list[str]:
    """Return list of all 38 class names."""
    return list(DISEASE_DATABASE.keys())


def get_crop_diseases(crop_name: str) -> list[tuple]:
    """Return all diseases for a specific crop."""
    crop_name = crop_name.lower()
    return [
        (key, info)
        for key, info in DISEASE_DATABASE.items()
        if crop_name in info["crop"].lower()
    ]
