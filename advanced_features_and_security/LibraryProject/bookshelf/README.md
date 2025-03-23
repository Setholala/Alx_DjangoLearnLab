# README.md
# Django Permissions and Groups Implementation

## Objective
Implement and manage permissions and groups to control access to different parts of the Django application.

## Custom Permissions
Defined permissions on the `Article` model:
- `can_view`: Can view articles
- `can_create`: Can create articles
- `can_edit`: Can edit articles
- `can_delete`: Can delete articles

## Groups Setup
- `Viewers`: Access to view articles only.
- `Editors`: Access to view, create, and edit articles.
- `Admins`: Full access (view, create, edit, delete).

## Testing
1. Create test users and assign them to the above groups.
2. Log in and verify access control using the implemented views.

## Usage
Ensure you run the group and permission setup via the Django shell or management command:

```bash
python manage.py shell
```