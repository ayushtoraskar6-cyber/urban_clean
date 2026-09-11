import json
from database import SessionLocal, engine
import models

def seed_database():
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    try:
        with open("db.json", "r") as f:
            data = json.load(f)
            
        print("Seeding complaints...")
        for comp_data in data.get("complaints", []):
            raw_id = comp_data.get("id")
            num_id = int(raw_id.replace("COMP-", "")) if isinstance(raw_id, str) and "COMP-" in raw_id else raw_id

            existing = db.query(models.Complaint).filter_by(id=num_id).first()
            if not existing:
                complaint = models.Complaint(
                    id=num_id,
                    title=comp_data.get("title"),
                    complaint_type=comp_data.get("category"),
                    state=comp_data.get("state", "Maharashtra"),        # Default value to satisfy NOT NULL
                    district=comp_data.get("district", "Mumbai"),      # Default value to satisfy NOT NULL
                    city=comp_data.get("city", "Mumbai"),
                    latitude=comp_data.get("lat"),
                    longitude=comp_data.get("lng"),
                    photo_before=comp_data.get("photo"),
                    status=comp_data.get("status", "Open")
                )
                db.add(complaint)
        
        db.commit()
        print("Database seeded successfully!")
        
    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()