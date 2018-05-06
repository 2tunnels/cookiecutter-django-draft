# cookiecutter-django-draft

Very opinionated, yet simple [cookie][cookiecutter] for [Django][django].

## Opinions

1. Everyone should use [Pipenv][pipenv] insted of `pip`.
`Pipfile` is better than `requirements.txt`.
2. Everyone should use [django-environ][django-environ].
There are other ways to manage configuration in Django project,
but this one is the best.
3. Everyone should use PostgreSQL. Period.
4. Everyone should use [django-debug-toolbar][django-debug-toolbar].
5. Everyone should use [pytest-django][pytest-django].
Django by default utilized built-in `unittest` package, butItIsNotVeryPythonic.

[cookiecutter]: https://github.com/audreyr/cookiecutter
[django]: https://www.djangoproject.com/
[pipenv]: https://docs.pipenv.org/
[django-environ]: https://github.com/joke2k/django-environ
[django-debug-toolbar]: https://github.com/jazzband/django-debug-toolbar
[pytest-django]: https://pytest-django.readthedocs.io/en/latest/


## Usage

```bash
$ cookiecutter gh:2tunnels/cookiecutter-django-draft
```
