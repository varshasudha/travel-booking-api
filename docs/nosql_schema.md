# NoSQL Schema — search_preferences (MongoDB collection)

Example document:

{
  "user_id": 1,
  "preferred_time": "morning",
  "seat_type": "window",
  "max_budget": 500
}

## Fields
- user_id: integer, links to the SQL user
- preferred_time: string ("morning" / "afternoon" / "evening")
- seat_type: string ("window" / "aisle" / "middle")
- max_budget: number