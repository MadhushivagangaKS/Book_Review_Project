Register a User:

URL: /api/register/
Method: POST
Body (JSON):
json
Copy code
{
  "username": "abc",
  "password": "password123",
  "password2": "password123",
  "email": "abc@example.com",
  "first_name": "Abc",
  "last_name": "De"
}
Login:

URL: /api/login/
Method: POST
Body (JSON):
json
Copy code
{
  "username": "abc",
  "password": "password123"
}
Search for Books:

URL: /api/books/
Method: GET
Add a Review for a Book:

URL: /api/books/{book_id}/reviews/
Method: POST
Body (JSON):
json
Copy code
{
  "review": "Amazing book!",
  "rating": 5
}
Get Reviews for a Book:

URL: /api/books/{book_id}/reviews/list/
Method: GET
