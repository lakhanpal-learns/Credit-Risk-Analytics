import random
def generate_branch() -> dict:
    """
    Generate branch information.
    """

    branches = [

        ("BR001", "Mumbai Central", "Mumbai", "Maharashtra", "West", "Large"),
        ("BR002", "Delhi CP", "New Delhi", "Delhi", "North", "Large"),
        ("BR003", "Bengaluru MG Road", "Bengaluru", "Karnataka", "South", "Large"),
        ("BR004", "Chandigarh", "Chandigarh", "Chandigarh", "North", "Medium"),
        ("BR005", "Jaipur", "Jaipur", "Rajasthan", "North", "Medium"),
        ("BR006", "Ahmedabad", "Ahmedabad", "Gujarat", "West", "Large"),
        ("BR007", "Lucknow", "Lucknow", "Uttar Pradesh", "North", "Medium"),
        ("BR008", "Hyderabad", "Hyderabad", "Telangana", "South", "Large"),
        ("BR009", "Chennai", "Chennai", "Tamil Nadu", "South", "Large"),
        ("BR010", "Kolkata", "Kolkata", "West Bengal", "East", "Large")

    ]

    branch = random.choice(branches)

    return {

        "branch_code": branch[0],
        "branch_name": branch[1],
        "city": branch[2],
        "state": branch[3],
        "region": branch[4],
        "branch_type": branch[5]

    }