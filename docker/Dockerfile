FROM jupyter/scipy-notebook:1386e2046833

ARG NB_USER=jovyan
ARG NB_UID=1000
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

USER root

COPY install-linux.sh install-linux.sh
COPY install-dependencies.sh install-dependencies.sh

RUN chown -R ${NB_UID} ${HOME}

RUN ./install-linux.sh

EXPOSE 8888

USER ${NB_USER}

ENV PATH=/home/${NB_USER}/.local/bin/:$PATH

ENTRYPOINT ["jupyter-lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]