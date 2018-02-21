FROM openjdk:8u151-jdk

LABEL "maintainer"="Heston Snodgrass heston.snodgrass@connexta.com"

ENV JENKINS_HOME /jenkins

RUN apt-get updated \
    && apt-get install yamllint

COPY scripts/entrypoint.sh /

RUN mkdir -p $JENKINS_HOME

ENTRYPOINT ["/entrypoint.sh"]
