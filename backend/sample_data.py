"""
Sample legal data for JurisAI
This file contains mock data for Indian laws and case studies
"""

INDIAN_LAWS_EXTENDED = {
    # Indian Penal Code Sections
    "IPC_302": {
        "title": "Punishment for murder",
        "description": "Whoever commits murder shall be punished with death, or imprisonment for life, and shall also be liable to fine.",
        "punishment": "Death or life imprisonment with fine",
        "category": "Criminal Law"
    },
    "IPC_420": {
        "title": "Cheating and dishonestly inducing delivery of property",
        "description": "Whoever cheats and thereby dishonestly induces the person deceived to deliver any property to any person, or to make, alter or destroy the whole or any part of a valuable security, or anything which is signed or sealed, and which is capable of being converted into a valuable security, shall be punished with imprisonment of either description for a term which may extend to seven years, and shall also be liable to fine.",
        "punishment": "Imprisonment up to 7 years and fine",
        "category": "Criminal Law"
    },
    "IPC_376": {
        "title": "Punishment for rape",
        "description": "Whoever commits rape shall be punished with rigorous imprisonment of either description for a term which shall not be less than ten years, but which may extend to imprisonment for life, and shall also be liable to fine.",
        "punishment": "Minimum 10 years to life imprisonment with fine",
        "category": "Criminal Law"
    },
    "IPC_378": {
        "title": "Theft",
        "description": "Whoever, intending to take dishonestly any movable property out of the possession of any person without that person's consent, moves that property in order to such taking, is said to commit theft.",
        "punishment": "Imprisonment up to 3 years or fine or both",
        "category": "Criminal Law"
    },
    "IPC_498A": {
        "title": "Husband or relative of husband of a woman subjecting her to cruelty",
        "description": "Whoever, being the husband or the relative of the husband of a woman, subjects such woman to cruelty shall be punished with imprisonment for a term which may extend to three years and shall also be liable to fine.",
        "punishment": "Imprisonment up to 3 years and fine",
        "category": "Criminal Law"
    }
}

CYBERCRIME_LAWS = {
    "IT_ACT_66": {
        "title": "Computer related offences",
        "description": "If any person, dishonestly or fraudulently, does any act referred to in section 43, he shall be punishable with imprisonment for a term which may extend to three years or with fine which may extend to five lakh rupees or with both.",
        "punishment": "Imprisonment up to 3 years or fine up to 5 lakh or both",
        "category": "Cybercrime"
    },
    "IT_ACT_66C": {
        "title": "Identity theft",
        "description": "Whoever, fraudulently or dishonestly make use of the electronic signature, password or any other unique identification feature of any other person, shall be punished with imprisonment of either description for a term which may extend to three years and shall also be liable to fine which may extend to rupees one lakh.",
        "punishment": "Imprisonment up to 3 years and fine up to 1 lakh",
        "category": "Cybercrime"
    }
}

CONSUMER_PROTECTION_LAWS = {
    "CONSUMER_PROTECTION_ACT": {
        "title": "Consumer Protection Act, 2019",
        "description": "An Act to provide for protection of the interests of consumers and for the said purpose, to establish authorities for timely and effective administration and settlement of consumers' disputes.",
        "key_rights": [
            "Right to be protected against marketing of goods and services which are hazardous to life and property",
            "Right to be informed about the quality, quantity, potency, purity, standard and price of goods or services",
            "Right to be assured of access to a variety of goods and services at competitive prices",
            "Right to be heard and to be assured that consumers' interests will receive due consideration",
            "Right to seek redressal against unfair trade practices or restrictive trade practices or unscrupulous exploitation",
            "Right to consumer education"
        ],
        "category": "Consumer Law"
    }
}

