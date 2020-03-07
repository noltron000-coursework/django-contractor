# Keyboard Wiki
Check out the [instructions] and [proposal] for more details.
There is also a [license].
Completed by Nolan Kovacik.

## Run Locally
1. Fork or clone this project from GitHub.
1. `cd` into the downloaded project root directory.
1. Run `python manage.py runserver`.

## Run Tests
1. `python manage.py test <app>`

## Update Database Structure
1. Run `python manage.py migrate`.
1. Make your changes to the database models.
	- These can usually be found in a `models.py` file.
1. Run `python manage.py makemigrations <app>`
	- One example of `<app>` is `polls`.
1. Run `python manage.py migrate` again.

**\*NOTE**: If you are going to make changes to the database more than once, step 1 may be superfluous.

### Remembering Commands
If you have trouble remembering which command does what, this tidbit from Stack Overflow may help you&hellip;
- `python manage.py makemigrations <app>`: Create the migrations (generate the SQL commands).
- `python manage.py migrate`: Run the migrations (execute the SQL commands).

## Other Useful Commands
- `python manage.py shell`: Run the Django Shell.
- `python manage.py createsuperuser`: Create a new superuser.

## Credits
Many thanks to the Django team, their [tutorial], and their great documentation.
Thanks also to @Dani from Make School, and her team.


[tutorial]: https://docs.djangoproject.com/en/3.0/intro/tutorial01/
[proposal]: ./PROPOSAL.md
[instructions]: ./INSTRUCTIONS.md
