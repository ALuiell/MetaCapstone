If you plan to test with MySQL, comment out the SQLite configuration in your `settings.py` and uncomment the MySQL settings.
## API Endpoints

### Menu API
- `GET /restaurant/menu/`
- `POST /restaurant/menu/`
- `GET /restaurant/menu/<int:pk>`
- `PUT /restaurant/menu/<int:pk>`
- `PATCH /restaurant/menu/<int:pk>`
- `DELETE /restaurant/menu/<int:pk>`

### Booking API
- `GET /restaurant/booking/tables/`
- `POST /restaurant/booking/tables/`
- `GET /restaurant/booking/tables/<int:pk>/`
- `PUT /restaurant/booking/tables/<int:pk>/`
- `PATCH /restaurant/booking/tables/<int:pk>/`
- `DELETE /restaurant/booking/tables/<int:pk>/`

### User Authentication (Djoser)
- `POST /auth/users/`  *Register a new user*
- `POST /auth/token/login/`  *Login and receive an authentication token*
- `POST /auth/token/logout/`  *Logout*

### Additional Endpoints
- `POST /restaurant/api-token-auth/`  *Obtain token using DRF*
- `GET /hello/`  *Serve a static HTML page*