MOCK_CASE_STUDIES = [
    {
        "id": 1,
        "case_name": "State of Maharashtra v. Rajesh Kumar",
        "court": "Bombay High Court",
        "year": "2023",
        "citation": "2023 BHC 156",
        "section": "IPC 302",
        "category": "Criminal Law",
        "summary": "Murder case involving domestic violence. The court emphasized the importance of circumstantial evidence and witness testimony. Key precedent for cases involving marital disputes leading to violence.",
        "key_points": [
            "Circumstantial evidence can be sufficient for conviction",
            "Pattern of domestic violence relevant for establishing motive",
            "Witness testimony credibility assessment"
        ],
        "judgment": "Convicted under IPC 302, sentenced to life imprisonment"
    },
    {
        "id": 2,
        "case_name": "Cyber Cell Delhi v. Tech Solutions Pvt Ltd",
        "court": "Delhi High Court",
        "year": "2022",
        "citation": "2022 DHC 298",
        "section": "IT Act Section 66",
        "category": "Cybercrime",
        "summary": "Online fraud case involving fake investment schemes through social media platforms. The case highlights the importance of digital evidence collection and cybercrime investigation procedures.",
        "key_points": [
            "Digital evidence collection procedures",
            "Social media platform liability",
            "Cross-border cybercrime challenges"
        ],
        "judgment": "Company fined 10 lakh rupees, directors imprisoned for 2 years"
    },
    {
        "id": 3,
        "case_name": "Consumer Forum v. E-Commerce Giant",
        "court": "National Consumer Disputes Redressal Commission",
        "year": "2023",
        "citation": "2023 NCDRC 445",
        "section": "Consumer Protection Act 2019",
        "category": "Consumer Law",
        "summary": "Case involving defective product delivery and poor customer service. Established precedent for e-commerce platform liability and consumer rights in online transactions.",
        "key_points": [
            "E-commerce platform responsibility for product quality",
            "Consumer right to replacement and refund",
            "Timeline for grievance redressal"
        ],
        "judgment": "Platform ordered to refund amount with compensation of 50,000 rupees"
    },
    {
        "id": 4,
        "case_name": "State v. Mobile Theft Gang",
        "court": "Punjab and Haryana High Court",
        "year": "2023",
        "citation": "2023 PHC 187",
        "section": "IPC 378, 411",
        "category": "Criminal Law",
        "summary": "Large-scale mobile phone theft ring case. Important for understanding organized crime prosecution and recovery of stolen property procedures.",
        "key_points": [
            "Organized crime investigation techniques",
            "Recovery and identification of stolen property",
            "Multiple accused trial procedures"
        ],
        "judgment": "All 8 accused convicted, sentences ranging from 3-7 years"
    },
    {
        "id": 5,
        "case_name": "Women's Rights Organization v. State",
        "court": "Supreme Court of India",
        "year": "2022",
        "citation": "2022 SCC 234",
        "section": "IPC 498A",
        "category": "Women's Rights",
        "summary": "Landmark case on domestic violence and dowry harassment. Established guidelines for police investigation and court procedures in 498A cases.",
        "key_points": [
            "Immediate arrest guidelines in 498A cases",
            "Evidence collection in domestic violence cases",
            "Protection of complainant during investigation"
        ],
        "judgment": "Guidelines issued for uniform implementation across states"
    }
]

LEGAL_TERMS_DICTIONARY = {
    "Affidavit": "A written statement confirmed by oath or affirmation, for use as evidence in court",
    "Bail": "The temporary release of an accused person awaiting trial, sometimes on condition that a sum of money be lodged as security",
    "Cognizable Offense": "An offense for which a police officer may arrest without warrant",
    "Defendant": "An individual, company, or institution sued or accused in a court of law",
    "Evidence": "The available body of facts or information indicating whether a belief or proposition is true or valid",
    "FIR": "First Information Report - the first document recorded by police upon receiving information about a cognizable offense",
    "Injunction": "An authoritative warning or order, especially a judicial order restraining a person from beginning or continuing an action",
    "Jurisdiction": "The official power to make legal decisions and judgments",
    "Plaintiff": "A person who brings a case against another in a court of law",
    "Summons": "An order to appear before a judge or magistrate, or the writ containing it",
    "Warrant": "A document issued by a legal or government official authorizing the police to make an arrest, search premises, or carry out some other action",
    "Writ": "A formal written order issued by a body with administrative or judicial jurisdiction"
}

# Quick response templates for common legal queries
QUICK_RESPONSES = {
    "file_fir": "To file an FIR (First Information Report):\n1. Visit the nearest police station\n2. Provide details of the incident in writing\n3. Ensure the FIR is registered and you receive a copy\n4. Note down the FIR number for future reference\n5. If police refuse to register FIR, you can approach the Superintendent of Police or file online complaint",
    
    "consumer_complaint": "To file a consumer complaint:\n1. Try resolving with the company first\n2. File complaint with District Consumer Forum (up to ₹20 lakh)\n3. Required documents: receipt, warranty, correspondence\n4. Pay prescribed fee\n5. Case will be heard within 90 days\n6. Can appeal to State and National forums if needed",
    
    "cyber_crime": "For cybercrime complaints:\n1. File complaint at www.cybercrime.gov.in\n2. Visit nearest cyber crime police station\n3. Preserve all digital evidence (screenshots, emails, messages)\n4. File FIR if financial loss occurred\n5. Report to bank immediately for financial frauds\n6. Keep all transaction details and communication records",
    
    "domestic_violence": "For domestic violence help:\n1. Call National Domestic Violence Helpline: 181\n2. File complaint under Domestic Violence Act, 2005\n3. Seek protection order from magistrate\n4. Can file FIR under IPC 498A if applicable\n5. Contact local women's cell or NGO for support\n6. Preserve evidence of violence (medical reports, photos)"
}