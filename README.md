# PetPal

PetPal is a Django-based web application for pet owners and service providers. It offers features such as pet management, lost pet reporting, reviews, and integration with various pet-related services (boarding, grooming, vet clinics, pet stores, etc.).

## Features

- User authentication and account management
- Pet profile management (with QR code support)
- Lost pet reporting and search
- Reviews for vets, boarding, grooming, and stores
- Service provider modules: pet boarding, grooming, vet clinics, pet stores
- Admin panel for site management

## Project Structure

```
accounts/       # User authentication and profiles
common/         # Shared models (e.g., reviews)
core/           # Project settings and core views
lost_pets/      # Lost pet reporting and management
pet_boarding/   # Pet boarding services
pet_grooming/   # Pet grooming services
pet_owner/      # Pet owner dashboard and pet management
pet_store/      # Pet store management
site_admin/     # Site administration
vet_clinic/     # Veterinary clinic management
media/          # Uploaded media files
static/         # Static files (CSS, JS, images)
staticfiles/    # Collected static files for deployment
manage.py       # Django management script
requirements.txt# Python dependencies
LICENSE         # License information
```

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd idog
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (admin account):**
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

7. **Access the app:**
   - Visit [http://localhost:8000/](http://localhost:8000/) in your browser.

## Usage

- Register as a user or log in as an admin.
- Add and manage your pets.
- Report lost pets or search for found pets.
- Leave reviews for service providers.
- Admins can manage users and services via the admin panel.

## License

This project is licensed under the Business Source License 1.1 (BSL).  
See [LICENSE](LICENSE) for details.

**Note:** Commercial use is prohibited until the Change Date (**2030-07-11**). For commercial licensing, contact the Licensor.

## Contact

For questions or commercial licensing, contact:  
**matin.alijani@gmail.com**