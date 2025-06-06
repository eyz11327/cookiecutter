FROM python:{{ cookiecutter.project_python_version }}-bullseye
RUN mkdir /config

COPY pyproject.toml /
COPY bin/ bin/
COPY {{ cookiecutter.project_slug | replace('-', '_') }} /{{ cookiecutter.project_slug | replace('-', '_') }}
COPY /config/example_secret_config.json /config
COPY requirements.txt /

ENV PIP_CONFIG_FILE=/run/secrets/pipconf

RUN --mount=type=secret,id=pipconf pip install .
FROM python:{{ cookiecutter.project_python_version }}-slim-bullseye

COPY --from=0 /usr/local/lib/python{{ cookiecutter.project_python_version }}/site-packages /usr/local/lib/python{{ cookiecutter.project_python_version }}/site-packages/
COPY --from=0 /bin/{{ cookiecutter.project_slug | replace('-', '_') }} /usr/local/bin/{{ cookiecutter.project_slug | replace('-', '_') }}

CMD ["{{ cookiecutter.project_slug | replace('-', '_') }}"]